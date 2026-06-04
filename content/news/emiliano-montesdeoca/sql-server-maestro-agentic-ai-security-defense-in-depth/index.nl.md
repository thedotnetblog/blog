---
title: "MAESTRO, Defense-in-Depth en Waarom SQL Server Nu een Beveiligingsgrens Is voor AI"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Agentische AI introduceert bedreigingen waarvoor traditionele STRIDE-modellen niet zijn ontworpen. Zo mappt Microsoft SQL naar het MAESTRO-framework om een beheerde uitvoeringsgrens te bieden."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Beveiligingsbedreigingsmodellen worden gebouwd op aannames over wie of wat de verzoeken doet. STRIDE gaat uit van menselijke actoren die via gedefinieerde interfaces met systemen communiceren. AI-agents werken niet op die manier.

## STRIDE Werd Niet Ontworpen voor AI-Agents

Agentische systemen werken autonoom, koppelen tools via API-aanroepen, nemen beslissingen over welke data op te halen en welke acties uit te voeren, en kunnen instructies ontvangen van meerdere bronnen — gebruikersprompts, toolresultaten, opgehaalde data. Het STRIDE-bedreigingsmodel (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) legt agent-specifieke aanvalsvectoren zoals promptinjectie, contextvergiftiging of toolmisbruik niet adequaat vast.

De Cloud Security Alliance publiceerde het MAESTRO-framework specifiek voor het risico van AI-agents.

## Het MAESTRO-Framework

MAESTRO organiseert agentisch AI-risico in zeven lagen:

1. **Foundation Models** — de onderliggende LLM's en hun trainingskwetsbaarheden
2. **Data Operations** — gegevensopvraging, -opslag en -manipulatie
3. **Agent Frameworks** — de middleware voor agentorkestratie en -coördinatie
4. **Deployment & Infrastructure** — waar agents worden uitgevoerd en hoe ze zijn geconfigureerd
5. **Evaluation & Observability** — monitoring van agentgedrag in de loop van de tijd
6. **Security & Compliance** — toegangscontroles, audit en regelgevende naleving
7. **Agent Ecosystem** — hoe agents met elkaar en externe tools communiceren

Elke laag heeft specifieke aanvalsvectoren die traditionele beveiligingscontroles niet rechtstreeks aanpakken.

## Microsoft SQL als Beheerde Uitvoeringsgrens

SQL Server 2025 mapt op concrete manieren naar MAESTRO-lagen:

**Data Operations-laag**: `AI_GENERATE_EMBEDDINGS` ingebouwd in T-SQL houdt vectorbewerkingen binnen de beheerde grens van de database. Data hoeft de database niet te verlaten naar de modelservice voor embeddingverwerking.

**Security & Compliance-lagen**: Beveiliging op rijniveau (RLS) en dynamische datamaskering (DDM) worden toegepast ongeacht hoe het verzoek aankwam — van een menselijke gebruiker of een AI-agent. De agent kan controles niet omzeilen die door de database zelf worden afgedwongen.

**Agent Frameworks-laag**: Opgeslagen procedures dienen als toolgrenzen. In plaats van agents willekeurige SQL-toegang te geven, definieert u toegestane bewerkingen als procedures en stelt u ze beschikbaar als agenttools. Geparametriseerde queries voorkomen injectie op uitvoeringsniveau.

**Evaluation & Observability-laag**: Auditlogboekregistratie en Query Store leggen vast wat elke agent daadwerkelijk uitvoerde — niet alleen wat hem was gevraagd te doen. Deze traceerbaarheid is cruciaal voor incidentonderzoeken in agentische systemen waar attributie complex is.

## Defense-in-Depth voor Agentische AI

Het principe blijft hetzelfde als bij traditionele beveiliging: geen enkele controle is voldoende. Wat verandert is welke controles het meest tellen voor agents:

**Explosiestraal verkleinen**: toolbegrenzing via opgeslagen procedures betekent dat een gecompromitteerde agent alleen voorgedefinieerde bewerkingen kan uitvoeren. Het kan niet pivotteren naar willekeurige queries.

**Observeerbaarheid**: u moet na een incident kunnen antwoorden op "wat deed deze agent precies?". Agentische AI-systemen zonder traceerbaarheid op databaseniveau hebben blinde vlekken die applicatielogboekregistratie niet dekt.

**Beperkte uitvoering**: parametrisering, RLS en DDM zijn beveiligingsactiva ongeacht of de aanroeper menselijk is. Verzwak ze niet om agents te accommoderen.

**Verantwoording**: SQL Server-auditlogboekregistratie maakt een record van wie (welke agent, met welke credentials) wat op welk moment uitvoerde. Dit telt wanneer agentische systemen acties ondernemen met reële gevolgen in de wereld.

SQL Server 2025 werd niet gebouwd om agentisch risico abstract op te lossen — het werd gebouwd om een relationele database te zijn. Maar de governance die een enterprise database betrouwbaar maakt, blijkt precies wat een agent-uitvoeringsgrens veilig maakt.

Originele post: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
