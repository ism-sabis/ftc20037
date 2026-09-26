# Cloudflare Pages

This site can build directly from GitHub in Cloudflare Pages. The build helper runs the same CSS and gallery preprocessing as the GitHub Pages workflow, then builds Jekyll for the domain root.

Use these Cloudflare Pages build settings:

- **Build command:** `bash scripts/build_cloudflare.sh`
- **Build output directory:** `_site`
- **Root directory:** `/`
- **Deploy command** (if the project uses a separate deploy command): `npx wrangler pages deploy ./_site --project-name=ftc20037`

The site URL is configured as `https://www.ftc20037.com` in `_config.yml`; `baseurl` stays empty because the site is served at the domain root. Add `www.ftc20037.com` under the Pages project's **Custom domains** and follow Cloudflare's DNS instructions.

The existing GitHub Pages deployment remains enabled during the transition.
