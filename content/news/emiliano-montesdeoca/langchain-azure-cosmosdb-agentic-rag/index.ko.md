---
title: "LangChain + Azure Cosmos DB: 에이전틱 앱과 RAG를 위한"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb는 벡터 검색, 채팅 기록, 에이전트 상태 체크포인팅, 시맨틱 캐싱, 장기 메모리를 단일 Azure Cosmos DB for NoSQL 백엔드에 통합한 새로운 Python 패키지입니다."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`)는 LangChain과 LangGraph를 Azure Cosmos DB for NoSQL에 연결하고, 벡터 저장, 캐싱, 기록, 메모리를 위한 일반적인 5개 이상의 별도 서비스를 단일 데이터베이스로 대체하는 새로운 Python 패키지입니다.

## 하나의 패키지에 6가지 통합

패키지에는 6개의 통합 클래스가 포함됩니다(각각 동기 및 비동기 변형 포함):

1. **AzureCosmosDBNoSqlVectorSearch** — 벡터, 전체 텍스트(BM25), 하이브리드(RRF를 사용한 벡터+텍스트), 가중치 하이브리드 검색
2. **AzureCosmosDBNoSqlSemanticCache** — 반복 쿼리에서 지연 시간과 비용을 줄이기 위한 LLM 응답 캐시
3. **CosmosDBChatMessageHistory** — TTL 지원을 통한 대화 기록 유지
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph 체크포인터: 호출 간 thread_id별 그래프 상태 유지
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph 노드 수준 결과 캐싱
6. **CosmosDBStore / AsyncCosmosDBStore** — 네임스페이스 조직화 및 시맨틱 검색을 갖춘 장기 메모리

액세스 키 및 관리 ID(Entra ID) 인증이 모든 통합에서 지원됩니다.

## 벡터 및 하이브리드 검색

Azure Cosmos DB for NoSQL은 DiskANN 및 Quantized Flat 벡터 인덱스를 지원하며, 수천에서 수십억 개의 벡터로 확장됩니다 — OpenAI에서 ChatGPT 대화 기록과 메모리를 지원하는 것과 동일한 데이터베이스입니다. 하이브리드 검색 설정:

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

## Cosmos 체크포인팅을 사용한 LangGraph 멀티 턴 에이전트

`CosmosDBSaverSync` 체크포인터는 LangGraph 그래프 상태를 유지하여 에이전트가 별도의 호출 간에 컨텍스트를 기억할 수 있게 합니다 — 인메모리 상태 불필요:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# 턴 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# 턴 2 — 턴 1에서 상태가 유지됨
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# 반환: "Your name is Alice!"
```

## 다섯 개 대신 하나의 데이터베이스

모든 것을 Cosmos DB for NoSQL에 통합하면 하나의 연결, 하나의 자격 증명 세트, 하나의 확장 다이얼, 그리고 문제가 발생했을 때 찾아볼 한 곳이 생깁니다. 패키지는 PyPI에서 이용 가능하며 소스는 GitHub의 [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure)에 있습니다.

전체 세부 정보는 [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/)에서 확인하세요.
