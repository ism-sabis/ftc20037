# Legal & Accessibility Compliance Plan — Team Standard Deviation (FTC 20037)

## Research Findings (2026-07-12)

### 1. School Privacy Policy Alignment ✅ RESEARCHED
**ISM/SABIS has an existing privacy policy:** https://www.sabis.net/privacy-policy/
- Updated October 2024
- Covers: data collection, Google Analytics, children's privacy, FERPA considerations
- Contact for data inquiries: **privacy@sabis.net**
- Data transferred to SABIS Educational Systems, Inc., Eden Prairie, Minnesota (same location as ISM)
- Children's privacy section explicitly addresses minors under applicable age
- Students/parents may use this site's privacy policy but it must reference and align with the main SABIS policy

### 2. Parental Consent for Student Photos ✅ RESEARCHED
- FERPA applies: ISM is a US educational institution receiving federal funds
- COPPA applies: some team members are under 13 (sophomores)
- SABIS privacy policy states minors must use services with parental/guardian supervision and consent
- **Recommendation**: Add a prominent notice on the About page linking to SABIS's main privacy policy, stating that student photos/names are published with appropriate parental consent per school district policy

### 3. Cookie Policy + Google Fonts ✅ RESEARCHED
- Current site uses: localStorage (dark mode, accessibility preferences) — strictly necessary, no consent required
- **Google Fonts issue**: Loading from fonts.googleapis.com and fonts.gstatic.com transmits IP addresses to Google servers in US/EU
- Under GDPR, this requires user consent for non-essential cookies/tracking
- **Solution**: Self-host the Google Fonts (Lato + Inter) locally instead of loading from Google's CDN. This eliminates IP transmission entirely and removes need for cookie consent banner

### 4. FIRST IP Compliance ✅ RESEARCHED
From FIRST Brand & Logo Files page:
- FIRST has strict brand guidelines: https://www.firstinspires.org/brand
- Team websites must comply with the Trademark & Copyrighted Materials Policy
- **Required disclaimer**: Teams cannot imply FIRST endorsement of their website or products
- FTC logo may only be used "in connection with official team, event, or program materials"
- LEGO trademarks are jointly held by FIRST and LEGO Group
- **Recommendation**: Add a footer disclaimer: "FIRST®, the FIRST® logo, and FIRST® Tech Challenge are trademarks of For Inspiration & Recognition of Science and Technology (FIRST®). This website is not endorsed by or affiliated with FIRST®."

### 5. Gallery Admin Page ✅ IDENTIFIED
- `/gallery-admin/` displays raw DNG files and metadata forms — this is a development/debugging aid
- **Must be removed** before production launch or made inaccessible

### 6. Existing Legal Documents
- **LICENSE**: MIT License (covers code only, not content) — appropriate for the template nature of the site
- No Privacy Policy page exists
- No Terms of Use page exists
- No Cookie Policy page exists
- No FIRST IP disclaimer in footer

---

## Design System: Red Theme (from jersey photos)

### Color Palette
| Role | Light Mode | Dark Mode | WCAG AA Ratio |
|------|-----------|-----------|---------------|
| **Primary Red** | `#DC2626` (vibrant red from jerseys) | `#EF4444` (slightly brighter for dark bg) | 4.53:1 on white / 5.94:1 on dark |
| **Red Dark** | `#B91C1C` (hover states, links) | `#DC2626` | — |
| **Red Light** | `#FEE2E2` (subtle backgrounds) | `#7F1D1D` | — |
| **White/Cream** | `#FFFFFF` / `#FAFAFA` | — | 18.5:1 on dark |
| **Black/Charcoal** | `#111827` (text) | `#F9FAFB` (light text) | — |
| **Gray** | `#6B7280` / `#D1D5DB` | `#9CA3AF` / `#374151` | 7:1 on white / 6.8:1 on dark bg |

### Typography
- Keep Inter (UI) + Lato (headings) — self-hosted to avoid Google tracking
- Font weights: 400 (body), 600 (subheads), 700 (headings), 900 (hero text)

### Design Direction
Modern, bold, energetic — matching the competitive spirit of FTC robotics. Red as accent/power color with clean whites and deep darks for contrast. Subtle animations: fade-ins on scroll, hover effects on cards, smooth transitions between light/dark mode.

---

## Implementation Plan (Phases)

### Phase 1: Legal Pages
1. Create `privacy.md` → `/privacy/` — Privacy Policy aligned with SABIS policy
2. Create `terms.md` → `/terms-of-use/` — Terms of Use
3. Merge cookie disclosure into Privacy Policy (no separate page needed since we self-host fonts)

### Phase 2: Accessibility Fixes
4. Audit all images for alt text quality
5. Check color contrast ratios across themes
6. Verify focus-visible styles on interactive elements
7. Test keyboard navigation through gallery lightbox, mobile menu

### Phase 3: Footer & Navigation Updates
8. Update footer with legal page links + FIRST IP disclaimer
9. Add "Privacy" and "Terms of Use" to footer Quick Links

### Phase 4: Frontend Redesign (Red Theme)
10. Update `_config.yml` palette colors → red theme
11. Update Tailwind config / CSS custom properties for new color scheme
12. Redesign hero section with animated gradient using red tones
13. Add scroll-triggered animations (fade-in, slide-up) to sections
14. Improve card hover effects and transitions
15. Ensure both light and dark modes look polished

### Phase 5: Cleanup
16. Remove or disable `/gallery-admin/` page
17. Self-host Google Fonts (download Lato + Inter, serve locally)
18. Add FIRST IP disclaimer to footer

---

## Key Decisions Made by User
1. ✅ Research school privacy policy → Found SABIS policy, will align with it
2. ✅ Research parental consent → FERPA/COPPA apply, add notice linking to SABIS policy
3. ✅ Cookie policy + Google Fonts → Self-host fonts (eliminates tracking entirely)
4. ✅ FIRST IP compliance → Add disclaimer footer text
