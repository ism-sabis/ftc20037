#!/usr/bin/env python3
"""
Batch Asset Converter for MESGRO
================================

Scans the assets folder for source files (SPICE, STL, STEP) and converts them
to their web-viewable formats (SVG, GLTF) if:
- The converted file doesn't exist, OR
- The source file is newer than the converted file

This script is used by GitHub Actions and can also be run locally.

Usage:
    python scripts/convert_all_assets.py [--force] [--dry-run] [--assets-dir PATH]

Options:
    --force      Force reconversion of all files, ignoring timestamps
    --dry-run    Show what would be converted without actually converting
    --assets-dir  Path to assets directory (default: ./assets)
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


# File extension mappings
CONVERSIONS = {
    # SPICE -> SVG
    '.cir': ('.cir.svg', 'spice_to_svg.py'),
    # CAD -> GLTF
    '.stl': ('.gltf', 'cad_to_gltf.py'),
    '.step': ('.gltf', 'cad_to_gltf.py'),
    '.stp': ('.gltf', 'cad_to_gltf.py'),
}


def get_script_dir() -> Path:
    """Get the directory containing this script."""
    return Path(__file__).parent.resolve()


def find_source_files(assets_dir: Path) -> List[Path]:
    """Find all source files that can be converted."""
    source_files = []
    for ext in CONVERSIONS.keys():
        source_files.extend(assets_dir.rglob(f'*{ext}'))
    return sorted(source_files)


def get_converted_path(source_path: Path) -> Path:
    """Get the expected path of the converted file."""
    ext = source_path.suffix.lower()
    new_ext, _ = CONVERSIONS[ext]

    # For .cir files, append .svg (file.cir -> file.cir.svg)
    if ext == '.cir':
        return source_path.with_suffix(source_path.suffix + '.svg')
    else:
        # For CAD files, replace extension (file.stl -> file.gltf)
        return source_path.with_suffix(new_ext)


def needs_conversion(source_path: Path, converted_path: Path, force: bool = False) -> Tuple[bool, str]:
    """
    Check if a source file needs to be converted.

    Returns:
        (needs_conversion, reason)
    """
    if force:
        return True, "forced"

    if not converted_path.exists():
        return True, "converted file missing"

    # Compare modification times
    source_mtime = source_path.stat().st_mtime
    converted_mtime = converted_path.stat().st_mtime

    if source_mtime > converted_mtime:
        return True, "source file newer"

    return False, "up to date"


def convert_spice(source_path: Path, output_path: Path, script_dir: Path) -> bool:
    """Convert a SPICE file to SVG."""
    script = script_dir / 'spice_to_svg.py'
    try:
        result = subprocess.run(
            [sys.executable, str(script), str(source_path), str(output_path)],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print(f"  ERROR: {result.stderr.strip()}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print("  ERROR: Conversion timed out")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def convert_cad(source_path: Path, output_path: Path, script_dir: Path) -> bool:
    """Convert a CAD file to GLTF."""
    script = script_dir / 'cad_to_gltf.py'
    try:
        result = subprocess.run(
            [sys.executable, str(script), '-i', str(source_path), '-o', str(output_path)],
            capture_output=True,
            text=True,
            timeout=300  # CAD conversion can take longer
        )
        if result.returncode != 0:
            print(f"  ERROR: {result.stderr.strip()}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print("  ERROR: Conversion timed out")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Batch convert source files to web-viewable formats"
    )
    parser.add_argument(
        '--force', '-f',
        action='store_true',
        help='Force reconversion of all files'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be converted without converting'
    )
    parser.add_argument(
        '--assets-dir',
        type=Path,
        default=None,
        help='Path to assets directory (default: ./assets)'
    )
    args = parser.parse_args()

    # Determine paths
    script_dir = get_script_dir()
    repo_root = script_dir.parent

    if args.assets_dir:
        assets_dir = args.assets_dir.resolve()
    else:
        assets_dir = repo_root / 'assets'

    if not assets_dir.exists():
        print(f"ERROR: Assets directory not found: {assets_dir}")
        sys.exit(1)

    print("=" * 60)
    print("MESGRO Asset Converter")
    print("=" * 60)
    print(f"Assets directory: {assets_dir}")
    print(f"Force mode: {args.force}")
    print(f"Dry run: {args.dry_run}")
    print()

    # Find all source files
    source_files = find_source_files(assets_dir)

    if not source_files:
        print("No source files found to convert.")
        print(f"Supported formats: {', '.join(CONVERSIONS.keys())}")
        sys.exit(0)

    print(f"Found {len(source_files)} source file(s)")
    print()

    # Process each file
    converted = 0
    skipped = 0
    failed = 0

    for source_path in source_files:
        converted_path = get_converted_path(source_path)
        needs_conv, reason = needs_conversion(source_path, converted_path, args.force)

        rel_source = source_path.relative_to(repo_root)
        rel_converted = converted_path.relative_to(repo_root)

        if not needs_conv:
            print(f"[SKIP] {rel_source} ({reason})")
            skipped += 1
            continue

        print(f"[CONVERT] {rel_source} -> {rel_converted.name} ({reason})")

        if args.dry_run:
            converted += 1
            continue

        # Perform conversion
        ext = source_path.suffix.lower()
        if ext == '.cir':
            success = convert_spice(source_path, converted_path, script_dir)
        else:
            success = convert_cad(source_path, converted_path, script_dir)

        if success:
            converted += 1
            print(f"  OK: Created {rel_converted}")
        else:
            failed += 1

    # Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Converted: {converted}")
    print(f"  Skipped:   {skipped}")
    print(f"  Failed:    {failed}")

    if args.dry_run:
        print()
        print("(Dry run - no files were actually converted)")

    sys.exit(1 if failed > 0 else 0)


if __name__ == '__main__':
    main()
