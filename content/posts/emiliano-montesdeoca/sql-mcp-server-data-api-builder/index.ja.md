---
title: "SQL MCP Server — AIエージェントにデータベースアクセスを与える正しい方法"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Data API builderのSQL MCP Serverは、スキーマを公開したりNL2SQLに頼ることなく、AIエージェントに安全で決定的なデータベースアクセスを提供します。RBAC、キャッシュ、マルチデータベース対応 — すべて組み込み済み。"
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "sql-mcp-server-data-api-builder.md" >}})をご覧ください。*

正直に言いましょう：今日利用可能なほとんどのデータベースMCPサーバーは恐ろしいものです。自然言語のクエリを受け取り、その場でSQLを生成し、本番データに対して実行します。何がうまくいかないでしょうか？（全部です。全部うまくいかない可能性があります。）

Azure SQLチームが[SQL MCP Serverを発表](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)しましたが、根本的に異なるアプローチを取っています。Data API builder（DAB）2.0の機能として構築され、AIエージェントに構造化された決定的なデータベース操作アクセスを提供します — NL2SQLなし、スキーマの公開なし、そしてすべてのステップで完全なRBAC付き。

## なぜNL2SQLを使わないのか？

これが最も興味深い設計判断です。モデルは決定的ではなく、複雑なクエリは微妙なエラーを生み出す可能性が最も高いです。ユーザーがAIに生成してほしいと思う正にそのクエリが、非決定的に生成された場合に最も精査が必要なものでもあります。

代わりに、SQL MCP Serverは**NL2DAB**アプローチを使用します。エージェントはData API builderのエンティティ抽象化レイヤーと組み込みのクエリビルダーで作業し、正確で整形されたT-SQLを決定的に生成します。ユーザーにとっては同じ結果ですが、幻覚されたJOINや偶発的なデータ漏洩のリスクがありません。

## 7つのツール、700ではなく

SQL MCP Serverは、データベースのサイズに関係なく、正確に7つのDMLツールを公開します：

- `describe_entities` — 利用可能なエンティティと操作を発見
- `create_record` — 行を挿入
- `read_records` — テーブルとビューをクエリ
- `update_record` — 行を変更
- `delete_record` — 行を削除
- `execute_entity` — ストアドプロシージャを実行
- `aggregate_records` — 集計クエリ

これは賢明です。コンテキストウィンドウはエージェントの思考空間だからです。何百ものツール定義で氾濫させると、推論のための空間が減ります。7つの固定ツールは、エージェントを*ナビゲーション*ではなく*思考*に集中させ続けます。

各ツールは個別に有効化・無効化できます：

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## 3つのコマンドで開始

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

これでCustomersテーブルを公開するSQL MCP Serverが稼働します。エンティティ抽象化レイヤーにより、名前やカラムにエイリアスを設定し、ロールごとにフィールドを制限し、エージェントが見るものを正確に制御できます — 内部スキーマの詳細を公開することなく。

## セキュリティストーリーは堅実

ここがData API builderの成熟さが活きるところです：

- **あらゆるレイヤーでRBAC** — 各エンティティがどのロールが読み取り、作成、更新、削除できるか、どのフィールドが表示されるかを定義
- **Azure Key Vault統合** — 接続文字列とシークレットを安全に管理
- **Microsoft Entra + カスタムOAuth** — 本番グレードの認証
- **Content Security Policy** — エージェントは生のSQLではなく、制御されたコントラクトを通じてやり取り

スキーマの抽象化は特に重要です。内部テーブル名やカラム名はエージェントに露出しません。AI対話に意味のあるエンティティ、エイリアス、説明を定義します — データベースのERD図ではなく。

## マルチデータベースとマルチプロトコル

SQL MCP ServerはMicrosoft SQL、PostgreSQL、Azure Cosmos DB、MySQLをサポートします。そしてDABの機能であるため、同じ設定からREST、GraphQL、MCPのエンドポイントを同時に取得できます。同じエンティティ定義、同じRBACルール、同じセキュリティ — 3つのプロトコルすべてで。

DAB 2.0の自動設定は、データベースを検査して設定を動的に構築することもできます。迅速なプロトタイピングのために抽象化を減らしても良い場合に便利です。

## 私の見解

これがAIエージェント向けのエンタープライズデータベースアクセスのあるべき姿です。「ねぇLLM、SQLを書いてプロダクションにYOLO」ではなく。代わりに：明確に定義されたエンティティレイヤー、決定的なクエリ生成、各ステップでのRBAC、キャッシュ、モニタリング、テレメトリ。最高の意味で退屈です。

.NET開発者にとって、統合ストーリーはクリーンです — DABは.NETツールで、MCP Serverはコンテナとして動作し、ほとんどの人がすでに使っているAzure SQLで機能します。データアクセスが必要なAIエージェントを構築しているなら、ここから始めましょう。

## まとめ

SQL MCP Serverは無料、オープンソースで、どこでも動作します。AIエージェントに安全なデータベースアクセスを提供するためのMicrosoftの規範的アプローチです。始めるには[完全な記事](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)と[ドキュメント](https://aka.ms/sql/mcp)をご覧ください。
