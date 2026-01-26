---
layout: page
title: News & Updates
description: The latest news, updates, and stories from our team.
permalink: /news/
---

Stay up to date with our team's activities, competition results, and community events.

<div class="space-y-8 my-8">
{% assign posts = site.posts | sort: "date" | reverse %}
{% for post in posts %}
<article class="card">
  <div class="card-body">
    <div class="flex flex-col md:flex-row gap-6">
      {% if post.image %}
      <div class="md:w-48 flex-shrink-0">
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="w-full h-32 md:h-full object-cover rounded-lg">
      </div>
      {% endif %}
      <div class="flex-grow">
        <div class="flex items-center gap-2 mb-2">
          <time datetime="{{ post.date | date_to_xmlschema }}" class="text-sm text-[var(--color-text-muted)]">
            {{ post.date | date: "%B %d, %Y" }}
          </time>
          {% for category in post.categories %}
          <span class="badge badge-primary text-xs">{{ category }}</span>
          {% endfor %}
        </div>
        <h2 class="text-xl font-bold mb-2">
          <a href="{{ post.url | relative_url }}" class="hover:text-primary no-underline">{{ post.title }}</a>
        </h2>
        <p class="text-[var(--color-text-muted)]">{{ post.excerpt | strip_html | truncate: 200 }}</p>
        <a href="{{ post.url | relative_url }}" class="inline-flex items-center gap-1 text-primary mt-2 hover:underline">
          Read more
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </a>
      </div>
    </div>
  </div>
</article>
{% endfor %}
</div>

{% if posts.size == 0 %}
<div class="card">
  <div class="card-body text-center py-12">
    <p class="text-[var(--color-text-muted)]">No posts yet. Check back soon!</p>
  </div>
</div>
{% endif %}
