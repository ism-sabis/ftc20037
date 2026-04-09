#!/usr/bin/env python3
"""Simplify uploaded GLTF/GLB models to stay under a target size.

This script is intended for textured/color models exported from CAD/DCC tools.
It simplifies geometry while preserving materials where possible.

Usage:
  python scripts/simplify_gltf.py -i assets/models/uploads/model.gltf -o assets/models/2025-2026/model.gltf --max-mb 100
"""

from __future__ import annotations

import argparse
from pathlib import Path

import trimesh


def simplify_mesh(mesh: trimesh.Trimesh, ratio: float) -> trimesh.Trimesh:
    if ratio >= 0.999:
        return mesh
    target_faces = max(5000, int(len(mesh.faces) * ratio))
    if len(mesh.faces) <= target_faces:
        return mesh

    try:
        simplified = mesh.simplify_quadric_decimation(face_count=target_faces)
        if simplified is not None and len(simplified.faces) > 0:
            return simplified
    except Exception as exc:
        print(f"  decimation skipped for mesh: {exc}")
    return mesh


def simplify_scene(scene: trimesh.Scene, ratio: float) -> trimesh.Scene:
    new_scene = trimesh.Scene()
    for node_name, geom_name in scene.graph.nodes_geometry:
        geom = scene.geometry[geom_name]
        transform = scene.graph.get(node_name)[0]

        if isinstance(geom, trimesh.Trimesh):
            simplified = simplify_mesh(geom.copy(), ratio)
            new_scene.add_geometry(simplified, node_name=node_name, transform=transform)
        else:
            new_scene.add_geometry(geom, node_name=node_name, transform=transform)
    return new_scene


def export_scene(scene: trimesh.Scene, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    export_data = scene.export(file_type="glb")
    output_path.write_bytes(export_data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Simplify GLTF/GLB to target file size")
    parser.add_argument("-i", "--input", required=True, help="Input .gltf/.glb path")
    parser.add_argument("-o", "--output", required=True, help="Output .gltf/.glb path")
    parser.add_argument("--max-mb", type=float, default=100.0, help="Maximum allowed size in MB")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 1

    scene = trimesh.load(str(input_path), force="scene")

    # Try progressive simplification passes until target is met.
    ratios = [1.0, 0.9, 0.75, 0.6, 0.5, 0.4, 0.3, 0.25]

    best_bytes: bytes | None = None
    best_size = None

    for ratio in ratios:
        candidate_scene = simplify_scene(scene, ratio)
        export_data = candidate_scene.export(file_type="glb")
        size_mb = len(export_data) / (1024 * 1024)
        print(f"ratio={ratio:.2f} size={size_mb:.2f} MB")

        if best_bytes is None or len(export_data) < len(best_bytes):
            best_bytes = export_data
            best_size = size_mb

        if size_mb <= args.max_mb:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(export_data)
            print(f"Saved: {output_path} ({size_mb:.2f} MB)")
            return 0

    if best_bytes is None:
        print("Failed to export simplified model.")
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(best_bytes)
    print(
        f"Could not get under {args.max_mb:.2f} MB. "
        f"Saved smallest result: {output_path} ({best_size:.2f} MB)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
