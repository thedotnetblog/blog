---
title: "Ein WinUI-Agent-Plugin für GitHub Copilot und Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft hat Agent-Skills für die WinUI-Entwicklung veröffentlicht: Scaffolding, Kompilieren, Ausführen, Testen, Iterieren – alles mit GitHub Copilot CLI oder Claude Code. Die zentrale Innovation: zweckgebundene Werkzeuge, die den Agent in WinUI-spezifischen Fakten verankern."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft hat ein Open-Source-Set von Agent-Skills für die WinUI-Anwendungsentwicklung veröffentlicht, verfügbar unter [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Installation und Einrichtung

Installieren Sie das Plugin mit `/plugin install winui@awesome-copilot`, dann führen Sie die initiale Einrichtung mit `/winui:winui-setup` durch. Der Setup-Prozess prüft Voraussetzungen, installiert notwendige Abhängigkeiten und konfiguriert die Umgebung für die WinUI-Anwendungsentwicklung.

## Die End-to-End-Entwicklungsschleife

Die Skills decken den vollständigen Entwicklungszyklus ab:

- **Scaffolding:** Generiert die richtige Projektvorlage mit `dotnet new WinUI` und den entsprechenden Parametern — der Agent kennt die richtigen Vorlagen und Standardkonfigurationswerte.
- **Kompilieren:** Verwaltet das gepackte Ausführungsmodell, das WinUI-Anwendungen erfordern, einschließlich Paketsignierung und Manifestkonfigurationen.
- **Interaktion und Validierung:** Startet die Anwendung, interagiert damit und validiert das Verhalten.
- **Kompilierfehler beheben:** Der Agent versteht WinUI-spezifische Fehlermeldungen und weiß, wie er sie beheben kann.

## Token-Effizienz durch zweckgebundene Werkzeuge

Die zentrale Innovation ist, dass die Skills zweckgebundene Werkzeuge enthalten, die bei Bedarf konkrete Referenzdaten abrufen:

- WinUI- und Fluent Design-API-Details
- MVVM-Muster und Best Practices
- MSIX-Packaging, Code-Signierung und Store-Einreichung
- Barrierefreiheit, Theming und UI-Automatisierung

Anstatt die gesamte WinUI-Dokumentation in den Kontext zu injizieren, rufen die Werkzeuge genau das ab, was der Agent im jeweiligen Moment benötigt. Dies hält die Kontextnutzung effizient und verbessert die Präzision in spezialisierten Domänen.

## Warum zweckgebundene Skills wichtig sind

Allgemeine Sprachmodelle haben begrenzte Kenntnisse über WinUI-spezifische Nuancen: das gepackte Ausführungsmodell, Fluent Design-APIs, MSIX-Integration oder die spezifische Art und Weise, wie Windows App SDK Win32-Funktionalität umhüllt. Zweckgebundene Werkzeuge lösen dies, indem sie den Agent in verifizierten WinUI-Fakten verankern, anstatt in potenziell veralteten oder falschen Modellkenntnissen.

Dasselbe Muster gilt für jedes spezialisierte Framework oder SDK mit eigenen Konventionen und Anforderungen, die von allgemeinen Entwicklungsmustern abweichen.

Originalbeitrag: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
