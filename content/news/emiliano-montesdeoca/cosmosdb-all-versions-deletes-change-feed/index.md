---
title: "Cosmos DB Change Feed: See Every Version and Delete"
description: "All Versions and Deletes change feed mode captures creates, intermediate updates, and deletes, with Azure Functions trigger support for .NET workflows."
date: 2026-10-02
author: "Emiliano Montesdeoca"
tags: [azure-cosmos-db, change-feed, event-sourcing, data-synchronization, dotnet, azure-functions]
slug: cosmosdb-all-versions-deletes-change-feed
---

Original source: [Azure Cosmos DB All Versions and Deletes Change Feed Mode is Now Generally Available](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-all-versions-and-deletes-change-feed-mode-is-now-generally-available/)

The default Cosmos DB change feed shows the latest version of an item after a create or update. It does not show deletes, and if an item changes several times between reads, intermediate versions disappear. That is fine for many synchronization jobs, but it is a blocker for audit trails, event sourcing, and systems that need to react differently to a user delete and a TTL expiration.

All Versions and Deletes change feed mode is now generally available for Azure Cosmos DB for NoSQL. It turns the feed into a more complete event stream and adds support for the Azure Functions trigger in both .NET isolated worker and in-process hosting models.

## What the Mode Contains

Creates and updates include the current document and an operation type. Deletes include the item ID, partition key, and metadata indicating whether the delete was explicit or caused by TTL expiration. Ordering is preserved, including intermediate updates that the latest-version mode would collapse.

That enables several patterns:

- Audit and compliance records that need every state transition.
- Synchronization to a secondary system without soft-delete flags.
- Delete-triggered cleanup, notifications, or cache invalidation.
- Event sourcing where the full sequence is part of the model.

The distinction between explicit delete and TTL expiration can be operationally important. A retention policy event should not automatically be treated as a user request, and the metadata gives downstream code a way to make that decision.

## Azure Functions Makes the Loop Familiar

The Azure Cosmos DB trigger handles lease management, checkpointing, and scaling. In the function, set `ChangeFeedMode = CosmosDBChangeFeedMode.AllVersionsAndDeletes` and process a list of `ChangeFeedItem<T>` values. The wrapper exposes the current document and metadata for each change. On a delete, the current document is null while the metadata still includes the ID, partition key, and TTL information.

A simplified shape looks like this:

```csharp
[CosmosDBTrigger(
    databaseName: "store-db",
    containerName: "orders",
    Connection = "CosmosDBConnection",
    LeaseContainerName = "leases",
    CreateLeaseContainerIfNotExists = true,
    ChangeFeedMode = CosmosDBChangeFeedMode.AllVersionsAndDeletes)]
IReadOnlyList<ChangeFeedItem<Order>> changes
```

Your handler should treat the operation type as data, not infer it from whether the document happens to be present. Log or route creates, replaces, and deletes explicitly, and make the downstream action idempotent because a reliable event stream still needs reliable consumers.

The source says the trigger works in both isolated and in-process .NET hosting models. Other language support is coming, while the .NET path is available at GA. For more control, the change feed processor and pull model also support this mode.

## You Can Run Both Modes

All Versions and Deletes is enabled as an account capability, but the mode is selected per processor, trigger, or pull-model iterator. A container can therefore have one latest-version processor for a simple search-index sync and another all-versions processor for audit logging, using separate lease containers.

That makes migration less disruptive. Do not change every consumer at once if only one workflow needs historical transitions. Start a dedicated processor, compare its output with the existing consumer, and define retention for the additional event history.

## Prerequisites and Tradeoffs

The source says continuous backup must be enabled before enabling All Versions and Deletes. Turn on the capability from the Azure portal Features page or through the REST API, then install the appropriate Cosmos DB Functions extension for the hosting model.

The tradeoff is volume. A container with frequent updates will produce more events when intermediate versions are retained, and the consumer must process and store that data responsibly. Estimate throughput, lease behavior, storage, and downstream retry load before enabling the mode on a high-churn container.

Do not choose this mode solely because “more history” sounds safer. If a consumer only needs the latest state and has no delete-specific workflow, latest-version mode may be simpler and cheaper to operate. The new mode is most valuable when the intermediate state or deletion reason changes the business outcome.

## Recommendations for .NET Teams

1. Enable continuous backup and verify the account prerequisite first.
2. Pilot the mode on a non-critical container with a dedicated lease container.
3. Upgrade the Azure Functions Cosmos DB extension for the selected hosting model.
4. Test create, replace, explicit delete, TTL expiration, ordering, and retry behavior.
5. Keep latest-version and all-versions processors separate until the new output is trusted.

All Versions and Deletes closes a meaningful observability gap in the Cosmos DB change feed. For .NET teams, the important improvement is not only that deletes appear; it is that the platform turns the complete stream into a normal Azure Functions trigger with metadata your code can reason about.