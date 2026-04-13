#!/usr/bin/env python3
"""Reduce OBJ face density by keeping every Nth face.

This script preserves mtllib/usemtl/group/object statements and rewrites the
OBJ with compacted vertex/uv/normal pools so file size drops substantially.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FaceToken:
    v: int
    vt: int | None
    vn: int | None


@dataclass
class FaceRecord:
    tokens: list[FaceToken]


@dataclass
class RawRecord:
    line: str


Record = FaceRecord | RawRecord


def parse_face_token(tok: str) -> FaceToken:
    parts = tok.split("/")
    v = int(parts[0]) if parts and parts[0] else 0
    vt = int(parts[1]) if len(parts) > 1 and parts[1] else None
    vn = int(parts[2]) if len(parts) > 2 and parts[2] else None
    return FaceToken(v=v, vt=vt, vn=vn)


def format_face_token(tok: FaceToken, v_map: dict[int, int], vt_map: dict[int, int], vn_map: dict[int, int]) -> str:
    v = v_map[tok.v]
    vt = vt_map[tok.vt] if tok.vt is not None else None
    vn = vn_map[tok.vn] if tok.vn is not None else None

    if vt is None and vn is None:
        return f"{v}"
    if vt is not None and vn is None:
        return f"{v}/{vt}"
    if vt is None and vn is not None:
        return f"{v}//{vn}"
    return f"{v}/{vt}/{vn}"


def reduce_obj(input_path: Path, output_path: Path, step: int) -> tuple[int, int, int, int, int, int]:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    face_idx = 0
    kept = 0
    records: list[Record] = []
    used_v: set[int] = set()
    used_vt: set[int] = set()
    used_vn: set[int] = set()

    total_v = 0
    total_vt = 0
    total_vn = 0

    # First pass: sample faces + collect used indices + keep directive stream.
    with input_path.open("r", encoding="utf-8", errors="ignore") as src:
        for line in src:
            if line.startswith("v "):
                total_v += 1
                continue
            if line.startswith("vt "):
                total_vt += 1
                continue
            if line.startswith("vn "):
                total_vn += 1
                continue

            if line.startswith("f "):
                face_idx += 1
                if (face_idx - 1) % step == 0:
                    kept += 1
                    toks = [parse_face_token(t) for t in line.strip().split()[1:]]
                    for t in toks:
                        used_v.add(t.v)
                        if t.vt is not None:
                            used_vt.add(t.vt)
                        if t.vn is not None:
                            used_vn.add(t.vn)
                    records.append(FaceRecord(tokens=toks))
                continue

            if line.startswith(("v ", "vt ", "vn ")):
                continue

            records.append(RawRecord(line=line))

    # Build old->new maps with sorted index order.
    v_map = {old: i + 1 for i, old in enumerate(sorted(used_v))}
    vt_map = {old: i + 1 for i, old in enumerate(sorted(used_vt))}
    vn_map = {old: i + 1 for i, old in enumerate(sorted(used_vn))}

    # Second pass: emit only used v/vt/vn lines.
    with input_path.open("r", encoding="utf-8", errors="ignore") as src, output_path.open(
        "w", encoding="utf-8", newline="\n"
    ) as dst:
        v_i = 0
        vt_i = 0
        vn_i = 0
        for line in src:
            if line.startswith("v "):
                v_i += 1
                if v_i in used_v:
                    dst.write(line)
                continue
            if line.startswith("vt "):
                vt_i += 1
                if vt_i in used_vt:
                    dst.write(line)
                continue
            if line.startswith("vn "):
                vn_i += 1
                if vn_i in used_vn:
                    dst.write(line)
                continue

        # Replay directives and kept faces.
        for rec in records:
            if isinstance(rec, RawRecord):
                dst.write(rec.line)
            else:
                tokens = [format_face_token(t, v_map, vt_map, vn_map) for t in rec.tokens]
                dst.write("f " + " ".join(tokens) + "\n")

    return face_idx, kept, total_v, len(used_v), total_vt, len(used_vt)


def main() -> int:
    parser = argparse.ArgumentParser(description="Reduce OBJ face count by sampling faces")
    parser.add_argument("-i", "--input", required=True, help="Input OBJ path")
    parser.add_argument("-o", "--output", required=True, help="Output OBJ path")
    parser.add_argument(
        "--step",
        type=int,
        default=10,
        help="Keep every Nth face (default: 10)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Input not found: {input_path}")
        return 1
    if args.step < 1:
        print("--step must be >= 1")
        return 1

    total, kept, total_v, kept_v, total_vt, kept_vt = reduce_obj(input_path, output_path, args.step)
    pct = (kept / total * 100.0) if total else 0.0
    print(f"Faces: {total:,} -> {kept:,} ({pct:.2f}%)")
    if total_v:
        print(f"Vertices: {total_v:,} -> {kept_v:,} ({kept_v / total_v * 100.0:.2f}%)")
    if total_vt:
        print(f"UVs: {total_vt:,} -> {kept_vt:,} ({kept_vt / total_vt * 100.0:.2f}%)")
    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
