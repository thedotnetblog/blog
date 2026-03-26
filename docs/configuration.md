# Configuration

The site is configured via `hugo.toml` in the project root.

---

## Core Settings

```toml
baseURL      = "https://thedotnetblog.com"
languageCode = "en-us"
title        = "The .NET Blog"
theme        = "dotnet-minimal"
paginate     = 10                  # Posts per page
enableRobotsTXT = true
summaryLength   = 70               # Words in auto-generated summaries
```

---

## Markup

```toml
[markup]
  [markup.highlight]
    style      = "nord"   # Base highlight style (overridden by CSS per theme)
    lineNos    = false
    noClasses  = false    # Required — emits CSS classes instead of inline styles
  [markup.goldmark.renderer]
    unsafe = true         # Allow raw HTML in Markdown
```

---

## Taxonomies

```toml
[taxonomies]
  tag = "tags"
```

---

## Output Formats

The site generates two additional text files for LLM discoverability:

```toml
[outputFormats]
  [outputFormats.llmstxt]
    mediaType    = "text/plain"
    baseName     = "llms"
    isPlainText  = true
    notAlternative = true
  [outputFormats.llmsfulltxt]
    mediaType    = "text/plain"
    baseName     = "llms-full"
    isPlainText  = true
    notAlternative = true

[outputs]
  home = ["HTML", "RSS", "llmstxt", "llmsfulltxt"]
```

This produces `/llms.txt` (index) and `/llms-full.txt` (full content) at the site root.

---

## Sitemap

```toml
[sitemap]
  changeFreq = "weekly"
  priority   = 0.5
  filename   = "sitemap.xml"
```

---

## Parameters

```toml
[params]
  description   = "Articles, tutorials and insights from the .NET community."
  homeTitle     = "The .NET Blog · .NET, Azure, AI, and Cloud-Native Tutorials"
  eyebrow       = "The .NET Community Blog"
  hero_title    = 'Where <span class="accent">.NET developers</span><br/>share what they build.'
  hero_desc     = "Deep dives, tutorials and community stories — written by developers, for developers."

  # SEO & Social
  defaultImage  = "/img/og-default.png"
  logo          = "/img/og-default.png"
  twitter       = "thedotnetblog"
  socialProfiles = [
    "https://github.com/thedotnetblog/blog",
    "https://x.com/thedotnetblog"
  ]
```

---

## Menus

```toml
[menus]
  [[menus.main]]
    name   = "posts"
    url    = "/posts"
    weight = 1
  [[menus.main]]
    name   = "events"
    url    = "/events"
    weight = 2
  [[menus.main]]
    name   = "authors"
    url    = "/authors"
    weight = 3
  [[menus.main]]
    name   = "tags"
    url    = "/tags"
    weight = 4
```

Footer menu items follow the same pattern under `[[menus.footer]]`.

---

For the full list of Hugo configuration options see the [Hugo documentation](https://gohugo.io/getting-started/configuration/).
