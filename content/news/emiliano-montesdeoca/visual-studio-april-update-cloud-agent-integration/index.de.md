---
title: "Visual Studio 2026 April-Update: Cloud-Agent, benutzerdefinierte Agents und Debugger-Agent"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Das April-Update von Visual Studio 2026 (18.5) bringt Cloud-Agent-Integration, benutzerbezogene benutzerdefinierte Agents, C++-Tools als GA und einen Debugger-Agent, der Fixes gegen das echte Laufzeitverhalten validiert."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Das April-Update von Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) liefert Cloud-Agent-Integration, benutzerbezogene benutzerdefinierte Agents, C++-Tools die GA erreichen, und einen neuen Debugger-Agent.

## Cloud-Agent: Arbeit an eine Remote-Copilot-Sitzung delegieren

Im Agent-Picker des Chat-Fensters können Sie durch Auswahl von **Cloud** eine Aufgabe an einen Remote-Copilot-Coding-Agent übergeben. Sie beschreiben die Arbeit, der Agent erstellt ein GitHub-Issue in Ihrem Repository und öffnet einen PR, wenn er fertig ist. Sie erhalten eine Benachrichtigung mit "View PR" / "Open in browser" — das Ganze läuft, während Sie weiterarbeiten oder sogar mit geschlossener IDE.

## Benutzerdefinierte Agents begleiten Sie jetzt überall

Benutzerbezogene benutzerdefinierte Agents unter `%USERPROFILE%/.github/agents/` sind nicht mehr auf ein Repository beschränkt — sie begleiten Sie projektübergreifend. Der Speicherpfad ist unter Tools > Optionen > GitHub > Copilot > Chat konfigurierbar. Die `+`-Schaltfläche im Agent-Picker ermöglicht die direkte Erstellung neuer Agents. Sie erhalten dieselben Fähigkeiten wie repository-bezogene Agents: Arbeitsbereichsbewusstsein, Tools, Modellauswahl und MCP-Verbindungen.

Integrierte Agents: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## C++-Code-Editing-Tools werden GA

Zwei Tools — `get_symbol_call_hierarchy` und `get_symbol_class_hierarchy` — sind jetzt standardmäßig aktiviert. Sie geben Copilot sprachbewusste Navigation durch C++-Codebasen und decken Vererbungshierarchien sowie Funktionsaufrufketten ab. Aktivierung über das Tools-Symbol im Copilot Chat. Funktioniert am besten mit Tool-Calling-Modellen.

## Debugger-Agent: Fixes werden gegen echtes Laufzeitverhalten validiert

Starten Sie von einem GitHub- oder Azure-DevOps-Issue (oder einer Beschreibung in natürlicher Sprache), wechseln Sie in den Debugger-Modus, und der Agent:

1. Erstellt einen minimalen Reproducer
2. Generiert Fehlerhypothesen
3. Instrumentiert die App mit Tracepoints und bedingten Breakpoints
4. Führt eine echte Debug-Sitzung durch
5. Analysiert Live-Telemetrie
6. Schlägt eine präzise Lösung vor

Sie bleiben während des gesamten Prozesses eingebunden — es ist interaktiv, nicht vollständig autonom.

## IntelliSense-Prioritätskorrektur

VS unterdrückt jetzt Copilot-Vervollständigungen, während die IntelliSense-Liste aktiv ist. Jeweils nur ein Vorschlag. Dies war ein häufiger Reibungspunkt und ist jetzt standardmäßig aktiviert.

Vollständige Release-Notes und Download auf [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
