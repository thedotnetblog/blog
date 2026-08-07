---
title: "Changing a Cosmos DB Partition Key Without Rewriting the Application"
description: "Azure Cosmos DB Change Partition Key is now generally available with online copy support, giving .NET teams a managed path to repartition containers and limit application downtime."
date: 2026-10-03
author: "Emiliano Montesdeoca"
tags: [azure-cosmos-db, data-modeling, nosql, dotnet]
slug: cosmosdb-change-partition-keys-ga
---

Original source: [Change Partition Keys in Azure Cosmos DB is Now Generally Available](https://devblogs.microsoft.com/cosmosdb/change-partition-keys-in-azure-cosmos-db-is-now-generally-available/)

A partition key is easy to defend when an application is new. The traffic is still an estimate, the query patterns are still moving, and the data is small enough that almost any reasonable design appears to work. Two years later, the same choice can be the reason for hot partitions, cross-partition queries, or a logical partition approaching its size limit.

Azure Cosmos DB for NoSQL now makes that design decision less permanent. **Change Partition Key** is generally available and uses the container copy infrastructure to move data into a container with a different key. The important part for .NET teams is not simply that a new portal button exists. It is that repartitioning can become an operational migration instead of an application rewrite.

## The partition key is part of the workload

The source calls the partition key "one of the most important design choices" in Cosmos DB. That is not just a modeling concern. It affects how data is distributed across physical partitions, how requests are routed, and whether a query can stay within one logical partition.

The original choice can become a poor fit when:

- traffic concentrates on a small set of logical partitions;
- new access patterns turn formerly targeted queries into cross-partition queries;
- a logical partition grows toward the 20-GB limit; or
- a changed data model needs a different distribution strategy.

Previously, the usual answer was to create another container, write migration code, keep the two models synchronized, and plan a cutover. That is all possible with the SDK, but it creates a lot of application-specific failure modes. A managed copy job gives teams a more deliberate path.

## What the managed change does

The workflow has three stages:

1. Select the source container and create a partition key job from the **Partition Keys** tab under **Scale & Settings** in the Azure portal.
2. Choose online or offline copy mode, create or select the destination container with the desired key, and monitor the number of documents copied.
3. Once the destination catches up, update the application to use the new container. The source container can be deleted afterward if it is no longer needed.

The copy relies on Azure Cosmos DB's [intra-account container copy](https://learn.microsoft.com/azure/cosmos-db/container-copy) infrastructure. The destination is a real container with its own partition key, so this is still a migration that deserves a rollout plan. The difference is that the platform handles the document copy and the online write replication rather than forcing every team to build that machinery.

Online mode is the useful option for a live service. Writes continue to be replicated from the source while the copy is in progress. It is not magic zero downtime, though. When the processed document count is close to the total, the source instructs you to stop writes, select **Complete**, and let the remaining changes flush. That creates a short write pause before the application switches to the destination. Calling it near-zero downtime is fair; calling it no operational coordination would not be.

## What changes in a .NET application?

The Cosmos DB SDK does not need a new programming model for this migration. Your application still creates a client, selects a database, and works with a container. The change is the container your configuration points to and, more importantly, the partition-key assumptions in your code.

Before cutover, inspect code that:

- builds point reads from the old key shape;
- routes messages or jobs using the old partition key;
- constructs transactional batch operations; or
- assumes a particular logical partition contains all related records.

A new partition key can improve query routing while invalidating those assumptions. Treat the destination as a new data contract even when the document schema itself has not changed. A configuration-only switch is safe only after the key is no longer embedded in those workflows.

## A migration plan I would actually use

Start in a non-production environment and compare the old and new containers with the queries that matter most. The source specifically recommends verifying that the new key distributes data evenly and that important queries become point reads or single-partition queries.

Watch RU consumption during the copy. The job uses provisioned throughput, so a migration can compete with normal traffic. Temporarily scaling capacity may be cheaper than letting the copy create a production incident, especially when the source container shares throughput with other workloads.

For online mode, define the write pause as part of the release plan. Stop the writers, complete the job, switch the container reference, run smoke tests, and only then resume writes. Keep the source container until the new path has been observed for a sensible period. It is easier to recover from a missed assumption when the old data is still available.

The same container-copy approach can also support cross-account partition-key changes by selecting another account in the portal's container copy experience. That is useful for a larger boundary change, but it adds identity, networking, and rollback questions that deserve their own test.

## My take

A bad partition key used to feel like a sentence. The new GA capability does not remove the need to model access patterns carefully, and it does not make cutover risk disappear. It does make the correction practical.

If a Cosmos DB workload is showing hot partitions, rising cross-partition query cost, or growth pressure around a logical partition, measure the problem first and then prototype a new key in a copied container. For .NET teams, the best outcome is a smaller application change backed by a better data-distribution decision, not a rushed rewrite disguised as a migration.

Resources:

- [Documentation: Change partition key](https://learn.microsoft.com/azure/cosmos-db/change-partition-key)
- [Documentation: Container copy jobs](https://learn.microsoft.com/azure/cosmos-db/container-copy)
- [Documentation: Hierarchical partition keys](https://learn.microsoft.com/azure/cosmos-db/hierarchical-partition-keys)
- [Best practices: Choosing a partition key](https://learn.microsoft.com/azure/cosmos-db/partitioning-overview#choose-partitionkey)
