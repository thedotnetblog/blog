---
title: "Agent Harness, Hosted Agents en CodeAct: dit is de Agent Framework-update waar ik me op zou richten"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "De aankondiging van Agent Framework op Build 2026 zit vol, maar de belangrijkste lijnen zijn het harness-model, Foundry-hosted agents en CodeAct om orkestratie-overhead te verminderen."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

De grote Agent Framework-aankondiging op Build behandelt veel, maar drie thema's springen er voor mij meteen uit:

- **het harness dat een meer first-class onderdeel van het runtime-verhaal wordt**
- **Foundry-hosted agents die een pad naar productie bieden**
- **CodeAct dat de overhead van meerstapsorkestratie verlaagt**

Dat zijn de onderdelen waar ik scherp op zou letten.

## Het harness wordt het echte zwaartepunt

De bronpost beschrijft het harness als de laag waar modelredenering en echte uitvoering elkaar ontmoeten.

Dat is de juiste beschrijving, en ook de reden dat ik denk dat dit belangrijker is dan veel losse feature-bullets.

Zodra een agent nodig heeft:

- bestandstoegang
- shell-uitvoering
- planningsmodi
- to-do's
- sessiegeheugen
- goedkeuringsworkflows

heb je het niet meer alleen over een prompt plus een model.

Je hebt het over runtime-gedrag.

Daar worden frameworks óf echt nuttig, óf speelgoed.

En Microsoft Agent Framework probeert duidelijk op precies die laag nuttiger te worden.

## Hosted agents zijn waar het verhaal van lokaal naar productie echt wordt

Ik vind ook dat het hosted agents-gedeelte een van de strategisch belangrijkste onderdelen van de aankondiging is.

De bronpost zegt expliciet dat dit de gemakkelijkste manier is om die agent een thuis in productie te geven.

Die formulering doet ertoe, omdat de meeste agentframeworks nog altijd veel sterker zijn in lokale experimenten dan in operationele deployment.

Als Foundry-hosted agents de stap van lokale ontwikkeling naar:

- schaalvergroting
- observability
- managed identity
- sessieafhandeling
- versiebeheer

aanzienlijk eenvoudiger maken, dan sluit dat een van de grootste gaten in het huidige agent-ecosysteem.

Dat zou een betekenisvolle verbetering zijn.

## CodeAct is het meest opwindende technische idee in de update

Als ik het interessantste technische concept uit de post moest kiezen, zou ik waarschijnlijk CodeAct kiezen.

Het probleem dat het probeert op te lossen is heel reëel: te veel meerstaps agent-workflows zijn duur omdat de orkestratielus zelf te veel modelrondes opslokt.

Dus wanneer de bronpost een resultaat laat zien als:

- 52.4% sneller
- 63.9% minder tokens

valt dat meteen op.

Natuurlijk zijn dat benchmarkcijfers voor een representatieve workload, geen universele wet. Maar het grotere idee blijft overtuigend.

Als het model een tool-calling-keten kan samendrukken tot een efficiëntere uitvoervorm, verandert dat de economie van agentsystemen behoorlijk.

## Wat ontwikkelaars hier volgens mij echt uit moeten halen

De belangrijke les is niet hoeveel functies er zijn geleverd.

De les is dat het framework sterker wordt op de plekken waar echte toepassingen het meest nodig hebben:

- runtime shell
- deployment-pad
- uitvoeringsefficiëntie
- ingebouwde operationele patronen

Dat is het soort volwassenheidssignaal dat ik veel belangrijker vind dan weer een oppervlakkige AI-featurechecklist.

## Mijn kijk

Deze update is belangrijk omdat hij niet alleen meer oppervlak toevoegt.

Hij versterkt het runtime- en deployment-verhaal rond agents op een manier die voor echte toepassingen belangrijk zou moeten zijn, vooral voor teams die van lokale experimenten willen doorgroeien naar systemen die ze echt kunnen draaien en onderhouden.

Daar wordt het framework overtuigender.

En als ik deze release nauwlettend zou volgen, dan waren harness, hosted agents en CodeAct absoluut de onderdelen waaraan ik de meeste aandacht zou geven.

Oorspronkelijke post: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
