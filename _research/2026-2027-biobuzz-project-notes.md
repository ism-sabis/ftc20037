# FTC 20037 BIOBUZZ project notes

**Updated:** 2026-11-21  
**Team:** Standard Deviation, FTC 20037  
**Season:** BIOBUZZ presented by RTX, part of FIRST CANOPY

This is the working context for the 2026-2027 robot, website, and game strategy. The detailed cited game summary is `_research/2026-2027-biobuzz-game-reference.md` in the website repository and `research/2026-11-21-biobuzz-game-context.md` in the AI Playground project. Localization and pathing source notes are in `_research/2026-2027-ftc-localization-pathing-reference.md` and the companion AI Playground `research` folder. Confirm the current manual and Team Updates again before making competition decisions.

## Game context

- The current combined BIOBUZZ Competition Manual is TU10, updated November 19, 2026. The materials page listed Section 11 (Game Rules) as TU09 and Section 12 (ROBOT Construction Rules) as TU08 when this note was written.
- Two alliances collect POLLEN and NECTAR. The official game verb is **LAUNCH**. Elements launched into the upward-facing CELL of a HIVE can tip it; teams can also score in FLOWERS and GARDENS.
- A MATCH consists of 30 seconds of AUTO, an 8-second transition, and 2 minutes of TELEOP.
- Each ROBOT starts with four POLLEN. Tipping a HIVE unlocks one NECTAR for its corresponding alliance; remaining NECTAR may be entered with 60 seconds left.
- A HIVE TIP is worth 20 points. At the end of a MATCH, each element left in an upward-facing CELL is worth 2 points.
- FLOWER scoring opens in the final 60 seconds. The highest alliance-color NECTAR determines FLOWER ownership; each qualifying element scores 2 points, and the bottom-most NECTAR of that alliance's color earns a 5-point bonus.
- Each element in a GARDEN is worth 1 point for the matching alliance. Either alliance may remove elements from either GARDEN.
- A ROBOT may control at most four scoring elements at once. Do not design around controlling the opponent's NECTAR or catching elements falling from a tipped HIVE before they hit another surface.
- Starting size is limited to an 18 x 18 x 18 inch cube; the expanded ROBOT must remain within an 18 x 24 x 29 inch volume.

## Current robot CAD snapshot

- Fusion's active design is **Master Assembly V3** in the **2026-2027 BIOBUZZ** project.
- The user provided a color-annotated CAD view and explained the mechanisms. Treat this as team-provided design intent, not a validated physical mechanism sequence:
  - Purple/front: a front intake pivots up and down with gravity assisting its movement. Three rows of surgical tubing guide game elements through the robot. The linkage has not been confirmed as a four-bar; keep public wording generic until the CAD is checked.
  - Brown: a pair of spring-mounted flywheels, one on each side, can spread apart to passively accommodate both POLLEN and NECTAR. Added mass is intended to help them retain rotational speed. The team plans to keep them spinning between shots and use motor control to maintain a target RPM.
  - Rear flipper: acts as a retaining gate, holding an element until the team wants to release it for launch.
  - Green turret: normally aims the launcher at the HIVE CELL. A Limelight is mounted on the turret to help aim it; the exact vision mode or target detector is not specified.
  - Blue adjustable hood: part of the turret's launch-trajectory adjustment.
  - Yellow slide-out guide: extends on drawer slides to redirect a turret shot down through the top of a FLOWER. The user confirmed that the direct HIVE CELL shot and redirected FLOWER shot are the intended routing.
  - Red mechanism: servo-positioned ramp behind or inside the FLOWER lets POLLEN slide out through the bottom; it is not a pusher.
  - Drive: mecanum wheels. The chassis uses heavily pocketed 7075 aluminum panels to reduce weight.
- The user estimates the current robot at approximately **27 lb**.
- “Passive” describes the spring-mounted flywheels moving apart to accommodate either game element. The motors still actively maintain RPM, and the flipper controls release. Added flywheel mass is intended to help preserve speed between shots; do not describe the entire launcher as passive.
- The user confirmed **Pedro Pathing** as the planned motion/pathing software and identified **goBILDA odometry pods** plus an **IMU**. Public wording should stay general (“odometry pod and IMU”); the exact pod model and sensor arrangement are unspecified. “Aspen” remains unresolved.
- These mechanism descriptions are visible or team-described design intent, not tested performance claims. Confirm the final CAD and test hardware before presenting them as completed capabilities.
- The website asset is `assets/robot-viewers/2026-2027/turntable.html` in the website repository. It is a self-contained HTML turntable with embedded rendered frames, not a live 3D CAD model. The file is about 10 MB and is outside the repository's excluded `assets/models` folder.

### Assembly review confidence

A read-only Fusion review of Master Assembly V3 reported 2,453 occurrences, 1,159 joints, 138 rigid groups, and no root-level motion links. It also found several named gear and axle occurrences without direct joint or rigid-group connections. That is a reason to inspect the assembly constraints, not proof that those parts can move: full degrees of freedom were not established, and joint lock/suppression states could not be verified in that review. Physical endplay and backlash were not measured. No Fusion edits were made.

Useful follow-up checks are to verify which axles should rotate, whether each gear is rigidly attached to its axle, the remaining degrees of freedom and joint states, and physical endplay/backlash. Then test the intended POLLEN and NECTAR feed and launch paths with game elements.

## Website state and copy

- The current roster is Roshan, Ryan, Asif, Ean, Alex, Yevhen, and Lucas: two seniors, four juniors, and one seventh grader.
- Roshan and Ryan appear in every season in the archive. Asif, Ean, and Alex have been with the team since at least 2025-2026. Yevhen is joining Standard Deviation this season.
- Mentor support is one lead mentor with industry engineering experience.
- The public Team Overview should list the current seven members and team composition, without the archive-history and mentor-support bullets.
- Lucas's bio should say he enjoys taking things apart to see how they work, helps with building and disassembly, and keeps the team motivated.
- The “Additional Member — Coming Soon” card and matching Team Overview sentence have been removed.
- The public game name on this season page should be **BIOBUZZ** without “presented by RTX.” The full official game name remains in internal research notes.
- Current robot copy is in `_seasons/2026-2027.md`; use a first-person team voice, avoid an unverified four-bar claim, and describe the FLOWER POLLEN mechanism as a ramp that lets POLLEN slide out.
- The CAD preview uses a titled, lazy-loaded iframe. Keep the robot-name and design-in-progress notes next to that preview, remove the visible drag/36-view caption, and avoid scrollbars inside the frame.
- Team photos are shared across current and archived rosters. Use a centered, contain fit so portraits are not off-center or clipped.
- The Gallery is temporarily disabled in navigation and shows a brief unavailable notice at its direct URL; keep its content and image data so it can be re-enabled.
- Outreach this season includes a visit to Tolomatic's Hamel, Minnesota facility for a design review with an applications engineer, a controls engineer, and a mechanical engineer, followed by a facility tour. The team is also in communication with 99 Technologies for help improving robot-code efficiency. These details are team-reported.
- The team is still deciding its primary match strategy, so the public overview gives the HIVE launcher and FLOWER mechanisms balanced coverage.

## Open design questions

1. Confirm the exact odometry pod model, IMU arrangement, and vision method/target used by the turret-mounted Limelight.
2. “Aspen” remains unresolved; likely recall prompts include Road Runner or Pedro Pathing. Do not list Road Runner as part of this team's stack unless confirmed.
3. Verify the front intake linkage in CAD before naming its geometry; test the intake, tubing feed, flywheel spring travel/speed retention, and flipper release with both POLLEN and NECTAR.
4. Test the turret/hood and slide guide against the HIVE CELL and FLOWER top; verify the servo-positioned ramp lets POLLEN slide out through the FLOWER bottom.
5. The primary match strategy is still undecided. Later choose whether to prioritize HIVE tipping, FLOWER scoring, GARDEN scoring, or a combination.
6. Choose a robot name if the team wants one.

## Official references

- [FIRST Tech Challenge Game & Season Materials](https://ftc-resources.firstinspires.org/ftc/game) — current manual, Team Updates, Q&A, and game resources.
- [BIOBUZZ Competition Manual, TU10](https://ftc-resources.firstinspires.org/ftc/game/cm-html/BIOBUZZ%20Competition%20Manual%20-%20TU10.htm) — rules and definitions. Check for updates before relying on specific thresholds or constraints.
- [Tolomatic contact page](https://www.tolomatic.com/contact-us/) — company-published Hamel, Minnesota headquarters address. The design review and tour are team-reported.
- [99 Technologies](https://www.99technologies.com/life-at-99/) — company-published overview and Eagan, Minnesota address. Code-efficiency support is team-reported.
