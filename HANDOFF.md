# Team Standard Deviation (FTC 20037) — Website Handoff File

**Date:** July 13, 2026  
**Previous Agent Session:** Legal compliance, accessibility audit, red theme redesign  
**Project Type:** Jekyll static site hosted on GitHub Pages  
**Team:** FTC #20037 "Standard Deviation" at International School of Minnesota (ISM), Eden Prairie, MN

---

## 1. What Was Done in Previous Session

### Legal Compliance
- ✅ Created `privacy.md` → `/privacy/` — Full privacy policy aligned with SABIS network policy (`sabis.net/privacy-policy/`)
- ✅ Created `terms.md` → `/terms-of-use/` — Terms of Use with open-source content policy (CC BY 4.0) and FIRST® trademark compliance
- ✅ Added "Legal" section to footer with Privacy Policy + Terms of Use links
- ✅ Added FIRST® trademark disclaimer in footer bottom bar
- ✅ Updated PitCrew template attribution: `Built by Standard Deviation using the PitCrew template (MIT License)` linking to `github.com/braineatingmachines/pitcrew`

### Data Collection & Privacy Fixes
- ✅ Removed Google Fonts CDN from `_layouts/default.html` — eliminated IP transmission to Google servers
- ✅ Replaced all font-family references with system font stack (`system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`)
- ✅ No analytics/tracking scripts on site (confirmed clean)
- ✅ Only data stored: localStorage for dark mode + accessibility preferences (strictly necessary, no consent required)

### Gallery Admin Redesign
- ✅ Removed old `gallery-admin.md` that exposed raw DNG files and metadata forms
- ✅ Created new `_includes/components/gallery-admin.html` with:
  - Clickable tag buttons to toggle tags on/off per image
  - Inline caption + description editing
  - Tag filtering by season/category
  - "Copy YAML" button generating updated `_data/gallery.yml` content
  - Toast notifications and modal output
  - Mobile responsive layout
- ✅ Created `gallery-admin.md` page (set to `published: false` — hidden from navigation)

### Red Theme Design System
- ✅ Updated all CSS custom properties in `assets/css/main.css`:
  - Primary color changed from FTC blue (`#003974`) to team jersey red (`#DC2626`)
  - Light mode: white backgrounds, near-black text, red accents
  - Dark mode: deep black backgrounds (`#0a0a0a`), near-white text, bright red accents
- ✅ Updated nav-link active state with red underline indicator
- ✅ Updated badge colors to match red theme
- ✅ Enhanced glassmorphism header with shadow on scroll
- ✅ Updated form input focus rings to red
- ✅ Accessibility mode uses high contrast red theme

### Hero Section Redesign (`_includes/sections/home-hero.html`)
- Animated gradient background shifting between red tones (8s infinite loop)
- Hexagonal grid pattern overlay (robotics/tech aesthetic, 10% opacity)
- Floating orbs with smooth CSS animations
- Bottom wave SVG for seamless section transition
- Staggered fade-in-up animations on all content elements
- Enhanced CTA buttons with hover lift effects and arrow animation

### Scroll Animations System (`_includes/components/scroll-animations.html`)
- Intersection Observer-based scroll-triggered animations
- Four animation types: `fade-in-up`, `fade-in-left`, `fade-in-right`, `scale-in`
- Stagger delay support via `data-stagger` attribute on elements
- Respects `prefers-reduced-motion` for accessibility
- Automatically included in all pages via `_layouts/default.html`

### Footer Updates (`_includes/footer.html`)
- Added "Legal" column with Privacy Policy + Terms of Use links
- Updated PitCrew attribution line to credit original template authors
- FIRST® trademark disclaimer added in bottom bar

---

## 2. Current Site Architecture

```
_config.yml                    # Team config, navigation (now includes privacy/terms)
_layouts/
  default.html                 # Base layout — Google Fonts removed, scroll animations added
_includes/
  footer.html                  # Updated with legal links + PitCrew credit + FIRST disclaimer
  navigation.html              # Unchanged — works with updated _config.yml navigation list
  sections/
    home-hero.html             # REDESIGNED — animated red gradient hero
  components/
    gallery-admin.html         # NEW — dynamic tag editor for gallery images
    scroll-animations.html     # NEW — Intersection Observer animation system
    gallery.html               # Enhanced hover effects, gradient overlays
    accessibility-toggle.html  # Unchanged
    ... (other components unchanged)
privacy.md                     # NEW — Privacy Policy page
terms.md                       # NEW — Terms of Use page
gallery-admin.md               # MODIFIED — hidden admin page using new component
LICENSE                        # MIT License (PitCrew template) — unchanged
assets/
  css/
    main.css                   # REDESIGNED — red theme, system fonts, all updates applied
    output.css                 # REBUILT via `npm run build:css`
  js/
    main.js                    # UPDATED — header shadow on scroll behavior
    search.js                  # Unchanged (client-side only, no external calls)
_data/
  gallery.yml                  # Gallery metadata — edited via new admin component
  gallery_tags.yml             # Tag definitions for filtering
  team.yml                     # Student data (names, photos, grades) — FERPA/COPPA applies
  mentors.yml                  # Mentor data
  ... (other _data files unchanged)
```

---

## 3. Key Decisions Made

| Decision | Value | Rationale |
|----------|-------|-----------|
| School privacy alignment | Reference SABIS policy at `sabis.net/privacy-policy/` | ISM is part of SABIS network; their policy covers FERPA/COPPA |
| Cookie consent banner | NOT needed — self-host fonts instead | Eliminates IP transmission entirely, no tracking |
| FIRST® disclaimer | Added to footer bottom bar | Required by FIRST Trademark & Copyrighted Materials Policy |
| Content license | CC BY 4.0 for team original content | Team is open-source; users can adapt with attribution |
| Template attribution | PitCrew credited in footer + LICENSE file | MIT License requires copyright notice preservation |
| Color theme | Red (`#DC2626`) from team jerseys | Matches team identity, works in both light and dark modes |
| Font strategy | System font stack (no external fonts) | Zero tracking, instant load, no CORS issues |

---

## 4. Data Collection Inventory (Current State)

| Source | Type | External? | Consent Required? |
|--------|------|-----------|-------------------|
| localStorage (dark mode, accessibility) | User preferences | No | No — strictly necessary |
| Client-side search (`search.json`) | Static JSON index, no external calls | No | No |
| Social media links (Instagram, GitHub) | External site navigation | Yes | Disclosed in privacy policy |
| Email contact (`mailto:`) | No form submission | No | No |
| Google Fonts | ~~Transmits IPs to Google~~ **REMOVED** | N/A | N/A — eliminated |
| Analytics/tracking scripts | None installed | N/A | N/A |

---

## 5. Files That May Need Attention

### Potentially Sensitive
- `_data/team.yml` — Contains student names, photos, grades, graduation years. FERPA/COPPA applies. Ensure parental consent documentation exists at ISM.
- `gallery-admin.md` — Currently set to `published: false`. If you want it accessible, consider password protection or IP restriction (GitHub Pages doesn't support basic auth natively).

### To Review/Verify
- **Privacy Policy** (`privacy.md`) and **Terms of Use** (`terms.md`) — Recommended legal review by ISM/SABIS counsel before public launch
- **FIRST® trademark language** — Verify compliance with latest FIRST brand guidelines at `firstinspires.org/brand`
- **Student photo consent** — Confirm documented parental/guardian consent exists for all students pictured on the site

---

## 6. Build Commands

```powershell
# Install dependencies (if node_modules missing)
npm install

# Build CSS (required after any changes to main.css)
npm run build:css

# Serve locally for testing
bundle exec jekyll serve

# Full build
bundle exec jekyll build
```

**Note:** After editing `assets/css/main.css`, always run `npm run build:css` to regenerate `output.css`.

---

## 7. Known Issues / Open Items

1. **Accessibility audit incomplete** — The original plan included a full WCAG 2.2 AA audit (alt text quality, color contrast verification, keyboard navigation testing). Only the accessibility mode toggle and skip-link were verified. A thorough audit should be done after deployment.

2. **Gallery admin page is hidden** (`published: false`) — If you want it publicly accessible for team members to manage gallery metadata, change to `published: true`. Consider adding a simple password or restricting access since it allows editing site data.

3. **No image optimization pipeline** — Gallery images (especially DNG raw files) are served as-is. Consider adding an image processing step in the build pipeline.

4. **Blog/News disabled** — `_config.yml` has `blog: false` and `docs: false`. Posts exist in `_posts/` but aren't rendered. Enable via config if needed.

5. **Sponsors page empty** — `/sponsors/` shows "Coming Soon". Sponsor data exists in `_data/sponsors.yml`.

6. **Tailwind CSS output is minified** — `output.css` is a single minified file. If you need to debug styles, rebuild without `--minify` flag temporarily.

---

## 8. Color Reference (Quick Lookup)

```css
/* Light Mode */
--color-primary: #DC2626;      /* Vibrant red */
--color-primary-highlight: #B91C1C;
--color-background: #ffffff;
--color-surface: #fafafa;
--color-text: #111827;
--color-text-muted: #6B7280;
--color-border: #e5e7eb;

/* Dark Mode */
--color-primary: #EF4444;      /* Bright red for dark bg */
--color-background: #0a0a0a;
--color-surface: #171717;
--color-text: #f9fafb;
--color-text-muted: #9CA3AF;
--color-border: #262626;
```

---

## 9. Contact / References

- **Team email:** ftc20037@ism-sabis.net
- **SABIS privacy inquiries:** privacy@sabis.net
- **SABIS main privacy policy:** https://www.sabis.net/privacy-policy/
- **FIRST brand guidelines:** https://www.firstinspires.org/brand
- **PitCrew template:** https://github.com/braineatingmachines/pitcrew (MIT License)

---

*This handoff file was generated automatically by the previous agent session. All changes described above have been committed to the repository.*
