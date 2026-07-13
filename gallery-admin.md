---
layout: page
title: Gallery Admin
description: Manage gallery image metadata, captions, and tags. Click tags to add/remove them from each image, then copy the updated YAML.
permalink: /gallery-admin/
published: false
---

## Gallery Image Manager

Browse all gallery images below. For each image you can:
- **Edit caption** — short text shown with the image
- **Add description** — longer optional description
- **Toggle tags** — click tag buttons to add/remove them from the image
- **Copy YAML** — generate updated metadata for `_data/gallery.yml`

{% include components/gallery-admin.html %}

---

## How to Apply Changes

1. Edit captions, descriptions, and tags using the interface above
2. Click **"Copy YAML"** to copy the updated metadata
3. Open `_data/gallery.yml` in your editor
4. Replace its contents with the copied YAML
5. Commit and push changes to update the gallery

---

## Adding New Tags

To add new filterable tags:

1. Edit `_data/gallery_tags.yml`
2. Add a new entry under `filters:`:

```yaml
- value: "new-tag"
  label: "New Tag Label"
```

3. The tag will automatically appear as a clickable button for all images
