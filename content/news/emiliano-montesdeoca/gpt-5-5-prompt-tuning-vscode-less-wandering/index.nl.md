---
title: "VS Code's GPT-5.5-prompttuning bewijst een harde waarheid: harnessontwerp verslaat hype"
date: 2026-07-17
author: Emiliano Montesdeoca
description: "Het VS Code-experiment met GPT-5.5 laat zien dat meetbare winst voortkomt uit gedisciplineerde harness- en promptiteratie, niet alleen uit het overstappen naar nieuwere foundation models."
tags:
  - VS Code
  - GPT-5.5
  - Prompt Engineering
  - AI Agents
  - Developer Tools
  - Benchmarking
---

Het waardevolste deel van VS Code's GPT-5.5-tuningpost is niet de winnende variant. Het is de methodologie. Een duidelijke hypothese, gecontroleerde behandelingen, live-verkeer-metingen en guardrail-metrics is precies hoe agentkwaliteit verbeterd zou moeten worden in productieomgevingen.

Oorspronkelijke bron: https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers

Het kernidee was simpel: verkennende drift verminderen en eerder valideren na wijzigingen. Dat klinkt voor de hand liggend, maar de interessante bevinding is dat structurele promptsturing op de harness-laag statistisch sterke verbeteringen opleverde in latentie, tail-tokengebruik en aantal tool-calls, zonder grote kwaliteitsinstorting.

Mijn standpunt is bot: organisaties die alleen modelupgrades najagen, laten makkelijke prestatie- en kostenwinst liggen. Harnessgedrag en systeempromptontwerp kunnen bedrijfsmetrics sneller bewegen dan modelwisseling, vooral wanneer usage-based facturatie in het spel is.

Behandeling B won omdat het de volledige lus formaliseerde, niet alleen zoekterughoudendheid. Het spoorde het model aan om een lokale, falsifieerbare hypothese te vormen, een gefundeerde eerste wijziging te maken en direct gerichte validatie uit te voeren. Die volgorde weerspiegelt hoe goede menselijke engineers debuggen onder tijdsdruk.

Wat zouden teams die interne codeeragents bouwen moeten overnemen?

Definieer kwaliteitsguardrails vooraf, en optimaliseer vervolgens voor latentie en kosten binnen die grenzen. Meet zowel mediaan- als tail-gedrag. De p95-verbeteringen in tijd-tot-eerste-wijziging en tokengebruik zijn vaak waardevoller dan p50-winsten voor echte gebruikerstevredenheid.

Vermijd ook overfitting op alleen offline-evaluaties. Het VS Code-team gebruikte offline controles en valideerde vervolgens op live verkeer vóór uitrol. Die volgorde is belangrijk omdat echte workflows gedrag blootleggen dat synthetische benchmarks missen.

Eén afweging verdient aandacht: lichte beweging in kortetermijn-overlevingsmetrics. Het team heeft dit correct afgehandeld door effectgrootte en significantie af te wegen tegen sterkere, zeer significante efficiëntiewinsten. Dit is volwassen besluitvorming, geen cherry-picking van metrics.

De bredere les is strategisch. Prompt engineering is geen "promptmagie". Het is productengineering: hypotheses, experimenten, controles en deploymentpoorten. Teams die deze lus operationaliseren, zullen continu verbeteren. Teams die modelranglijsten bediscussiëren op sociale media, zullen dat niet doen.

In het komende jaar zal concurrentievoordeel in ontwikkelaars-AI minder komen van toegang tot een specifieke modelfamilie en meer van wie deze optimalisatielus betrouwbaar kan draaien. De resultaten van VS Code zijn een praktische blauwdruk: observeer, hypothetiseer, test, lever, herhaal.
