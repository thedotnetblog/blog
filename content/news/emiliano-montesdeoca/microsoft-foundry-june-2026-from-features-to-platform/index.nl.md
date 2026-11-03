---
title: "Microsoft Foundry juni 2026: van featuredruppels naar een bestuurd agentplatform"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "De Foundry-updates van juni signaleren een platformovergang: distributie, tooling, geheugen, observability en optimalisatie convergeren tot een enterprise-klare agent-operationsstack."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

De Foundry-golf van juni 2026 is niet zomaar nog een maandelijkse samenvatting. Het markeert een volwassenheidsovergang van "bouw coole agents" naar "beheer agents als bestuurde enterprise-systemen". Dat onderscheid is belangrijker dan welke individuele feature dan ook.

Oorspronkelijke bron: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Drie updates definiëren de verschuiving. Ten eerste bereikte agentpublicatie naar Microsoft 365 Copilot en Teams GA, wat distributie verplaatst van aangepaste integratieprojecten naar een opinionated deploymentbaan. Ten tweede kregen Toolboxes sterkere ontdekkings- en uitvoeringscontroles, inclusief toolzoeken en routines. Ten derde werd observability plus optimalisatie een bewuste gesloten lus, geen nagedachte.

Mijn standpunt: dit is het belangrijkste patroon in de release. Tracing, evaluatie, optimalisatie en gecontroleerde uitrol vormen het minimaal levensvatbare operationele model voor niet-deterministische systemen. Als je slechts één van die onderdelen hebt, heb je telemetrie of tuning, geen governance.

Claude GA binnen Foundry is ook strategisch, maar niet vooral vanwege modelkwaliteit. De grotere waarde is enterprise-integratie: Entra-authenticatie, RBAC, facturatiecontinuïteit en beleidsafstemming. Teams die overstappen van directe model-endpoints naar Foundry zouden dit moeten framen als operationele consolidatie, niet alleen providerwissel.

Autopilot-agents zijn veelbelovend, maar organisaties zouden ze moeten benaderen met nuchtere architectuurkeuzes. Gedeelde-ruimtesamenwerking in Teams kan productiviteit ontgrendelen, maar verhoogt snel de complexiteit van identiteit, rechten en verantwoordelijkheid. Begin met afgebakende scopes en strikte goedkeuringscontrolepunten vóór brede uitrol.

Praktische aanbevelingen:

Als je al in pilot zit, geef prioriteit aan instrumentatie boven capaciteitsuitbreiding. Bekabel eerst GenAI-tracing. Zet vervolgens evaluatiesuites op die gekoppeld zijn aan bedrijfsresultaten, geen generieke modelmetrics. Pas daarna zou je optimizer-lussen en promotieworkflows moeten draaien.

Voor toolbox-zware agents, schakel toolzoeken vroeg in om contextruis en het risico op verkeerde toolselectie te verminderen naarmate catalogi groeien. Voor agents met geheugen, definieer TTL- en retentiebeleid vooraf. Geheugen zonder levenscyclus-controles wordt compliance-schuld.

De meest eigenzinnige conclusie die ik kan trekken is deze: Foundry gaat nu minder over "welk model kies ik?" en meer over "kan ik agentgedrag draaien als een beheerde levenscyclus?" Teams die de tweede vraag goed beantwoorden, passen zich makkelijk aan bij modelverloop. Teams die gefixeerd zijn op modelranglijsten blijven elk kwartaal broze stacks herbouwen.

De release van juni maakt één ding duidelijk. Foundry wordt een operationsplatform voor AI-systemen, niet alleen een ontwikkeltoolkit. Dat is een moeilijker product om te bouwen, en een veel waardevoller om te adopteren.
