---
title: "Deep Agents + Cosmos DB Show a Practical Pattern for Working Against Live Operational Data"
date: 2026-11-12
author: "Emiliano Montesdeoca"
description: "The Deep Agents sample with Azure Cosmos DB is interesting because it shows an agent working directly on operational data, planning across multiple steps, verifying writes, and staying grounded in the same store the business already uses."
tags:
  - Azure Cosmos DB
  - AI
  - Agents
  - Azure
  - Architecture
---

I like agent samples that stay close to real operational workflows.

This new **Deep Agents + Azure Cosmos DB** example does exactly that.

Instead of inventing a detached demo world, it puts the agent on top of a support ticket queue stored in Cosmos DB and asks it to do things teams actually care about:

- triage work
- detect patterns
- update records
- verify results

That is a much more useful shape for an agent system.

## The real value is not “AI talks to the database”

We have seen that story already.

What makes this sample better is the operational discipline around it:

- the agent uses specific tools
- writes go through a controlled path
- read-after-write verification is part of the flow
- partitioning and query cost are considered
- the system works on live-style operational data, not a side cache pretending to be reality

That combination is what makes the pattern interesting.

## Why Cosmos DB fits well here

Cosmos DB is a good match for this kind of workload because the data is already dynamic, document-shaped, and operational.

The agent can:

- read tickets directly
- run queue-wide queries when needed
- patch specific items
- keep state and history close to the data itself

For agent scenarios, that is often more useful than forcing everything through a separate analytical layer first.

## My take

The biggest takeaway here is that agent systems become much more compelling when they operate on the same data and same workflows the business already relies on.

That is what this sample gets right.

It treats the agent as an operational participant with clear tool boundaries, not as a disconnected chat interface pretending to help.

That is a pattern worth studying.

Original post: [How to Use Deep Agents with Azure Cosmos DB – Plan, act, and verify against operational data](https://devblogs.microsoft.com/cosmosdb/deep-agents-to-plan-act-verify-against-operational-data/)