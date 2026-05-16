---
title: "Visual Studio 2026 april-update: cloudagent, aangepaste agenten en debuggeragent"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "De april-update van Visual Studio 2026 (18.5) brengt cloudagentintegratie, aangepaste agenten op gebruikersniveau, C++-tools als GA en een Debuggeragent die oplossingen valideert tegen echt runtimegedrag."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[De april-update van Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) levert cloudagentintegratie, aangepaste agenten op gebruikersniveau, C++-tools die GA bereiken en een nieuwe Debuggeragent.

## Cloudagent: werk delegeren aan een externe Copilot-sessie

In de agentselectie van het Chat-venster kunt u via **Cloud** een taak delegeren aan een externe Copilot-codeeragent. U beschrijft het werk, de agent maakt een GitHub-issue aan in uw repository en opent een PR wanneer het klaar is. U ontvangt een melding met "View PR" / "Open in browser" — het geheel draait terwijl u doorwerkt, of zelfs met de IDE gesloten.

## Aangepaste agenten reizen nu met u mee

Aangepaste agenten op gebruikersniveau opgeslagen in `%USERPROFILE%/.github/agents/` zijn niet langer beperkt tot een repository — ze volgen u door projecten heen. Het opslagpad is configureerbaar via Tools > Opties > GitHub > Copilot > Chat. De `+`-knop in de agentselectie maakt het mogelijk direct nieuwe agenten aan te maken. Ze hebben dezelfde mogelijkheden als repository-gebonden agenten: werkruimtebewustzijn, tools, modelkeuze en MCP-verbindingen.

Ingebouwde agenten: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## C++-codebewerking tools worden GA

Twee tools — `get_symbol_call_hierarchy` en `get_symbol_class_hierarchy` — zijn nu standaard ingeschakeld. Ze geven Copilot taalbewuste navigatie door C++-codebases, inclusief overervingshiërarchieën en functieaanroepketens. Activeer via het Tools-pictogram in Copilot Chat. Werkt het beste met tool-calling modellen.

## Debuggeragent: oplossingen gevalideerd tegen echt runtimegedrag

Start vanuit een GitHub- of Azure DevOps-issue (of een beschrijving in natuurlijke taal), schakel naar de Debugger-modus en de agent:

1. Maakt een minimale reproducer
2. Genereert faalshypothesen
3. Instrumenteert de app met tracepoints en voorwaardelijke breakpoints
4. Voert een echte debugsessie uit
5. Analyseert live telemetrie
6. Stelt een precieze oplossing voor

U blijft betrokken gedurende het hele proces — het is interactief, niet volledig autonoom.

## IntelliSense-prioriteitsoplossing

VS onderdrukt nu Copilot-aanvullingen terwijl de IntelliSense-lijst actief is. Één suggestie tegelijk. Dit was een frequent knelpunt en is nu standaard ingeschakeld.

Volledige releasenotes en download op [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
