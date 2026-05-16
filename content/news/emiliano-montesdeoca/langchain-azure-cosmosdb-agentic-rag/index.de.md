---
title: "LangChain + Azure Cosmos DB für agentische Apps und RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb ist ein neues Python-Paket, das Vektorsuche, Chat-Verlauf, Agent-Zustands-Checkpointing, semantisches Caching und Langzeitgedächtnis in einem einzigen Azure Cosmos DB for NoSQL-Backend konsolidiert."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) ist ein neues Python-Paket, das LangChain und LangGraph mit Azure Cosmos DB for NoSQL verbindet und die üblichen 5+ separaten Dienste für Vektorspeicher, Caching, Verlauf und Gedächtnis durch eine einzige Datenbank ersetzt.

## Sechs Integrationen in einem Paket

Das Paket enthält sechs Integrationsklassen (jeweils mit synchronen und asynchronen Varianten):

1. **AzureCosmosDBNoSqlVectorSearch** — Vektor-, Volltext- (BM25), Hybrid- (Vektor+Text mit RRF) und gewichtete Hybridsuche
2. **AzureCosmosDBNoSqlSemanticCache** — LLM-Antworten cachen, um Latenz und Kosten bei wiederholten Abfragen zu senken
3. **CosmosDBChatMessageHistory** — Gesprächsverlauf mit TTL-Unterstützung persistieren
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph-Checkpointer: persistiert den Graphzustand pro thread_id über Aufrufe hinweg
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph-Knoten-Level-Ergebnis-Caching
6. **CosmosDBStore / AsyncCosmosDBStore** — Langzeitgedächtnis mit Namensraum-Organisation und semantischer Suche

Sowohl Zugriffsschlüssel- als auch Managed Identity (Entra ID)-Authentifizierung werden für alle Integrationen unterstützt.

## Vektor- und Hybridsuche

Azure Cosmos DB for NoSQL unterstützt DiskANN- und Quantized Flat-Vektorindizes, die von Tausenden bis zu Milliarden von Vektoren skalieren — dieselbe Datenbank, die ChatGPT-Gesprächsverläufe und -erinnerungen bei OpenAI antreibt. Einrichtung der Hybridsuche:

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

## LangGraph-Multi-Turn-Agenten mit Cosmos-Checkpointing

Der `CosmosDBSaverSync`-Checkpointer persistiert den LangGraph-Graphzustand, sodass Agenten den Kontext über separate Aufrufe hinweg behalten — kein In-Memory-Zustand erforderlich:

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

# Turn 2 — Zustand aus Turn 1 persistiert
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Gibt zurück: "Your name is Alice!"
```

## Eine Datenbank statt fünf

Alles in Cosmos DB for NoSQL zu konsolidieren bedeutet eine Verbindung, einen Satz Anmeldeinformationen, einen Skalierungsregler und einen Ort zum Nachschauen, wenn etwas schiefläuft. Das Paket ist auf PyPI verfügbar und der Quellcode befindet sich bei [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) auf GitHub.

Vollständige Details bei [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
