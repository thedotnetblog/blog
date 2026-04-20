---
title: "SQL MCP Server, Copilot in SSMS en een Database Hub met AI-agents: Wat Er Echt Toe Doet van SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft deed een reeks databaseaankondigingen op SQLCon 2026. Dit is wat er echt toe doet als je AI-aangedreven apps bouwt op Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "agentic-ai-microsoft-databases-what-matters" >}}).*

Microsoft heeft zojuist [SQLCon 2026 gelanceerd naast FabCon in Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/). Ik sla de enterprise-prijsslides over en focus op de onderdelen die ertoe doen voor ontwikkelaars die met Azure SQL en AI bouwen.

## SQL MCP Server is in openbare preview

Dit is de kop voor mij. Azure SQL Database Hyperscale heeft nu een **SQL MCP Server** in openbare preview waarmee je SQL-gegevens veilig kunt verbinden met AI-agents en Copilots via het [Model Context Protocol](https://modelcontextprotocol.io/).

Voor .NET-ontwikkelaars die AI-agents bouwen met Semantic Kernel of Microsoft Agent Framework opent dit een schoon integratiepad. Je agent moet voorraad controleren? Een klantrecord opzoeken? Een bestelling valideren? MCP geeft het een gestructureerde manier om dat te doen zonder aangepaste data-ophaalcode.

## GitHub Copilot in SSMS 22 is nu GA

Als je tijd doorbrengt in SQL Server Management Studio, is GitHub Copilot nu algemeen beschikbaar in SSMS 22. Dezelfde Copilot-ervaring die je al gebruikt in VS Code en Visual Studio, maar voor T-SQL.

De praktische waarde is direct: op chat gebaseerde hulp bij het schrijven van query's, refactoring van opgeslagen procedures, het oplossen van prestatieproblemen en beheertaken.

## Vectorindexen kregen een serieuze upgrade

Azure SQL Database heeft nu snellere, capabelere vectorindexen met volledige ondersteuning voor invoegen, bijwerken en verwijderen. Dat betekent dat je vectorgegevens in real-time actueel blijven — geen batchherindexering nodig.

Wat nieuw is:
- **Kwantisering** voor kleinere indexgroottes zonder te veel nauwkeurigheid te verliezen
- **Iteratief filteren** voor preciezere resultaten
- **Tightere query-optimizer-integratie** voor voorspelbare prestaties

Als je RAG doet met Azure SQL als vectoropslag, zijn deze verbeteringen direct bruikbaar.

## Database Hub in Fabric: agentisch beheer

Microsoft kondigde de **Database Hub in Microsoft Fabric** aan (vroege toegang), die één venster biedt over Azure SQL, Cosmos DB, PostgreSQL, MySQL en SQL Server via Arc.

AI-agents bewaken continu je database-omgeving, signaleren wat veranderd is, leggen uit waarom het belangrijk is en stellen voor wat je vervolgens moet doen.

## Wat dit betekent voor .NET-ontwikkelaars

1. **Probeer SQL MCP Server** als je AI-agents bouwt — de schoonste manier om agents databasetoegang te geven.
2. **Schakel Copilot in SSMS in** als je dat nog niet hebt gedaan.
3. **Kijk naar vectorindexen** als je RAG doet en momenteel een aparte vectoropslag gebruikt.

Bekijk de [volledige aankondiging van Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) en [schrijf je in voor vroege toegang tot Database Hub](https://aka.ms/database-hub).
