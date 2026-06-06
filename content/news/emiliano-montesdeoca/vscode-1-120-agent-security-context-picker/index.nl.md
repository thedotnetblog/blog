---
title: "VS Code 1.120: Wachtwoordprompts, Contextgrootte-kiezer, GitHub-metadata in Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 is een gerichte release voor Copilot-gebruikers: veilige wachtwoordpromptverwerking, modelcontextgrootte-kiezer, GitHub PR-metadata in agentsessies en sessiearchivebeheer."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 werd geleverd met een reeks Copilot-agentverbeteringen die individueel klein zijn, maar merkbaar beter in dagelijks gebruik.

## Veilige Wachtwoordpromptdetectie in Agentterminals

Wanneer een Copilot-agent een terminalopdracht uitvoert die een wachtwoord- of wachtwoordzinprompt activeert, detecteert VS Code dit nu en toont een bevestigingsdialoog. Het dialoog focust de terminal zodat u het geheim direct kunt typen — en cruciaal is dat geheimen nooit via het model worden gerouteerd.

Dit is een betekenisvolle beveiligingsverbetering. Eerder konden agenten die opdrachten uitvoerden die authenticatieprompts activeerden situaties creëren waarbij gebruikers mogelijk onbedoeld referenties konden blootstellen. De schermleezerannouncement betekent dat ook toegankelijkheidsgebruikers de melding ontvangen.

## Contextgrootte-kiezer in de Modelkiezer

Een nieuwe contextgrootte-kiezer laat u kiezen hoeveel context het model voor een sessie gebruikt. Verschillende modellen hebben verschillende contextvenstergroottes, en sommige workflows profiteren van het beperken ervan (lagere latentie, lagere kosten) of maximaliseren (complexe codebases, langlopende sessies).

## GitHub PR-metadata in Agent Host-sessies

Voor sessies ondersteund door een GitHub-repository toont VS Code nu GitHub-metadata — inclusief een pull-requestknop — in de agent host-gebruikersinterface. Minder contextoverschakeling naar de browser of GitHub-extensie wanneer u aan een PR werkt.

## Chatsessiearchivebeheer

Twee verbeteringen voor de sessies Quick Pick:
- Gearchiveerde sessies zijn standaard verborgen (minder visuele rommel)
- Zoeken matcht nog steeds gearchiveerde sessies, zodat u er een op titel kunt herstellen

Sessies worden ook standaard gegroepeerd op recentheid, waardoor recent werk gemakkelijker te vinden is.

## Copilot CLI Plugin-detectie

VS Code detecteert nu automatisch door gebruikers geïnstalleerde Copilot CLI-plug-ins van `~/.copilot/installed-plugins/`. Als u WinUI of andere domeinspecifieke agentvaardigheden hebt ingesteld, worden ze opgepikt zonder handmatige configuratie.

## Aangepaste Diff Editor-API (Voorbeeld)

Voor extensieauteurs: een nieuwe voorgestelde API `customDiffEditorProvider` laat extensies een uniforme diff renderen in één webview met toegang tot zowel originele als gewijzigde documenten, in plaats van twee naast elkaar geplaatste aangepaste editorweergaven.

Originele post: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
