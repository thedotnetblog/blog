# Content Guide

Hugo archetypes scaffold new content files with the correct front matter. Always use `hugo new` to create content — it ensures consistent structure.

---

## Writing a Blog Post

```bash
hugo new posts/my-post.md
```

Creates `content/posts/my-post.md` with this front matter:

```yaml
---
title: "My Post"
date: 2026-03-26T00:00:00+00:00
author: ""
description: ""
tags:
  - dotnet
draft: true
---

<!-- Write your post here -->
```

### Front Matter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Post title shown in listings and the post header |
| `date` | ✅ | Publication date (`YYYY-MM-DD` or full ISO 8601) |
| `author` | ✅ | Author display name — **must match the `title` in the author profile** (e.g., `"Emiliano Montesdeoca"`) |
| `description` | Recommended | Short summary shown below the title |
| `tags` | Recommended | List of tags for categorization and the tag cloud |
| `draft` | Optional | `true` = hidden in production builds (visible with `--buildDrafts`) |

### Example

```yaml
---
title: "Getting Started with Blazor in .NET 9"
date: 2025-12-01
author: "Emiliano Montesdeoca"
description: "A step-by-step guide to building your first Blazor WebAssembly app."
tags:
  - blazor
  - dotnet
  - frontend
---

Your Markdown content here.

## Section Heading

Regular paragraph text.

```csharp
Console.WriteLine("Hello, Blazor!");
\```

> Blockquotes render with a colored left border.
```

---

## Adding an Author

```bash
hugo new authors/jane-doe.md
```

Creates `content/authors/jane-doe.md`:

```yaml
---
title: "Jane Doe"
role: ""
bio: ""
avatar: ""
socials:
  - platform: "GitHub"
    url: ""
  - platform: "Twitter"
    url: ""
---
```

### Front Matter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Display name — posts reference this value in their `author` field |
| `role` | Recommended | Role/title shown under the name (e.g., `"Senior .NET Engineer"`) |
| `bio` | Recommended | Short biography shown on the author profile page and in author cards |
| `avatar` | Recommended | Path to the avatar image (e.g., `"/img/authors/jane.png"`) |
| `socials` | Optional | List of social links, each with `platform` and `url` |

### Avatar Images

Place the image in `static/img/authors/`. Supported formats: SVG, PNG, JPG, WebP.

```bash
cp ~/my-photo.png static/img/authors/jane.png
```

Then reference it in the front matter:

```yaml
avatar: "/img/authors/jane.png"
```

> **No avatar?** The theme shows a styled placeholder with the author's initial.

### Supported Social Platforms

The `platform` field is free-text — use any label:

```yaml
socials:
  - platform: "GitHub"
    url: "https://github.com/janedoe"
  - platform: "Twitter"
    url: "https://twitter.com/janedoe"
  - platform: "LinkedIn"
    url: "https://linkedin.com/in/janedoe"
  - platform: "Mastodon"
    url: "https://mastodon.social/@janedoe"
  - platform: "YouTube"
    url: "https://youtube.com/@janedoe"
  - platform: "Blog"
    url: "https://janedoe.dev"
```

---

## Adding an Event

```bash
hugo new events/my-conference-2026.md
```

Creates `content/events/my-conference-2026.md`:

```yaml
---
title: "My Conference 2026"
date: 2026-03-26T00:00:00+00:00
event_type: "Meetup"
location: ""
featured: false
description: ""
tags:
  - dotnet
---

<!-- Describe the event here -->
```

### Front Matter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Event name |
| `date` | ✅ | Event date — used for timeline ordering and year grouping |
| `event_type` | ✅ | Category badge (see table below) |
| `location` | Recommended | Shown with a 📍 pin (e.g., `"Virtual"`, `"Oslo, Norway"`) |
| `featured` | Optional | `true` = highlighted dot on the timeline (default: `false`) |
| `description` | Recommended | Short description shown in the event header |
| `tags` | Optional | Tags for categorization |

### Event Type Badges

| `event_type` | Color |
|--------------|-------|
| `Conference` | Cyan |
| `Meetup` | Purple |
| `Release` | Green |
| `Webinar` | Yellow |
| `Workshop` | Red |

> **Custom types:** Any value renders as a badge. To add a custom color, add a `.event-type-yourtype` CSS class to `style.css`.

---

## Front Matter Quick Reference

### Post

```yaml
---
title: "Post Title"
date: 2025-11-15
author: "Emiliano Montesdeoca"
description: "Short summary..."
tags:
  - dotnet
  - performance
draft: false
---
```

### Author

```yaml
---
title: "Emiliano Montesdeoca"
role: "Senior .NET Engineer"
bio: "Emiliano is a..."
avatar: "/img/authors/emiliano.png"
socials:
  - platform: "GitHub"
    url: "https://github.com/emiliano"
  - platform: "Twitter"
    url: "https://twitter.com/emiliano"
---
```

### Event

```yaml
---
title: ".NET Conf 2025"
date: 2025-11-10
event_type: "Conference"
location: "Virtual"
featured: true
description: "The biggest .NET event of the year."
tags:
  - dotnet
  - conference
---
```
