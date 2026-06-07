---
title: "VS Code 1.121: Favoriete Modellen Vastmaken, Terminaluitvoercompressie, Agent SSH"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 voegt modelingfavorieten toe, uitgebreide terminaluitvoercompressie voor test-runners en buildtools, een idle-stiltetimer voor achtergrondterminals en toetsenbord-interactieve SSH-verificatie in agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 zet de kwaliteitsverbeteringen van de Copilot-agent uit 1.120 voort, met focus op modelbeheer en terminalgedrag.

## Favoriete Modellen Vastmaken

De modelselectie ondersteunt nu vastmaken. Als u altijd hetzelfde model of twee gebruikt, maak ze dan vast aan de bovenkant van de lijst. Vermindert scrollen wanneer u toegang heeft tot veel modellen van meerdere providers.

## Uitgebreide Terminaluitvoercompressie

De agentterminaltools comprimeerden al uitvoer voor veelgebruikte opdrachten. 1.121 breidt dit uit om test-runners en buildtools te omvatten:

- **Test-runners:** `pytest`, `jest`, `cargo test`
- **Buildtools:** `tsc`, `cargo build`, `make`
- **Linters, Docker, pakketbeheerders**

Lange builduitvoer en teststoringsrapporten worden gecomprimeerd tot relevante fragmenten voordat ze aan het model worden doorgegeven. Dit houdt het contextgebruik beheersbaar wanneer de agent bouwcycli of testsuites uitvoert die duizenden regels uitvoer kunnen produceren.

## Idle-Stiltetimer voor Achtergrondterminals

Een nieuwe idle-stiltetimer voor de `run_in_terminal`-tool: als een synchrone opdracht gedurende een configureerbare periode geen uitvoer produceert, wordt deze automatisch gepromoveerd naar achtergronduitvoering. Dit voorkomt dat langlopende opdrachten de agent blokkeren tijdens stille verwerking. U krijgt een terminal-ID om later te controleren.

## VSCODE_AGENT Omgevingsvariabele

Wanneer Copilot Chat opdrachten in de terminal uitvoert, wordt nu een omgevingsvariabele `VSCODE_AGENT` ingesteld. Handig als u scripts of tools heeft die zich anders gedragen wanneer ze vanuit een agentsessie worden aangeroepen versus interactief.

## Aan Chat Toevoegen vanuit Browser

Rechtsklikken in de geïntegreerde browser toont nu de optie "Aan Chat Toevoegen". Selecteer inhoud van een webpagina en voeg deze direct toe aan uw Copilot Chat-context zonder kopiëren en plakken.

## Opgelost: Meerregelige Shellopdrachten in Agent Host

Een langverwachte bugfix: meerregelige shellopdrachten in de agenterminaltools van Agent Host werken nu correct. Eerder konden deze mislukken of onjuist gedrag vertonen.

## Toetsenbord-Interactieve SSH-Verificatie

Agent Host SSH-verbindingen ondersteunen nu toetsenbord-interactieve verificatie — de fallback-verificatiemethode die door sommige SSH-servers wordt gebruikt (inclusief sommige oudere bedrijfsconfiguraties). Agenten die op externe SSH-hosts werken, zijn minder kans om verificatiestoringen te ondervinden.

Originele post: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
