---
layout: page
title: About Us
description: Learn about our team's history, mission, and the passionate students who make it all happen.
permalink: /about/
---

## Our Mission

We are a FIRST {{ site.site.program }} team dedicated to inspiring students in science, technology, engineering, and math (STEM) through hands-on robotics experience. We believe in **Gracious Professionalism** and **Coopertition** - the core values that make FIRST unique.

## Team History

{% assign history = site.data.team_history %}
{% if history %}
{% include components/timeline.html events=history %}
{% else %}

Our team was founded with a simple goal: give students the opportunity to learn real-world engineering skills while having fun competing in robotics competitions.

Since our founding, we've grown from a small group of students meeting after school to a thriving program with multiple subteams, dedicated mentors, and a track record of success at competitions.

{% endif %}

## Our Team

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

## What We Do

### Build Season
During build season, we design, build, and program a competition robot in just a few weeks. This intense period teaches us project management, teamwork, and technical skills.

### Competition Season
We compete at local league meets, qualifiers, and championships. These events are not just about winning - they're about learning, collaborating with other teams, and having fun.

### Outreach
We're committed to giving back to our community. We host STEM workshops, mentor younger teams, and demonstrate robotics at local events to inspire the next generation of engineers.

## Join Our Team {#join}

Interested in joining our team? We welcome students of all skill levels! Whether you're interested in building, programming, design, marketing, or outreach - there's a place for you.

**Requirements:**
- Be a student in grades 7-12
- Commit to attending team meetings regularly
- Have a passion for learning and teamwork

**No prior experience necessary!** We'll teach you everything you need to know.

[Contact us](/contact/) to learn more about joining the team.
