---
title: "Schreibe für The .NET Blog"
description: "Teile dein Wissen mit der .NET-Community. Lerne, wie du als Autor mitmachst und deinen ersten Beitrag einreichst."
---

The .NET Blog ist eine community-getriebene Publikation, in der Entwickler Einblicke, Tutorials und Geschichten rund um .NET, Azure, KI und Cloud-native-Entwicklung teilen. **Wir begrüßen Beiträge von Entwicklern aller Erfahrungsstufen** — egal ob du deinen ersten technischen Artikel schreibst oder ein erfahrener Speaker bist.

## So machst du mit

Alles liegt auf GitHub und folgt einem Pull-Request-Workflow. So legst du los:

### 1. Repository forken

Gehe zu [github.com/thedotnetblog/blog](https://github.com/thedotnetblog/blog) und forke das Repository in deinen GitHub-Account.

### 2. Autorenprofil anlegen

Wenn du zum ersten Mal beiträgst, füge dich als Autor hinzu, indem du einen Ordner unter `content/authors/dein-benutzername/` mit einer `index.md`-Datei erstellst:

```yaml
---
title: "Dein Name"
id: "dein-benutzername"
role: "Deine Rolle oder Position"
bio: "Eine kurze Biografie über dich."
avatar: "/img/authors/dein-avatar.jpg"
socials:
  - platform: "GitHub"
    url: "https://github.com/dein-benutzername"
  - platform: "Twitter"
    url: "https://x.com/dein-benutzername"
---
```

Füge dein Avatar-Bild (quadratisch, mindestens 200×200px) unter `static/img/authors/` hinzu.

### 3. Beitrag schreiben

Erstelle einen neuen Ordner unter `content/posts/dein-benutzername/dein-beitrag-slug/` und füge eine `index.md`-Datei hinzu:

```yaml
---
title: "Titel deines Beitrags"
date: 2025-01-01
author: "dein-benutzername"
description: "Eine kurze Beschreibung deines Beitrags."
tags: ["dotnet", "azure"]
---

Inhalt deines Beitrags in Markdown...
```

### 4. Pull Request öffnen

Pushe deine Änderungen in deinen Fork und öffne einen Pull Request gegen den `main`-Branch. Unser Team wird ihn reviewen und innerhalb weniger Tage Feedback geben.

## Was wir suchen

- **Tutorials** — Schritt-für-Schritt-Anleitungen zu .NET, Azure, KI, Blazor, Aspire und mehr
- **Tiefgehende Analysen** — ausführliche Erkundungen einer Technologie, eines Musters oder einer Architektur
- **Community-Geschichten** — deine Erfahrungen beim Bauen mit .NET in der Produktion
- **Event-Zusammenfassungen** — Berichte von Konferenzen, Meetups oder Webinaren

## Richtlinien

- Inhalte sollten technisch und für das .NET-Ökosystem relevant sein
- Codebeispiele müssen korrekt und in einem echten Projekt getestet sein
- Füge eine aussagekräftige Beschreibung und mindestens ein relevantes Tag hinzu
- Beiträge werden automatisch in alle unterstützten Sprachen übersetzt

## Kontakt

Öffne ein Issue auf [GitHub](https://github.com/thedotnetblog/blog/issues) oder schreib uns auf [X / Twitter](https://x.com/thedotnetblog). Wir freuen uns, dich in der Community willkommen zu heißen!
