---
layout: page
title: Judge Mode
description: Quick reference for competition judges - key team information at a glance.
permalink: /judge/
---

<div class="no-print mb-8 p-4 bg-accent/10 rounded-lg">
  <p class="text-sm"><strong>Note:</strong> This page is optimized for competition judges. <a href="javascript:window.print()" class="text-primary">Print this page</a> for a portable reference.</p>
</div>

## Team Overview

<div class="grid md:grid-cols-3 gap-4 my-6">
  <div class="card">
    <div class="card-body text-center">
      <p class="text-4xl font-bold text-primary">{{ site.site.team_number }}</p>
      <p class="text-[var(--color-text-muted)]">Team Number</p>
    </div>
  </div>
  <div class="card">
    <div class="card-body text-center">
      <p class="text-4xl font-bold text-primary">{{ site.site.program }}</p>
      <p class="text-[var(--color-text-muted)]">Program</p>
    </div>
  </div>
  <div class="card">
    <div class="card-body text-center">
      <p class="text-4xl font-bold text-primary">{{ site.data.team.size }}</p>
      <p class="text-[var(--color-text-muted)]">Team Members</p>
    </div>
  </div>
</div>

---

## Robot Overview

Our 2025-2026 robot uses a custom mecanum drivetrain and highly iterative subsystem design.

- **Drivetrain:** Mecanum with custom chassis, pocketed 5052 aluminum plates, drag-chain turret wiring protection
- **Intake/Deposit:** Six major iterations, currently converging on adjustable-hood flywheel architecture
- **Lift:** Scissor-lift-based architecture with custom coupler fix for torque transfer
- **Indexer/Kicker:** Iterative servo-based carousel and strengthened kicker with metal gears
- **Autonomous:** LEAVE plus artifact scoring from all start positions with path adaptation for alliance partners

[View detailed robot documentation →](/season/)

---

## Engineering Process

### Design Philosophy
Our design method is iterative and evidence-based:

Identify -> Ideate -> Design -> Create -> Test

This process is inherited from former team Catlateral Damage and applied to both hardware and software.

### Documentation
- Engineering notebook maintained throughout the season
- CAD models created in Onshape
- Regular design reviews with mentors

---

## Awards History

{% for award in site.data.awards limit: 6 %}
- **{{ award.name }}** - {{ award.event }} ({{ award.season }})
{% endfor %}

[View all awards →](/awards/)

---

## Outreach Impact

Our outreach strategy has two themes: Motivate and Connect.

- **Valentine's Bot Event:** Campus robot gift-delivery activity that engaged hundreds of students
- **International Day Exhibition:** Robotics room with demos, notebook walkthroughs, and STEM activities
- **City Park Demo:** Public drive experience and FTC systems education
- **Industry Collaboration:** Esmeril Industries tour and custom coupler support for lift torque issue

---

## Team Culture

### Core Values
- **Gracious Professionalism:** We compete hard but treat everyone with respect
- **Coopertition:** We help other teams succeed
- **Continuous Learning:** We embrace challenges as opportunities to grow

### Sustainability
- 3D printing and laser cutting reduce fabrication costs
- Annual recruitment ensures continuity and role handoff
- Budget control improved remaining budget from 2983 (2024) to 3367 (2025)

### Team and Mentor Snapshot

- Team members: Jason, Ryan, Roshan, Ean, Asif, Alex
- Composition: 1 senior, 1 junior, 1 fifth-year sophomore, 3 first-year sophomores
- Mentor: Erik (Lead Mentor, engineer at Amazon)

---

## Quick Links

- [Current Season Details](/season/)
- [About Our Team](/about/)

---

<div class="text-center text-sm text-[var(--color-text-muted)] mt-8">
  <p>{{ site.site.team_name }} | Team #{{ site.site.team_number }}</p>
  <p>{{ site.site.current_season }} Season</p>
</div>
