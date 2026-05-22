---
title: "Azure SQL Can Generate Embeddings Now — In Pure T-SQL, No App Layer Needed"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS and CREATE EXTERNAL MODEL are now GA in Azure SQL Database and Managed Instance. RAG pipelines built entirely in T-SQL, no data movement required."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

If you've ever built a RAG pipeline, you know the pipeline tax: your data lives in SQL, but to generate embeddings you need to extract it, call an embedding API, handle batching and rate limits, and store the results somewhere vector-searchable. Often in a different database entirely.

Azure SQL just removed most of that with two features that are now generally available: `CREATE EXTERNAL MODEL` and `AI_GENERATE_EMBEDDINGS`.

## What They Do

These two T-SQL features work as an integrated pipeline:

**`CREATE EXTERNAL MODEL`** — registers an external AI model endpoint as a named database object. You set the location, API format, model type, and credentials once. Reuse it everywhere.

**`AI_GENERATE_EMBEDDINGS`** — a scalar T-SQL function that calls the registered model and returns a JSON array of vector values. Works in SELECT, INSERT, UPDATE, and MERGE statements.

Together they form an end-to-end embedding pipeline without leaving the SQL engine.

## The Complete Workflow

```sql
-- Step 1: Register your embedding provider once
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Step 2: Generate embeddings inline in T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Step 3: Search with vector distance
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

That's the whole pipeline: data in SQL, embeddings generated in SQL, similarity search in SQL. No orchestration layer, no ETL, no separate vector database.

## Supported API Formats and Options

At GA, `API_FORMAT` supports **Azure OpenAI** and **OpenAI**. `MODEL_TYPE` is locked to `EMBEDDINGS` for now. The `PARAMETERS` JSON lets you set model-level defaults including retry count:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Authentication uses database credentials, so secrets stay out of your application code.

## What This Enables for .NET Applications

For .NET developers building AI features on top of existing SQL data, this is significant. You don't need to:

- Extract data to an intermediate store for embedding
- Manage an external embedding pipeline
- Set up a separate vector database (though you can use Azure AI Search if you want a full-featured vector store)
- Change your application's data access layer

You can add semantic search to existing SQL applications incrementally, using the same T-SQL tooling you already have.

## Wrapping Up

RAG patterns on SQL data just got dramatically simpler. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` means your existing SQL application can gain vector search capabilities without adding new infrastructure.

Both features are GA in Azure SQL Database and Azure SQL Managed Instance today.

Original post: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
