---
title: "LangChain + Azure Cosmos DB dla aplikacji agentycznych i RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb to nowy pakiet Python, który konsoliduje wyszukiwanie wektorowe, historię czatu, checkpointing stanu agenta, semantyczne buforowanie i pamięć długoterminową w jednym backendzie Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) to nowy pakiet Python, który łączy LangChain i LangGraph z Azure Cosmos DB for NoSQL, zastępując zwykłe 5+ oddzielnych usług do przechowywania wektorów, buforowania, historii i pamięci jedną bazą danych.

## Sześć integracji w jednym pakiecie

Pakiet zawiera sześć klas integracji (każda z wariantami synchronicznymi i asynchronicznymi):

1. **AzureCosmosDBNoSqlVectorSearch** — wyszukiwanie wektorowe, pełnotekstowe (BM25), hybrydowe (wektor+tekst z RRF) i ważone hybrydowe
2. **AzureCosmosDBNoSqlSemanticCache** — buforowanie odpowiedzi LLM w celu zmniejszenia opóźnień i kosztów przy powtarzających się zapytaniach
3. **CosmosDBChatMessageHistory** — utrwalanie historii konwersacji z obsługą TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — checkpointer LangGraph: utrwala stan grafu per thread_id między wywołaniami
5. **CosmosDBCacheSync / CosmosDBCache** — buforowanie wyników na poziomie węzłów LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — pamięć długoterminowa z organizacją przestrzeni nazw i wyszukiwaniem semantycznym

Uwierzytelnianie kluczem dostępu i Managed Identity (Entra ID) jest obsługiwane we wszystkich integracjach.

## Wyszukiwanie wektorowe i hybrydowe

Azure Cosmos DB for NoSQL obsługuje indeksy wektorowe DiskANN i Quantized Flat, skalując się od tysięcy do miliardów wektorów — ta sama baza danych, która napędza historię konwersacji i wspomnienia ChatGPT w OpenAI. Konfiguracja wyszukiwania hybrydowego:

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

## Agenci wieloturowi LangGraph z checkpointingiem Cosmos

Checkpointer `CosmosDBSaverSync` utrwala stan grafu LangGraph, dzięki czemu agenci pamiętają kontekst między oddzielnymi wywołaniami — bez wymaganego stanu w pamięci:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Tura 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Tura 2 — stan utrwalony z tury 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Zwraca: "Your name is Alice!"
```

## Jedna baza danych zamiast pięciu

Konsolidacja wszystkiego w Cosmos DB for NoSQL oznacza jedno połączenie, jeden zestaw poświadczeń, jeden przełącznik skalowania i jedno miejsce do sprawdzenia, gdy coś pójdzie nie tak. Pakiet jest dostępny na PyPI, a źródło znajduje się na [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) na GitHub.

Pełne szczegóły na [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
