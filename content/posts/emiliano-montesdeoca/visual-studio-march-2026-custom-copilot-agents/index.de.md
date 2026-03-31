---
title: "Visual Studios März-Update lässt dich eigene Copilot-Agenten bauen — und find_symbol ist ein großes Ding"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studios März 2026-Update bringt benutzerdefinierte Copilot-Agenten, wiederverwendbare Agent Skills, ein sprachbewusstes find_symbol-Tool und Copilot-gestütztes Profiling aus dem Test Explorer."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}}).*

Visual Studio hat gerade sein bedeutendstes Copilot-Update bekommen. Mark Downie [hat das März-Release angekündigt](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), und die Überschrift sind Custom Agents — aber ehrlich gesagt könnte das `find_symbol`-Tool weiter unten die Funktion sein, die deinen Workflow am meisten verändert.

## Benutzerdefinierte Copilot-Agenten in deinem Repo

Willst du, dass Copilot deinen Team-Codierstandards folgt, deine Build-Pipeline ausführt oder deine internen Docs abfragt? Jetzt kannst du genau das bauen.

Custom Agents werden als `.agent.md`-Dateien definiert, die du in `.github/agents/` in deinem Repository ablegst. Jeder Agent hat vollen Zugriff auf Workspace-Awareness, Code-Verständnis, Tools, dein bevorzugtes Modell und MCP-Verbindungen.

## Agent Skills: wiederverwendbare Instruktionspakete

Skills werden automatisch aus `.github/skills/` in deinem Repo oder `~/.copilot/skills/` in deinem Profil geladen. Denke an Skills als modulare Expertise, die du mischen und kombinieren kannst.

## find_symbol: sprachbewusste Navigation

Das neue `find_symbol`-Tool gibt Copilots Agent-Modus sprachservice-gestützte Symbol-Navigation. Statt Text zu suchen, kann der Agent alle Referenzen eines Symbols finden und auf Typ-Informationen, Deklarationen und Scope zugreifen.

Für .NET-Entwickler ist das eine massive Verbesserung — C#-Codebasen mit tiefen Typ-Hierarchien profitieren enorm.

## Tests mit Copilot profilen

Im Test Explorer gibt es jetzt **Profile with Copilot**. Der Profiling Agent führt den Test aus und analysiert automatisch CPU-Nutzung und Instrumentierungsdaten.

## Perf Tips beim Live-Debugging

Performance-Optimierung passiert jetzt während des Debuggens. Visual Studio zeigt inline Ausführungszeit und Performance-Signale. Siehst du eine langsame Zeile? Klicke auf den Perf Tip und frage Copilot nach Optimierungsvorschlägen.

## NuGet-Schwachstellen aus dem Solution Explorer beheben

Bei erkannten NuGet-Schwachstellen siehst du einen **Fix with GitHub Copilot**-Link direkt im Solution Explorer.

## Zusammenfassung

Custom Agents und Skills sind die Überschrift, aber `find_symbol` ist der Sleeper Hit — es verändert grundlegend, wie genau Copilot beim Refactoring von .NET-Code sein kann. Kombiniert mit Live-Profiling und Schwachstellen-Fixes fühlen sich die KI-Features von Visual Studio jetzt wirklich praktisch an.

Lade [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) herunter, um alles auszuprobieren.
