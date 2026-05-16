---
title: "LangChain + Azure Cosmos DB للتطبيقات الذكية وRAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb هو حزمة Python جديدة تدمج البحث الشعاعي وسجل المحادثات ونقاط تفتيش حالة الوكيل والتخزين المؤقت الدلالي والذاكرة طويلة الأمد في قاعدة بيانات Azure Cosmos DB for NoSQL واحدة."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) هي حزمة Python جديدة تربط LangChain وLangGraph بـ Azure Cosmos DB for NoSQL، لتحل محل 5 خدمات منفصلة أو أكثر للتخزين الشعاعي والتخزين المؤقت والسجل والذاكرة بقاعدة بيانات واحدة.

## ست تكاملات في حزمة واحدة

تأتي الحزمة بست فئات تكامل (كل منها بنسخة متزامنة وغير متزامنة):

1. **AzureCosmosDBNoSqlVectorSearch** — البحث الشعاعي والنصي الكامل (BM25) والهجين (شعاعي+نصي مع RRF) والهجين الموزون
2. **AzureCosmosDBNoSqlSemanticCache** — تخزين استجابات LLM مؤقتًا لتقليل الكمون والتكلفة على الاستعلامات المتكررة
3. **CosmosDBChatMessageHistory** — استمرار سجل المحادثات مع دعم TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — نقطة تفتيش LangGraph: تحافظ على حالة الرسم البياني لكل thread_id عبر الاستدعاءات
5. **CosmosDBCacheSync / CosmosDBCache** — تخزين مؤقت لنتائج العقد في LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — ذاكرة طويلة الأمد مع تنظيم الفضاء الاسمي والبحث الدلالي

يتم دعم مصادقة مفتاح الوصول والهوية المُدارة (Entra ID) عبر جميع التكاملات.

## البحث الشعاعي والهجين

يدعم Azure Cosmos DB for NoSQL فهارس DiskANN وQuantized Flat الشعاعية، بقدرة تتراوح من الآلاف إلى المليارات من المتجهات — نفس قاعدة البيانات التي تشغّل سجلات محادثات ChatGPT وذاكرته في OpenAI. إعداد البحث الهجين:

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

## وكلاء متعددو الأدوار مع نقاط تفتيش Cosmos في LangGraph

تحافظ نقطة التفتيش `CosmosDBSaverSync` على حالة الرسم البياني في LangGraph حتى يتذكر الوكلاء السياق عبر الاستدعاءات المنفصلة — دون الحاجة إلى حالة في الذاكرة:

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

# Turn 2 — state persisted from turn 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Returns: "Your name is Alice!"
```

## قاعدة بيانات واحدة بدلاً من خمس

يعني دمج كل شيء في Cosmos DB for NoSQL اتصالاً واحداً، ومجموعة واحدة من بيانات الاعتماد، ومقبضاً واحداً للتوسع، ومكاناً واحداً للبحث عند حدوث خطأ. الحزمة متاحة على PyPI والمصدر في [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) على GitHub.

التفاصيل الكاملة في [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
