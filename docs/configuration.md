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
    name       = "posts"
    url        = "/posts"
    weight     = 1
    identifier = "posts"
  [[menus.main]]
    name       = "events"
    url        = "/events"
    weight     = 2
    identifier = "events"
  [[menus.main]]
    name       = "authors"
    url        = "/authors"
    weight     = 3
    identifier = "authors"
  [[menus.main]]
    name       = "tags"
    url        = "/tags"
    weight     = 4
    identifier = "tags"
```

Menu item names are localized via the i18n system. The `identifier` field maps to translation keys like `nav_posts`, `nav_events`, etc. in `i18n/{lang}.toml`.

Footer menu items follow the same pattern under `[[menus.footer]]`.

---

## Languages

The site supports 10 languages using Hugo's filename-based translation matching:

```toml
defaultContentLanguage = "en"
enableMissingTranslationPlaceholders = false

[languages]
  [languages.en]
    languageCode = "en"
    languageName = "English"
    weight = 1
  [languages.es]
    languageCode = "es"
    languageName = "Español"
    weight = 2
  [languages.de]
    languageCode = "de"
    languageName = "Deutsch"
    weight = 3
  [languages.fr]
    languageCode = "fr"
    languageName = "Français"
    weight = 4
  [languages.pt]
    languageCode = "pt"
    languageName = "Português"
    weight = 5
  [languages.it]
    languageCode = "it"
    languageName = "Italiano"
    weight = 6
  [languages.ja]
    languageCode = "ja"
    languageName = "日本語"
    weight = 7
  [languages.zh]
    languageCode = "zh"
    languageName = "中文"
    weight = 8
  [languages.ko]
    languageCode = "ko"
    languageName = "한국어"
    weight = 9
  [languages.ru]
    languageCode = "ru"
    languageName = "Русский"
    weight = 10
```

### i18n Translation Files

UI strings are translated via TOML files in `i18n/`:

```
i18n/
  en.toml   es.toml   de.toml   fr.toml   pt.toml
  it.toml   ja.toml   zh.toml   ko.toml   ru.toml
```

Each file contains key-value pairs used by templates via `{{ i18n "key" }}`.

### Language Selector

The header includes a language dropdown that:
- Shows all available languages
- Highlights the current language
- Links to the translated version of the current page (or the language homepage if no translation exists)
- Saves the user's preferred language in `localStorage` and auto-redirects on first visit

---

For the full list of Hugo configuration options see the [Hugo documentation](https://gohugo.io/getting-started/configuration/).
