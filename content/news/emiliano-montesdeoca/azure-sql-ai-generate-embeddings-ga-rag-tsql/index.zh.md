---
title: "Azure SQL 现在可以生成嵌入向量了 — 纯 T-SQL，无需应用层"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS 和 CREATE EXTERNAL MODEL 现已在 Azure SQL Database 和 Managed Instance 中正式发布。完全用 T-SQL 构建的 RAG 管道，无需数据移动。"
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

如果你曾经构建过 RAG 管道，你就知道管道税：你的数据存在于 SQL 中，但要生成嵌入向量，你需要提取数据、调用嵌入 API、处理批处理和速率限制，并将结果存储到支持向量搜索的地方。通常是在完全不同的数据库中。

Azure SQL 刚刚通过两个现已正式发布的功能消除了大部分这些问题：`CREATE EXTERNAL MODEL` 和 `AI_GENERATE_EMBEDDINGS`。

## 它们的作用

这两个 T-SQL 功能作为集成管道工作：

**`CREATE EXTERNAL MODEL`** — 将外部 AI 模型端点注册为命名数据库对象。你只需设置一次位置、API 格式、模型类型和凭据。随处可重用。

**`AI_GENERATE_EMBEDDINGS`** — 一个标量 T-SQL 函数，调用注册的模型并返回向量值的 JSON 数组。可在 SELECT、INSERT、UPDATE 和 MERGE 语句中使用。

它们共同形成端到端的嵌入管道，无需离开 SQL 引擎。

## 完整工作流程

```sql
-- 步骤 1：一次性注册嵌入提供程序
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- 步骤 2：在 T-SQL 中内联生成嵌入
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- 步骤 3：用向量距离搜索
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

这就是整个管道：SQL 中的数据、SQL 中生成的嵌入、SQL 中的相似性搜索。没有编排层，没有 ETL，没有单独的向量数据库。

## 支持的 API 格式和选项

正式发布时，`API_FORMAT` 支持 **Azure OpenAI** 和 **OpenAI**。`MODEL_TYPE` 目前固定为 `EMBEDDINGS`。`PARAMETERS` JSON 允许设置模型级别的默认值，包括重试次数：

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

身份验证使用数据库凭据，因此密钥保留在应用程序代码之外。

## 这为 .NET 应用程序带来了什么

对于在现有 SQL 数据上构建 AI 功能的 .NET 开发者来说，这意义重大。你不需要：

- 为嵌入将数据提取到中间存储
- 管理外部嵌入管道
- 设置单独的向量数据库（如果你想要全功能的向量存储，可以使用 Azure AI Search）
- 更改应用程序的数据访问层

你可以使用已有的相同 T-SQL 工具，逐步向现有 SQL 应用程序添加语义搜索。

## 总结

SQL 数据上的 RAG 模式变得简单多了。`AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` 意味着你现有的 SQL 应用程序可以在不添加新基础设施的情况下获得向量搜索功能。

这两个功能今天在 Azure SQL Database 和 Azure SQL Managed Instance 中已正式发布。

原始帖子：[Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
