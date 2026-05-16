---
title: "LangChain + Azure Cosmos DB voor agentische apps en RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb is een nieuw Python-pakket dat vectorzoekopdrachten, chatgeschiedenis, agent-state checkpointing, semantische caching en langetermijngeheugen consolideert in één Azure Cosmos DB for NoSQL-backend."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) is een nieuw Python-pakket dat LangChain en LangGraph verbindt met Azure Cosmos DB for NoSQL, en de gebruikelijke 5+ afzonderlijke services voor vectoropslag, caching, geschiedenis en geheugen vervangt door één database.

## Zes integraties in één pakket

Het pakket bevat zes integratieklassen (elk met synchrone en asynchrone varianten):

1. **AzureCosmosDBNoSqlVectorSearch** — vector-, volledige tekst (BM25)-, hybride (vector+tekst met RRF)- en gewogen hybride zoekopdrachten
2. **AzureCosmosDBNoSqlSemanticCache** — LLM-antwoorden cachen om latentie en kosten bij herhaalde zoekopdrachten te verlagen
3. **CosmosDBChatMessageHistory** — gespreksgeschiedenis bewaren met TTL-ondersteuning
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph-checkpointer: bewaart grafieektoestand per thread_id tussen aanroepen
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph-resultaatcaching op knooppuntniveau
6. **CosmosDBStore / AsyncCosmosDBStore** — langetermijngeheugen met naamruimte-organisatie en semantisch zoeken

Authenticatie met toegangssleutel en Managed Identity (Entra ID) wordt ondersteund voor alle integraties.

## Vector- en hybride zoekopdrachten

Azure Cosmos DB for NoSQL ondersteunt DiskANN- en Quantized Flat-vectorindexen, schaalbaar van duizenden tot miljarden vectoren — dezelfde database die ChatGPT-gespreksgeschiedenissen en -herinneringen bij OpenAI aandrijft. Hybride zoekopdracht instellen:

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

## LangGraph multi-turn agenten met Cosmos checkpointing

De `CosmosDBSaverSync`-checkpointer bewaart de LangGraph-grafiekstoestand zodat agenten context onthouden tussen afzonderlijke aanroepen — geen in-memory staat vereist:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Beurt 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Beurt 2 — toestand bewaard van beurt 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Geeft terug: "Your name is Alice!"
```

## Één database in plaats van vijf

Alles consolideren in Cosmos DB for NoSQL betekent één verbinding, één set referenties, één schaaldraaiknop en één plek om te kijken als er iets misgaat. Het pakket is beschikbaar op PyPI en de broncode staat op [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) op GitHub.

Volledige details op [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
