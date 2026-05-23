---
title: "Com Copilot Studio Va Migrar a .NET 10 WebAssembly i Va Ser un 20% Més Ràpid"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Les millores de .NET 10 WASM no són només per a projectes nous. Aquí teniu el que Copilot Studio va mesurar després d'actualitzar des de .NET 8: empremtes automàtiques, WasmStripILAfterAOT per defecte i números reals de rendiment d'execució."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

L'equip de Copilot Studio va fer alguna cosa sobre la qual tots els desenvolupadors Blazor WASM han tingut curiositat: van actualitzar una aplicació de producció de .NET 8 a .NET 10 i van mesurar els resultats. La publicació comparteix números específics, cosa que és rara i genuïnament útil.

## L'Actualització Va Ser Avorrida (Això és Positiu)

Actualitzar el framework de destinació, actualitzar les referències de paquets, corregir els canvis trencadors. Això és tot. La compilació de .NET 10 ara s'executa en producció. La migració en si no va ser la part interessant — els canvis de .NET 10 sí que ho són.

## Empremta Digital Automàtica d'Actius

Anteriorment, distribuir una aplicació WASM significava escriure scripts personalitzats per reanomenar els actius publicats amb hashes SHA256 per a la invalidació de caché. Copilot Studio tenia un script PowerShell fent exactament això — reanomenar fitxers, injectar atributs `integrity` al carregador JavaScript, gestionar tot manualment.

A .NET 10, tot això és integrat. Els actius publicats s'empremten automàticament, s'importen directament de `dotnet.js` i es validen amb integritat sense intervenció manual. L'equip va eliminar l'script de reanomenament.

Petit canvi en abast, reducció significativa de la complexitat.

## WasmStripILAfterAOT Ara Està Activat per Defecte

A .NET 8, eliminar IL de les assemblies compilades AOT era opt-in. A .NET 10 és el valor per defecte. Després de la compilació AOT, el codi de bytes IL original s'elimina de la sortida — no es necessita en temps d'execució, i mantenir-lo inflava la mida del paquet sense raó.

Copilot Studio utilitza una optimització específica: distribueix tant un motor JIT (inici ràpid) com un motor AOT (rendiment màxim en estat estable), carregant ambdós en paral·lel i passant de JIT a AOT un cop està llest. També deduplicà els fitxers idèntics entre els dos motors.

El nou comportament d'eliminació de IL significa que les assemblies AOT ja no coincideixen bit per bit amb les seves contraparts JIT, de manera que menys fitxers es dedupliquen:
- .NET 8: 59 fitxers compartits
- .NET 10: 22 fitxers compartits

Resultat net: mida del paquet aproximadament un 15% major per al motor AOT. La descàrrega AOT és ~6% més lenta en LAN ràpida, ~17% més lenta en 4G. Però tot passa en segon pla després que l'aplicació ja és interactiva.

## Els Números de Rendiment

Aquesta és la part que importa:

- **~20% més ràpid** en la primera crida (camí fred)
- **~5% més ràpid** en crides posteriors (camí calent)

Les millores són més visibles en "bots grans" — agents grans i complexos on el codi compilat AOT domina. Per a fluxos de treball més simples el guany és menor.

## Si Encara Esteu a .NET 8

La història de migració és genuïnament senzilla: actualitzeu `<TargetFramework>`, actualitzeu les referències de paquets, elimineu qualsevol script d'empremtes personalitzat, i us beneficiareu automàticament de `WasmStripILAfterAOT`. Si esteu compilant AOT, espereu guanys de rendiment similars.

Una nota de la publicació: si carregueu el runtime de .NET WASM dins d'un `WebWorker`, configureu `dotnetSidecar = true` en inicialitzar.

Post original: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
