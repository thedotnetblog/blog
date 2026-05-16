---
title: "LangChain + Azure Cosmos DB per applicazioni agentiche e RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb è un nuovo pacchetto Python che consolida ricerca vettoriale, cronologia chat, checkpointing dello stato dell'agente, caching semantico e memoria a lungo termine in un unico backend Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) è un nuovo pacchetto Python che connette LangChain e LangGraph ad Azure Cosmos DB for NoSQL, sostituendo i soliti 5+ servizi separati per archiviazione vettoriale, caching, cronologia e memoria con un singolo database.

## Sei integrazioni in un unico pacchetto

Il pacchetto include sei classi di integrazione (ciascuna con varianti sincrone e asincrone):

1. **AzureCosmosDBNoSqlVectorSearch** — ricerca vettoriale, testo completo (BM25), ibrida (vettore+testo con RRF) e ibrida ponderata
2. **AzureCosmosDBNoSqlSemanticCache** — cache delle risposte LLM per ridurre latenza e costi su query ripetute
3. **CosmosDBChatMessageHistory** — persistenza della cronologia delle conversazioni con supporto TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — checkpointer LangGraph: persiste lo stato del grafo per thread_id tra le invocazioni
5. **CosmosDBCacheSync / CosmosDBCache** — caching dei risultati a livello di nodo LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — memoria a lungo termine con organizzazione per namespace e ricerca semantica

L'autenticazione con chiave di accesso e Managed Identity (Entra ID) è supportata per tutte le integrazioni.

## Ricerca vettoriale e ibrida

Azure Cosmos DB for NoSQL supporta indici vettoriali DiskANN e Quantized Flat, scalando da migliaia a miliardi di vettori — lo stesso database che alimenta le cronologie delle conversazioni e i ricordi di ChatGPT in OpenAI. Configurazione della ricerca ibrida:

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

## Agenti multi-turno LangGraph con checkpointing Cosmos

Il checkpointer `CosmosDBSaverSync` persiste lo stato del grafo LangGraph in modo che gli agenti ricordino il contesto tra invocazioni separate — nessuno stato in memoria richiesto:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Turno 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Turno 2 — stato persistito dal turno 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Restituisce: "Your name is Alice!"
```

## Un database invece di cinque

Consolidare tutto in Cosmos DB for NoSQL significa una connessione, un set di credenziali, un cursore di scalabilità e un unico posto dove guardare quando qualcosa va storto. Il pacchetto è disponibile su PyPI e il sorgente è su [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) su GitHub.

Dettagli completi su [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
