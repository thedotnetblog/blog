---
title: "Cosmos DB Shell Is nu in Openbare Preview — En Heeft een Ingebouwde MCP-Server"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell is een nieuwe open source CLI die databaseopdrachten beschikbaar stelt als MCP-tools. Uw AI-agents kunnen containers navigeren, query's uitvoeren en gegevens beheren met dezelfde interface die u gebruikt."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Als u ooit tussen een portaltabblad, een SDK-voorbeeld en een half afgemaakt script moest schakelen om één vraag over Cosmos DB te beantwoorden, kent u de wrijving die dit project is ontworpen om te elimineren.

Azure Cosmos DB Shell is zojuist in openbare preview gegaan. Het is een open source CLI met bash-achtige syntaxis en — het deel dat het interessant maakt — een ingebouwde MCP-server.

## Wat Het Onderscheidt van Andere Database CLI's

De CLI zelf is nuttig: bekende opdrachten, scriptingondersteuning, CI/CD-integratie. Dat deel is de minimumvereiste voor een op ontwikkelaars gericht databasehulpmiddel.

Het interessante deel is de MCP-serverintegratie. Elke opdracht die de CLI beschikbaar stelt, wordt beschikbaar als een MCP-tool die uw AI-agents kunnen aanroepen. Geen aangepaste API-laag, geen integratiecode om te schrijven. Uw agent kan:

- Databasehiërarchieën navigeren met `cd`, `ls`, `pwd`
- SQL-query's uitvoeren met `query` en gestructureerde resultaten ontvangen
- Items maken en wijzigen met `create item`, `update`, `rm`
- Databases en containers beheren met `mkdb`, `mkcon`, `rmdb`, `rmcon`
- De huidige context inspecteren met `endpoint`, `pwd`

De essentiële verandering: uw agent praat niet met een Cosmos DB-API — het praat met dezelfde shell-interface die u gebruikt. De opdrachten zijn deterministisch, auditeerbaar en open source zodat u precies kunt inspecteren wat er gebeurt.

## De Open Source-Basis Is Belangrijk

Dit is geen beheerde service met een zwarte doos. De shell is open source, wat betekent:

- Beveiligingsteams kunnen de implementatie auditen
- Platformteams kunnen het forken en uitbreiden voor hun specifieke normen
- Ontwikkelaars kunnen verbeteringen bijdragen die iedereen ten goede komen

Voor enterprise-teams die AI-tools adopteren, wordt "kunnen we precies zien hoe het werkt" steeds minder een optionele vereiste. Open source hier is een significante differentiator.

## Drie Scenario's Die Eenvoudiger Worden

**Intelligente gegevensanalyse** — verbind een agent met de shell, stel vragen in natuurlijke taal, ontvang gestructureerde queryresultaten. De agent verwerkt de querybouw; de shell verwerkt de uitvoering.

**Autonoom gegevensbeheer** — workflows die gegevens in Cosmos DB moeten maken, bijwerken of verwijderen, kunnen dit doen via MCP-tools zonder aangepaste integratie.

**Realtime monitoring en meldingen** — een agent kan containers periodiek opvragen, resultaten vergelijken en anomalieën rapporteren via elk zinvol notificatiekanaal.

De MCP-interface maakt deze scenario's combineerbaar met elk AI-platform dat MCP ondersteunt — niet alleen Microsoft-tools.

## Aan de Slag

De shell is in openbare preview. Installeer het, configureer uw Cosmos DB-verbinding en schakel de MCP-server in. Daarna kan elke MCP-compatibele agenthost de tools ontdekken en gebruiken.

Originele post: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
