---
title: "LangChain + Azure Cosmos DB para aplicações agênticas e RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb é um novo pacote Python que consolida pesquisa vetorial, histórico de chat, checkpointing de estado do agente, cache semântico e memória de longo prazo em um único backend Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) é um novo pacote Python que conecta LangChain e LangGraph ao Azure Cosmos DB for NoSQL, substituindo os 5+ serviços separados habituais para armazenamento vetorial, cache, histórico e memória por um único banco de dados.

## Seis integrações em um pacote

O pacote inclui seis classes de integração (cada uma com variantes síncronas e assíncronas):

1. **AzureCosmosDBNoSqlVectorSearch** — pesquisa vetorial, texto completo (BM25), híbrida (vetor+texto com RRF) e híbrida ponderada
2. **AzureCosmosDBNoSqlSemanticCache** — cache de respostas LLM para reduzir latência e custo em consultas repetidas
3. **CosmosDBChatMessageHistory** — persistência do histórico de conversas com suporte TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — checkpointer LangGraph: persiste o estado do grafo por thread_id entre invocações
5. **CosmosDBCacheSync / CosmosDBCache** — cache de resultados em nível de nó LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — memória de longo prazo com organização por namespace e pesquisa semântica

Autenticação com chave de acesso e Identidade Gerenciada (Entra ID) é suportada em todas as integrações.

## Pesquisa vetorial e híbrida

O Azure Cosmos DB for NoSQL suporta índices vetoriais DiskANN e Quantized Flat, escalando de milhares a bilhões de vetores — o mesmo banco de dados que alimenta os históricos de conversação e memórias do ChatGPT na OpenAI. Configurando pesquisa híbrida:

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

## Agentes multi-turno LangGraph com checkpointing no Cosmos

O checkpointer `CosmosDBSaverSync` persiste o estado do grafo LangGraph para que os agentes lembrem o contexto entre invocações separadas — sem estado em memória necessário:

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

# Turno 2 — estado persistido do turno 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Retorna: "Your name is Alice!"
```

## Um banco de dados em vez de cinco

Consolidar tudo no Cosmos DB for NoSQL significa uma conexão, um conjunto de credenciais, um botão de escala e um lugar para verificar quando algo der errado. O pacote está disponível no PyPI e o código-fonte está em [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) no GitHub.

Detalhes completos em [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
