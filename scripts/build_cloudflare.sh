#!/usr/bin/env bash
set -euo pipefail

# Cloudflare's build image can default Ruby's external encoding to US-ASCII.
# The GitHub Pages theme stylesheet contains UTF-8 characters, which makes
# Jekyll's legacy Sass converter fail unless Ruby is told to read UTF-8.
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export RUBYOPT="${RUBYOPT:+$RUBYOPT }-EUTF-8:UTF-8"

# Match the preprocessing used by the GitHub Pages workflow, then build for a
# site served from the domain root.
npm ci
npm run build:css

python3 -m pip install -r requirements.txt
python3 scripts/convert_dng_gallery.py
python3 scripts/sync_gallery_metadata.py

bundle exec jekyll build --baseurl ""

# Raw gallery files are build inputs. Keep them out of the Pages artifact even
# if a Jekyll version does not apply the glob exclusion in _config.yml.
find _site/assets/images/gallery/uploads -type f -iname '*.dng' -print -delete
