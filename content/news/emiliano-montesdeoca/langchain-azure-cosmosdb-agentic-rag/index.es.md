---
title: "LangChain + Azure Cosmos DB para aplicaciones agénticas y RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb es un nuevo paquete Python que consolida búsqueda vectorial, historial de chat, checkpointing de estado de agente, caché semántica y memoria a largo plazo en un único backend de Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) es un nuevo paquete Python que conecta LangChain y LangGraph a Azure Cosmos DB for NoSQL, reemplazando los 5+ servicios separados habituales para almacenamiento vectorial, caché, historial y memoria con una sola base de datos.

## Seis integraciones en un paquete

El paquete incluye seis clases de integración (cada una con variantes síncronas y asíncronas):

1. **AzureCosmosDBNoSqlVectorSearch** — búsqueda vectorial, de texto completo (BM25), híbrida (vector+texto con RRF) e híbrida ponderada
2. **AzureCosmosDBNoSqlSemanticCache** — cachear respuestas LLM para reducir latencia y coste en consultas repetidas
3. **CosmosDBChatMessageHistory** — persistir el historial de conversación con soporte TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — checkpointer de LangGraph: persiste el estado del grafo por thread_id entre invocaciones
5. **CosmosDBCacheSync / CosmosDBCache** — caché de resultados a nivel de nodo en LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — memoria a largo plazo con organización por espacio de nombres y búsqueda semántica

La autenticación con clave de acceso e Identidad Administrada (Entra ID) es compatible con todas las integraciones.

## Búsqueda vectorial e híbrida

Azure Cosmos DB for NoSQL admite índices vectoriales DiskANN y Quantized Flat, escalando de miles a miles de millones de vectores — la misma base de datos que impulsa los historiales de conversación y memorias de ChatGPT en OpenAI. Configuración de la búsqueda híbrida:

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

## Agentes multi-turno de LangGraph con checkpointing en Cosmos

El checkpointer `CosmosDBSaverSync` persiste el estado del grafo de LangGraph para que los agentes recuerden el contexto entre invocaciones separadas — sin necesidad de estado en memoria:

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

# Turno 2 — estado persistido del turno 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Devuelve: "Your name is Alice!"
```

## Una base de datos en lugar de cinco

Consolidar todo en Cosmos DB for NoSQL significa una conexión, un conjunto de credenciales, un botón de escala y un lugar donde buscar cuando algo va mal. El paquete está disponible en PyPI y el código fuente está en [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) en GitHub.

Detalles completos en [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
