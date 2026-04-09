"""Convert DNG files in the gallery uploads folder to JPG previews.

The converter writes a same-named .jpg next to each .dng file so the site can
render thumbnails and provide a viewable download target.
"""

from __future__ import annotations

from pathlib import Path

import imageio.v2 as imageio
import rawpy


GALLERY_UPLOADS = Path("assets/images/gallery/uploads")


def convert_dng_file(dng_path: Path) -> tuple[bool, str]:
    jpg_path = dng_path.with_suffix(".jpg")

    # Skip conversion when a newer/equal JPG already exists.
    if jpg_path.exists() and jpg_path.stat().st_mtime >= dng_path.stat().st_mtime:
        return False, f"skip  {dng_path} (up-to-date)"

    try:
        with rawpy.imread(str(dng_path)) as raw:
            rgb = raw.postprocess(
                use_camera_wb=True,
                no_auto_bright=False,
                bright=1.8,
                output_bps=8,
                gamma=(2.222, 4.5),
            )

        imageio.imwrite(str(jpg_path), rgb, quality=95)
        return True, f"write {jpg_path}"
    except Exception as exc:  # pragma: no cover - defensive in CI script
        return False, f"error {dng_path}: {exc}"


def main() -> int:
    if not GALLERY_UPLOADS.exists():
        print(f"Gallery uploads folder not found: {GALLERY_UPLOADS}")
        return 0

    dng_files = sorted(GALLERY_UPLOADS.rglob("*.dng"))
    if not dng_files:
        print("No DNG files found.")
        return 0

    converted = 0
    for dng_file in dng_files:
        changed, message = convert_dng_file(dng_file)
        print(message)
        if changed:
            converted += 1

    print(f"DNG conversion complete. Converted: {converted}, Found: {len(dng_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
