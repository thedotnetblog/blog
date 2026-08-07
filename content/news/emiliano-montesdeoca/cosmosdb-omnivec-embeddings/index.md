---
title: "OmniVec Turns Embedding Synchronization into an Azure Pipeline"
description: "Microsoft's open-source OmniVec platform connects operational data, embedding models, and vector stores with change tracking, backfill, and a manageable Azure deployment."
date: 2026-10-04
author: "Emiliano Montesdeoca"
tags: [azure-cosmos-db, ai, vector-search, rag, dotnet]
slug: cosmosdb-omnivec-embeddings
---

Original source: [Introducing OmniVec: An Open-Source Embedding Platform for AI Apps on Azure](https://devblogs.microsoft.com/cosmosdb/introducing-omnivec-an-open-source-embedding-platform-for-ai-apps-on-azure/)

Most RAG projects begin with a deceptively small requirement: keep the vector representation of changing business data up to date. The first prototype can generate embeddings in a loop. The production version needs initial backfill, change capture, batching, retries, model credentials, destination writes, and a way to see whether the pipeline is falling behind.

That infrastructure is often unrelated to the application feature the team actually wants to ship. OmniVec is Microsoft's open-source attempt to make it a reusable platform instead. It lets a team register data sources, embedding models, and vector stores, then connect them with a pipeline. The source describes the design as "four configurable components: a source, a model, a destination, and a pipeline." That separation is the important idea.

## The four pieces of an embedding system

An OmniVec **source** is the system from which records are read and changes are tracked. The supported paths include Azure Cosmos DB, PostgreSQL, and SQL Server. A **model** describes the embedding provider, model name, endpoint, and credentials. A **destination** is where the generated vector is written, alongside or as an update to the original record. Cosmos DB, PostgreSQL, SQL Server, and Azure Blob Storage are supported destinations in the announcement.

The **pipeline** binds those pieces together. It declares which source fields should be embedded and which destination field receives the vector. That makes the embedding decision visible and replaceable instead of burying it inside a worker implementation.

The change-tracking mechanism depends on the source. OmniVec can use the Cosmos DB change feed, Blob Storage events, or change data capture for SQL Server and PostgreSQL. Workers pull records from the queue, call the registered model, and write the result to the destination. The worker pool is horizontally scalable, while the model routing layer gives a pipeline a consistent way to call Azure OpenAI or a self-hosted GPU model.

For a .NET application, this creates a useful boundary. The application can continue writing normal business records through its existing SDK and service layer. The embedding concern can consume those records without turning every write path into an AI orchestration problem.

## What the Azure deployment includes

OmniVec is not a single library added to an ASP.NET Core project. You deploy it into your own Azure subscription. The `azd up` flow provisions an AKS cluster for the API, controller, and workers, an Azure Cosmos DB account for pipeline metadata and job state, and an Azure Container Registry for the service images.

That ownership model is both a strength and a responsibility. You control the AKS node size and count, whether to provision a GPU pool, and whether the embedding model is hosted by Azure OpenAI or served by your own GPU workload. You also control the subscription, networking, and data path. The tradeoff is that this remains an AKS-based platform with real capacity and operations to plan for.

The source quickstart uses Azure Cosmos DB as both the source and destination. It creates a container with a vector embedding policy and a DiskANN index, seeds 100 product documents, registers an Azure OpenAI embedding model, and then creates a source, destination, and pipeline. After the pipeline is resumed, new inserts and updates flow through the change feed and receive embeddings automatically. The same shape can be adapted to other supported source and destination combinations.

## The permission detail that matters

OmniVec pods authenticate to Azure Cosmos DB with a managed identity rather than a connection string. The quickstart assigns two different roles:

- **Cosmos DB Built-in Data Contributor** for reading source documents and writing embeddings.
- **Cosmos DB Account Reader Role** for account-level metadata and vector policies inspected by the change-feed processor.

The second role is easy to overlook because the operation looks like ordinary data access. The source calls out that omitting it can result in a `readMetadata` error. For a team deploying from an Azure DevOps or GitHub pipeline, these role assignments belong in the environment setup and should be tested before the first pipeline is created.

The same principle applies to the embedding model. Register the model with its provider, endpoint, model name, and credentials, then reference it by the model identifier when creating the pipeline. Keep those credentials in the deployment's identity and secret-management path; they should not become application configuration copied into every worker.

## A practical first run

I would start with the Cosmos DB quickstart even if the eventual source is SQL Server or PostgreSQL. It exercises the complete path with a familiar change feed and makes the operational questions visible:

1. Deploy OmniVec with `azd up` and save the generated service URL and admin token.
2. Register the hosted embedding model through the CLI or web UI.
3. Create the Cosmos DB source and vector destination.
4. Create a pipeline that maps fields such as `name` and `description` to an `embedding` field.
5. Resume the pipeline, observe its progress, and run a vector search.
6. Update a source record and verify that the change is re-embedded.

That last step is more valuable than a successful initial search. A vector index that works after backfill proves that embedding generation works; an update flowing through the change path proves that the system can stay useful.

## What I would measure before production

Measure change-feed lag, worker throughput, model latency, failed records, and the RU or database cost of the destination writes. Compare hosted and self-hosted model options with the actual document sizes and update frequency from your workload. Also decide whether the vector should live beside the original record or in a separate store, because that choice affects indexing, retention, and query shape.

OmniVec is a public preview, so pin the deployment configuration and treat the CLI and REST surface as something to test during upgrades. It is a promising way to stop rebuilding the same embedding plumbing, but the AKS footprint means it is not a free abstraction. Start with one bounded dataset, verify the end-to-end change path, and then decide whether the operational control is worth the platform cost for your application.

Resources:

- [OmniVec on GitHub](https://github.com/AzureCosmosDB/OmniVec)
- [OmniVec quickstart repository](https://github.com/AzureCosmosDB/omnivec-cosmosdb-quickstart)
- [Azure Cosmos DB vector search](https://learn.microsoft.com/azure/cosmos-db/vector-search)
