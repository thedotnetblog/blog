---
title: "LangChain + Azure Cosmos DB для агентных приложений и RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb — новый Python-пакет, консолидирующий векторный поиск, историю чата, контрольные точки состояния агента, семантическое кэширование и долгосрочную память в единый бэкенд Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Этот пост был переведён автоматически. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) — новый Python-пакет, соединяющий LangChain и LangGraph с Azure Cosmos DB for NoSQL, заменяющий привычные 5+ отдельных сервисов для векторного хранения, кэширования, истории и памяти единственной базой данных.

## Шесть интеграций в одном пакете

Пакет содержит шесть классов интеграции (каждый в синхронном и асинхронном варианте):

1. **AzureCosmosDBNoSqlVectorSearch** — векторный, полнотекстовый (BM25), гибридный (вектор+текст с RRF) и взвешенный гибридный поиск
2. **AzureCosmosDBNoSqlSemanticCache** — кэширование ответов LLM для снижения задержки и стоимости при повторных запросах
3. **CosmosDBChatMessageHistory** — сохранение истории разговора с поддержкой TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — чекпоинтер LangGraph: сохраняет состояние графа по thread_id между вызовами
5. **CosmosDBCacheSync / CosmosDBCache** — кэширование результатов на уровне узлов LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — долгосрочная память с организацией по пространствам имён и семантическим поиском

Аутентификация с помощью ключа доступа и управляемого удостоверения (Entra ID) поддерживается во всех интеграциях.

## Векторный и гибридный поиск

Azure Cosmos DB for NoSQL поддерживает векторные индексы DiskANN и Quantized Flat, масштабируясь от тысяч до миллиардов векторов — та же база данных, которая обеспечивает историю разговоров и воспоминания ChatGPT в OpenAI. Настройка гибридного поиска:

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

## Мультиходовые агенты LangGraph с контрольными точками Cosmos

Чекпоинтер `CosmosDBSaverSync` сохраняет состояние графа LangGraph, чтобы агенты помнили контекст между отдельными вызовами — без необходимости хранения состояния в памяти:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Ход 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Ход 2 — состояние сохранено с хода 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Возвращает: "Your name is Alice!"
```

## Одна база данных вместо пяти

Консолидация всего в Cosmos DB for NoSQL означает одно подключение, один набор учётных данных, один регулятор масштабирования и одно место для поиска, когда что-то идёт не так. Пакет доступен на PyPI, исходный код — на [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) на GitHub.

Полные подробности на [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
