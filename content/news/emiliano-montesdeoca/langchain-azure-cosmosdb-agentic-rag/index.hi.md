---
title: "LangChain + Azure Cosmos DB एजेंटिक ऐप्स और RAG के लिए"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb एक नया Python पैकेज है जो वेक्टर सर्च, चैट हिस्ट्री, एजेंट स्टेट चेकपॉइंटिंग, सेमांटिक कैशिंग और लॉन्ग-टर्म मेमोरी को एक ही Azure Cosmos DB for NoSQL बैकएंड में एकत्रित करता है।"
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) एक नया Python पैकेज है जो LangChain और LangGraph को Azure Cosmos DB for NoSQL से जोड़ता है, वेक्टर स्टोरेज, कैशिंग, हिस्ट्री और मेमोरी के लिए आमतौर पर उपयोग होने वाली 5+ अलग-अलग सेवाओं को एक ही डेटाबेस से बदलता है।

## एक पैकेज में छह इंटीग्रेशन

पैकेज में छह इंटीग्रेशन क्लासेस हैं (प्रत्येक के सिंक और एसिंक वैरिएंट के साथ):

1. **AzureCosmosDBNoSqlVectorSearch** — वेक्टर, फुल-टेक्स्ट (BM25), हाइब्रिड (वेक्टर+टेक्स्ट RRF के साथ), और वेटेड हाइब्रिड सर्च
2. **AzureCosmosDBNoSqlSemanticCache** — दोहराई जाने वाली क्वेरी पर लेटेंसी और लागत कम करने के लिए LLM प्रतिक्रियाएं कैश करें
3. **CosmosDBChatMessageHistory** — TTL सपोर्ट के साथ कन्वर्सेशन हिस्ट्री बनाए रखें
4. **CosmosDBSaverSync / CosmosDBSaver** — LangGraph चेकपॉइंटर: इनवोकेशन के दौरान thread_id के अनुसार ग्राफ स्टेट बनाए रखता है
5. **CosmosDBCacheSync / CosmosDBCache** — LangGraph नोड-स्तरीय रिज़ल्ट कैशिंग
6. **CosmosDBStore / AsyncCosmosDBStore** — नेमस्पेस ऑर्गनाइज़ेशन और सेमांटिक सर्च के साथ लॉन्ग-टर्म मेमोरी

सभी इंटीग्रेशन में एक्सेस की और मैनेज्ड आइडेंटिटी (Entra ID) ऑथेंटिकेशन दोनों समर्थित हैं।

## वेक्टर और हाइब्रिड सर्च

Azure Cosmos DB for NoSQL DiskANN और Quantized Flat वेक्टर इंडेक्स को सपोर्ट करता है, हजारों से लेकर अरबों वेक्टर तक स्केल करता है — वही डेटाबेस जो OpenAI में ChatGPT की कन्वर्सेशन हिस्ट्री और मेमोरी को पावर करता है। हाइब्रिड सर्च सेटअप:

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

## Cosmos चेकपॉइंटिंग के साथ LangGraph मल्टी-टर्न एजेंट

`CosmosDBSaverSync` चेकपॉइंटर LangGraph ग्राफ स्टेट को बनाए रखता है ताकि एजेंट अलग-अलग इनवोकेशन के दौरान संदर्भ याद रख सकें — इन-मेमोरी स्टेट की आवश्यकता नहीं:

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# टर्न 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# टर्न 2 — टर्न 1 से स्टेट बनाए रखा गया
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# रिटर्न करता है: "Your name is Alice!"
```

## पांच के बजाय एक डेटाबेस

सब कुछ Cosmos DB for NoSQL में कंसॉलिडेट करने का मतलब है एक कनेक्शन, क्रेडेंशियल का एक सेट, एक स्केलिंग नॉब, और एक जगह जब कुछ गलत हो जाए। पैकेज PyPI पर उपलब्ध है और सोर्स GitHub पर [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) पर है।

पूरी जानकारी [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) पर।
