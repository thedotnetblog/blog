---
title: "De echte grens voor agentic SQL: auditeerbaarheid met OBO in SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "On-Behalf-Of-authenticatie in Data API builder plus SQL MCP Server is een grote mijlpaal voor governance omdat Azure SQL eindelijk de mens achter een agentactie kan auditen."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Er is een pijnlijke waarheid in enterprise-AI-projecten: veel teams zijn geobsedeerd door modelkwaliteit en negeren verantwoording. Wanneer een agent productiedata schrijft of leest, is de eerste vraag bij een incidentonderzoek niet "was het antwoord goed?" Het is "wie heeft dit eigenlijk gedaan?"

Oorspronkelijke bron: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

Daarom is OBO-ondersteuning in Data API builder 2.0 met SQL MCP Server een grotere zaak dan het eerst lijkt. Gebruikersnaam/wachtwoord- en managed-identity-benaderingen werken operationeel nog steeds, maar beide laten identiteit samenvallen met de servicegrens. Logs tonen de app of middleware, niet de menselijke oorsprong van het verzoek. Dat is acceptabel voor eenvoudige automatisering. Het is niet acceptabel voor gereguleerde agentic workflows.

Met OBO authenticeert SQL de gedelegeerde gebruikerscontext, niet de identiteit van de toolhost. Dat geeft je een fundamenteel beter auditmodel: gebruikersprincipal, actie, statementcontext en middle-tier-app-identifier samen. Je krijgt traceerbaarheid zonder het controleoppervlak van MCP-tools en DAB-entiteitsrechten te verliezen.

Mijn mening is hier stellig: als je agent gevoelige SQL-data kan aanraken, zou OBO je standaardarchitectuur moeten zijn, geen optionele verhardingstaak. De setup is uitgebreider, maar identiteitsschuld wordt altijd later betaald, meestal tijdens beveiligingsincidenten, compliance-audits of escalaties naar het management.

Praktische implementatierichtlijnen:

Begin met het valideren van de identiteitsflow met een minimale "WhoAmI"-view en geautomatiseerde controles in integratietests. Als de SQL-principal niet overeenkomt met de ingelogde gebruiker, stop en fix voordat je uitlevert. Bekabel vervolgens Log Analytics-queries voor SQLSecurityAuditEvents naar je SOC-dashboards en alert op hoogrisicoacties geïnitieerd via OBO-paden. Stem tot slot RBAC en DAB-rechten af zodat identiteit op gebruikersniveau en autorisatie op actieniveau end-to-end consistent blijven.

Eén subtiel maar belangrijk ontwerppunt in de aankondiging is cachegedrag. DAB blokkeert expliciet responscaching wanneer user-delegated auth is ingeschakeld. Die afweging is correct. Prestatietrucs die gebruikersgebonden resultaten kunnen lekken, zijn het niet waard in multi-tenant of gereguleerde omgevingen.

SQL MCP Server plus OBO is het begin van een volwassen patroon: agents als gecontroleerde operators, gebruikers als verantwoordelijke principals, dataplanes als auditeerbare systemen. Als je architectuur niet met vertrouwen kan antwoorden op "wie heeft dit gedaan", is het geen productieklare AI, hoe gepolijst de demo er ook uitziet.
