---
title: "Azure SDK Abril 2026: AI Foundry 2.0 y Lo Que Deben Saber los Desarrolladores .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "El lanzamiento del Azure SDK de abril 2026 incluye Azure.AI.Projects 2.0.0 stable con cambios importantes, correcciones críticas de seguridad en Cosmos DB y nuevas bibliotecas de Provisioning para .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-sdk-april-2026-ai-foundry-2-stable/).*

Los lanzamientos mensuales del SDK son fáciles de ignorar. Este tiene algunas cosas que vale la pena atender — especialmente si construyes con AI Foundry, Cosmos DB en Java, o haces aprovisionamiento de infraestructura desde código .NET.

## Azure.AI.Projects 2.0.0 — Cambios Breaking que Tienen Sentido

El paquete NuGet `Azure.AI.Projects` alcanza la versión estable 2.0.0 con cambios arquitectónicos significativos:

- **Divisiones de namespace**: Evaluaciones movidas a `Azure.AI.Projects.Evaluation`, operaciones de memoria a `Azure.AI.Projects.Memory`
- **Tipos renombrados**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, etc.
- **Convenciones de nomenclatura**: Propiedades booleanas siguen consistentemente la convención `Is*`

Estos son los cambios breaking que duelen una vez y luego se sienten correctos para siempre.

## Cosmos DB Java: Corrección Crítica de Seguridad (RCE)

Esta es seria. La biblioteca Java Cosmos DB versión 4.79.0 incluye una corrección crítica para una **vulnerabilidad de Ejecución Remota de Código (CWE-502)**.

Si tienes servicios Java usando Azure Cosmos DB, actualiza a 4.79.0 inmediatamente.

## Nuevas Bibliotecas de Provisioning para .NET

Varias bibliotecas estables de Provisioning llegan a 1.0.0:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

## Resumiendo

Lo más destacado para desarrolladores .NET es `Azure.AI.Projects 2.0.0` alcanzando estabilidad. Post original: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).
