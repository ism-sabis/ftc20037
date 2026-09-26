#!/usr/bin/env bash
set -euo pipefail

# Match the preprocessing used by the GitHub Pages workflow, then build for a
# site served from the domain root.
npm ci
npm run build:css

python3 -m pip install -r requirements-cloudflare.txt
python3 scripts/convert_dng_gallery.py
python3 scripts/sync_gallery_metadata.py

bundle exec jekyll build --baseurl ""
