---
title: "Azure SDK d'abril de 2026: AI Foundry 2.0 i el que els desenvolupadors de .NET han de saber"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "La versió d'abril de 2026 de l'Azure SDK publica Azure.AI.Projects 2.0.0 estable amb canvis trencadors importants, correccions de seguretat crítiques per a Cosmos DB i una onada de noves biblioteques de Provisioning per a .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Les versions mensuals de l'SDK sovint són fàcils d'ignorar. Aquesta en té algunes coses que val la pena tenir en compte — sobretot si estàs construint amb AI Foundry, amb Cosmos DB en Java o si fas aprovisionament d'infraestructura des de codi .NET.

## Azure.AI.Projects 2.0.0 — Canvis trencadors que tenen sentit

El paquet NuGet `Azure.AI.Projects` arriba a la versió estable 2.0.0 amb alguns canvis arquitectònics importants. Si ja estàs fent servir la preview, això és el que ha canviat:

- **Separació de namespaces**: Evaluations s'ha mogut a `Azure.AI.Projects.Evaluation`, i memory operations a `Azure.AI.Projects.Memory`. Hauràs d'actualitzar els `using`.
- **Tipus reanomenats**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Convencions de nomenclatura**: les propietats booleanes ara segueixen de manera consistent la convenció `Is*`

Són el tipus de canvis trencadors que fan mal una vegada i després semblen els correctes per sempre. Si has construït sobre la preview, actualitza les importacions i deixa que el compilador t'assenyali la resta.

La bona notícia: ara és estable. Ja pots confiar de debò en aquesta API.

## Cosmos DB Java: correcció de seguretat crítica (RCE)

Això és seriós. La biblioteca Java de Cosmos DB (`azure-cosmos`) versió 4.79.0 inclou una correcció de seguretat crítica per a una **vulnerabilitat d'execució remota de codi (CWE-502)**.

El problema era la deserialització Java a `CosmosClientMetadataCachesSnapshot`, `AsyncCache` i `DocumentCollection`. La correcció substitueix la deserialització Java per serialització basada en JSON, eliminant tota la classe d'atacs de deserialització.

Si tens algun servei Java que faci servir Azure Cosmos DB, actualitza immediatament a 4.79.0. Això no és opcional.

## Noves biblioteques de Provisioning per a .NET

Aquest mes han arribat diverses biblioteques de Provisioning estables a 1.0.0 — són les biblioteques que et permeten definir infraestructura d'Azure en codi C# en lloc de plantilles ARM o Bicep:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

N'hi ha diverses més en beta.1, que cobreixen API Management, Batch, Compute, Monitor, MySQL i Security Center. Si fas infraestructura com a codi des de .NET — especialment amb desplegaments Aspire — aquestes biblioteques són el teu punt d'entrada.

## Azure AI Agents Java: 2.0.0 GA

La biblioteca Java d'Azure AI Agents també arriba aquest mes a disponibilitat general. Els principals canvis trencadors són:

- Diversos tipus `enum` convertits en classes basades en `ExpandableStringEnum` (més flexibles per a valors nous)
- Les classes de model `*Param` reanomenades a `*Parameter`
- `MCPToolConnectorId` → `McpToolConnectorId` (coherència en la capitalització)
- Nou overload de conveniència per a `beginUpdateMemories`

## Tancant

La notícia principal per als desenvolupadors de .NET aquest mes és que `Azure.AI.Projects 2.0.0` passa a estable — si construeixes amb AI Foundry, ara és el moment de fixar-te en la versió estable i actualitzar les importacions. Per als equips Java que fan servir Cosmos DB, l'actualització de seguretat és urgent.

Tens les notes de llançament completes a [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases). Publicació original: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).