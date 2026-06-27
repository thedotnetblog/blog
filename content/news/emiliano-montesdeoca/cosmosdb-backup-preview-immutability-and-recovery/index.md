---
title: "Immutable Backup for Cosmos DB Is the Kind of Feature You Appreciate Too Late"
date: 2026-06-27
author: "Emiliano Montesdeoca"
description: "Azure Backup for Azure Cosmos DB now adds immutable backups and long-term retention in public preview. The key point is not just recovery, but improving resilience and evidence preservation for regulated or high-risk workloads."
tags:
  - Azure Cosmos DB
  - Azure
  - Backup
  - Security
  - Resilience
---

Backup features are easy to ignore right up until the moment they become the most important thing in the room.

That is why I think the new **Azure Backup for Azure Cosmos DB** preview deserves attention.

The interesting part here is not merely “another backup option.” It is the addition of **immutable recovery points** and **long-term retention** in a model that is much better aligned with ransomware readiness, auditability, and regulated recovery requirements.

## Immutability changes the conversation

When attackers target production systems, the next question is no longer just “do we have a backup?”

It is:

- can the backup be trusted?
- can it be altered or deleted?
- do we still have a protected recovery point after the incident starts?

That is why immutable backups matter. They improve the recovery path when the environment around it may no longer be trustworthy.

## My take

This is not the kind of announcement that excites everyone.

But for teams running critical workloads on Cosmos DB, it is exactly the kind of capability that becomes central during the worst day of the quarter.

And those are often the most important features to track.

Original post: [Azure Backup for Azure Cosmos DB Public Preview Adds Immutable Backups and Long-Term Retention](https://devblogs.microsoft.com/cosmosdb/azure-backup-for-azure-cosmos-db-public-preview-adds-immutable-backups-and-long-term-retention/)