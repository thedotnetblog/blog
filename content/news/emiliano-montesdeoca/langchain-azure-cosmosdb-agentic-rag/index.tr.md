---
title: "LangChain + Azure Cosmos DB: Ajantik Uygulamalar ve RAG için"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb, vektör araması, sohbet geçmişi, ajan durum kontrol noktası, anlamsal önbellekleme ve uzun süreli belleği tek bir Azure Cosmos DB for NoSQL arka ucunda birleştiren yeni bir Python paketidir."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`), LangChain ve LangGraph'ı Azure Cosmos DB for NoSQL'e bağlayan ve vektör depolama, önbellekleme, geçmiş ve bellek için genellikle kullanılan 5+ ayrı hizmeti tek bir veritabanıyla değiştiren yeni bir Python paketidir.

## Tek pakette altı entegrasyon

Paket altı entegrasyon sınıfı içerir (her biri senkron ve asenkron varyantlarla):

1. **AzureCosmosDBNoSqlVectorSearch** — vektör, tam metin (BM25), hibrit (RRF ile vektör+metin) ve ağırlıklı hibrit arama
2. **AzureCosmosDBNoSqlSemanticCache** — tekrarlanan sorgularda gecikme ve maliyeti azaltmak için LLM yanıtlarını önbelleğe alma
3. **CosmosDBChatMessageHistory** — TTL desteğiyle konuşma geçmişini kalıcı hale getirme
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph kontrol noktalayıcısı: çağrılar arasında thread_id başına grafik durumunu kalıcı kılar
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph düğüm düzeyinde sonuç önbellekleme
6. **CosmosDBStore / AsyncCosmosDBStore** — ad alanı organizasyonu ve anlamsal arama ile uzun süreli bellek

Erişim anahtarı ve Yönetilen Kimlik (Entra ID) kimlik doğrulaması tüm entegrasyonlarda desteklenmektedir.

## Vektör ve hibrit arama

Azure Cosmos DB for NoSQL, binlerden milyarlarca vektöre ölçeklenen DiskANN ve Quantized Flat vektör dizinlerini destekler — OpenAI'de ChatGPT konuşma geçmişlerini ve anılarını destekleyen aynı veritabanı. Hibrit arama kurulumu:

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

## Cosmos kontrol noktalaması ile LangGraph çok turlu ajanlar

`CosmosDBSaverSync` kontrol noktalayıcısı, ajanların ayrı çağrılar arasında bağlamı hatırlaması için LangGraph grafik durumunu kalıcı kılar — bellekte durum tutmaya gerek yoktur:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Tur 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Tur 2 — tur 1'den durum kalıcı kılındı
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Döndürür: "Your name is Alice!"
```

## Beş yerine bir veritabanı

Her şeyi Cosmos DB for NoSQL'de birleştirmek, bir bağlantı, bir kimlik bilgisi seti, bir ölçeklendirme düğmesi ve bir şeyler ters gittiğinde bakılacak tek bir yer anlamına gelir. Paket PyPI'da mevcuttur ve kaynak kodu GitHub'da [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure)'dedir.

Tüm ayrıntılar [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/)'da.
