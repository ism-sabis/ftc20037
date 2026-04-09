---
layout: page
title: About Us
description: Learn about our team's history, mission, and the passionate students who make it all happen.
permalink: /about/
---

## Our Mission

We are a FIRST {{ site.site.program }} team dedicated to improving ourselves and our community through outreach, STEM learning, and inspiring younger students to explore robotics and engineering.

We also uphold **Gracious Professionalism** and **Coopertition** as the core values behind how we compete and collaborate.

## Team History

{% assign history = site.data.team_history %}
{% if history %}
{% include components/timeline.html events=history %}
{% else %}

Our team was founded with a simple goal: give students the opportunity to learn real-world engineering skills while having fun competing in robotics competitions.

Since our founding, we've grown from a small group of students meeting after school to a thriving program with multiple subteams, dedicated mentors, and a track record of success at competitions.

{% endif %}

## Our Team

Standard Deviation is a team of six students from the International School of Minnesota in Eden Prairie, Minnesota.

- 1 senior
- 1 junior
- 1 fifth-year sophomore
- 3 first-year sophomores
- 3 original members and 3 new members

### Current Members

<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
{% for member in site.data.team %}
{% include components/team-member-card.html member=member %}
{% endfor %}
</div>

### Mentors

<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
{% for mentor in site.data.mentors %}
{% include components/team-member-card.html member=mentor %}
{% endfor %}
</div>

## Future Goals

- Strengthen team skills, especially CAD and building
- Increase outreach hours
- Improve event performance
- Build stronger connections with lower school robotics

## Sustainability

We keep our program sustainable by using 3D printing and laser cutting to reduce costs while recruiting new students each year to maintain continuity.

## What We Do

### Build Season
During build season, we design, build, and program a competition robot in just a few weeks. This intense period teaches us project management, teamwork, and problem-solving.

### Competition Season
We compete at local league meets, qualifiers, and championships. These events are not just about winning - they're about learning, collaborating with other teams, and having fun.

### Outreach
We're committed to giving back to our community. We host STEM workshops, mentor younger teams, and demonstrate robotics at local events to inspire the next generation of engineers.

## Our Portfolio

Our engineering portfolio showcases the full story of Team Standard Deviation — from our design process and robot build to community outreach.

<div class="my-6 p-6 card">
  <div class="flex flex-col sm:flex-row items-center gap-6">
    <div class="text-5xl">📄</div>
    <div class="flex-1">
      <h3 class="font-bold text-lg mb-2">2025-2026 Robotics Portfolio</h3>
      <p class="text-[var(--color-text-muted)] mb-4">Explore our comprehensive engineering notebook covering robot design and outreach efforts.</p>
      <div class="flex flex-col sm:flex-row gap-3">
        <a href="{{ '/portfolio/' | relative_url }}" class="btn bg-[#003974] text-white hover:bg-[#002855] font-semibold px-5 py-2">View Portfolio</a>
        <a href="{{ '/assets/images/Robotics Portfolio 2025-2026.pdf' | relative_url }}" download class="btn bg-[#F57E25] text-white hover:bg-[#d96a1f] font-semibold px-5 py-2">Download PDF</a>
      </div>
    </div>
  </div>
</div>

## Join Our Team {#join}

Interested in joining our team? We welcome students of all skill levels! Whether you're interested in building, design, marketing, or outreach - there's a place for you.

**Requirements:**
- Be a student in grades 7-12
- Commit to attending team meetings regularly
- Have a passion for learning and teamwork

**No prior experience necessary!** We'll teach you everything you need to know.

[Contact us]({{ '/contact/' | relative_url }}) to learn more about joining the team.
