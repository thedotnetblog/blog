---
title: "Foundry IQ: Build Smarter Agents with Unified Knowledge and Serverless Retrieval"
description: "Foundry IQ combines permission-aware knowledge sources, agentic retrieval, and a serverless Developer tier so .NET teams can focus on agent behavior instead of retrieval plumbing."
date: 2026-09-24
author: "Emiliano Montesdeoca"
tags: [azure-foundry, ai-agents, knowledge-bases, serverless, dotnet]
slug: foundry-iq-unified-knowledge
---

Original source: [Foundry IQ: Build smarter agents faster with unified knowledge and serverless retrieval](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/)

If you've shipped an agent to production, you know the pattern: the agent logic is often the smallest problem. The real complexity lives underneath, in a knowledge layer that has to scale, respect permissions, ingest difficult documents, and return useful context without making every team build its own retrieval stack.

Foundry IQ is aimed at that infrastructure gap. The announcement combines a serverless Developer tier, multi-source knowledge bases, an MCP server, retrieval improvements, and new security and ingestion capabilities. The practical question for a .NET team is not whether every feature is ready for every workload. It is which parts can shorten the path from a prototype to a governed knowledge service.

## Serverless Fits Bursty Agent Workloads

Agent workloads can execute hundreds of retrieval steps in seconds and then sit idle for hours. Reserving capacity for the peak creates waste; sizing for the idle period creates latency. Foundry IQ Serverless is in public preview and scales to zero when idle. It measures resource consumption with Compute Units, including CPU, memory, and storage I/O, with usage calculated each minute in 0.25-CU increments.

The Developer tier lists 1 GB of indexed storage per index, 30 indexes per service, and five services per subscription per region. The announcement lists an estimated compute price of $0.24 per CU per hour and notes that billing is expected to begin in late 2026, with details provided at least 30 days in advance. Treat those values as estimates, not a finalized cost model.

The limits are a useful design prompt. Put a prototype or a bounded internal workload on the serverless tier, measure index growth and retrieval behavior, and know when a dedicated tier becomes necessary. Do not make a capacity decision from the price estimate alone; include ingestion, query volume, security requirements, and the cost of maintaining a custom alternative.

## One Knowledge Base Across Sources

The new sources in preview include Work IQ for organizational signals, Fabric IQ for data agents and ontologies, File Search, Azure SQL, and MCP servers. Instead of writing a separate connector and ranking strategy for every source, a team can expose them through a multi-source knowledge base.

That matters for .NET applications because business context rarely lives in one system. A support agent may need product documentation, a SQL record, a decision from a meeting, and a domain tool. A single knowledge boundary can make the agent workflow simpler, while permission-aware retrieval keeps access rules closer to the data layer.

The Foundry IQ MCP server exposes knowledge bases to MCP-compatible hosts and clients, including the Microsoft Agent Framework and other agent ecosystems named in the announcement. For a C# application, MCP gives you a standard tool boundary rather than a reason to duplicate provider-specific retrieval logic in every agent.

Do not interpret “one endpoint” as “one authorization decision.” Test document-level security, source-specific permissions, identity propagation, and failure behavior. A unified retrieval surface is useful only when its security semantics are clear to the team operating it.

## Retrieval Quality Is an Engineering Metric

The announcement reports up to a 20% improvement in answer-quality benchmarks and up to a 54% recall improvement compared with single-shot RAG. These are product benchmarks, not promises for every corpus. Still, the direction is important: retrieval quality should be measured as part of the agent system, not treated as a configuration detail.

Foundry IQ's updated retrieval loop batches queries more effectively, uses semantic ranking, and applies server-side token caching across multi-turn conversations. That can reduce redundant token consumption while improving the passages supplied to the model.

The data pipeline preview adds layout-aware document ingestion, image enrichment, broader SharePoint indexing, and image verbalization for diagrams, charts, and scanned documents. If your .NET agent reads PDFs or operational documents, inspect the grounded answer against the original visual content. Better ingestion is valuable only when the resulting context remains faithful.

Build a small evaluation set before migrating a production agent. Include questions with known answers, permission boundaries, missing information, and conflicting sources. Compare recall, answer quality, latency, token use, and citation behavior before and after the change.

## Security and Production Boundaries

Foundry IQ knowledge bases and selected knowledge sources are generally available with stable APIs, SLA coverage, compliance certifications, network isolation, managed identity support, and document-level security described in the announcement. Other capabilities, including cross-tenant customer-managed keys, Purview sensitivity-label auditing, incremental SharePoint permissions sync, and some integrations, remain in preview.

That split is important for architecture reviews. Use generally available capabilities as the baseline, and treat preview security features as experiments requiring a specific risk decision. A permission-aware agent still needs application-level authorization for actions it performs after retrieval.

## Recommendations for .NET Teams

1. Start with a small, permission-sensitive evaluation corpus rather than a broad production migration.
2. Use the serverless Developer tier to test bursty retrieval, while treating its limits and pricing as preview estimates.
3. Expose shared knowledge through the MCP server only after testing identity and document-level access.
4. Benchmark retrieval quality with real .NET domain questions and adversarial permission cases.
5. Keep ingestion, security, and agent evaluation in the same release checklist.

Foundry IQ is compelling because it turns knowledge infrastructure into a reusable platform boundary. The best result will come from using that boundary to simplify agent code while keeping data ownership, evaluation, and authorization explicit.