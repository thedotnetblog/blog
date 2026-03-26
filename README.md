# The .NET Blog

A community-driven .NET blog built with [Hugo](https://gohugo.io) and a custom minimal dark theme. Features multi-author profiles, tagged blog posts, and an event timeline.

> **Live site:** [thedotnetblog.com](https://thedotnetblog.com)

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Running Locally](#running-locally)
- [Creating Content](#creating-content)
  - [Writing a Blog Post](#writing-a-blog-post)
  - [Adding an Author](#adding-an-author)
  - [Adding an Event](#adding-an-event)
- [Content Reference](#content-reference)
  - [Post Front Matter](#post-front-matter)
  - [Author Front Matter](#author-front-matter)
  - [Event Front Matter](#event-front-matter)
- [Theme](#theme)
  - [Design](#design)
  - [Layouts](#layouts)
  - [Customizing](#customizing)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| **Hugo (extended)** | `v0.121.0` or later | [gohugo.io/installation](https://gohugo.io/installation/) |
| **Git** | any recent version | [git-scm.com](https://git-scm.com/) |

> **Why extended?** The extended version of Hugo includes built-in Sass/SCSS processing support. While the current theme uses plain CSS, the extended build ensures compatibility if you later add Sass.

### Installing Hugo

**macOS** (Homebrew):

```bash
brew install hugo
```

**Windows** (Chocolatey):

```bash
choco install hugo-extended
```

**Windows** (Winget):

```bash
winget install Hugo.Hugo.Extended
```

**Linux** (Snap):

```bash
snap install hugo
```

**Linux** (download binary):

```bash
# Replace version as needed
HUGO_VERSION="0.121.2"
curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
  -o hugo.tar.gz
tar -xzf hugo.tar.gz hugo
sudo mv hugo /usr/local/bin/hugo
```

Verify the installation:

```bash
hugo version
# hugo v0.121.2+extended linux/amd64 ...
```

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/thedotnetblog/blog.git
cd blog

# 2. Start the development server
hugo server --buildDrafts --buildFuture

# 3. Open in your browser
# → http://localhost:1313
```

That's it — the site will hot-reload as you edit content and templates.

---

## Project Structure

```
blog/
├── archetypes/              # Templates for `hugo new` scaffolding
│   ├── authors.md           #   → Author profile template
│   ├── events.md            #   → Event template
│   ├── posts.md             #   → Blog post template
│   └── default.md           #   → Default template
│
├── content/                 # All Markdown content (this is where you write)
│   ├── authors/             #   Author profiles
│   │   ├── alice-nguyen.md
│   │   ├── marco-rossi.md
│   │   └── sofia-petrova.md
│   ├── events/              #   Community events (timeline)
│   │   ├── dotnet-conf-2025.md
│   │   ├── ndc-oslo-2025.md
│   │   └── ...
│   └── posts/               #   Blog posts
│       ├── whats-new-dotnet-9.md
│       ├── event-driven-microservices-dotnet.md
│       └── ...
│
├── static/                  # Static assets served as-is
│   └── img/
│       └── authors/         #   Author avatar images (SVG/PNG/JPG)
│           ├── alice.svg
│           ├── marco.svg
│           └── sofia.svg
│
├── themes/
│   └── dotnet-minimal/      # Custom theme (see Theme section)
│       ├── layouts/         #   All HTML templates
│       ├── static/css/      #   Theme stylesheet
│       └── theme.toml       #   Theme metadata
│
├── hugo.toml                # Site configuration
├── .gitignore               # Ignores public/, resources/, .hugo_build.lock
└── README.md                # ← You are here
```

---

## Running Locally

### Development Server

```bash
hugo server
```

This starts a local server at `http://localhost:1313` with live reload enabled. Changes to content, templates, or CSS are reflected instantly in the browser.

### Useful Flags

| Flag | Description |
|------|-------------|
| `--buildDrafts` / `-D` | Include posts with `draft: true` |
| `--buildFuture` / `-F` | Include posts with future dates |
| `--port 8080` | Use a custom port (default: `1313`) |
| `--bind 0.0.0.0` | Allow access from other devices on the network |
| `--disableFastRender` | Full rebuild on every change (slower but more reliable) |

**Example:** Run with drafts and future content visible on port 8080:

```bash
hugo server -D -F --port 8080
```

### Production Build

To generate the static site into the `public/` directory:

```bash
hugo
```

The output in `public/` is ready to deploy to any static hosting provider.

To preview exactly what will be deployed (with the correct `baseURL`):

```bash
hugo --minify
hugo server --renderToDisk
```

---

## Creating Content

Hugo provides archetypes that scaffold new content files with the correct front matter. Always use `hugo new` to create content — it ensures consistent structure.

### Writing a Blog Post

```bash
hugo new posts/my-awesome-post.md
```

This creates `content/posts/my-awesome-post.md` with the following scaffolded front matter:

```yaml
---
title: "My Awesome Post"
date: 2026-03-23T03:19:23+00:00
author: ""
description: ""
tags:
  - dotnet
draft: true
---

<!-- Write your post here -->
```

**Fill in the fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Post title displayed in listings and the post header |
| `date` | ✅ | Publication date (`YYYY-MM-DD` or full ISO 8601) |
| `author` | ✅ | Author's display name — **must match the `title` field** in the author's profile (e.g., `"Alice Nguyen"`) |
| `description` | Recommended | Short summary shown below the title on the post page |
| `tags` | Recommended | List of tags for categorization and the tag cloud |
| `draft` | Optional | Set to `true` to hide from production builds (visible with `--buildDrafts`) |

**Example:**

```yaml
---
title: "Getting Started with Blazor in .NET 9"
date: 2025-12-01
author: "Alice Nguyen"
description: "A step-by-step guide to building your first Blazor WebAssembly app."
tags:
  - blazor
  - dotnet
  - frontend
draft: false
---

Your Markdown content here. Use standard Markdown syntax — headings, code blocks,
lists, images, links, bold, italic, etc.

## Section Heading

Regular paragraph text.

```csharp
Console.WriteLine("Hello, Blazor!");
\```

> Blockquotes render with a purple left border.
```

### Adding an Author

```bash
hugo new authors/jane-doe.md
```

This creates `content/authors/jane-doe.md`:

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

**Fill in the fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Display name — this is what blog posts reference in their `author` field |
| `role` | Recommended | Role/title shown under the name (e.g., `"Senior .NET Engineer"`) |
| `bio` | Recommended | Short biography shown on the author's profile page and author cards |
| `avatar` | Recommended | Path to the avatar image (e.g., `"/img/authors/jane.png"`) |
| `socials` | Optional | List of social links, each with `platform` and `url` |

**Avatar images:** Place your avatar in `static/img/authors/`. Supported formats: SVG, PNG, JPG, WebP. The image will be served at `/img/authors/filename.ext`.

```bash
# Copy your avatar into the project
cp ~/my-photo.png static/img/authors/jane.png
```

Then reference it in the author's front matter:

```yaml
avatar: "/img/authors/jane.png"
```

> **No avatar?** The theme displays a styled placeholder with the first letter of the author's name.

**Supported social platforms** (the `platform` field is free-text — use any label):

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

### Adding an Event

```bash
hugo new events/my-conference-2026.md
```

This creates `content/events/my-conference-2026.md`:

```yaml
---
title: "My Conference 2026"
date: 2026-03-23T03:19:23+00:00
event_type: "Meetup"
location: ""
featured: false
description: ""
tags:
  - dotnet
---

<!-- Describe the event here -->
```

**Fill in the fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Event name |
| `date` | ✅ | Event date — used for timeline ordering and year grouping |
| `event_type` | ✅ | Category badge — determines color (see table below) |
| `location` | Recommended | Location shown with a 📍 pin (e.g., `"Virtual"`, `"Oslo, Norway"`) |
| `featured` | Optional | Set to `true` for a highlighted dot on the timeline (default: `false`) |
| `description` | Recommended | Short description shown in the event header |
| `tags` | Optional | Tags for categorization |

**Event type badges** and their colors:

| `event_type` | Color | Badge |
|--------------|-------|-------|
| `Conference` | Cyan | ![conference](https://img.shields.io/badge/-Conference-56d1f0) |
| `Meetup` | Purple | ![meetup](https://img.shields.io/badge/-Meetup-7c6cfa) |
| `Release` | Green | ![release](https://img.shields.io/badge/-Release-34d399) |
| `Webinar` | Yellow | ![webinar](https://img.shields.io/badge/-Webinar-fbbf24) |
| `Workshop` | Red | ![workshop](https://img.shields.io/badge/-Workshop-f87171) |

> **Custom types:** You can use any value for `event_type`. It will render as a badge — just without a predefined color unless you add a corresponding CSS class (`.event-type-yourtype`).

---

## Content Reference

### Post Front Matter

```yaml
---
title: "Post Title"                  # Display title
date: 2025-11-15                     # Publication date
author: "Alice Nguyen"               # Must match an author's title exactly
description: "Short summary..."      # Shown below the title
tags:                                # Used for tag pages and tag cloud
  - dotnet
  - performance
draft: false                         # true = hidden in production
---
```

### Author Front Matter

```yaml
---
title: "Alice Nguyen"                # Display name (posts link via this)
role: "Senior .NET Engineer"         # Role/title
bio: "Alice is a..."                 # Biography paragraph
avatar: "/img/authors/alice.svg"     # Avatar image path
socials:                             # Social media links
  - platform: "GitHub"
    url: "https://github.com/alice"
  - platform: "Twitter"
    url: "https://twitter.com/alice"
---
```

### Event Front Matter

```yaml
---
title: ".NET Conf 2025"              # Event name
date: 2025-11-10                     # Event date (for timeline)
event_type: "Conference"             # Badge type (see table above)
location: "Virtual"                  # Shown with 📍 icon
featured: true                       # Highlighted on timeline
description: "The biggest..."        # Short description
tags:                                # Tags for categorization
  - dotnet
  - conference
---
```

---

## Theme

### Design

The **dotnet-minimal** theme is built from scratch with a focus on:

- **Dark palette** — Background `#0d0f12` with card surfaces at `#13161b`
- **Accent colors** — Purple (`#7c6cfa`) and cyan (`#56d1f0`)
- **Monospace headings** — JetBrains Mono for a developer-first aesthetic
- **Body text** — Inter for readability
- **Big headings** — Responsive `clamp()` sizing for impact
- **Glassmorphism navbar** — Sticky header with blur backdrop
- **Cards** — Hover effects with subtle transitions
- **Timeline** — Year-grouped with colored dots and type badges
- **Responsive** — Mobile-first with breakpoints at 640px

### Layouts

| Path | Description |
|------|-------------|
| `layouts/_default/baseof.html` | Base template (HTML head, body, fonts) |
| `layouts/index.html` | Home page (hero, latest posts, upcoming events) |
| `layouts/posts/list.html` | Blog post listing page |
| `layouts/posts/single.html` | Individual blog post page |
| `layouts/authors/list.html` | Author grid page |
| `layouts/authors/single.html` | Individual author profile page |
| `layouts/events/list.html` | Events timeline page |
| `layouts/events/single.html` | Individual event detail page |
| `layouts/tags/list.html` | Tag cloud page |
| `layouts/tags/single.html` | Posts filtered by a single tag |
| `layouts/partials/header.html` | Site navigation header |
| `layouts/partials/footer.html` | Site footer |
| `layouts/partials/pagination.html` | Pagination component |

### Customizing

**Colors:** Edit the CSS custom properties at the top of `themes/dotnet-minimal/static/css/style.css`:

```css
:root {
  --bg:           #0d0f12;     /* Page background */
  --bg-card:      #13161b;     /* Card background */
  --accent:       #7c6cfa;     /* Primary accent (purple) */
  --accent-2:     #56d1f0;     /* Secondary accent (cyan) */
  --text:         #e2e8f0;     /* Body text */
  --heading:      #f8fafc;     /* Heading text */
  --font-sans:    'Inter', ...;
  --font-mono:    'JetBrains Mono', ...;
  /* ... more variables available */
}
```

**Fonts:** The theme loads Inter and JetBrains Mono from Google Fonts in `baseof.html`. Replace the `<link>` tag to use different fonts.

**Navigation:** Menus are defined in `hugo.toml` under `[menus]`. Add or remove items:

```toml
[[menus.main]]
  name = "about"
  url = "/about"
  weight = 5
```

**Site title & hero:** Edit `[params]` in `hugo.toml`:

```toml
[params]
  description = "Your blog description"
  eyebrow = "Your Eyebrow Text"
  hero_title = 'Your <span class="accent">hero</span> title.'
  hero_desc = "Your hero description paragraph."
```

---

## Configuration

The site is configured via `hugo.toml`. Key settings:

```toml
baseURL = "https://thedotnetblog.com"    # Your production URL
title = "The .NET Blog"                   # Site title
theme = "dotnet-minimal"                  # Theme directory name
paginate = 10                             # Posts per page

[taxonomies]
  tag = "tags"                            # Enable tag taxonomy

[markup.highlight]
  style = "nord"                          # Syntax highlighting theme

[markup.goldmark.renderer]
  unsafe = true                           # Allow raw HTML in Markdown
```

### All Hugo Configuration Options

For the full list of Hugo configuration options, see the [Hugo documentation](https://gohugo.io/getting-started/configuration/).

---

## Deployment

The `hugo` command generates a static site in the `public/` directory. You can deploy it to any static hosting service.

### GitHub Pages

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: "0.121.2"
          extended: true

      - name: Build
        run: hugo --minify

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Netlify

Create `netlify.toml` in the project root:

```toml
[build]
  command = "hugo --minify"
  publish = "public"

[build.environment]
  HUGO_VERSION = "0.121.2"
```

### Azure Static Web Apps

```yaml
# In your Azure pipeline or GitHub Actions
- task: HugoTask@1
  inputs:
    hugoVersion: "0.121.2"
    extendedVersion: true
    args: "--minify"
```

### Vercel

Create `vercel.json`:

```json
{
  "build": {
    "env": {
      "HUGO_VERSION": "0.121.2"
    }
  }
}
```

Set the framework preset to **Hugo** in Vercel's project settings.

### Manual / Any Static Host

```bash
hugo --minify
# Upload the contents of public/ to your web server
```

---

## Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a branch** for your changes:
   ```bash
   git checkout -b my-new-post
   ```
4. **Make your changes** (see [Creating Content](#creating-content) above)
5. **Preview locally:**
   ```bash
   hugo server -D -F
   ```
6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add new blog post: My Awesome Post"
   git push origin my-new-post
   ```
7. **Open a Pull Request** against `main`

### Content Guidelines

- Write in clear, accessible English
- Use code blocks with language identifiers (e.g., ` ```csharp `)
- Keep post descriptions under 200 characters
- Tag posts with relevant terms (check existing tags at `/tags`)
- Test locally before submitting

### Theme Changes

If you're modifying the theme:

- CSS is in `themes/dotnet-minimal/static/css/style.css`
- Templates are in `themes/dotnet-minimal/layouts/`
- Test on both desktop and mobile viewport sizes
- Ensure the site builds without errors: `hugo --minify`

---

## License

This project is open source under the [MIT License](LICENSE).