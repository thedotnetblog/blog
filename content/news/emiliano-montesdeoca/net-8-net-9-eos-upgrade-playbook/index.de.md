---
title: '.NET 8 und .NET 9 Ende des Supports: Behandeln Sie dies als Liefertermin'
date: 2026-07-19
author: 'Emiliano Montesdeoca'
description: 'Der 10. November 2026 ist nicht nur ein Support-Datum; es ist der Punkt, an dem aufgeschobenes Upgrade-Risiko explizit wird.'
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Originalquelle: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Diese Ankündigung ist unkompliziert, und Teams sollten mit gleicher Klarheit antworten: Wenn Sie planen, nach dem 10. November 2026 weiterhin auf .NET 8 oder .NET 9 auszuliefern, treffen Sie eine bewusste Entscheidung für eine nicht unterstützte Laufzeit.

Anwendungen werden weiterlaufen. Das ist nicht der Punkt. Der Punkt ist, dass Sicherheits- und Service-Updates aufhören. Sobald das passiert, wird jede bekannte Schwachstelle ohne Backport-Pfad zu Ihrer betrieblichen Verantwortung.

Meine Meinung: Organisationen behandeln Framework-Upgrades oft als optionale Wartung und zahlen dann für diese Entscheidung in Notfallfenstern, Audit-Feststellungen und übereilten Verkäufer-Eskalationen. Upgrade-Planung sollte ein Produkt-Roadmap-Element sein, kein Side-Quest.

Ein praktischer Migrationsansatz für .NET-Teams:

Setzen Sie .NET 10-Neuausrichtung als datiertes Ziel, nicht als offenes Backlog-Element.

Führen Sie Kompatibilitäts- und Regressionstests jetzt parallel zur Feature-Arbeit durch, nicht erst im Q4.

Verfolgen Sie Abhängigkeits- und Hosting-Bereitschaft als separate Workstreams, weil viele Fehler außerhalb der Projektdatei auftreten.

Verwenden Sie Upgrade Assistant und Breaking-Change-Dokumentation frühzeitig, um Überraschungen vorzuladen.