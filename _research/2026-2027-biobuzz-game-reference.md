# 2026–2027 FTC BIOBUZZ game reference

**Research checked:** 2026-11-21  
**Current manual:** BIOBUZZ Competition Manual, Version TU10, updated 2026-11-19. The materials page currently lists Section 11 (Game Rules) as TU09 (updated November 12) and Section 12 (ROBOT Construction Rules) as TU08 (updated November 5).

This note captures the game flow, scoring, and official language needed for the season page and robot discussion. The official game materials page lists TU10 as the current manual and also links the latest Team Updates and Q&A. Check those materials again before relying on a rule at an event; this is a quick reference, not a replacement for the manual. [FIRST Tech Challenge Game & Season Materials](https://ftc-resources.firstinspires.org/ftc/game)

## Game at a glance

- The official game name is **BIOBUZZ™ presented by RTX**, within the broader **FIRST® CANOPY™** season. [FIRST FTC game page](https://www.firstinspires.org/programs/ftc/game-and-season) · [Competition Manual, §§1, 7–8](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- Two alliances, each with two teams, collect **POLLEN** and **NECTAR**. They **LAUNCH** elements into the upward-facing **CELL** of their **HIVE**, and place elements in **FLOWERS**. Elements in a **GARDEN** can also score. [Competition Manual, §§8, 10.1](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- A MATCH has 30 seconds of autonomous **AUTO**, an 8-second AUTO-to-**TELEOP** transition, and 2 minutes of TELEOP. [Competition Manual, §10.1](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- The central frame holds a red and blue HIVE, each with two pivoting CELLS. Each HIVE tips when enough scoring elements are launched into its upward-facing CELL. There are four FLOWERS around the FIELD and alliance-colored GARDENS. [Competition Manual, §§8–9.7](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- Each ROBOT starts with four preloaded POLLEN. A TIPPED HIVE unlocks one additional NECTAR for its corresponding alliance; any remaining NECTAR can be entered when 60 seconds remain. [Competition Manual, §§10.1, 10.3.1, 11.4.6 (G426)](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)

## Scoring and timing

- A **HIVE TIP** is worth 20 points. At the end of the MATCH, each POLLEN or NECTAR remaining in an upward-facing CELL is worth 2 points. Launching into the upward-facing CELL is the only legal way to induce a HIVE TIP. [Competition Manual, §§10.5.1, 10.5.5 and 11.4.4 (G417)](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- FLOWER scoring opens with 60 seconds left. POLLEN and NECTAR score in the volume between the top and middle rings. The alliance whose color NECTAR is highest in a FLOWER owns it and scores 2 points for each qualifying element there; the bottom-most NECTAR of an alliance’s color earns a 5-point bonus. Only the top of a FLOWER may be used to enter elements, and only POLLEN may be removed through its bottom. [Competition Manual, §10.5.2 and §11.4.3–4 (G410, G418)](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- Each POLLEN or NECTAR in a GARDEN is worth 1 point for the alliance matching that GARDEN’s color. Either alliance may remove elements from either GARDEN. [Competition Manual, §10.5.3](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- A ROBOT earns 3 points for leaving the perimeter wall in AUTO and 5 points for parking in the LOADING ZONE in either AUTO or TELEOP. [Competition Manual, §10.5.4–5](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- At most four scoring elements may be under a ROBOT’s control at once. A ROBOT may not control the opponent’s NECTAR, and may not catch elements falling from a tipped HIVE before they contact something else. [Competition Manual, §11.4.3 (G407–G409)](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- For Regional Championships and most other events, TU10 lists thresholds of 16 combined LEAVE + PARK points for a SWARM RP, 4 HIVE TIPS for POLLINATOR 1 RP, and 7 HIVE TIPS for POLLINATOR 2 RP. FIRST Championship thresholds are TBA, and Premier Events may set their own thresholds. [Competition Manual, §10.5.5](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)

## Language for the website

- The manual’s defined action is **LAUNCH/LAUNCHING**. Its glossary definition includes shooting an element into the air, propelling it across the floor, or throwing it forcefully. “Shoot” is understandable in casual copy, but **launch** matches FIRST’s terminology. [Competition Manual, §16](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- **POLLEN**, **NECTAR**, **HIVE**, **CELL**, **FLOWER**, **GARDEN**, **AUTO**, and **TELEOP** are defined game terms and appear capitalized in the manual. Keeping that capitalization makes season copy easy to map to the rules. [Competition Manual, §1.7.1 and §16](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- “Passive” is not a defined BIOBUZZ term in the manual. Use it only to describe the team’s mechanism, and explain what is passive (for example, feeding or indexing) so it does not sound like a claim that the robot launches without an active mechanism. This is a terminology recommendation based on the manual’s glossary, not a rule interpretation.

**Provisional public-copy draft, based on the team’s stated design goal:**

> For BIOBUZZ, our robot is being designed to launch both POLLEN and NECTAR into the HIVE. We’re refining the design and will share more as we test it.

This draft describes design intent. Confirm the robot can launch both elements in practice before publishing capability as demonstrated. If “passively” refers to a specific feeder or indexing behavior, name that behavior separately once the team confirms it.

## Robot construction constraints

- Robot sizing remains an important design constraint: the starting configuration must fit an 18 x 18 x 18 in cube, and the expanded ROBOT must stay within an 18 x 24 x 29 in volume. BIOBUZZ has no ROBOT weight limit. Preloaded SCORING ELEMENTS may extend outside the starting volume. [Competition Manual, R102, R104-R105](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)

## Robot-design implications

These are engineering considerations inferred from the official game description, not claims about the current CAD or a completed robot:

- A shared path for both scoring elements may reduce mechanism changes during play, but it needs to feed and launch both reliably. FIRST notes that POLLEN and NECTAR are not perfectly spherical and may vary in size, so validate the actual elements through repeated intake and launch trials. [Competition Manual, §9.8](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- A launch mechanism aimed at the HIVE should target the upward-facing CELL. Flower scoring is a separate late-MATCH task and requires entering elements through the top. [Competition Manual, §§10.5.1–2, 11.4.4 (G417–G418)](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)
- The scoring sequence changes over the MATCH: four preloaded POLLEN are available at the start, HIVE TIPS unlock additional NECTAR, and FLOWER scoring opens during the final minute. Design and software plans should account for that progression. [Competition Manual, §§10.1, 10.3.1, 10.5.2 and 11.4.6 (G426)](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm)

## Primary sources

1. [FIRST Tech Challenge 2026–2027 Game & Season Materials](https://ftc-resources.firstinspires.org/ftc/game) — current manual version, section versions, Team Updates, official Q&A, and game animation.
2. [BIOBUZZ Competition Manual — HTML, Version TU10](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm) — updated 2026-11-19; §§8–10 and 16 provide the game overview, details, scoring, and defined terminology; §11 contains relevant gameplay rules.
