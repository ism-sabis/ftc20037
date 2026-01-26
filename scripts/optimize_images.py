#!/usr/bin/env python3
"""
Image Optimizer for MESGRO
==========================

Optimizes images in the assets folder for web viewing:
- Compresses JPG/PNG images to reduce file size
- Resizes oversized images to maximum dimensions
- Optionally generates WebP versions for modern browsers
- Preserves originals with .original extension (optional)

Usage:
    python scripts/optimize_images.py [--force] [--dry-run] [--webp] [--max-width WIDTH]

Options:
    --force       Re-optimize all images, ignoring previous optimization
    --dry-run     Show what would be optimized without actually processing
    --webp        Generate WebP versions alongside originals
    --max-width   Maximum width in pixels (default: 1920)
    --quality     JPEG/WebP quality 1-100 (default: 85)
    --assets-dir  Path to assets directory (default: ./assets)
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Tuple, Optional
import json

try:
    from PIL import Image, ImageOps
except ImportError:
    print("ERROR: Pillow is required for image optimization")
    print("Install with: pip install Pillow")
    sys.exit(1)


# Supported image formats
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

# Marker file to track optimized images
OPTIMIZATION_MARKER = '.image_optimization_cache.json'

# Default settings
DEFAULT_MAX_WIDTH = 1920
DEFAULT_MAX_HEIGHT = 1080
DEFAULT_QUALITY = 85
DEFAULT_PNG_COMPRESS = 6  # 0-9, higher = more compression


def get_script_dir() -> Path:
    """Get the directory containing this script."""
    return Path(__file__).parent.resolve()


def load_optimization_cache(assets_dir: Path) -> dict:
    """Load the optimization cache to track already-optimized images."""
    cache_file = assets_dir / OPTIMIZATION_MARKER
    if cache_file.exists():
        try:
            with open(cache_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_optimization_cache(assets_dir: Path, cache: dict):
    """Save the optimization cache."""
    cache_file = assets_dir / OPTIMIZATION_MARKER
    with open(cache_file, 'w') as f:
        json.dump(cache, f, indent=2)


def get_file_hash(file_path: Path) -> str:
    """Get a simple hash based on file size and modification time."""
    stat = file_path.stat()
    return f"{stat.st_size}_{stat.st_mtime}"


def find_images(assets_dir: Path) -> List[Path]:
    """Find all image files in assets directory."""
    images = []
    for ext in IMAGE_EXTENSIONS:
        images.extend(assets_dir.rglob(f'*{ext}'))
        images.extend(assets_dir.rglob(f'*{ext.upper()}'))

    # Filter out already-generated WebP files and originals
    images = [
        img for img in images
        if not str(img).endswith('.original.jpg')
        and not str(img).endswith('.original.png')
        and '.optimized' not in str(img)
    ]

    return sorted(set(images))


def needs_optimization(
    image_path: Path,
    cache: dict,
    force: bool = False,
    max_width: int = DEFAULT_MAX_WIDTH,
    max_height: int = DEFAULT_MAX_HEIGHT
) -> Tuple[bool, str]:
    """Check if an image needs optimization."""
    if force:
        return True, "forced"

    rel_path = str(image_path)
    file_hash = get_file_hash(image_path)

    # Check cache
    if rel_path in cache and cache[rel_path].get('hash') == file_hash:
        return False, "already optimized"

    # Check if image is oversized
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width > max_width or height > max_height:
                return True, f"oversized ({width}x{height})"
    except Exception:
        return False, "cannot read image"

    # Check file size (optimize if > 500KB for JPG, > 1MB for PNG)
    size_kb = image_path.stat().st_size / 1024
    ext = image_path.suffix.lower()

    if ext in ['.jpg', '.jpeg'] and size_kb > 500:
        return True, f"large file ({size_kb:.0f}KB)"
    elif ext == '.png' and size_kb > 1000:
        return True, f"large file ({size_kb:.0f}KB)"
    elif ext == '.gif' and size_kb > 2000:
        return True, f"large file ({size_kb:.0f}KB)"

    # If not in cache, optimize anyway to add to cache
    if rel_path not in cache:
        return True, "not in cache"

    return False, "up to date"


def optimize_image(
    image_path: Path,
    max_width: int = DEFAULT_MAX_WIDTH,
    max_height: int = DEFAULT_MAX_HEIGHT,
    quality: int = DEFAULT_QUALITY,
    generate_webp: bool = False,
    dry_run: bool = False
) -> Tuple[bool, dict]:
    """
    Optimize a single image.

    Returns:
        (success, stats_dict)
    """
    stats = {
        'original_size': image_path.stat().st_size,
        'new_size': 0,
        'webp_size': 0,
        'resized': False,
        'original_dimensions': None,
        'new_dimensions': None
    }

    try:
        with Image.open(image_path) as img:
            original_format = img.format
            stats['original_dimensions'] = img.size

            # Handle EXIF orientation
            img = ImageOps.exif_transpose(img)

            # Convert RGBA to RGB for JPEG (remove alpha channel)
            if img.mode == 'RGBA' and image_path.suffix.lower() in ['.jpg', '.jpeg']:
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            elif img.mode == 'P':
                img = img.convert('RGBA' if 'transparency' in img.info else 'RGB')

            # Resize if needed
            width, height = img.size
            if width > max_width or height > max_height:
                # Calculate new dimensions maintaining aspect ratio
                ratio = min(max_width / width, max_height / height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                stats['resized'] = True
                stats['new_dimensions'] = (new_width, new_height)
            else:
                stats['new_dimensions'] = img.size

            if dry_run:
                stats['new_size'] = stats['original_size']  # Estimate
                return True, stats

            # Save optimized image
            ext = image_path.suffix.lower()

            if ext in ['.jpg', '.jpeg']:
                img.save(
                    image_path,
                    'JPEG',
                    quality=quality,
                    optimize=True,
                    progressive=True
                )
            elif ext == '.png':
                # For PNG, try to optimize without losing quality
                img.save(
                    image_path,
                    'PNG',
                    optimize=True,
                    compress_level=DEFAULT_PNG_COMPRESS
                )
            elif ext == '.gif':
                # For GIF, just save (Pillow doesn't optimize GIFs well)
                img.save(image_path, 'GIF')
            elif ext == '.webp':
                img.save(
                    image_path,
                    'WEBP',
                    quality=quality,
                    method=6  # Slower but better compression
                )

            stats['new_size'] = image_path.stat().st_size

            # Generate WebP version if requested
            if generate_webp and ext not in ['.webp', '.gif']:
                webp_path = image_path.with_suffix('.webp')
                # Don't overwrite if WebP already exists and is newer
                if not webp_path.exists() or webp_path.stat().st_mtime < image_path.stat().st_mtime:
                    img.save(
                        webp_path,
                        'WEBP',
                        quality=quality,
                        method=6
                    )
                    stats['webp_size'] = webp_path.stat().st_size

            return True, stats

    except Exception as e:
        print(f"  ERROR: {e}")
        return False, stats


def format_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f}KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f}MB"


def main():
    parser = argparse.ArgumentParser(
        description="Optimize images for web viewing"
    )
    parser.add_argument(
        '--force', '-f',
        action='store_true',
        help='Force re-optimization of all images'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be optimized without processing'
    )
    parser.add_argument(
        '--webp',
        action='store_true',
        help='Generate WebP versions alongside originals'
    )
    parser.add_argument(
        '--max-width',
        type=int,
        default=DEFAULT_MAX_WIDTH,
        help=f'Maximum image width (default: {DEFAULT_MAX_WIDTH})'
    )
    parser.add_argument(
        '--max-height',
        type=int,
        default=DEFAULT_MAX_HEIGHT,
        help=f'Maximum image height (default: {DEFAULT_MAX_HEIGHT})'
    )
    parser.add_argument(
        '--quality',
        type=int,
        default=DEFAULT_QUALITY,
        help=f'JPEG/WebP quality 1-100 (default: {DEFAULT_QUALITY})'
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
    print("MESGRO Image Optimizer")
    print("=" * 60)
    print(f"Assets directory: {assets_dir}")
    print(f"Max dimensions: {args.max_width}x{args.max_height}")
    print(f"Quality: {args.quality}")
    print(f"Generate WebP: {args.webp}")
    print(f"Force mode: {args.force}")
    print(f"Dry run: {args.dry_run}")
    print()

    # Load optimization cache
    cache = load_optimization_cache(assets_dir)

    # Find all images
    images = find_images(assets_dir)

    if not images:
        print("No images found to optimize.")
        print(f"Supported formats: {', '.join(IMAGE_EXTENSIONS)}")
        sys.exit(0)

    print(f"Found {len(images)} image(s)")
    print()

    # Process each image
    optimized = 0
    skipped = 0
    failed = 0
    total_saved = 0

    for image_path in images:
        needs_opt, reason = needs_optimization(
            image_path, cache, args.force,
            args.max_width, args.max_height
        )

        rel_path = image_path.relative_to(repo_root)

        if not needs_opt:
            print(f"[SKIP] {rel_path} ({reason})")
            skipped += 1
            continue

        print(f"[OPTIMIZE] {rel_path} ({reason})")

        success, stats = optimize_image(
            image_path,
            args.max_width,
            args.max_height,
            args.quality,
            args.webp,
            args.dry_run
        )

        if success:
            optimized += 1
            saved = stats['original_size'] - stats['new_size']
            total_saved += saved

            # Update cache
            if not args.dry_run:
                cache[str(image_path)] = {
                    'hash': get_file_hash(image_path),
                    'optimized_at': str(image_path.stat().st_mtime)
                }

            # Print stats
            size_info = f"{format_size(stats['original_size'])} -> {format_size(stats['new_size'])}"
            if saved > 0:
                pct = (saved / stats['original_size']) * 100
                size_info += f" (saved {pct:.1f}%)"

            print(f"  {size_info}")

            if stats['resized']:
                orig_dim = f"{stats['original_dimensions'][0]}x{stats['original_dimensions'][1]}"
                new_dim = f"{stats['new_dimensions'][0]}x{stats['new_dimensions'][1]}"
                print(f"  Resized: {orig_dim} -> {new_dim}")

            if stats['webp_size'] > 0:
                print(f"  WebP: {format_size(stats['webp_size'])}")
        else:
            failed += 1

    # Save cache
    if not args.dry_run:
        save_optimization_cache(assets_dir, cache)

    # Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Optimized: {optimized}")
    print(f"  Skipped:   {skipped}")
    print(f"  Failed:    {failed}")
    if total_saved > 0:
        print(f"  Total saved: {format_size(total_saved)}")

    if args.dry_run:
        print()
        print("(Dry run - no files were actually modified)")

    sys.exit(1 if failed > 0 else 0)


if __name__ == '__main__':
    main()
