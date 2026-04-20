---
title: "Foundry RFT Is Goedkoper en Slimmer Geworden — Dit Is Wat Er Veranderd Is"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry stuurde deze maand drie RFT-updates: globale training voor o4-mini, nieuwe GPT-4.1-modelbeoordelaars en een best practices-gids."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Als je .NET-apps bouwt die op fijnafgestelde modellen vertrouwen, zijn de Foundry-updates van deze maand de moeite waard.

De volledige details staan in de [officiële aankondiging](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/).

## Globale training voor o4-mini

o4-mini is het go-to-model voor redeneerwerk en agentische workloads. Je kunt nu fine-tuning-taken starten vanuit 13+ Azure-regio's met lagere per-token-trainingstarieven.

```bash
"trainingType": "globalstandard"
```

## Nieuwe modelbeoordelaars: GPT-4.1-familie

Drie nieuwe opties: GPT-4.1, GPT-4.1-mini en GPT-4.1-nano.

Indelingsstrategie:
- **GPT-4.1-nano** voor eerste iteraties. Lage kosten, snelle feedbacklussen.
- **GPT-4.1-mini** zodra de beoordelingsrubric stabiel is.
- **GPT-4.1** voor productiebeoordeling.

## De RFT-gegevensformaatval

RFT-gegevensformaat verschilt van SFT. Het laatste bericht in elke rij moet de rol User of Developer hebben — niet Assistant.

## Waarom dit belangrijk is voor .NET-ontwikkelaars

Goedkopere training betekent agressiever kunnen itereren. De [best practices-gids op GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) bespaart echte debugging-tijd.
