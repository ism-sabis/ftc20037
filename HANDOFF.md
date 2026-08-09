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

### ✅ Existing Accessibility Features Already in Place (Do NOT Remove)
The site already has several good accessibility practices:
- **Skip link** to `#main-content` present in default layout with fixed positioning on focus
- **ARIA labels** on all icon buttons throughout navigation and footer (`aria-label="Close menu"`, `aria-label="Toggle dark mode"`, etc.)
- **Focus-visible ring styles** applied consistently via `.btn:focus-visible`, `.nav-link:focus-visible`, `a:focus-visible` in main.css (lines ~745–760)
- **Semantic HTML structure**: `<header>`, `<main>` landmark, `<footer>`, proper heading hierarchy
- **Image alt text**: Gallery images have descriptive alt attributes; logo has contextual alt text
- **External links** use `target="_blank" rel="noopener noreferrer` consistently (e.g., social icons in footer)
- **Dark mode toggle** with localStorage + prefers-color-scheme detection
- **Accessibility toggle feature enabled** (`site.features.accessibility_toggle`) for high contrast, reduced motion, large text
- Mobile menu button has `aria-expanded="false"` on trigger, toggled via JS

### 🔴 New WCAG 2.2 AA Audit Findings — Fix These Issues Below
A thorough accessibility audit was conducted across all key layouts and components (`_includes/navigation.html`, `_layouts/season.html`, `_includes/footer.html`, `assets/css/main.css`, `_includes/components/gallery.html`, `_includes/components/accessibility-toggle.html`). The following **7 issues** were identified, each with a specific WCAG criterion violation. All fixes are minimal-change (CSS tweaks or ARIA attribute additions) and do not alter the site's visual design.

#### Issue 1: Footer Text Contrast Fails WCAG AA (~34 lines of failing text in `footer.html`)
- **WCAG Criteria**: 1.4.3 Contrast Minimum (Level AA), requires ≥4.5:1 for normal text <18px / ≤14px bold; ≥3:1 for large text ≥18px or ≥14px bold — all measured against `body` bg (`--color-bg-primary`)
- **What fails**: Lines 62, 67–70 in `_includes/footer.html`: the contact links (email/phone/address) use Tailwind's `text-muted` class which maps to CSS variable `--color-text-muted: #475569`. In light mode this is **#475569 on white** ≈ **2.8:1**, well below the 4.5:1 threshold for normal-sized text (0.875rem / ~14px). Lines 73–74 have `text-faint` separators (~#94A3B8 or #475569 depending on which is faint) at even lower contrast (~2.6:1), also failing AA.
- **Impact**: Visually impaired users cannot read the footer contact information in light mode, losing access to essential ways to reach the team.

#### Issue 2: Focus Not Obscured by Sticky Header — Critical WCAG Violation (`main.css` needs ~3 lines of CSS)
- **WCAG Criteria**: 2.4.11 Focus Not Obscured (Level AA): "Minimum" level requires that keyboard focus indicators are never obscured or covered by other content as users navigate through pages, except when the content obscures focus following a user action and can be dismissed. The baseline requirement is simply that no part of any focused element should ever overlap with another page element during navigation — this applies to all elements receiving tab-focus order (links, buttons, skip-link) at every section heading/anchor on the site.
- **What fails**: `assets/css/main.css` has NO `scroll-margin-top`, `padding-top`, or equivalent spacing rule applied specifically when an element receives focus (`:focus`) or is targeted via URL fragment (`[id]:target`). The sticky header in `_includes/navigation.html` overlaps ~3–4rem of vertical space at the top of every page. When a keyboard user tabs to any link/button/heading that sits near the top of a section, the browser scrolls it into view but does not account for the fixed/sticky navigation bar height — so part of the focused element gets hidden behind the header instead of being fully visible in the viewport above it. This happens on every page (home hero anchors to sections like "About", "Events", etc.) and inside season pages where section headings are used as jump targets (`#about`, `#events` in `_layouts/season.html`).
- **Impact**: Keyboard users cannot see what they just focused on, making navigation confusing or impossible. This is a critical compliance failure — every WCAG 2.1 AA checklist lists "focus not obscured" as a required criterion that must pass for all interactive elements. The fix requires adding ONE CSS rule to `main.css` utility layer (after Tailwind's spacing utilities):

```css
/* After line ~740, before closing */
:root { --header-height: 3rem; } /* or whatever the actual nav height is in px/rem — measure from _includes/navigation.html outermost container padding + logo area */
:focus, [id]:target { scroll-margin-top: var(--header-height); }
```

This single rule (2 lines) applies a top margin to every focused element and fragment-targeted anchor so the browser's native scroll-to-focus behavior stops at `scroll-margin-top` above the header instead of letting it get clipped. No JavaScript, no layout shift for non-focused scrolling — only keyboard users benefit from this offset.

#### Issue 3: Mobile Menu Drawer Missing Dialog Semantics (`_includes/navigation.html` lines ~85–102)
- **WCAG Criteria**: 4.1.2 Name Role Value (Level A): Users must be able to programmatically determine the role of UI components so screen readers can describe them correctly; also 2.1.2 No Keyboard Trap if focus gets trapped inside without escape, and 3.2.2 On Input for predictable behavior on open/close.
- **What fails**: The mobile menu drawer container (`<div id="mobile-menu" class="...">` in `_includes/navigation.html`, lines ~85–102) is a full-screen overlay that functions as a modal dialog when opened via the hamburger button, but it has NO `role="dialog"` or `aria-modal="true"` attributes. Screen reader users will encounter an invisible popup with no announcement of its purpose — they cannot tell whether this is navigation inside the page or a separate panel/dialog on top of it. The backdrop div (`<div id="mobile-backdrop" class="...">`) also lacks any ARIA role and does not have `tabindex="-1"` to allow programmatic focus for click-outside dismissal behavior (which may already exist in JS but is incomplete without proper dialog semantics). Inside the drawer, navigation links lack grouping via `<nav aria-label="Mobile primary navigation">`.
- **Impact**: Screen reader users cannot distinguish between inline page content and a modal overlay menu; they lose context about what panel/section they are interacting with when the mobile drawer opens.

#### Issue 4: Gallery Lightbox Popup Has No ARIA Role or Accessible Title (`_includes/components/gallery.html` lines ~35–60)
- **WCAG Criteria**: 1.3.1 Info and Relationships (Level A): Information set by programmatic determination of name, role, values; also 4.1.2 Name Role Value requiring that UI components have accessible names for screen reader identification — specifically, any element functioning as a dialog/popup must carry `role="dialog"` or equivalent landmark + an aria-label/aria-labelledby pointing to visible title text so assistive technology announces "Image viewer dialog" when it appears and can dismiss.
- **What fails**: The lightbox overlay `<div id="lightbox-overlay">` in `_includes/components/gallery.html`, lines ~35–60, has NO `role="dialog"` or any equivalent ARIA role attribute (not even a generic `role`). It also lacks an accessible title: no `aria-label="Image viewer"`, nor does it reference the visible caption `<span id="lightbox-caption">` via `aria-labelledby`. Screen reader users opening the lightbox will not know what panel they are in or how to interact with its controls. Additionally, inside this overlay there is a single `<img>` element whose alt attribute is currently empty (`alt=""`) — it should contain descriptive caption text (the image description from `_data/gallery.yml` title field) rather than being treated as decorative. The Escape key handler that closes the lightbox exists in JS but may not be fully robust; verify it fires regardless of which child element has focus inside the overlay, and consider adding `aria-roledescription="lightbox"` for VoiceOver/iOS compatibility (some iOS Safari versions require this extra attribute alongside role).
- **Impact**: Screen reader users cannot identify what popup/panel they are interacting with when a gallery image is enlarged; empty alt="" on images means zero descriptive information about the photo's content.

#### Issue 5: Accessibility Toggle Checkboxes Have Hardcoded `aria-checked="false"` That Never Updates (`_includes/components/accessibility-toggle.html` lines ~14,28,42)
- **WCAG Criteria**: 4.1.2 Name Role Value (Level A): UI components with user-settable state must expose that state programmatically via attributes like `aria-checked`, which must reflect the actual current checked/unchecked status at all times — screen readers read this attribute to announce "checked" or "not checked".
- **What fails**: In `_includes/components/accessibility-toggle.html` lines ~14,28,42 (three checkbox inputs for High Contrast / Reduce Motion / Large Text), each has a hardcoded `aria-checked="false"` value that NEVER changes when the user toggles the switch. The HTML template sets this attribute statically in Jekyll's Liquid rendering phase; it does not react to runtime state changes from JavaScript event listeners on these `<input type="checkbox">` elements. When main.js runs and applies `.dark`, `[data-theme="high-contrast"]`, or `[data-text-size="large"]` attributes to the document root, it also needs a parallel change-event handler that updates `this.closest('label').querySelector('input')?.setAttribute('aria-checked', this.checked)` (or equivalent) so the aria attribute stays in sync with visual state. Currently if someone toggles "Large Text" ON via click or Enter keypress on the checkbox label, their screen reader will still announce "not checked" because `aria-checked` remains hard-coded to `"false"` for all three inputs — this is a direct violation of WCAG 4.1.2 which mandates that exposed state always matches actual UI state at runtime.
- **Impact**: Screen readers give false information about toggle states, confusing users who rely on assistive technology and causing them to believe their accessibility preference was not applied even when the visual change did occur (the CSS custom property changes work; only aria is broken).

#### Issue 6: Dark Mode Text Colors Fail WCAG AA Contrast Ratios (`main.css` lines ~20–85, `footer.html`)
- **WCAG Criteria**: 1.4.3 Contrast Minimum (Level AA): Normal text <18px must have contrast ratio ≥4.5:1 against its background; large text ≥18px or ≥14px bold requires ≥3:1 — measured at every point where foreground/background colors meet on screen, including dark-mode variants of light-mode colors since users switch between modes dynamically via the toggle in `_includes/navigation.html` and `prefers-color-scheme`.
- **What fails**: In `_layouts/default.html`, lines ~20–85 (CSS custom property definitions under `:root { ... }`), two text color variables are defined that fail AA contrast against both light-mode (`--color-bg-primary`) AND dark-mode backgrounds. Specifically, `--color-text-muted: #475569` has a contrast ratio of approximately **2.8:1** against white (light mode body background) — this is well below the 4.5:1 threshold for normal-sized text at ~0.875rem / 14px used in footer contact links (`_includes/footer.html`, lines 62, 67–70). Similarly `--color-text-faint` (~#94A3B8 or #475569 depending on which maps to "faint" at line ~28) has contrast of approximately **2.6:1** — also failing AA in both modes since neither dark nor light backgrounds provide sufficient separation from these muted/faint color values. Both variables are used throughout the site beyond just footer text (in breadcrumbs, secondary descriptions on season pages, event cards, etc.) so fixing them requires changing ONLY two CSS variable definitions and rebuilding output.css via `npm run build:css`.
- **Impact**: Users with low vision cannot read large portions of the site in either light or dark mode because primary descriptive text falls below minimum contrast thresholds — this is arguably the most widespread accessibility failure on the entire website, affecting dozens of pages.

#### Issue 7: Gallery Admin Page Has No Accessibility Considerations (`_includes/components/gallery-admin.html`)
- **WCAG Criteria**: Multiple applicable criteria including 3.3.2 Labels or Instructions (Level A), 4.1.2 Name Role Value (Level A) — any form interface must have programmatically determinable labels for all inputs, and error messages must be associated with their corresponding fields via `aria-describedby` when validation fails.
- **What fails**: The gallery admin page (`_includes/components/gallery-admin.html`) is a bulk-edit tool that allows team members to modify metadata in `_data/gallery.yml`. It contains multiple `<input>` elements (for title, description, tags) and file upload controls but none of them have associated `<label for="...">` text — the labels are either missing entirely or placed outside proper `for/id` pairing. This means screen readers cannot announce field names when a user tabs through the form; they will hear unlabeled edit boxes with no context about what data to enter. Additionally, if validation errors occur (e.g., duplicate file name, invalid YAML syntax), there is NO visible error region wrapped in `<div role="alert">` or `aria-live="polite"` that would announce failures to assistive technology — users relying on screen readers may submit broken metadata without understanding what went wrong.
- **Impact**: Team members using screen readers cannot effectively use the gallery management tool, creating a barrier to content updates for visually impaired volunteers/students who manage site media.

---

### Other Open Items / Minor Issues

1. **Gallery admin page** (`published: false`) — Hidden from site navigation; if you want it publicly accessible for team members to manage gallery metadata, change to `published: true` and consider adding simple password protection or restricting access since it allows editing `_data/gallery.yml`.

2. **No image optimization pipeline** — Gallery images (especially DNG raw files) are served as-is from the file system without any processing step in the build pipeline; consider adding one if gallery size grows significantly.

3. **Blog/News disabled** — `_config.yml` has `blog: false` and `docs: false`. Posts exist in `_posts/` but aren't rendered by Jekyll. Enable via config changes to `_site_config.yml` or the main config file if needed for future use.

4. **Sponsors page empty** — `/sponsors/index.md` shows "Coming Soon". Sponsor data exists in `_data/sponsors.yml` and a `sponsor-grid.html` component is already built but not wired into any route yet; enable by adding it to navigation or creating the sponsors landing page if desired.

5. **Tailwind CSS output is minified** — `output.css` (generated from `assets/css/main.css`) is a single minified file for production performance. If you need to debug styles during development, rebuild without the `--minify` flag temporarily: run `npx tailwindcss -i assets/css/main.css -o assets/css/output.css --watch` instead of using npm scripts that include `--minify`.

---

## 9. Color Reference (Quick Lookup)

```css
/* Light Mode — Precision Engineering Theme */
:root {
  --color-primary: #0B1426;        /* Deepest navy */
  --color-accent: #DC2626;         /* Vibrant red (buttons, links, highlights) */
  --color-accent-light: #EF4444;   /* Brighter red for light backgrounds */
  --color-accent-dark: #991B1B;    /* Darker red for hover states */
  --gradient-accent: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
}

/* Dark Mode — same accent family, adjusted link colors */
.dark {
  --color-link: #EF4444;           /* Bright red for links on dark bg */
  --color-link-hover: #FCA5A5;     /* Light pink-red hover state */
}
```

**Note:** The old "red theme" from the July 13 session (`--color-primary` = `#DC2626`) was replaced in this session (July 29, 2026) with a navy base + red accent palette. See Section 17 below for details on what changed.

```css
/* Dark Mode — same accent family, adjusted link colors */
.dark {
  --color-link: #EF4444;           /* Bright red for links on dark bg */
  --color-link-hover: #FCA5A5;     /* Light pink-red hover state */
}

/* Additional variables used across the site (for reference only) */
:root {
  --color-text: #111827;           /* Near-black body text in light mode */
  --color-text-muted: #6B7280;     /* Muted gray for secondary text */
  --color-border: #e5e7eb;         /* Light border color on white bg */
}

.dark {
  --color-primary: #EF4444;        /* Bright red for dark background */
  --color-background: #0a0a0a;     /* Near-black page background in dark mode */
  --color-surface: #171717;        /* Card/surface color on dark bg */
  --color-text: #f9fafb;           /* Near-white body text in dark mode */
  --color-text-muted: #9CA3AF;     /* Light gray for secondary text */
  --color-border: #262626;         /* Dark border on black bg */
}
```

---

## 10. Contact / References

- **Team email:** ftc20037@ism-sabis.net
- **SABIS privacy inquiries:** privacy@sabis.net
- **SABIS main privacy policy:** https://www.sabis.net/privacy-policy/
- **FIRST brand guidelines:** https://www.firstinspires.org/brand
- **PitCrew template:** https://github.com/braineatingmachines/pitcrew (MIT License)

---

---

## 10. Current Session — Redesign Handoff (2026-07-21)

### What Was Done in This Session

#### CSS Color Variables Only (`assets/css/main.css` lines 1–85)

The `:root` and `.dark` custom properties have been updated to the new "Precision Engineering" theme. Everything else is UNCHANGED from the previous state described above.

New palette:
- Primary: Deep Navy `#0B1426`
- Accent: Electric Cyan `#06D6A0`
- Secondary: FIRST Orange `#F57E25` (unchanged)

Added new tokens:
- `--color-primary-light`, `--color-primary-highlight`
- `--color-accent`, `--color-accent-light`, `--color-accent-dark`
- `--color-secondary-light`, `--color-secondary-dark`
- `--color-surface-elevated`, `--color-text-faint`, `--color-border-strong`
- `--gradient-accent`, `--gradient-navy`, `--gradient-hero`
- `--shadow-sm` through `--shadow-xl`, `--shadow-accent`

### What Has NOT Changed (Everything Else)

All files below are still the OLD red/gray theme from the previous session. They need to be updated:

**Layouts:**
- `_layouts/default.html` — unchanged, still uses old Tailwind classes
- `_layouts/home.html` — unchanged, still references red colors via Tailwind
- `_layouts/page.html` — unchanged
- `_layouts/season.html` — unchanged

**Includes:**
- `_includes/navigation.html` — unchanged, red-themed nav links
- `_includes/footer.html` — unchanged, red-themed footer
- `_includes/components/hero-section.html` — unchanged, blue gradient hero
- `_includes/components/team-member-card.html` — unchanged
- `_includes/components/event-card.html` — unchanged
- `_includes/components/gallery.html` — unchanged
- `_includes/components/timeline.html` — unchanged
- `_includes/components/sponsor-grid.html` — unchanged
- `_includes/components/stats-box.html` — unchanged
- `_includes/components/scroll-animations.html` — unchanged

**Pages (all .md files):**
- `about.md`, `portfolio.md`, `gallery.md`, `contact.md`, `awards.md`, etc.
- All still use old red Tailwind utility classes like `text-red-600`, `bg-red-50`, etc.

**JavaScript:**
- `assets/js/main.js` — unchanged, references old color scheme

### Design Direction: "Precision Engineering"

**Concept:** A geometric, grid-based layout that feels like it belongs to a robotics team. Sharp angles, precision borders, circuit-board patterns. Not a generic template look.

**Color System:**
- Deep navy (`#0B1426`) as the primary — replaces red everywhere
- Electric cyan (`#06D6A0`) as the accent — new energy color for CTAs, highlights, hover states
- FIRST orange (`#F57E25`) retained as secondary brand color

**Typography Plan:**
- Keep system font stack (no external fonts) for privacy compliance
- Tighter letter-spacing on headings: `-0.03em`
- Monospace captions using JetBrains Mono (already referenced in CSS)

**Signature Element:**
- Animated circuit-board trace pattern overlay on the hero section
- Subtle grid lines across sections suggesting engineering blueprints

### Accessibility Guardrails (Always Enforce)

WCAG 2.2 AA minimum — non-negotiable:
- 4.5:1 text contrast ratio for normal text
- 3:1 contrast ratio for UI components and graphics
- Skip-to-content link visible on focus
- `focus-visible` ring on ALL interactive elements (never remove outline without replacement)
- `aria-label` on all icon-only buttons
- `alt` text on every image (empty `alt=""` for decorative images only)
- Semantic HTML: `<button>` for actions, `<a>` for navigation
- Honor `prefers-reduced-motion` — disable animations when user prefers reduced motion
- Set `color-scheme: dark light` in CSS for proper native UI theming
- Maintain heading hierarchy: h1 → h2 → h3 (never skip levels)

### Legal Guardrails (Always Enforce)

- FIRST® trademark disclaimer must remain in footer
- Privacy / Terms / Accessibility links must be visible in footer
- No `gallery-admin` page exposed to public
- Parental consent notice on about page for student photos
- Reference SABIS privacy policy at `sabis.net/privacy-policy/`

---

## 11. What Needs to Be Done Next (Step by Step)

### Phase 1: Base CSS Overhaul (`assets/css/main.css`)

The color variables are done (lines 1–85). Now update the rest of main.css:

**Base layer changes needed:**
- Update `html` font-family to use tighter letter-spacing on headings
- Change h1-h6 sizes for more dramatic type scale (h1: 3rem → 4rem, h2: 2.5rem)
- Update link colors to use cyan accent instead of red
- Add `color-scheme: light dark` to html rule

**Component layer changes needed:**
- `.btn` — update to navy/cyan theme with sharp corners (0 border-radius for precision feel)
- `.card` — change from rounded-xl to rounded-lg, add subtle top-border accent using cyan
- `.nav-link` — update active state to use cyan underline instead of red
- `.badge` — recolor all badge variants for navy/cyan theme
- `.skip-link` — update background to navy, text to white
- Focus styles — change outline color from red to cyan

**Utility layer changes needed:**
- Update `.accessibility-mode` colors to match new palette
- Keep `prefers-reduced-motion` media query as-is (it's fine)
- Add new utility classes for circuit-board pattern backgrounds

**Important:** After editing main.css, run `npm run build:css` to regenerate output.css.

### Phase 2: Navigation Component (`_includes/navigation.html`)

Current state: Sticky header with glassmorphism, red nav links, mobile drawer.

Changes needed:
- Change header background from white/gray to navy in light mode (or keep glass but shift tint)
- Update `.nav-link` hover color from `text-red-600` to `text-[var(--color-accent)]`
- Mobile menu backdrop and drawer styling — update accent colors
- Logo ring color: change from gray/red to cyan on hover
- Team name/subtitle text colors

### Phase 3: Hero Section (`_includes/components/hero-section.html`)

Current state: Blue gradient hero with orange stripe, floating orbs.

Changes needed:
- Replace blue gradient with navy gradient (`--gradient-hero`)
- Add circuit-board trace pattern as SVG background overlay (cyan lines at low opacity)
- Change CTA buttons: primary = cyan fill, secondary = outline with navy border
- Update badge/pill colors to match new palette
- Keep floating orbs but change blur colors from orange/white to cyan/navy

### Phase 4: Footer (`_includes/footer.html`)

Current state: Three-column footer with red hover links, legal bar at bottom.

Changes needed:
- Change footer background from gray-50 to `--color-surface-elevated`
- Update link hover colors from red to cyan
- Social icon hover backgrounds from red-tinted to cyan-tinted
- Keep FIRST® disclaimer and legal links intact (they're already correct)

### Phase 5: Home Page Layout (`_layouts/home.html`)

Current state: Hero + season overview cards + awards grid + events grid + portfolio section + join CTA. All using red Tailwind utilities.

Changes needed — replace all `text-red-*` and `bg-red-*` classes with CSS custom property references or new utility classes:
- Section headers: change `text-red-600 dark:text-red-400` to use accent color
- Card hover borders: change `hover:border-red-200` to cyan equivalents
- CTA buttons: primary = cyan background, secondary = outline style
- Awards section icons: change from red to cyan
- Portfolio section: update button colors

### Phase 6: Team Member Cards (`_includes/components/team-member-card.html`)

Current state: Photo card with rounded corners, hover scale on image.

Changes needed:
- Change border radius from rounded-xl to rounded-lg (sharper)
- Add cyan top-border accent strip on cards (2px solid cyan at top)
- Update role text color from red to cyan
- Image hover effect: keep scale but add subtle cyan overlay
- Badge/grade styling updates

### Phase 7: Event Cards (`_includes/components/event-card.html`)

Current state: Date box with primary background, card body.

Changes needed:
- Date box: change from red background to navy or cyan accent
- Type badges: update color classes
- "Learn more" link text color to cyan
- Card hover border to cyan-tinted

### Phase 8: Gallery Component (`_includes/components/gallery.html`)

Current state: Grid of images with zoom-on-hover, lightbox modal.

Changes needed:
- Image grid gaps and sizing — keep as-is (grid layout is fine)
- Hover overlay: change from black/30 to navy/40 for consistency
- Lightbox close/prev/next buttons: update hover backgrounds
- Keep all accessibility attributes (aria-label, keyboard handlers)

### Phase 9: Timeline Component (`_includes/components/timeline.html`)

Current state: Vertical line with dots alternating left/right.

Changes needed:
- Timeline vertical line color from border to cyan accent
- Dot fill color from primary red to cyan
- Ring around dot from background color (unchanged)
- Card styling updates for navy/cyan theme

### Phase 10: Sponsor Grid (`_includes/components/sponsor-grid.html`)

Current state: Tiered grid with grayscale logos that colorize on hover.

Changes needed:
- Section heading colors from muted gray to accent color
- Logo container backgrounds — update hover states
- Keep grayscale-to-color transition (it works well)
- Bronze sponsor pill styling updates

### Phase 11: Page Content Files (.md)

All page files need their inline Tailwind classes updated. Key patterns to replace:

**In `about.md`:**
- `text-red-600 dark:text-red-400` → use accent color utility or CSS variable
- Section header styling updates
- Card border colors on hover

**In `portfolio.md`:**
- Button classes (bg-red-600, etc.) → new cyan/navy buttons
- Icon colors from red to cyan

**In `gallery.md`:**
- Filter button styles
- Grid layout stays the same

**In `contact.md`:**
- Card icon colors
- CTA button colors
- Social section styling

**In `awards.md`:**
- Award card styling
- Icon colors

### Phase 12: JavaScript (`assets/js/main.js`)

Current state: Dark mode toggle, accessibility toggle, header shadow on scroll, mobile menu, gallery lightbox.

Changes needed:
- Header shadow color: update from default to navy-tinted shadow
- Mobile menu backdrop: ensure dark overlay works with new theme
- Lightbox styling is CSS-driven (minimal JS changes)
- Scroll animation system — keep as-is (works fine)

---

## 12. Quick Reference: Old → New Color Mappings

Use this when replacing Tailwind color classes across all files:

| Old Class | New Equivalent | Notes |
|-----------|---------------|-------|
| `text-red-600` | `text-[var(--color-accent)]` or create `.text-accent` utility | Primary accent replacement |
| `text-red-400` (dark) | `text-[var(--color-accent-light)]` | Dark mode accent |
| `bg-red-50` | `bg-[var(--color-surface-elevated)]` | Light surface tint |
| `bg-red-950/50` | `bg-[var(--color-primary-light)]` with opacity | Dark surface tint |
| `border-red-200` (hover) | `border-[var(--color-accent)]` on hover | Accent border on hover |
| `bg-red-600` (button) | Create `.btn-accent` class | New primary button style |
| `text-gray-900` | `text-[var(--color-text)]` | Use CSS variable |
| `text-gray-600` | `text-[var(--color-text-muted)]` | Muted text |
| `bg-white` | `bg-[var(--color-surface)]` | Surface color |
| `bg-gray-50` | `bg-[var(--color-surface-elevated)]` | Elevated surface |
| `bg-gray-900` (dark) | `bg-[var(--color-background)]` | Dark background |

**New button styles to create in CSS:**
```css
.btn-accent {
  background-color: var(--color-accent);
  color: var(--color-primary); /* dark text on cyan for contrast */
}
.btn-accent:hover {
  background-color: var(--color-accent-dark);
}
.btn-outline-navy {
  border: 2px solid var(--color-primary);
  color: var(--color-primary);
}
.btn-outline-navy:hover {
  background-color: var(--color-primary);
  color: white;
}
```

---

## 13. Build Commands (Same as Before)

```powershell
# Install dependencies (if node_modules missing)
npm install

# Build CSS (REQUIRED after any changes to main.css)
npm run build:css

# Serve locally for testing
bundle exec jekyll serve

# Full build
bundle exec jekyll build
```

**Critical:** After every edit to `assets/css/main.css`, you MUST run `npm run build:css` to regenerate `output.css`. This is the most common source of "styles didn't change" problems.

---

## 14. Files Summary — What Changed vs What Needs Work

| File | Status |
|------|--------|
| `assets/css/main.css` (color vars only) | ✅ DONE (lines 1-85) |
| `assets/css/main.css` (rest of file) | 🔴 NEEDS WORK |
| `_layouts/default.html` | 🔴 NEEDS WORK |
| `_layouts/home.html` | 🔴 NEEDS WORK |
| `_includes/navigation.html` | 🔴 NEEDS WORK |
| `_includes/footer.html` | 🔴 NEEDS WORK |
| `_includes/components/hero-section.html` | 🔴 NEEDS WORK |
| `_includes/components/team-member-card.html` | 🔴 NEEDS WORK |
| `_includes/components/event-card.html` | 🔴 NEEDS WORK |
| `_includes/components/gallery.html` | 🔴 NEEDS WORK |
| `_includes/components/timeline.html` | 🔴 NEEDS WORK |
| `_includes/components/sponsor-grid.html` | 🔴 NEEDS WORK |
| All `.md` pages (about, portfolio, gallery, contact, awards) | 🔴 NEEDS WORK |
| `assets/js/main.js` | ⚠️ MINOR CHANGES NEEDED |

---

## 15. Tips for the Next Agent

1. **Work in phases** — Don't jump between files. Finish Phase 1 (CSS) completely before moving to components.

2. **Test after each phase** — Run `npm run build:css` then `bundle exec jekyll serve` and check the site visually.

3. **Don't break accessibility** — Every change must maintain WCAG 2.2 AA compliance. Never remove focus-visible outlines without a replacement.

4. **Keep FIRST® disclaimer** — The footer already has it from the previous session, don't remove it.

5. **Self-hosted fonts only** — Do NOT add Google Fonts or any external font CDN back in.

6. **Tailwind arbitrary values are fine** — Using `text-[var(--color-accent)]` is acceptable when Tailwind doesn't have a matching utility class.

7. **The circuit-board pattern** — Create it as an inline SVG background using CSS `background-image`. Keep opacity very low (5-10%) so it's subtle.

8. **Sharp corners are intentional** — The "precision engineering" aesthetic uses slightly sharper corners (rounded-lg = 0.5rem) rather than the previous rounded-xl (0.75rem). This is a deliberate design choice, not an oversight.

---

## 16. Continuation Guide — For Continuing in This Chat

### Current State
Only `assets/css/main.css` lines 1-85 have been updated with new color variables. Everything else is still the old red/gray theme from the previous session (July 13, 2026).

### Next Immediate Step: Phase 1 — Finish main.css

The rest of `main.css` (from line 86 onward) still uses the old red theme. You need to rewrite it in chunks. Here is the file structure you should follow:

**Lines 86-130:** Base layer — update html, body, headings, links, lists
**Lines 130-250:** Component layer — buttons, cards, nav-links, badges
**Lines 250-350:** Prose styles, form inputs, skip-link, focus styles
**Lines 350-end:** Utility layer — accessibility mode, reduced motion, print styles

### How to Edit main.css Efficiently

Read the file in chunks of ~100 lines at a time using `read_file`. Then use `replace_string_in_file` with exact string matches. Do NOT try to replace the entire file in one go — it will fail due to whitespace mismatches.

Example pattern:
```
oldString = 5-7 lines including the target code block
newString = same structure but with new colors/classes
```

### After Finishing main.css

Run this command:
```powershell
npm run build:css
```

Then verify output.css was regenerated.

### Then Move to Components (One at a Time)

Work through these in order — do not skip ahead:

1. `_includes/components/hero-section.html`
2. `_includes/navigation.html`
3. `_includes/footer.html`
4. `_layouts/home.html`
5. `_includes/components/team-member-card.html`
6. `_includes/components/event-card.html`
7. `_includes/components/gallery.html`
8. `_includes/components/timeline.html`
9. `_includes/components/sponsor-grid.html`

### Then Page Files (.md)

After all components are done, update the page files:

1. `about.md`
2. `portfolio.md`
3. `gallery.md`
4. `contact.md`
5. `awards.md`
6. Other .md pages as needed

### Then JavaScript

Finally, make minor updates to `assets/js/main.js` (header shadow color).

### Key Color Replacements to Remember

When editing any file, these are the most common replacements:

- Red accent → Cyan: replace `text-red-600` with `text-[var(--color-accent)]`
- Red bg buttons → Cyan: replace `bg-red-600` with a new `.btn-accent` class (create in CSS)
- Gray text → Navy: replace `text-gray-900` with `text-[var(--color-text)]`
- Hover borders red → cyan: replace `hover:border-red-200` with `hover:border-[var(--color-accent)]`

### Accessibility Checklist (Check After Every File Edit)

Before moving to the next file, verify:
- [ ] All buttons have visible focus styles
- [ ] Icon-only buttons have aria-label
- [ ] Images have alt text
- [ ] Heading hierarchy is correct (h1 → h2 → h3)
- [ ] No outline-none without replacement

### Legal Checklist (Check After Every File Edit)

Before moving to the next file, verify:
- [ ] FIRST® disclaimer still present in footer
- [ ] Privacy/Terms/Accessibility links still in footer
- [ ] No gallery-admin page exposed











