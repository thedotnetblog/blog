---
title: "Cosmos DB Per-Partition Failover: Resilience Without Full-Account Disruption"
description: "Per-Partition Automatic Failover is generally available for Cosmos DB for NoSQL single-write-region accounts, redirecting affected partition writes while preserving configured consistency."
date: 2026-09-30
author: "Emiliano Montesdeoca"
tags: [azure-cosmos-db, database-resilience, high-availability, failover, dotnet]
slug: cosmosdb-per-partition-automatic-failover
---

Original source: [Announcing the General Availability of Per Partition Automatic Failover for Azure Cosmos DB NoSQL](https://devblogs.microsoft.com/cosmosdb/announcing-the-general-availability-of-per-partition-automatic-failover-for-azure-cosmos-db-nosql/)

Failover is often an all-or-nothing decision. If a write region has a partial outage, a traditional account-level approach can move every partition to another region even when most partitions are healthy. Multi-region writes provide another path, but they also require conflict-resolution design.

Per-Partition Automatic Failover, or PPAF, is now generally available for Azure Cosmos DB for NoSQL. It is designed for single-write-region accounts: when a partition set in the preferred write region is affected, Cosmos DB can promote another region for that partition set while unaffected partitions continue writing to the preferred region.

## A Smaller Blast Radius

The source describes failover within three minutes at P99. The decision is made at partition level rather than for the entire account, so a partial regional disruption does not have to become a full-account write event.

When the original region recovers, the system detects the recovery, initiates failback, and reconciles data changes during the process. That recovery behavior is as important as the initial redirect. A resilience feature should be tested across the whole incident lifecycle, not only the first failed request.

PPAF preserves the account's configured consistency level. The GA announcement supports Strong, Session, Consistent Prefix, and Eventual consistency; Bounded Staleness remains on the roadmap. For a Strong-consistency financial or inventory workload, the source states that RPO remains zero through a PPAF failover. Validate the exact consistency and ordering assumptions your application makes during the transition.

## Application Changes Are Minimal

The application continues writing to the Cosmos DB account endpoint. Supported SDKs handle redirection and retry writes to the new region for an affected partition. No application logic is required beyond upgrading to a supported SDK and enabling the feature at the account level.

For .NET, the source lists SDK version 3.60.0 or later. Other supported versions include Java 4.79.0 or later, Python 4.16.0 or later, and Node.js 4.7.0 or later. Upgrade the package deliberately, run the existing integration suite, and observe retry, timeout, and telemetry behavior before changing production traffic.

PPAF is not a replacement for good client behavior. Make write operations idempotent where possible, keep timeouts explicit, and understand how a retried request interacts with your business transaction. The platform can redirect a write; it cannot decide whether a duplicated business command is safe.

## Built-In Observability and Resilience Defaults

PPAF-enabled accounts have Per-Partition Circuit Breaker and Read Hedging enabled by default, with configurable thresholds. A new `PartitionWriteGlobalStatus` metric shows how many partitions are writing in each region at a point in time.

Surface that metric alongside application errors, latency, and region health. If a partition moves regions, the operational team should be able to correlate the platform event with the .NET service's request behavior. A dashboard that shows only account-level availability will hide the granularity that PPAF introduces.

The source also provides a chaos simulation kit for injecting partition-level faults. Use it in a non-production environment to verify failover, failback, consistency expectations, and alerting. Do not treat a green deployment as proof that a partial regional incident has been handled.

## Cost and Eligibility

PPAF is included in the Azure Cosmos DB Business Critical service tier. That makes the availability decision also a pricing decision. Compare the tier cost with the business impact of write downtime and the engineering cost of building a different multi-region strategy.

PPAF applies to single-write-region accounts. Teams already using multi-write regions and conflict resolution do not get a new shortcut from this feature; their existing architecture remains the relevant design. Teams that rejected multi-write primarily because of conflict-resolution complexity now have another resilience option to evaluate.

## Recommendations for .NET Teams

1. Confirm that the workload is single-write-region and that Bounded Staleness is not a requirement.
2. Upgrade the Cosmos DB .NET SDK to 3.60.0 or later in a staging environment.
3. Enable PPAF through the account Features blade and test both failover and failback.
4. Monitor `PartitionWriteGlobalStatus` with application latency and retry metrics.
5. Use the chaos simulation sample before relying on the feature for a mission-critical workload.

PPAF is a thoughtful change in granularity. It lets a single-write-region account approach active-active resilience without asking every application team to own conflict resolution, while keeping the operational proof in the hands of the team that runs the workload.