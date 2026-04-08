---
layout: page
title: Team Gallery
description: Photos uploaded to assets/images/gallery/uploads/ appear here automatically.
permalink: /gallery/
---

<div class="card mb-8">
  <div class="card-body">
    <p class="text-[var(--color-text-muted)]">
      Drop image files into <strong>assets/images/gallery/uploads/</strong> and they will show up here automatically.
    </p>
    <p class="text-[var(--color-text-muted)] mt-3">
      Add captions and tags in <strong>_data/gallery.yml</strong>. Use tags like <strong>2025-2026-DECODE</strong> or <strong>2024-2025-Into-the-Deep</strong> to filter by season. For raw <strong>.dng</strong> files, add a same-named <strong>.jpg</strong>, <strong>.jpeg</strong>, <strong>.png</strong>, or <strong>.webp</strong> preview in the same folder for a thumbnail.
    </p>
  </div>
</div>

{% assign gallery_images = site.static_files | sort: "name" %}
{% assign gallery_meta = site.data.gallery.items | default: empty %}

{% assign gallery_count = 0 %}
{% for image in gallery_images %}
  {% if image.path contains '/assets/images/gallery/uploads/' and image.name != '.gitkeep' %}
    {% assign gallery_count = gallery_count | plus: 1 %}
  {% endif %}
{% endfor %}

{% if gallery_count > 0 %}
<div class="flex flex-wrap gap-2 mb-6">
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="all">All</button>
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="2025-2026-DECODE">2025-2026 (DECODE)</button>
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="2024-2025-Into-the-Deep">2024-2025 (Into the Deep)</button>
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="outreach">Outreach</button>
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="build">Build</button>
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="robot">Robot</button>
  <button type="button" class="btn btn-secondary gallery-filter-btn" data-gallery-filter="events">Events</button>
</div>

<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 my-8">
  {% for image in gallery_images %}
  {% if image.path contains '/assets/images/gallery/uploads/' and image.name != '.gitkeep' %}
  {% assign image_base = image.name | split: '.' | first %}
  {% assign file_type = image.extname | downcase | remove: '.' %}
  {% assign meta = gallery_meta | where: "src", image.path | first %}
  {% if meta and meta.caption %}
    {% assign caption = meta.caption %}
  {% else %}
    {% assign caption = image_base | replace: '-', ' ' | replace: '_', ' ' | capitalize %}
  {% endif %}

  {% assign tags_text = '' %}
  {% assign season_label = '' %}
  {% if meta and meta.tags %}
    {% assign tags_text = meta.tags | join: ',' %}
    {% if tags_text contains '2025-2026-DECODE' %}
      {% assign season_label = '2025-2026 (DECODE)' %}
    {% elsif tags_text contains '2024-2025-Into-the-Deep' %}
      {% assign season_label = '2024-2025 (Into the Deep)' %}
    {% endif %}
  {% endif %}

  {% assign preview_src = '' %}
  {% if file_type == 'dng' %}
    {% for candidate in gallery_images %}
      {% assign candidate_base = candidate.name | split: '.' | first %}
      {% assign candidate_ext = candidate.extname | downcase | remove: '.' %}
      {% if candidate.path != image.path and candidate_base == image_base and candidate_ext != 'dng' and candidate_ext != 'gitkeep' %}
        {% assign preview_src = candidate.path %}
        {% break %}
      {% endif %}
    {% endfor %}
  {% endif %}

  <div class="gallery-card group relative aspect-square rounded-lg overflow-hidden bg-[var(--color-surface)] shadow-sm" data-gallery-item data-tags="{{ tags_text | downcase }}">
    <a href="{{ image.path | relative_url }}" class="block w-full h-full" target="_blank" rel="noopener" download>
      {% if file_type == 'dng' and preview_src != '' %}
      <img src="{{ preview_src | relative_url }}" alt="{{ caption }}" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300" loading="lazy" decoding="async">
      {% elsif file_type == 'dng' %}
      <div class="w-full h-full flex items-center justify-center p-4 text-center border border-dashed border-[var(--color-border)]">
        <div class="space-y-3">
          <div class="text-4xl">📷</div>
          <p class="font-semibold text-[var(--color-text)]">{{ caption }}</p>
          <p class="text-sm text-[var(--color-text-muted)]">Raw DNG file</p>
        </div>
      </div>
      {% else %}
      <img src="{{ image.path | relative_url }}" alt="{{ caption }}" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300" loading="lazy" decoding="async">
      {% endif %}

      <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors"></div>

      <div class="absolute top-2 left-2 flex flex-wrap gap-1 max-w-[calc(100%-5rem)]">
        {% if meta and meta.tags %}
          {% for tag in meta.tags %}
          {% if tag == '2025-2026-DECODE' or tag == '2024-2025-Into-the-Deep' %}
          <span class="badge badge-primary text-[10px]">{{ season_label }}</span>
          {% else %}
          <span class="badge bg-black/60 text-white text-[10px]">{{ tag }}</span>
          {% endif %}
          {% endfor %}
        {% endif %}
      </div>

      <div class="absolute bottom-0 left-0 right-0 bg-black/70 text-white text-sm p-2 translate-y-full group-hover:translate-y-0 transition-transform">
        <div class="flex items-center justify-between gap-2">
          <span class="truncate">{{ caption }}</span>
          <span class="text-xs opacity-90 whitespace-nowrap">Full quality</span>
        </div>
      </div>
    </a>
  </div>
  {% endif %}
  {% endfor %}
</div>
{% else %}
<div class="card">
  <div class="card-body text-center py-12">
    <h2 class="text-2xl font-bold mb-3">Coming Soon - Check Back Later.</h2>
    <p class="text-[var(--color-text-muted)]">Upload photos into assets/images/gallery/ to populate this page.</p>
  </div>
</div>
{% endif %}