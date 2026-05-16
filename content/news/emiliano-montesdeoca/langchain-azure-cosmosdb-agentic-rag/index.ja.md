---
title: "LangChain + Azure Cosmos DB：エージェントアプリとRAGのために"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdbは、ベクター検索、チャット履歴、エージェント状態のチェックポインティング、セマンティックキャッシュ、長期メモリを単一のAzure Cosmos DB for NoSQLバックエンドに統合した新しいPythonパッケージです。"
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) は、LangChainとLangGraphをAzure Cosmos DB for NoSQLに接続し、ベクターストレージ、キャッシュ、履歴、メモリ用の5つ以上の別々のサービスを単一のデータベースに置き換える新しいPythonパッケージです。

## 1つのパッケージに6つの統合

パッケージには6つの統合クラスが含まれています（それぞれ同期・非同期バリアント付き）：

1. **AzureCosmosDBNoSqlVectorSearch** — ベクター、全文検索（BM25）、ハイブリッド（RRF付きベクター+テキスト）、重み付きハイブリッド検索
2. **AzureCosmosDBNoSqlSemanticCache** — 繰り返しのクエリにおけるレイテンシとコストを削減するためのLLMレスポンスキャッシュ
3. **CosmosDBChatMessageHistory** — TTLサポート付きの会話履歴の永続化
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraphチェックポインター：呼び出し間でthread_idごとにグラフ状態を永続化
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraphノードレベルの結果キャッシュ
6. **CosmosDBStore / AsyncCosmosDBStore** — 名前空間組織とセマンティック検索を備えた長期メモリ

すべての統合でアクセスキーとManaged Identity（Entra ID）認証の両方がサポートされています。

## ベクターとハイブリッド検索

Azure Cosmos DB for NoSQLはDiskANNとQuantized Flatベクターインデックスをサポートし、数千から数十億のベクターにスケールします — OpenAIでChatGPTの会話履歴とメモリを支えているのと同じデータベースです。ハイブリッド検索のセットアップ：

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

## Cosmosチェックポインティングを使ったLangGraphマルチターンエージェント

`CosmosDBSaverSync`チェックポインターはLangGraphのグラフ状態を永続化し、エージェントが別々の呼び出し間でコンテキストを記憶できるようにします — インメモリ状態は不要です：

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# ターン1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# ターン2 — ターン1から状態が永続化されている
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# 返答: "Your name is Alice!"
```

## 5つではなく1つのデータベース

すべてをCosmos DB for NoSQLに統合することで、接続1つ、認証情報1セット、スケーリングノブ1つ、何か問題が起きたときに調べる場所が1つになります。パッケージはPyPIで入手可能で、ソースはGitHubの[langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure)にあります。

詳細は[devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/)で。
