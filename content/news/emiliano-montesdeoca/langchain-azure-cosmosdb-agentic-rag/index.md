---
title: "LangChain + Azure Cosmos DB for Agentic Apps and RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb is a new Python package that consolidates vector search, chat history, agent state checkpointing, semantic caching, and long-term memory into a single Azure Cosmos DB for NoSQL backend."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) is a new Python package that connects LangChain and LangGraph to Azure Cosmos DB for NoSQL, replacing the usual 5+ separate services for vector storage, caching, history, and memory with a single database.

## Six integrations in one package

The package ships six integration classes (each with sync and async variants):

1. **AzureCosmosDBNoSqlVectorSearch** — vector, full-text (BM25), hybrid (vector+text with RRF), and weighted hybrid search
2. **AzureCosmosDBNoSqlSemanticCache** — cache LLM responses to cut latency and cost on repeated queries
3. **CosmosDBChatMessageHistory** — persist conversation history with TTL support
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph checkpointer: persists graph state per thread_id across invocations
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph node-level result caching
6. **CosmosDBStore / AsyncCosmosDBStore** — long-term memory with namespace organization and semantic search

Both access key and Managed Identity (Entra ID) auth are supported across all integrations.

## Vector and hybrid search

Azure Cosmos DB for NoSQL supports DiskANN and Quantized Flat vector indexes, scaling from thousands to billions of vectors — the same database that powers ChatGPT conversation histories and memories at OpenAI. Setting up hybrid search:

```python
vectorstore = AzureCosmosDBNoSqlVectorSearch(
    cosmos_client=...,
    embedding=AzureOpenAIEmbeddings(...),
    ...
)
results = vectorstore.similarity_search(
    "distributed database",
    k=5,
    search_type="hybrid",
    full_text_rank_filter=[{"search_field": "text", "search_text": "distributed"}]
)
```

## LangGraph multi-turn agents with Cosmos checkpointing

The `CosmosDBSaverSync` checkpointer persists LangGraph graph state so agents remember context across separate invocations — no in-memory state required:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Turn 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Turn 2 — state persisted from turn 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Returns: "Your name is Alice!"
```

## One database instead of five

Consolidating everything into Cosmos DB for NoSQL means one connection, one set of credentials, one scaling knob, and one place to look when something goes wrong. The package is available on PyPI and the source is at [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) on GitHub.

Full details at [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
