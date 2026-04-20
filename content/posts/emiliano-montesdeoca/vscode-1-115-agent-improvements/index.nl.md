---
title: "VS Code 1.115 — Achtergrondterminalnotificaties, SSH-agentmodus en Meer"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 brengt achtergrondterminalnotificaties voor agenten, SSH-remote agenthosting, bestandsplakken in terminals en sessiegebonden bewerkingentracking. Dit is wat er toe doet voor .NET-ontwikkelaars."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "vscode-1-115-agent-improvements" >}}).*

VS Code 1.115 is zojuist [verschenen](https://code.visualstudio.com/updates/v1_115), en hoewel het een lichtere release is wat betreft hoofdfuncties, zijn de agentgerelateerde verbeteringen echt nuttig als je dagelijks met AI-codeassistenten werkt.

Laat me uitlichten wat er echt de moeite waard is om te weten.

## Achtergrondterminals praten terug naar agenten

Dit is de uitgelichte functie. Achtergrondterminals informeren agenten nu automatisch wanneer opdrachten zijn voltooid, inclusief de exitcode en terminaluitvoer.

Waarom is dit belangrijk? Als je de agentmodus van Copilot hebt gebruikt om build-opdrachten of testsuites op de achtergrond uit te voeren, ken je de pijn van "is dat al klaar?" — achtergrondterminals waren in wezen vuur en vergeet. Nu krijgt de agent een melding wanneer je `dotnet build` of `dotnet test` is voltooid, ziet de uitvoer en kan dienovereenkomstig reageren.

Er is ook een nieuwe `send_to_terminal`-tool waarmee agenten opdrachten naar achtergrondterminals kunnen sturen met gebruikersbevestiging.

## SSH-remote agenthosting

VS Code ondersteunt nu verbinding maken met externe machines via SSH, waarbij de CLI automatisch wordt geïnstalleerd en in agenthost-modus wordt gestart.

## Bewerkingentracking in agentsessies

Bestandsbewerkingen die tijdens agentsessies zijn gemaakt, worden nu bijgehouden en hersteld, met diffs, ongedaan maken/opnieuw uitvoeren en staatsherstel.

## Browsertabbladbewustzijn en andere verbeteringen

Nog een paar kwaliteitsverbeteringen:

- **Browsertabbladtracking** — chat kan nu tabbladen bijhouden die tijdens een sessie zijn geopend en er links naar maken
- **Bestanden plakken in terminal** — plak bestanden (inclusief afbeeldingen) in de terminal met Ctrl+V
- **Testdekking in minimap** — testdekkingsindicatoren verschijnen nu in de minimap
- **Knijpzoom op Mac** — geïntegreerde browser ondersteunt knijpzoomgebaren

## Afsluiting

VS Code 1.115 is een incrementele release, maar de agentverbeteringen — achtergrondterminalnotificaties, SSH-agenthosting en bewerkingentracking — zorgen voor een merkbaar soepelere ervaring voor AI-ondersteunde ontwikkeling. Bekijk de [volledige releasenotes](https://code.visualstudio.com/updates/v1_115) voor elk detail.
