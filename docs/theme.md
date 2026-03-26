# Theme

The custom theme lives at `themes/dotnet-minimal/`.

---

## Design

The **dotnet-minimal** theme is built from scratch with a developer-first aesthetic:

- **Dark palette** — Background `#0d0f12`, card surfaces `#13161b`
- **Accent colors** — Purple (`#7c6cfa`) and cyan (`#56d1f0`)
- **Monospace headings** — JetBrains Mono
- **Body text** — Inter for readability
- **Responsive headings** — `clamp()` for fluid sizing
- **Glassmorphism navbar** — Sticky header with blur backdrop
- **Cards** — Hover lift effect with subtle transitions
- **Timeline** — Year-grouped with colored dots and type badges
- **Syntax highlighting** — GitHub palette (light), Nord palette (dark)
- **Mobile-first** — Breakpoints at 640px

---

## Layouts

| File | Description |
|------|-------------|
| `layouts/_default/baseof.html` | Base HTML shell (head, fonts, body wrapper) |
| `layouts/index.html` | Home page (hero, latest posts, upcoming events) |
| `layouts/posts/list.html` | Blog post listing |
| `layouts/posts/single.html` | Individual blog post |
| `layouts/authors/list.html` | Author grid |
| `layouts/authors/single.html` | Author profile page |
| `layouts/events/list.html` | Events timeline |
| `layouts/events/single.html` | Individual event detail |
| `layouts/tags/list.html` | Tag cloud |
| `layouts/tags/single.html` | Posts filtered by tag |
| `layouts/partials/header.html` | Site navigation |
| `layouts/partials/footer.html` | Site footer |
| `layouts/partials/seo.html` | Canonical, OG, Twitter meta tags |
| `layouts/partials/schema.html` | JSON-LD structured data |
| `layouts/partials/pagination.html` | Pagination component |

---

## Customizing

### Colors

Edit the CSS custom properties at the top of `themes/dotnet-minimal/static/css/style.css`:

```css
:root {
  --bg:           #0d0f12;     /* Page background */
  --bg-card:      #13161b;     /* Card background */
  --accent:       #7c6cfa;     /* Primary accent (purple) */
  --accent-2:     #56d1f0;     /* Secondary accent (cyan) */
  --text:         #e2e8f0;     /* Body text */
  --heading:      #f8fafc;     /* Heading text */
  --font-sans:    'Inter', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;
}
```

Light mode colors are scoped under `[data-theme="light"]` in the same file.

### Fonts

The theme loads Inter and JetBrains Mono from Google Fonts in `baseof.html`. Replace the `<link>` tag to change fonts.

### Navigation

Menus are defined in `hugo.toml` under `[menus]`:

```toml
[[menus.main]]
  name = "about"
  url = "/about"
  weight = 5
```

### Syntax Highlighting

Syntax colors are provided via CSS classes (not inline styles). The theme uses:

- **Light mode** — GitHub palette (`[data-theme="light"] .chroma …`)
- **Dark mode** — Nord palette (`[data-theme="dark"] .chroma …`)

Both sets of classes are in `style.css`. The Hugo config must have `noClasses = false` (already set).

### Hero & Description

Edit `[params]` in `hugo.toml`:

```toml
[params]
  description  = "Articles, tutorials and insights from the .NET community."
  eyebrow      = "The .NET Community Blog"
  hero_title   = 'Where <span class="accent">.NET developers</span><br/>share what they build.'
  hero_desc    = "Deep dives, tutorials and community stories — written by developers, for developers."
```
