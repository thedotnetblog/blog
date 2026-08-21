---
title: "Aspire in VS Code 13.4 verstrakt de ontwikkelaarslus op alle juiste manieren"
date: 2026-06-16
author: "Emiliano Montesdeoca"
description: "Aspire in VS Code 13.4 is niet zomaar een feature-update. Het is een echte verbetering van de dagelijkse ontwikkellus met betere debugging, resourcezichtbaarheid, panel-integratie en TypeScript AppHost-ondersteuning."
tags:
  - Aspire
  - VS Code
  - .NET
  - Developer Experience
  - TypeScript
---

De beste tooling-updates zijn degene die je na een paar dagen voelt, niet degene die alleen goed ogen in release notes.

Zo lees ik **Aspire in VS Code 13.4**.

Deze update draait helemaal om het verstrakken van de innerlijke lus: sneller projecten aanmaken, meertalige resources natuurlijker debuggen, gezondheid en commando's direct in de editor tonen, en het dashboard dichtbij houden zonder het de enige plek te maken waar je kunt werken.

Dat is een heel goede richting.

## De grote winst is minder contextwisselingen

Als je Aspire serieus gebruikt, beweeg je meestal over meerdere oppervlakken:

- AppHost-code
- terminal
- dashboard
- logs
- debugsessies
- service-endpoints

Wat 13.4 goed doet, is de wrijving tussen die oppervlakken verminderen.

De nieuwe VS Code-ervaring maakt meer van de app-status zichtbaar precies waar je al werkt:

- resourcegezondheid in de editor
- commando's naast resourcedeclaraties
- eenvoudiger dashboardtoegang
- logtoegang vanuit de AppHost-context
- een panel dat nuttig blijft, zelfs voordat volledige debugging begint

Dat klinkt klein totdat je het elke dag doet.

## Debuggen van gemengde stacks is belangrijker dan mensen denken

Een van de sterkste onderdelen van deze update is het natuurlijkere verhaal voor het debuggen van **C#, TypeScript, Python, Go, browserapps en Azure Functions** in één Aspire-gedreven flow.

Dat weerspiegelt de echte vorm van moderne apps veel beter dan doen alsof alles in één enkele runtime leeft.

Voor .NET-ontwikkelaars is dat vooral waardevol, omdat velen van ons nu systemen bouwen die API-projecten, frontends, workers en AI-aangrenzende services in verschillende talen mengen.

Het feit dat Aspire dit meer uniform laat aanvoelen binnen VS Code is een zeer praktische verbetering.

## TypeScript AppHost-ondersteuning die GA bereikt is ook betekenisvol

Ik zou de TypeScript AppHost-kant van deze release niet negeren.

Aspire wordt natuurlijker voor zowel C# als TypeScript en verbreedt wie in hetzelfde systeemmodel kan werken zonder vreemde tweederangs-workflows. Dat is belangrijk voor teams waar platformcode, frontendcode en service-orchestratie allemaal dicht bij elkaar leven.

## Mijn standpunt

Aspire 13.4 in VS Code draait niet om één killer-feature. Het gaat om het gladstrijken van de ruwe randjes in de dagelijkse lus:

- sneller starten
- meer status zien waar je codeert
- natuurlijker debuggen
- alleen naar logs en het dashboard springen wanneer nodig

Dat is precies hoe goede tooling zou moeten evolueren.

Als je Aspire al gebruikt, lijkt deze update de moeite van het installeren waard. Als je je nog afvraagt of VS Code een serieus thuis is voor op Aspire gebaseerde ontwikkeling, wordt het antwoord steeds duidelijker.

Oorspronkelijke post: [Aspire in VS Code: the 13.4 developer loop](https://devblogs.microsoft.com/aspire/aspire-vscode-extension-13-4/)