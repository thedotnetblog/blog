---
title: "Building Agentic Apps with Microsoft Fabric and Databases"
description: "Rayfin, Azure HorizonDB, Cosmos DB, and Fabric IQ point toward a shared data foundation for production agent systems. What .NET teams should evaluate first."
date: 2026-09-25
author: "Emiliano Montesdeoca"
tags: [microsoft-fabric, databases, rayfin, azure-horizondb, dotnet]
slug: build-agentic-apps-fabric-databases
---

Original source: [Microsoft Build 2026: Building agentic apps with Microsoft Fabric and Microsoft Databases](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/)

There is a hidden tax in modern agent development: the gap between what a model can generate and what a production system requires. Application logic still needs data, identity, permissions, state, governance, and operations. Microsoft Build 2026 frames Microsoft Fabric and Microsoft Databases as a way to provide shared context instead of rebuilding those foundations for every agent.

The announcement covers two especially notable pieces: Rayfin, an open-source SDK and CLI for describing an application backend, and Azure HorizonDB, a PostgreSQL-compatible database designed for AI-powered applications. Around them, Fabric IQ, OneLake, Azure Cosmos DB, and existing Azure Database for PostgreSQL capabilities form a broader data platform story.

## Rayfin: Describe the Backend in Code

Rayfin lets developers and coding agents define data models, backend logic, access policies, authentication, and other application requirements in code. It then deploys the backend directly to Microsoft Fabric. Application data lands in OneLake and is available to the broader Fabric data, analytics, operational, and AI stack.

For a .NET team, the appeal is a more programmable interface for backend setup. A coding agent can work through a GitHub-based workflow and produce more than a UI or a collection of API methods; it can describe the supporting data and permission model as part of the application.

The architectural tradeoff is equally clear: Rayfin is Fabric-first. That can be a strong fit for a greenfield application that wants Fabric's unified data foundation, but it is not a neutral abstraction over every Azure subscription, hybrid environment, or multi-cloud estate. Review data residency, tenant ownership, deployment controls, and operational responsibility before treating it as a general-purpose backend generator.

Rayfin is also new. Start with a non-critical application, inspect the generated infrastructure and access rules, and keep the source definitions reviewable. “Describe it in code” is valuable only when the team can understand and test what the description produces.

## Azure HorizonDB: PostgreSQL Compatibility with an AI Focus

Azure HorizonDB is announced as a fully managed, PostgreSQL-compatible database in public preview. The source highlights zone resilience by default, elastic storage up to 128 TB, scale-out compute up to 3,072 vCores, and sub-millisecond multi-zone commit latency for demanding transactional scenarios.

It also includes capabilities designed for AI applications, including vector search, integrated AI model management, and direct connectivity to Microsoft Foundry and Fabric. The attractive use case is a system that needs both operational transactions and semantic context without immediately assembling separate stores and synchronization paths.

PostgreSQL compatibility gives .NET teams a familiar starting point, especially where Npgsql and existing SQL skills are already in use. Compatibility is not the same as “no validation required,” especially for a public preview. Test EF Core migrations, extensions, transaction behavior, connection pooling, vector queries, and failure handling with the exact workload you plan to run.

Preview status also changes the decision boundary. Confirm availability, feature coverage, pricing, SLA expectations, and support commitments before placing a critical workload on it. A good pilot can still produce useful evidence without making the preview a production dependency.

## Existing PostgreSQL Workloads Still Have a Path

The announcement does not position HorizonDB as the only database direction. Azure Database for PostgreSQL remains the foundation for existing PostgreSQL workloads. New tooling can assess Oracle and PostgreSQL environments, provide readiness and sizing insights, and help estimate migration costs. Microsoft Defender for Cloud integration is also announced in preview for continuous security and compliance assessments.

That is relevant for .NET modernization projects. A team can first understand its current workload, extensions, connection behavior, and operational requirements before deciding whether a move to another managed PostgreSQL offering is justified. The assessment step is cheaper than discovering compatibility gaps during a cutover.

## Fabric IQ Supplies Shared Business Meaning

The deeper theme is shared context. OneLake unifies data, semantic models provide governed business definitions, and ontologies add entities, relationships, properties, rules, and actions. Fabric IQ is described as a layer where agents can use that context consistently instead of relearning what “customer,” “order,” or “revenue” means in every application.

For .NET teams, this is less about a new client library and more about architecture. If an agent can query the same governed definitions used by analytics and operations, the application has a better chance of making decisions on trusted context. The governance still belongs to the data platform: define ownership, update processes, access policies, and the evidence an agent must provide before acting.

The announcement also describes Fabric IQ connections to Foundry, Agent 365, Microsoft 365 Copilot, and GitHub Copilot CLI. Those integrations make the shared context more portable, but they also increase the importance of identity and audit boundaries.

## Cosmos DB and the Local Development Story

Azure Cosmos DB updates in the announcement include general availability of the Linux Emulator for local development across Linux, macOS, and Windows, along with preview semantic reranking and an agent memory toolkit using Cosmos DB, Durable Functions, and Foundry models.

For .NET developers, a local emulator reduces the cost of testing data access and agent workflows without a cloud dependency. Use it for functional development, while keeping a separate integration stage for managed-service behavior, identity, throughput, and regional features.

## Recommendations for .NET Teams

1. Treat Rayfin as a Fabric-first pilot and review generated backend behavior like any other infrastructure change.
2. Evaluate HorizonDB with real Npgsql and EF Core workloads, not only PostgreSQL compatibility claims.
3. Use migration assessment tooling before changing an established PostgreSQL estate.
4. Record business definitions and ownership before asking agents to act on Fabric IQ context.
5. Use the Cosmos DB emulator for local feedback and a managed Azure environment for integration validation.

The Build announcements are ultimately about shared foundations. Agents become easier to scale when data, business meaning, permissions, and operations are treated as reusable platform capabilities rather than rediscovered inside every prompt.