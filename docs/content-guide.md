# Content Guide

Hugo archetypes scaffold new content files with the correct front matter. Always use `hugo new` to create content — it ensures consistent structure.

---

## Content Structure

The blog uses Hugo page bundles organized by author:

```
content/
  posts/
    emiliano-montesdeoca/
      my-post-slug/
        index.md          # English (default)
        index.es.md       # Spanish translation
        index.de.md       # German translation
        index.fr.md       # French
        index.pt.md       # Portuguese
        index.it.md       # Italian
        index.ja.md       # Japanese
        index.zh.md       # Chinese (Simplified)
        index.ko.md       # Korean
        index.ru.md       # Russian
  authors/
    emiliano-montesdeoca/
      index.md          # English (default)
      index.es.md       # Spanish translation
      index.de.md       # German translation
      index.fr.md       # French
      ...
  events/
    my-event.md
```

Posts live in **leaf bundles** under `content/posts/{author-id}/{post-slug}/`. The URL becomes `/posts/{author-id}/{post-slug}/`.

---

## Supported Languages

| Code | Language | Hugo weight |
|------|----------|-------------|
| en | English (default) | 1 |
| es | Spanish | 2 |
| de | German | 3 |
| fr | French | 4 |
| pt | Portuguese | 5 |
| it | Italian | 6 |
| ja | Japanese | 7 |
| zh | Chinese (Simplified) | 8 |
| ko | Korean | 9 |
| ru | Russian | 10 |

---

## Writing a Blog Post

Create a post directory and English file:

```bash
mkdir -p content/posts/emiliano-montesdeoca/my-post
hugo new posts/emiliano-montesdeoca/my-post/index.md
```

Creates `content/posts/emiliano-montesdeoca/my-post/index.md` with this front matter:

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

### Translation Files

After writing the English post, create translations by copying `index.md` and renaming:

```
index.es.md   index.de.md   index.fr.md   index.pt.md
index.it.md   index.ja.md   index.zh.md   index.ko.md   index.ru.md
```

Translation rules:
- **Translate**: title, description, body text, section headings
- **Preserve unchanged**: code blocks, URLs, image paths, `date`, `author`, `tags`
- **Adapt tone**: maintain the author's voice naturally in each language

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
id: "jane-doe"
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
| `id` | ✅ | Unique identifier — matches the author directory name under `content/posts/` |
| `role` | Recommended | Role/title shown under the name (e.g., `"Senior .NET Engineer"`) |
| `bio` | Recommended | Short biography shown on the author profile page and in author cards |
| `avatar` | Recommended | Path to the avatar image (e.g., `"/img/authors/jane.png"`) |
| `socials` | Optional | List of social links, each with `platform` and `url` |

### Localizing an Author

Authors use page bundles just like posts. Translation files go inside the author's directory:

```
content/authors/jane-doe/
  index.md        # English
  index.es.md     # Spanish
  index.de.md     # German
  index.fr.md     # French
  ...
```

Translate `role` and `bio`. Keep `title`, `id`, `avatar`, and `socials` unchanged.

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
id: "emiliano-montesdeoca"
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
