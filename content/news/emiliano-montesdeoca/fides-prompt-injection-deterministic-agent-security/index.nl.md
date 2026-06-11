---
title: "FIDES is precies het soort deterministische agentbeveiligingsverhaal dat ik vaker wil zien"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "De nieuwe FIDES-mogelijkheden in Agent Framework zijn belangrijk omdat ze de verdediging tegen prompt injection wegtrekken van heuristieken en richting afdwingbaar beleid op basis van gelabelde inhoud en middlewarecontroles bewegen."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Dit artikel is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

Prompt-injectionverdediging voelt vaak alsof ze op wankele grond staat.

Je voegt een sterkere system prompt toe. Je voegt een filter toe. Je zet een paar allowlists neer. En je hoopt dat de volgende vreemde input de aannames niet breekt.

Daarom is **FIDES** interessant.

Het sterke deel van het verhaal is dat het beveiliging verschuift naar iets deterministischers:

- labels op inhoud
- propagatie van labels door de workflow
- handhaving via middleware voordat geprivilegieerde tools worden uitgevoerd
- duidelijke beleidsgrenzen rond wat untrusted context mag beïnvloeden

## Het bronartikel is op de juiste manier direct

Het opent met de stelling dat prompt injection "**het nummer 1 risico in de OWASP LLM Top 10**" is.

Goed.

Ik houd hier van dat soort directheid, omdat te veel teams agentbeveiliging nog steeds behandelen alsof het een toekomstig probleem is in plaats van een actueel runtime-designprobleem.

En het artikel zet dat voort met een sterk praktisch contrast: de meeste huidige verdedigingsmechanismen zijn heuristisch, terwijl FIDES het systeem richting beleid en handhaving probeert te bewegen.

Dat is precies de juiste verschuiving.

## Waarom dit overtuigender is dan weer een security whitepaper

Veel AI-beveiligingsteksten blijven abstract.

Dit artikel doet iets beters. Het loopt door een heel concreet voorbeeld: een GitHub issue-triageagent, een kwaadaardige issue-body, een geprivilegieerde bestandslezing en een poging tot lekken via een publieke reactie.

Dat is nuttig omdat het hele gesprek aan een echte workflow koppelt.

En zodra je dat scenario ziet, wordt de waarde van deterministische controles veel makkelijker te begrijpen.

## Het kernidee is niet "maak het model slimmer"

Het belangrijkste hier is dat FIDES niet vraagt dat het model magisch beter wordt in het herkennen van aanvallen.

Het verandert het runtime-contract.

Dat betekent:

- inhoud krijgt labels
- labels propagateren
- tools verklaren wat ze accepteren
- middleware blokkeert onveilige paden vóór uitvoering

Dat is een veel gezondere aanpak.

Want zodra de agent tools met echte consequenties kan aanroepen, kan beveiliging niet alleen afhangen van of het model een goede dag had.

## Mijn mening

Dit is precies de richting in agentbeveiliging die ik vaker wil zien.

Niet "vertrouw erop dat het model slechte instructies negeert", maar "bouw de beleidsgrens in de runtime".

Dat is een veel gezonder model.

En als agentframeworks in productie serieus genomen willen worden, hebben ze meer verhalen zoals deze nodig.

Originele post: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)