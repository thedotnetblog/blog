---
title: ".NET 11 Preview 5: wat ik daadwerkelijk als eerste zou proberen"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 levert verbeteringen over de SDK, runtime, C#, ASP.NET Core en EF Core heen. Hier zijn de updates die ik denk dat het meest de moeite waard zijn om vroeg te testen als je echte .NET-apps bouwt."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

.NET-previewposts zitten altijd bomvol.

Dat is goed nieuws voor het platform, maar het betekent ook dat de praktische vraag begraven raakt: **wat zou je eigenlijk als eerste moeten testen?**

.NET 11 Preview 5 brengt veel over de SDK, runtime, bibliotheken, ASP.NET Core, C#, MAUI en EF Core. In plaats van hier een gigantische changelog-samenvatting van te maken, wil ik me richten op de onderdelen waarvan ik denk dat ze nu echt ontwikkelaarsaandacht verdienen.

## Het MCP-servertemplate in `dotnet new` is een signaal

Dit is waarschijnlijk het meest strategische item in het SDK-gedeelte.

Wanneer een projecttemplate direct in de SDK landt, betekent dat dat het platform het scenario niet langer als niche behandelt. Een **MCP Server-template** ingebouwd in `dotnet new` verlaagt de drempel om het patroon te proberen en stuurt een duidelijk signaal over waar het ecosysteem naartoe gaat.

Als je agenttooling, interne assistenten of AI-geïntegreerde ontwikkelaarshulpmiddelen in .NET bouwt, is dit een van de eerste dingen die ik zou testen.

## Build-time kwetsbaarheids- en end-of-life-controles zijn precies het soort defaults dat ik waardeer

Beveiliging en levenscyclusbewustzijn zijn veel beter wanneer het platform je helpt *tijdens de build*, niet achteraf in een apart rapport dat niemand leest.

De nieuwe SDK-controles op kwetsbaarheden en end-of-life-pakketten tijdens de build zijn het soort feature waar ik van houd omdat ze beter gedrag de standaard maken.

Dit is niet opvallend, maar het is het soort verbetering dat heel goed veroudert.

## C# blijft expressiever worden op de juiste plekken

De C#-items in Preview 5 zijn interessant, vooral:

- gesloten klassenhiërarchieën
- union-declaraties en union-patronen
- voortgezet werk aan unsafe-evolutie

Ik zou dit nog niet blindelings allemaal in productiecode overnemen, want previewtaalfeatures verdienen altijd een nuchtere testcyclus. Maar de richting is goed. C# blijft evolueren naar rijkere modellering zonder zijn identiteit te verliezen.

## ASP.NET Core en EF Core hebben praktische updates die het waard zijn om vroeg te testen

Twee gebieden waar ik zeker een spike op zou zetten:

### Blazor-verbeteringen

Client-side validatie voor Blazor SSR en QuickGrid-verbeteringen zonder interactiviteit zijn beide het soort quality-of-life-features die echte apps kunnen vereenvoudigen.

### EF Core-defaults en waarschuwingen

EF Core dat SQL Server 2022-compatibiliteit als standaard instelt en waarschuwingen toevoegt voor async EF-queries die synchroon draaien, zijn precies het soort veranderingen dat verborgen problemen in echte codebases aan het licht kan brengen.

Dat betekent dat het de moeite waard is om eerder dan later te testen.

## Mijn korte lijst voor een eerste doorloop

Als ik een halve dag had om Preview 5 te verkennen, zou ik dit doen:

1. het MCP-servertemplate proberen
2. builds draaien en de nieuwe kwetsbaarheids-/EOL-controles inspecteren
3. elke codebase testen die baat kan hebben bij de nieuwe C#-modelleringsfeatures
4. Blazor SSR-scenario's valideren als je op die stack zit
5. EF Core-zware paden draaien en letten op waarschuwingsveranderingen of SQL-verschillen

Daar denk ik dat de vroege waarde zit.

## Mijn standpunt

.NET 11 Preview 5 voelt als een van die releases waarbij het platform tegelijk in twee richtingen blijft duwen:

- ambitieuzere ontwikkelaarsmogelijkheden
- betere defaults voor productiegerichte teams

Die combinatie is wat ik wil van een previewcyclus.

Probeer het, maar probeer het met een doel.

Oorspronkelijke post: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)