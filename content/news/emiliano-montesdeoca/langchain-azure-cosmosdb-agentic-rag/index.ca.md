---
title: "LangChain + Azure Cosmos DB per a aplicacions agèntiques i RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb és un nou paquet Python que consolida la cerca vectorial, l'historial de xat, els punts de control d'estat de l'agent, la memòria cau semàntica i la memòria a llarg termini en un únic backend d'Azure Cosmos DB per a NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) és un nou paquet Python que connecta LangChain i LangGraph a Azure Cosmos DB per a NoSQL, substituint els 5+ serveis separats habituals per a emmagatzematge vectorial, memòria cau, historial i memòria amb una única base de dades.

## Sis integracions en un sol paquet

El paquet inclou sis classes d'integració (cadascuna amb variants síncrones i asíncrones):

1. **AzureCosmosDBNoSqlVectorSearch** — cerca vectorial, de text complet (BM25), híbrida (vector+text amb RRF) i híbrida ponderada
2. **AzureCosmosDBNoSqlSemanticCache** — emmagatzematge en memòria cau de les respostes LLM per reduir la latència i el cost en consultes repetides
3. **CosmosDBChatMessageHistory** — persistència de l'historial de conversa amb suport TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — punt de control de LangGraph: persisteix l'estat del graf per thread_id entre invocacions
5. **CosmosDBCacheSync / CosmosDBCache** — memòria cau de resultats a nivell de node de LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — memòria a llarg termini amb organització per espai de noms i cerca semàntica

L'autenticació amb clau d'accés i Identitat Gestionada (Entra ID) és compatible amb totes les integracions.

## Cerca vectorial i híbrida

Azure Cosmos DB per a NoSQL admet índexs vectorials DiskANN i Quantized Flat, escalant de milers a milers de milions de vectors — la mateixa base de dades que impulsa els historials de conversa i les memòries de ChatGPT a OpenAI. Configuració de la cerca híbrida:

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

## Agents multi-torn de LangGraph amb punts de control a Cosmos

El punt de control `CosmosDBSaverSync` persisteix l'estat del graf de LangGraph perquè els agents recordin el context entre invocacions separades — sense estat en memòria requerit:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Torn 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Torn 2 — estat persistit des del torn 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Retorna: "Your name is Alice!"
```

## Una base de dades en lloc de cinc

Consolidar-ho tot a Cosmos DB per a NoSQL significa una connexió, un conjunt de credencials, un botó d'escala i un lloc on buscar quan alguna cosa va malament. El paquet està disponible a PyPI i el codi font és a [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) a GitHub.

Detalls complets a [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
