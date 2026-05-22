---
title: "Azure SQL がエンベディングを生成できるようになりました — 純粋な T-SQL で、アプリ層不要"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS と CREATE EXTERNAL MODEL が Azure SQL Database と Managed Instance で GA になりました。T-SQL だけで構築された RAG パイプライン、データ移動不要。"
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

RAG パイプラインを構築したことがあれば、パイプライン税を知っているでしょう: データは SQL に存在しますが、エンベディングを生成するにはデータを抽出し、エンベディング API を呼び出し、バッチ処理とレート制限を処理し、ベクトル検索が可能な場所に結果を保存する必要があります。多くの場合、まったく異なるデータベースに。

Azure SQL は、現在一般提供されている 2 つの機能でその大部分を排除しました: `CREATE EXTERNAL MODEL` と `AI_GENERATE_EMBEDDINGS`。

## 何をするか

これら 2 つの T-SQL 機能は統合パイプラインとして機能します:

**`CREATE EXTERNAL MODEL`** — 外部 AI モデルエンドポイントを名前付きデータベースオブジェクトとして登録します。場所、API フォーマット、モデルタイプ、資格情報を一度設定します。どこでも再利用できます。

**`AI_GENERATE_EMBEDDINGS`** — 登録されたモデルを呼び出し、ベクトル値の JSON 配列を返すスカラー T-SQL 関数です。SELECT、INSERT、UPDATE、MERGE 文で動作します。

合わせて、SQL エンジンを離れることなくエンドツーエンドのエンベディングパイプラインを形成します。

## 完全なワークフロー

```sql
-- ステップ 1: エンベディングプロバイダーを一度登録する
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- ステップ 2: T-SQL でインラインにエンベディングを生成する
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- ステップ 3: ベクトル距離で検索する
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

これがパイプライン全体です: SQL のデータ、SQL で生成されたエンベディング、SQL での類似性検索。オーケストレーション層なし、ETL なし、別個のベクトルデータベースなし。

## サポートされる API フォーマットとオプション

GA では、`API_FORMAT` は **Azure OpenAI** と **OpenAI** をサポートします。`MODEL_TYPE` は現在 `EMBEDDINGS` に固定されています。`PARAMETERS` JSON では、再試行回数を含むモデルレベルのデフォルトを設定できます:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

認証はデータベース資格情報を使用するため、シークレットはアプリケーションコードの外に保持されます。

## .NET アプリケーションで何が可能になるか

既存の SQL データの上に AI 機能を構築する .NET 開発者にとって、これは重要です。以下は不要です:

- エンベディング用に中間ストアにデータを抽出する
- 外部エンベディングパイプラインを管理する
- 別個のベクトルデータベースを設定する (フル機能のベクトルストアが必要な場合は Azure AI Search を使用できますが)
- アプリケーションのデータアクセス層を変更する

既存の SQL アプリケーションに段階的にセマンティック検索を追加できます。すでにお持ちの同じ T-SQL ツールを使用して。

## まとめ

SQL データに対する RAG パターンが劇的にシンプルになりました。`AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` は、既存の SQL アプリケーションが新しいインフラを追加することなくベクトル検索機能を獲得できることを意味します。

両機能は本日、Azure SQL Database と Azure SQL Managed Instance で GA です。

元の投稿: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
