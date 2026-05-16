---
title: "LangChain + Azure Cosmos DB：用于代理应用和 RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb 是一个新的 Python 包，将向量搜索、聊天历史记录、代理状态检查点、语义缓存和长期记忆整合到单一的 Azure Cosmos DB for NoSQL 后端中。"
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) 是一个新的 Python 包，将 LangChain 和 LangGraph 连接到 Azure Cosmos DB for NoSQL，用单一数据库替代通常用于向量存储、缓存、历史记录和记忆的 5 个以上独立服务。

## 一个包中的六种集成

该包提供六个集成类（每个都有同步和异步变体）：

1. **AzureCosmosDBNoSqlVectorSearch** — 向量、全文（BM25）、混合（带 RRF 的向量+文本）和加权混合搜索
2. **AzureCosmosDBNoSqlSemanticCache** — 缓存 LLM 响应，以降低重复查询的延迟和成本
3. **CosmosDBChatMessageHistory** — 持久化支持 TTL 的对话历史记录
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph 检查点器：跨调用按 thread_id 持久化图状态
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph 节点级结果缓存
6. **CosmosDBStore / AsyncCosmosDBStore** — 具有命名空间组织和语义搜索的长期记忆

所有集成均支持访问密钥和托管标识（Entra ID）身份验证。

## 向量和混合搜索

Azure Cosmos DB for NoSQL 支持 DiskANN 和 Quantized Flat 向量索引，可从数千扩展到数十亿个向量——这是支持 OpenAI ChatGPT 对话历史和记忆的同一数据库。设置混合搜索：

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

## 带 Cosmos 检查点的 LangGraph 多轮代理

`CosmosDBSaverSync` 检查点器持久化 LangGraph 图状态，使代理在独立调用之间记住上下文——无需内存状态：

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# 第 1 轮
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# 第 2 轮 — 第 1 轮的状态已持久化
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# 返回："Your name is Alice!"
```

## 一个数据库代替五个

将一切整合到 Cosmos DB for NoSQL 意味着一个连接、一套凭据、一个扩展旋钮，以及出现问题时只需查看一个地方。该包在 PyPI 上提供，源代码在 GitHub 的 [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure)。

完整详情请访问 [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/)。
