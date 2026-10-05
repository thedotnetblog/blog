---
title: 'Cosmos DB-toegang zonder secrets is de nieuwe basislijn'
date: 2026-07-16
author: 'Emiliano Montesdeoca'
description: 'Als je Cosmos DB-app nog steeds afhankelijk is van keys, loop je al achter op operationele beveiliging.'
tags:
  - azure-cosmos-db
  - dotnet
  - managed-identity
  - rbac
  - cloud-security
---

Oorspronkelijke bron: [Which Azure Cosmos DB Role Does My App Need?](https://devblogs.microsoft.com/cosmosdb/which-azure-cosmos-db-role-does-my-app-need/)

Het belangrijkste idee in deze Cosmos DB-richtlijn is geen commando, geen rol-ID of een CLI-trucje. Het is architecturaal: stop met credentials behandelen als app-configuratie en begin identiteit te behandelen als runtime-status.

Te veel teams leveren nog steeds met connectiestrings omdat het snel aanvoelt. Het is niet snel. Het is uitgesteld risico. Elke key in een configbestand wordt een incident dat wacht op een overhaaste commit, een gekopieerde pijplijnvariabele of een gelekt log. Managed identity plus data-plane RBAC verwijdert die categorie fouten bijna volledig.

De praktische uitdaging is verwarring tussen control-plane- en data-plane-autorisatie. Hier verliezen veel verder sterke teams dagen. Azure RBAC-rollen op resources verlenen niet automatisch documenttoegang, en Cosmos data-plane-rollen verlenen geen accountbeheer. Als je team die scheiding niet expliciet documenteert in je runbooks, blijf je broze deployments en moeilijk te debuggen 403's krijgen.

Mijn eigenzinnige aanbeveling voor productieteams is simpel:

Begin met Data Reader voor leespaden en Data Contributor alleen waar schrijven echt vereist is.

Bepaal de scope breed alleen wanneer je één applicatiegrens per account hebt.

Als je een account deelt tussen services, verkleen de scope vroeg naar database- of containergrenzen in plaats van te wachten op auditdruk.

Dit is een van die beslissingen die zich opstapelt. Wanneer je je .NET-app bekabelt met DefaultAzureCredential en alleen-endpoint-configuratie, wordt elke omgeving schoner: lokaal, CI, staging en productie. Je maakt incidentrespons ook sneller omdat je over rechten kunt redeneren via roltoewijzingen in plaats van mysterieuze keys op te sporen.

Het artikel hint ook naar iets dat volwassen teams zouden moeten omarmen: rechten als iteratief ontwerp, geen eenmalige setup. Je kunt breed genoeg beginnen om te leveren, en vervolgens versmallen met telemetrie en toegangsreviews. Least privilege is geen filosofisch eindpunt; het is een leveringsgewoonte.

Als je maar één ding uit deze post overneemt, laat het dit zijn: verwijder secrets eerst, optimaliseer rollen als tweede. Teams die die volgorde omdraaien, lopen meestal vast in vergaderingen. Teams die eerst secrets verwijderen, leveren meestal, en verharden daarna.

In 2026 is secretless data-toegang geen geavanceerd patroon. Het is de minimale verantwoorde standaard voor serieuze .NET-systemen op Azure.
