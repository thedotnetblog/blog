---
title: "Aspire 13.2 liefert eine Docs-CLI — und dein KI-Agent kann sie auch nutzen"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 fügt aspire docs hinzu — eine CLI zum Suchen, Durchstöbern und Lesen offizieller Dokumentation, ohne das Terminal zu verlassen. Sie funktioniert auch als Werkzeug für KI-Agenten. Hier erfährst du, warum das wichtig ist."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "aspire-docs-cli-ai-skills.md" >}}).*

Kennst du diesen Moment, wenn du tief in einem Aspire AppHost steckst, Integrationen verdrahtest, und du genau nachschauen musst, welche Parameter die Redis-Integration erwartet? Du wechselst mit Alt-Tab zum Browser, suchst auf aspire.dev, kneifst die Augen zusammen bei den API-Docs, und kommst zurück zu deinem Editor. Kontext verloren. Flow unterbrochen.

Aspire 13.2 hat gerade [eine Lösung dafür geliefert](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). Die `aspire docs`-CLI ermöglicht es dir, offizielle Aspire-Dokumentation direkt aus deinem Terminal zu suchen, durchstöbern und lesen. Und weil sie auf wiederverwendbaren Services basiert, können KI-Agenten und Skills dieselben Befehle nutzen, um Docs nachzuschlagen, statt APIs zu halluzinieren, die gar nicht existieren.

## Das Problem, das hier wirklich gelöst wird

David Pine bringt es im Originalbeitrag auf den Punkt: KI-Agenten waren *furchtbar* darin, Entwicklern beim Bauen von Aspire-Apps zu helfen. Sie empfahlen `dotnet run` statt `aspire run`, verwiesen auf learn.microsoft.com für Docs, die auf aspire.dev leben, schlugen veraltete NuGet-Pakete vor, und — mein persönlicher Favorit — halluzinierten APIs, die nicht existieren.

Warum? Weil Aspire viel länger .NET-spezifisch war, als es polyglott ist, und LLMs mit Trainingsdaten arbeiten, die älter sind als die neuesten Features. Wenn du einem KI-Agenten die Möglichkeit gibst, tatsächlich die aktuellen Docs nachzuschlagen, hört er auf zu raten und wird nützlich.

## Drei Befehle, null Browser-Tabs

Die CLI ist erfrischend einfach:

### Alle Docs auflisten

```bash
aspire docs list
```

Gibt jede verfügbare Dokumentationsseite auf aspire.dev zurück. Brauchst du maschinenlesbare Ausgabe? Füge `--format Json` hinzu.

### Nach einem Thema suchen

```bash
aspire docs search "redis"
```

Durchsucht sowohl Titel als auch Inhalte mit gewichteter Relevanzbewertung. Dieselbe Suchmaschine, die intern die Dokumentationswerkzeuge antreibt. Du bekommst gerankte Ergebnisse mit Titeln, Slugs und Relevanzwerten.

### Eine vollständige Seite lesen (oder nur einen Abschnitt)

```bash
aspire docs get redis-integration
```

Streamt die vollständige Seite als Markdown in dein Terminal. Brauchst du nur einen Abschnitt?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Chirurgische Präzision. Kein Scrollen durch 500 Zeilen. Nur der Teil, den du brauchst.

## Der KI-Agent-Aspekt

Hier wird es interessant für uns Entwickler, die mit KI-Werkzeugen arbeiten. Dieselben `aspire docs`-Befehle funktionieren als Tools für KI-Agenten — über Skills, MCP-Server oder einfache CLI-Wrapper.

Statt dass dein KI-Assistent Aspire-APIs auf Basis veralteter Trainingsdaten erfindet, kann er `aspire docs search "postgres"` aufrufen, die offiziellen Integrations-Docs finden, die richtige Seite lesen und dir den dokumentierten Ansatz liefern. Echtzeit-aktuelle Dokumentation — nicht das, was das Modell vor sechs Monaten auswendig gelernt hat.

Die Architektur dahinter ist bewusst so gestaltet. Das Aspire-Team hat wiederverwendbare Services gebaut (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) anstelle einer einmaligen Integration. Das bedeutet, dieselbe Suchmaschine funktioniert für Menschen im Terminal, KI-Agenten in deinem Editor und Automatisierung in deiner CI-Pipeline.

## Praxisszenarien

**Schnelle Terminal-Nachschlagen:** Du steckst drei Dateien tief und brauchst Redis-Konfigurationsparameter. Zwei Befehle, neunzig Sekunden, zurück an die Arbeit:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**KI-gestützte Entwicklung:** Dein VS Code Skill wrapt die CLI-Befehle. Du fragst „Füge eine PostgreSQL-Datenbank zu meinem AppHost hinzu" und der Agent schlägt die echten Docs nach, bevor er antwortet. Keine Halluzinationen.

**CI/CD-Validierung:** Deine Pipeline validiert AppHost-Konfigurationen programmatisch gegen offizielle Dokumentation. Die `--format Json`-Ausgabe lässt sich sauber mit `jq` und anderen Tools weiterverarbeiten.

**Eigene Wissensdatenbanken:** Baust du deine eigenen KI-Tools? Leite strukturierte JSON-Ausgabe direkt in deine Wissensdatenbank:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Kein Web Scraping. Keine API-Keys. Dieselben strukturierten Daten, die intern von den Dokumentationswerkzeugen genutzt werden.

## Die Dokumentation ist immer aktuell

Das ist der Teil, den ich am meisten schätze. Die CLI lädt keinen Snapshot herunter — sie fragt aspire.dev mit ETag-basiertem Caching ab. In dem Moment, in dem die Docs aktualisiert werden, spiegelt deine CLI und jeder darauf aufbauende Skill das wider. Keine veralteten Kopien, keine „aber im Wiki stand doch..."-Momente.

## Zum Abschluss

`aspire docs` ist eines dieser kleinen Features, das ein echtes Problem sauber löst. Menschen bekommen terminal-nativen Dokumentationszugriff. KI-Agenten bekommen eine Möglichkeit, aufzuhören zu raten und stattdessen echte Docs zu referenzieren. Und alles wird von derselben Wahrheitsquelle gespeist.

Wenn du mit .NET Aspire baust und die CLI noch nicht ausprobiert hast, führe `aspire docs search "dein-thema-hier"` aus und schau, wie es sich anfühlt. Dann überleg dir, diese Befehle in dein KI-Skill- oder Automatisierungs-Setup einzubauen — deine Agenten werden es dir danken.

Schau dir [David Pines Deep Dive](https://davidpine.dev/posts/aspire-docs-mcp-tools/) an, wie die Dokumentationswerkzeuge entstanden sind, und die [offizielle CLI-Referenz](https://aspire.dev/reference/cli/commands/aspire-docs/) für alle Details.
