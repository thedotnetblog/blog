---
title: "NL2SQL is de SQL-injectie van het agenttijdperk"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Voordat je een agent je database laat bevragen met natuurlijke taal, lees dit. NL2SQL lijkt eenvoudig totdat je nadenkt over schemavolledigheid, niet-determinisme en wat SQL MCP Server eigenlijk oplost."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Er is een versie van de NL2SQL-pitch die perfect klinkt: gebruikers stellen vragen in natuurlijke taal, agents genereren SQL, data wordt teruggegeven. Minder schermen, minder queries, minder code. Simpel.

Dan denk je er nog vijf minuten over na.

## De problemen waar niemand het over heeft in de demo

**Schema's zijn niet ontworpen om dingen uit te leggen.** Cryptische tabelnamen, inconsistente kolomnamen, technisch valide relaties die semantisch ongeldig zijn zonder extra predicaten — dit is normaal in enterprise databases. Het zijn geen bugs, het is gewoon de geaccumuleerde geschiedenis van bedrijfswijzigingen. Maar als je een model vraagt om intentie af te leiden uit een schema dat niet ontworpen was om intentie over te brengen, probeert het model het toch. Het geeft niet op. Het genereert zijn beste query en geeft de resultaten vol vertrouwen terug.

**Modellen zijn niet-deterministisch.** Stel dezelfde vraag twee keer aan dezelfde database en je krijgt mogelijk andere SQL. Het model berekent kansen, en kleine variaties in context produceren andere output. Je kunt door testen geen garantie bereiken dat de agent altijd de correcte query genereert.

**Gebruikersreview schaalt niet.** "Bekijk elke query gewoon voor uitvoering" klinkt veilig. Maar dat gaat ervan uit dat gebruikers experts zijn in zowel het datamodel als SQL — precies de mensen die geen natuurlijke taalinterface nodig hadden. Het introduceert ook cognitieve overbelasting en een nieuwe klasse van bevestigingsbias, waarbij gebruikers die overweldigd zijn door de complexiteit van de query ongeldige queries goedkeuren in plaats van ze te onderzoeken.

**En dan is er injectie.** In traditionele SQL-ontwikkeling loste parameterisering injectie op omdat gebruikersinvoer parameters vulde, niet SQL-structuur. Met NL2SQL genereert het model zelf SQL. De prompt, schemacontext, gespreksgeschiedenis en opgehaalde data beïnvloeden allemaal wat er wordt uitgevoerd. Als iemand een prompt opstelt die verandert wat het model genereert, is dat injectie — niet op parameterniveau, maar op het niveau van querygeneratie. En in tegenstelling tot een DROP TABLE (duidelijk, herstelbaar), produceren NL2SQL-injecties queries die verkeerde resultaten retourneren zonder zichtbare fout. Zakelijke beslissingen worden genomen op basis van onjuiste data.

## Wat SQL MCP Server eigenlijk oplost

Hier maakt het artikel zijn meest nuttige praktische punt. In plaats van een agent willekeurige schematoegang te geven en het beste te hopen, stelt SQL MCP Server een **samengesteld API-oppervlak** beschikbaar gebouwd op [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

Het verschil is belangrijk: de agent genereert geen SQL. Het roept benoemde endpoints aan die vooraf gedefinieerde resultaatvormen retourneren. SQL wordt eenmalig geschreven, door een ontwikkelaar, en is deterministisch. De niet-determinisme van de agent is beperkt tot het kiezen *welk* endpoint aan te roepen, niet het samenstellen van willekeurige queries.

Dit is analoog aan wat parameterisering deed voor SQL-injectie in het traditionele app-model — het verwijdert de mogelijkheid om willekeurige queries samen te stellen uit niet-vertrouwde invoer.

## De juiste vraag

Het artikel zegt niet "gebruik NL2SQL nooit." Het zegt: wees doelbewust over *waar* je het toepast en *wat* je blootstelt. Voor verkennende analyse in een gecontroleerde omgeving, met een beperkt schema en alleen-lezen toegang, is NL2SQL misschien prima. Voor productiesystemen waarbij zakelijke beslissingen afhangen van de resultaten, is een samengestelde API-laag aanzienlijk veiliger.

Eerlijk gezegd: sommige problemen worden echt beter opgelost met gestructureerde queries achter benoemde endpoints dan met natuurlijke taal naar SQL. SQL MCP Server geeft je die optie zonder de agentische interface volledig op te geven.

Originele post: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
