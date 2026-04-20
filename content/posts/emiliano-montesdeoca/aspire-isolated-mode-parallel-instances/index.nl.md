---
title: "Aspire's Geïsoleerde Modus Lost de Port-Conflict Nachtmerrie op voor Parallelle Ontwikkeling"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introduceert --isolated modus: willekeurige poorten, afzonderlijke geheimen en nul botsingen bij het uitvoeren van meerdere instanties van dezelfde AppHost. Perfect voor AI-agents, worktrees en parallelle workflows."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Als je ooit twee instanties van hetzelfde project tegelijkertijd hebt geprobeerd uit te voeren, ken je de pijn. Poort 8080 is al in gebruik.

Aspire 13.2 lost dit op met één vlag. James Newton-King heeft [alle details opgeschreven](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/).

## De oplossing: `--isolated`

```bash
aspire run --isolated
```

Elke run krijgt:
- **Willekeurige poorten** — geen botsingen tussen instanties
- **Geïsoleerde gebruikersgeheimen** — verbindingsstrings en API-sleutels blijven afzonderlijk per instantie

## Echte scenario's

**Meerdere checkouts:**

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Beide draaien zonder conflicten.

**Achtergrondagents in VS Code.** Wanneer de achtergrondagent van Copilot Chat een git worktree aanmaakt om onafhankelijk te werken, zorgt de geïsoleerde modus ervoor dat beide instanties gewoon werken.

## Samenvatting

Geïsoleerde modus is een kleine functie die een reëel, steeds vaker voorkomend probleem oplost. Haal 13.2 op met `aspire update --self`.
