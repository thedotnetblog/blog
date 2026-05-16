---
title: "LangChain + Azure Cosmos DB untuk Aplikasi Agentik dan RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb adalah paket Python baru yang mengkonsolidasikan pencarian vektor, riwayat obrolan, checkpointing status agen, caching semantik, dan memori jangka panjang ke dalam satu backend Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) adalah paket Python baru yang menghubungkan LangChain dan LangGraph ke Azure Cosmos DB for NoSQL, menggantikan 5+ layanan terpisah yang biasa digunakan untuk penyimpanan vektor, caching, riwayat, dan memori dengan satu database.

## Enam integrasi dalam satu paket

Paket ini hadir dengan enam kelas integrasi (masing-masing dengan varian sinkron dan asinkron):

1. **AzureCosmosDBNoSqlVectorSearch** — pencarian vektor, teks lengkap (BM25), hibrid (vektor+teks dengan RRF), dan hibrid berbobot
2. **AzureCosmosDBNoSqlSemanticCache** — cache respons LLM untuk mengurangi latensi dan biaya pada kueri berulang
3. **CosmosDBChatMessageHistory** — menyimpan riwayat percakapan dengan dukungan TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — checkpointer LangGraph: menyimpan status graf per thread_id antar pemanggilan
5. **CosmosDBCacheSync / CosmosDBCache** — caching hasil tingkat node LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — memori jangka panjang dengan organisasi namespace dan pencarian semantik

Autentikasi kunci akses dan Managed Identity (Entra ID) didukung di semua integrasi.

## Pencarian vektor dan hibrid

Azure Cosmos DB for NoSQL mendukung indeks vektor DiskANN dan Quantized Flat, diskalakan dari ribuan hingga miliaran vektor — database yang sama yang mendukung riwayat percakapan dan memori ChatGPT di OpenAI. Menyiapkan pencarian hibrid:

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

## Agen multi-giliran LangGraph dengan checkpointing Cosmos

Checkpointer `CosmosDBSaverSync` menyimpan status graf LangGraph agar agen dapat mengingat konteks di berbagai pemanggilan terpisah — tanpa memerlukan status di memori:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Giliran 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Giliran 2 — status tersimpan dari giliran 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Mengembalikan: "Your name is Alice!"
```

## Satu database sebagai pengganti lima

Mengkonsolidasikan segalanya ke Cosmos DB for NoSQL berarti satu koneksi, satu set kredensial, satu tombol penskalaan, dan satu tempat untuk dilihat ketika ada yang salah. Paket tersedia di PyPI dan sumbernya ada di [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) di GitHub.

Detail lengkap di [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
