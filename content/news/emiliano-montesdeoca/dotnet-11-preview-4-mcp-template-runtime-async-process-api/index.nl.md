---
title: ".NET 11 Preview 4: MCP-Serversjabloon, Runtime-Async Bibliotheken, Proces-API"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 is beschikbaar. De hoogtepunten: het MCP-serversjabloon in de SDK, runtimebibliotheken gecompileerd met runtime-async, dotnet watch voor mobiel en een grote uitbreiding van de Proces-API."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 is beschikbaar. Elke release van een belangrijke .NET-preview voegt een lange lijst items toe over de runtime, SDK, bibliotheken, ASP.NET Core, MAUI, C# en Entity Framework. In plaats van de volledige lijst te herhalen, hier de dingen die mij opvielen.

## Het MCP-Serversjabloon Komt in de .NET SDK

Het meest interessante item: een MCP-server projectsjabloon is nu opgenomen in de SDK. Dit betekent dat `dotnet new mcp-server` (of hoe de opdracht uiteindelijk gaat heten) direct werkt. Voor iedereen die MCP-tooling in .NET bouwt, vermindert dit de initiële opstartmoeite aanzienlijk. MCP-integratie in de platform-toolchain geeft de richting aan die het ecosysteem op gaat.

## Runtimebibliotheken Gecompileerd met Runtime-Async

De runtime zelf compileert nu zijn standaardbibliotheken met de runtime-async-functie. Dit is een interne wijziging die de prestaties beïnvloedt — async-toestandsmachines in de runtime worden efficiënter. Het belang hier ligt niet in zichtbare API-wijzigingen; het is dat runtime-async volwassen genoeg is om gebruikt te worden voor de BCL zelf, wat een betekenisvol signaal is over de gereedheid van de functie.

## JIT-optimalisaties en Hardware Intrinsics

Preview 4 zet het JIT-werk voort. Verbeteringen in hardware intrinsics en codegeneratie worden hier geleverd — details zijn te vinden in de runtime-releasenotes. Dit soort wijzigingen verbetert doorgaans de doorvoer bij rekenintensieve lussen zonder codewijzigingen van uw kant.

## Uitbreiding van de Proces-API

Een grote update voor `System.Diagnostics.Process` komt in Preview 4:

- `Process.RunAndCaptureTextAsync` — start een proces, leg stdout/stderr vast, wacht op afsluiting, alles in één aanroep zonder deadlockrisico
- `KillOnParentExit` — lichte levensduurkoppeling tussen ouderprocesen kindprocessen
- `SafeProcessHandle`-gebaseerde API's die meer trimmer-vriendelijk zijn

Als u ooit boilerplate hebt geschreven om procesuitvoer vast te leggen zonder deadlocks te veroorzaken (asynchrone lezing van stdout *en* stderr tegelijkertijd), dan is `RunAndCaptureTextAsync` de API die u miste.

## dotnet watch voor Android en iOS

`dotnet watch` ondersteunt nu apparaatselectie voor .NET MAUI Android- en iOS-projecten. Snellere iteratie op mobiel zonder apparaatverbindingen handmatig te beheren in de buildlus.

## Span-gebaseerde Compressie-API's

Nieuwe span-gebaseerde Deflate-, ZLib- en GZip-encoder/decoder-API's komen in de bibliotheken. Minder allocaties bij het verwerken van gecomprimeerde gegevens — relevant als u gegevensverwerkingen met hoge doorvoer uitvoert.

## Probeer het Uit

[Download .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — het is een preview, niet productiongereed, maar het is de moeite waard om het tegen uw projecten te draaien om problemen vroeg te ontdekken vóór de RC-cyclus.

Originele post: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
