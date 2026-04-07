---
layout: season
title: "2025-2026 Season"
season: "2025-2026"
game_name: "DECODE"
robot_name: "Something II"
permalink: /seasons/2025-2026/
---

## Robot Overview {#robot}

Phoenix is our INTO THE DEEP robot, built around a custom mecanum drivetrain and iterative subsystem development to maximize scoring consistency.

### General Design Direction

- Mecanum drive selected for high maneuverability and cycle efficiency
- Custom drivetrain architecture optimized for scoring potential

### Chassis Design

- Custom 1/8 inch 5052 aluminum plates from SendCutSend
- Seven motors mounted between inner and outer panels
- Pocketed plates for weight reduction and wire management
- Drag chain to protect turret wiring
- Integrated battery door for quick swaps

### Intake and Deposit Iterations

1. Dual flywheel with fins and 2-axis wrist
2. Internalized wrist plus polycarbonate backplate
3. Flat flywheel with adjustable hood
4. Rear flywheel removed
5. Fixed hood (strong long-range consistency, weaker close-range adaptability)
6. Planned return to adjustable hood

### Lift System Iterations

- Initial flat-beam scissor lift was too weak
- Reinforced beams increased strength but reduced extension height
- Additional beams restored height but introduced separation risk
- Bottom plate prevented beam separation
- Custom coupler solved torque slippage
- Worm-gear flipper redesign showed insufficient tooth engagement and axial support

### Indexer Iterations

1. Dual-path servo feed (unreliable)
2. Mini mecanum carousel (too large and motor-heavy)
3. Carousel plus funnel plus Geneva mechanism (functional but lacked independent control)
4. Axon-servo carousel (best performer)
5. Planned servo-kicker tray (jam risk under evaluation)

### Kicker Iterations

- Shortened kicker to reduce torque demand
- Added anti-empty-fire logic
- Added rigid servo mount
- Switched to metal gears to eliminate stripping

### CAD and 3D Printing

- Onshape for CAD and modular design
- PETG-CF for rapid iteration
- Printers: Bambu P1S, Bambu X1C, Prusa MK3S+, Anycubic Vyper

---

## Autonomous Capabilities {#auto}

Our autonomous can score LEAVE points and some artifacts from any start position, and can adjust around alliance partner paths.

### Minimum Goal

- Score LEAVE points in auto
- Score some artifacts
- Achieve a partial park

### Maximum Goal

- Score 3 artifacts in auto
- Score consistently in teleop
- Complete full plus partial return-to-base in endgame

### Design Process

Identify -> Ideate -> Design -> Create -> Test

Adapted from former team Catlateral Damage.

### Driver Controls

- Three trigger-based controller layers
- Precision speed toggle
- Macros for flywheel, intake, and turret
- Manual override always available
- Color-sensor-aware macro behaviors
- Automatic aiming and dynamic shot-power math

---

## The Team {#team}

<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
{% for member in site.data.team %}
{% include components/team-member-card.html member=member %}
{% endfor %}
</div>

---

## Outreach {#outreach}

This season's outreach work focused on motivating future students and connecting with industry support.

### Motivate

#### Valentine's Bot Event

We built a gifting robot that delivered chocolates and 3D-printed gifts around campus, engaging hundreds of students.

#### International Day Robotics Exhibition

We hosted a robotics room with robot demos, notebook displays, and STEM activities to recruit and inspire new students.

#### City Park Demonstration

We demonstrated our robot in a public park and let visitors drive it while learning FTC systems.

### Connect

#### Problem/Solution: Lift Mechanism Failure

Our original endgame lift used a three-gear train and coupler driving a lead screw. The coupler repeatedly failed to transfer torque reliably.

#### Esmeril Industries Trip

Through a parent-connected industrial manufacturing visit, we received analysis help and designed a custom coupler that resolved the torque issue.

---

## Competition Results {#results}

Current event results are in progress and will be updated after official postings.

---

## Gallery {#gallery}

Coming Soon - Check Back Later.

---

## Controls Details {#controls}

Coming Soon - Check Back Later.

---

## CAD Preview {#cad}

Coming Soon - Check Back Later.

---

