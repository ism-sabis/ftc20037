"""Sync gallery metadata and generate an admin review document.

This script scans assets/images/gallery/uploads/, keeps one display entry per
photo (prefers non-DNG if both exist), preserves existing tags/captions/
descriptions when possible, and writes:

1) _data/gallery.yml
2) gallery-admin.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import yaml

UPLOADS_DIR = Path("assets/images/gallery/uploads")
GALLERY_DATA_PATH = Path("_data/gallery.yml")
GALLERY_ADMIN_PATH = Path("gallery-admin.md")

DISPLAY_PRIORITY = {
    "jpg": 5,
    "jpeg": 4,
    "png": 3,
    "webp": 2,
    "dng": 1,
}


@dataclass
class GalleryFile:
    path: Path
    rel_path: str
    stem: str
    ext: str


def to_site_path(path: Path) -> str:
    return "/" + str(path.as_posix())


def list_gallery_files() -> List[GalleryFile]:
    if not UPLOADS_DIR.exists():
        return []

    files: List[GalleryFile] = []
    for path in sorted(UPLOADS_DIR.rglob("*")):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        ext = path.suffix.lower().lstrip(".")
        if ext not in DISPLAY_PRIORITY:
            continue
        rel = to_site_path(path)
        files.append(GalleryFile(path=path, rel_path=rel, stem=path.stem, ext=ext))
    return files


def choose_display_files(files: List[GalleryFile]) -> List[GalleryFile]:
    by_stem: Dict[str, GalleryFile] = {}
    for item in files:
        current = by_stem.get(item.stem)
        if current is None:
            by_stem[item.stem] = item
            continue

        current_priority = DISPLAY_PRIORITY.get(current.ext, 0)
        item_priority = DISPLAY_PRIORITY.get(item.ext, 0)
        if item_priority > current_priority:
            by_stem[item.stem] = item

    return sorted(by_stem.values(), key=lambda f: f.path.name.lower())


def load_existing_items() -> Dict[str, dict]:
    if not GALLERY_DATA_PATH.exists():
        return {}

    with GALLERY_DATA_PATH.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    items = data.get("items", []) or []
    existing: Dict[str, dict] = {}
    for item in items:
        src = item.get("src")
        if src:
            existing[src] = item
    return existing


def build_items(display_files: List[GalleryFile], existing: Dict[str, dict]) -> List[dict]:
    # Build a stem map so metadata from old srcs can be retained if extension changed.
    existing_by_stem: Dict[str, dict] = {}
    for src, item in existing.items():
        stem = Path(src).stem
        existing_by_stem[stem] = item

    items: List[dict] = []
    for file in display_files:
        src = file.rel_path
        prior = existing.get(src) or existing_by_stem.get(file.stem, {})

        caption = prior.get("caption", "")
        description = prior.get("description", "")
        tags = prior.get("tags", [])

        item = {
            "src": src,
            "caption": caption,
            "description": description,
            "tags": tags if isinstance(tags, list) else [],
        }
        items.append(item)

    return items


def write_gallery_data(items: List[dict]) -> None:
    data = {
        "items": items,
    }

    with GALLERY_DATA_PATH.open("w", encoding="utf-8") as f:
        f.write("# Gallery metadata file\n")
        f.write("# Add/adjust tags and descriptions under each item.\n")
        f.write("# Add new available filter tags in _data/gallery_tags.yml\n\n")
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def render_admin_doc(items: List[dict]) -> str:
    lines: List[str] = [
        "---",
        "layout: page",
        "title: Gallery Admin",
        "description: Preview gallery items and edit metadata in _data/gallery.yml.",
        "permalink: /gallery-admin/",
        "---",
        "",
        "Edit metadata in _data/gallery.yml and add new filter tags in _data/gallery_tags.yml.",
        "",
    ]

    if not items:
        lines.extend(
            [
                "## No Gallery Files Found",
                "",
                "Upload files into assets/images/gallery/uploads/ and run this script again.",
            ]
        )
        return "\n".join(lines) + "\n"

    for item in items:
        src = item["src"]
        caption = item.get("caption", "")
        description = item.get("description", "")
        tags = item.get("tags", [])
        tag_text = ", ".join(tags) if tags else ""

        lines.extend(
            [
                f"## {Path(src).name}",
                "",
                f"<img src=\"{src}\" alt=\"{Path(src).stem}\" style=\"max-width: 360px; width: 100%; border-radius: 8px;\" />",
                "",
                "Caption:",
                f"{caption}",
                "",
                "Description:",
                f"{description}",
                "",
                "Tags (comma separated):",
                f"{tag_text}",
                "",
                f"Source: `{src}`",
                "",
                "---",
                "",
            ]
        )

    return "\n".join(lines)


def main() -> int:
    files = list_gallery_files()
    display_files = choose_display_files(files)
    existing = load_existing_items()
    items = build_items(display_files, existing)

    write_gallery_data(items)

    admin_doc = render_admin_doc(items)
    GALLERY_ADMIN_PATH.write_text(admin_doc, encoding="utf-8")

    print(f"Synced {len(items)} gallery metadata entries.")
    print(f"Wrote {GALLERY_DATA_PATH}")
    print(f"Wrote {GALLERY_ADMIN_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
