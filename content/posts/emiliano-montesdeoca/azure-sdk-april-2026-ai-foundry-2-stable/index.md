---
title: "Azure SDK April 2026: AI Foundry 2.0 and What .NET Developers Should Know"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "The April 2026 Azure SDK release ships Azure.AI.Projects 2.0.0 stable with significant breaking changes, critical Cosmos DB security fixes, and a wave of new Provisioning libraries for .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

Monthly SDK releases are often easy to skip. This one has a few things worth paying attention to — especially if you're building with AI Foundry, Cosmos DB in Java, or doing infrastructure provisioning from .NET code.

## Azure.AI.Projects 2.0.0 — Breaking Changes That Make Sense

The `Azure.AI.Projects` NuGet package reaches stable 2.0.0 with some significant architectural changes. If you're already using the preview, here's what changed:

- **Namespace splits**: Evaluations moved to `Azure.AI.Projects.Evaluation`, memory operations moved to `Azure.AI.Projects.Memory`. Your using statements will need updating.
- **Renamed types**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Naming conventions**: Boolean properties now follow the `Is*` convention consistently

These are the kinds of breaking changes that hurt once and then feel right forever. If you've been building on the preview, update your imports and let the compiler point you to the rest.

The good news: it's stable. You can actually rely on this API now.

## Cosmos DB Java: Critical Security Fix (RCE)

This one is serious. The Java Cosmos DB library (`azure-cosmos`) version 4.79.0 includes a critical security fix for a **Remote Code Execution vulnerability (CWE-502)**.

The issue was Java deserialization in `CosmosClientMetadataCachesSnapshot`, `AsyncCache`, and `DocumentCollection`. The fix replaces Java deserialization with JSON-based serialization, eliminating the entire class of deserialization attacks.

If you have any Java services using Azure Cosmos DB, update to 4.79.0 immediately. This isn't optional.

## New Provisioning Libraries for .NET

A wave of stable Provisioning libraries hit 1.0.0 this month — these are the libraries that let you define Azure infrastructure in C# code rather than ARM templates or Bicep:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

Several more are in beta.1, covering API Management, Batch, Compute, Monitor, MySQL, and Security Center. If you're doing infrastructure-as-code from .NET — particularly with Aspire deployments — these libraries are your entry point.

## Azure AI Agents Java: 2.0.0 GA

The Java Azure AI Agents library also reaches general availability this month. The key breaking changes:

- Several enum types converted to `ExpandableStringEnum`-based classes (more flexible for new values)
- `*Param` model classes renamed to `*Parameter`
- `MCPToolConnectorId` → `McpToolConnectorId` (consistent casing)
- New convenience overload for `beginUpdateMemories`

## Wrapping up

The headline for .NET developers this month is `Azure.AI.Projects 2.0.0` hitting stable — if you're building with AI Foundry, now's the time to pin to stable and update your imports. For Java shops using Cosmos DB, the security update is urgent.

Full release notes at [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases). Original post: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).
