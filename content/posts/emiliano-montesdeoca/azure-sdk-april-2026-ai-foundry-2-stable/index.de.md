---
title: "Azure SDK April 2026: AI Foundry 2.0 und Was .NET-Entwickler Wissen Sollten"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Das Azure SDK April 2026 Release bringt Azure.AI.Projects 2.0.0 stable mit bedeutenden Breaking Changes, kritische Cosmos DB Sicherheitsfixes und neue Provisioning-Bibliotheken für .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-sdk-april-2026-ai-foundry-2-stable/).*

Das April SDK-Release hat einiges, das Beachtung verdient — besonders wenn du mit AI Foundry, Cosmos DB in Java oder Infrastructure Provisioning aus .NET-Code arbeitest.

## Azure.AI.Projects 2.0.0 — Breaking Changes, die Sinn machen

Das `Azure.AI.Projects` NuGet-Paket erreicht stabile 2.0.0 mit significanten Änderungen: Namespace-Splits für Evaluations und Memory, umbenannte Typen und konsistente `Is*`-Konvention für Booleans.

## Cosmos DB Java: Kritischer Sicherheitsfix (RCE)

Der Java Cosmos DB Library 4.79.0 enthält einen kritischen Fix für eine **Remote Code Execution Schwachstelle (CWE-502)**. Sofort updaten.

## Neue Provisioning-Bibliotheken für .NET

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

## Fazit

Das Highlight für .NET-Entwickler diesen Monat: `Azure.AI.Projects 2.0.0` ist stabil. Originalpost: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).
