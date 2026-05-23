---
title: "Hoe Copilot Studio Migreerde naar .NET 10 WebAssembly en 20% Sneller Werd"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "De verbeteringen van .NET 10 WASM zijn niet alleen voor nieuwe projecten. Dit is wat Copilot Studio mat na de upgrade van .NET 8: automatische fingerprinting, WasmStripILAfterAOT standaard ingeschakeld en echte uitvoeringsprestaties."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Het Copilot Studio-team deed iets waar alle Blazor WASM-ontwikkelaars nieuwsgierig naar waren: ze upgradeden daadwerkelijk een productieapplicatie van .NET 8 naar .NET 10 en maten de resultaten. De post deelt specifieke cijfers, wat zeldzaam en oprecht nuttig is.

## De Upgrade Was Saai (Dat is een Goede Zaak)

Target framework bijwerken, pakketreferenties vernieuwen, breaking changes oplossen. Dat is alles. De .NET 10-build draait nu in productie. De migratie zelf was niet het interessante deel — de wijzigingen in .NET 10 zijn dat.

## Automatische Asset Fingerprinting

Vroeger betekende het distribueren van een WASM-app het schrijven van aangepaste scripts om gepubliceerde assets te hernoemen met SHA256-hashes voor cache-busting. Copilot Studio had een PowerShell-script dat precies dit deed — bestanden hernoemen, `integrity`-attributen injecteren in de JavaScript-loader, alles handmatig beheren.

In .NET 10 is dit allemaal ingebouwd. Gepubliceerde assets krijgen automatisch een fingerprint, worden direct geïmporteerd vanuit `dotnet.js` en worden gevalideerd op integriteit zonder handmatige tussenkomst. Het team verwijderde het hernoem-script.

Kleine verandering in scope, aanzienlijke vermindering van complexiteit.

## WasmStripILAfterAOT Is Nu Standaard Ingeschakeld

In .NET 8 was het verwijderen van IL uit AOT-gecompileerde assemblies opt-in. In .NET 10 is het de standaard. Na AOT-compilatie wordt de oorspronkelijke IL-bytecode verwijderd uit de uitvoer — het is niet nodig tijdens runtime, en het bewaren ervan blies de pakketgrootte op zonder reden.

Copilot Studio gebruikt een specifieke optimalisatie: het levert zowel een JIT-engine (snelle opstart) als een AOT-engine (maximale steady-state prestaties), laadt beide parallel en geeft over van JIT naar AOT zodra het klaar is. Het dedupliceert ook bestanden die identiek zijn tussen de twee engines.

Het nieuwe IL-stripping gedrag betekent dat AOT-assemblies niet meer bit-voor-bit overeenkomen met hun JIT-tegenhangers, dus worden er minder bestanden gededupliceerd:
- .NET 8: 59 gedeelde bestanden
- .NET 10: 22 gedeelde bestanden

Nettoresultaat: pakketgrootte ongeveer 15% groter voor de AOT-engine. De AOT-download is ~6% langzamer op snel LAN, ~17% langzamer op 4G. Maar dit alles gebeurt op de achtergrond nadat de app al interactief is.

## De Prestatiecijfers

Dit is het deel dat telt:

- **~20% sneller** bij de eerste aanroep (koud pad)
- **~5% sneller** bij volgende aanroepen (warm pad)

De verbeteringen zijn het meest zichtbaar in "grote bots" — grote, complexe agents waar AOT-gecompileerde code domineert. Voor eenvoudigere workflows is de winst kleiner.

## Als U Nog op .NET 8 Bent

Het migratieverhaal is oprecht eenvoudig: update `<TargetFramework>`, vernieuw pakketreferenties, verwijder aangepaste fingerprinting-scripts, en u profiteert automatisch van `WasmStripILAfterAOT`. Als u AOT compileert, verwacht dan vergelijkbare prestatiewinsten.

Een opmerking uit de post: als u de .NET WASM-runtime laadt binnen een `WebWorker`, stel dan `dotnetSidecar = true` in bij het initialiseren.

Originele post: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
