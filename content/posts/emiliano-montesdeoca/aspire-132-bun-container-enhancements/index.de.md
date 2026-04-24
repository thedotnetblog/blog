---
title: "Aspire 13.2: Bun-Support, bessere Container und weniger Debug-Reibung"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 fügt erstklassige Bun-Unterstützung für Vite-Apps hinzu, behebt Yarn-Zuverlässigkeit und liefert Container-Verbesserungen, die das lokale Dev-Verhalten vorhersehbarer machen."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/).*

Wenn du .NET-Backends mit JavaScript-Frontends in Aspire baust, ist 13.2 das Update, das deinen Alltag leise besser macht. Keine neuen Paradigmen. Nur solide Verbesserungen an Dingen, die leicht nervig waren.

## Bun ist jetzt erstklassig

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

Wenn dein Team Bun bereits verwendet, zwingt Aspire dich nicht mehr gegen den Strom zu schwimmen.

## Yarn wurde zuverlässiger

Yarn-Nutzer bekommen etwas mindestens genauso Wichtiges: weniger mysteriöse Fehler bei `withYarn()` mit `addViteApp()`.

## Container-Verbesserungen

### Explizite Pull Policy

```typescript
const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);
```

Perfekt für Workflows, wo du lokal Images baust und Compose genau dieses verwenden soll.

### PostgreSQL 18+ funktioniert korrekt

PostgreSQL 18 änderte sein internes Verzeichnislayout, was das Volume-Mapping still brach. 13.2 behebt das.

## Debugging-Verbesserungen

- `DebuggerDisplayAttribute` auf Core-Typen — nützliche Werte statt tiefer Objektbäume
- Bessere Fehlermeldungen für `WaitFor`
- `BeforeResourceStartedEvent` feuert zum richtigen Zeitpunkt

## Fazit

Aspire 13.2 ist ein fokussiertes Qualitäts-Release. Originalpost von David Pine: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
