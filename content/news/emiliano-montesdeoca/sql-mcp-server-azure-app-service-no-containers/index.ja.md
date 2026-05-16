---
title: "SQL MCP ServerをAzure App Serviceで動かす — コンテナ不要"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP ServerがDockerやKubernetesなしでAzure App Serviceで動作するようになりました。SQLデータベースと連携するAIエージェントを構築する.NET開発者にとって何を意味するのかを解説します。"
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})からご覧いただけます。*

正直に言うと、チュートリアルで「コンテナが必要」という言葉を見るたびに少しため息が出ます。コンテナは素晴らしいのですが、チームにコンテナ戦略がない場合、シンプルに見えた機能が予期しないオーケストレーションの複雑さに阻まれることになります。

だからこそ、これは注目に値します。SQL MCP ServerがAzure App Serviceで動作するようになりました — DockerもKubernetesも不要で、MCP、REST、GraphQLを通じてSQLデータベースを公開する同じData API Builder（DAB）の設定ファイルだけで動きます。

## SQL MCP Serverとは？

まだご存知でない方への簡単な説明です。SQL MCP ServerはAIエージェントとSQLデータベースの間に位置します。エージェントにデータベースへの直接アクセスを与える（これはひどいアイデアです）代わりに、テーブルやビューを権限が定義されたエンティティという抽象化レイヤーとして公開します。

[Data API Builder](https://learn.microsoft.com/ja-jp/azure/data-api-builder/)上に構築されており、1つの設定ファイルがMCP *と* REST *と* GraphQLを同時に管理します。エージェントはMCPエンドポイントと通信し、従来のアプリケーションはRESTまたはGraphQLと通信します。同じ設定、同じランタイム、異なるインターフェース。

これは本当に便利です。2つの別々なAPIレイヤーを管理する必要がありません。

## コンテナの問題（と解決策）

SQL MCP Serverの元のデプロイモデルはコンテナでした。多くのチームではうまく機能しますが、すべてのチームではありません。多くの.NETチームはAzure App ServiceやVMに標準化しています。SQLエンドポイントを公開するためだけにコンテナランタイムを必要とするのは、誰も求めていない摩擦を生み出します。

新しいウォークスルーではコンテナを完全にスキップする方法を示しています。すべて`dab start`コマンドで動作し、標準の.NET 8 Webプロセスとして App Serviceにホストされます。

```bash
# Data API Builderをインストール
dotnet tool install microsoft.dataapibuilder --prerelease -g

# 設定を初期化
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# エンティティを追加
dab add products --source dbo.products --permissions "authenticated:*"

# App Service認証プロバイダーを設定
dab configure --runtime.host.authentication.provider AppService

# サーバーを起動
dab start
```

この時点で、`/mcp`でMCP、同じプロセスからRESTとGraphQLが利用可能になり、コンテナは一切不要です。

## 共有APIキーなしの認証

これが私が最も評価する部分です。App Serviceにデプロイする際、Microsoft Entra IDを認証プロバイダーとして設定します。設定ファイルに共有シークレットを埋め込む必要はなく、APIキーをローテーションする必要もありません。

接続文字列はApp Serviceの環境変数に保持され（`dab-config.json`には含まれません）、MCPエンドポイントはプラットフォーム認証で保護されます。Azure AIのワークロードでEntra IDにすでに対応している場合、これは自然に統合されます。

ローカル開発では`Simulator`モードとSTIOトランスポートに切り替えます。デプロイ前に`AppService`モードに戻します。クリーンで明示的な設定です。

## App Serviceへのデプロイ

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

その後、チームがすでに使用しているコードデプロイ方法でDABプロジェクトをデプロイします。重要なポイント：これは**コード**のデプロイであり、コンテナのデプロイではありません。

## .NET開発者にとって重要な理由

.NETでAIエージェントを構築している場合、エージェントはいずれデータベースと通信する必要があります。SQL MCP Serverは、生の接続文字列を公開したりカスタムAPIレイヤーを書いたりすることなく、それを行う構造化された方法を提供します。

完全なウォークスルーは[元のブログ記事](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/)と[GitHubのサンプルリポジトリ](https://github.com/Azure-Samples/SQL-MCP-NoContainer)でご確認ください。

## まとめ

App Service上のSQL MCP Serverは、コンテナ戦略なしにエージェントに構造化されたSQLデータアクセスを提供したい.NETチームにとって、実用的な選択肢です。ぜひ試してみてください — エージェントはクリーンなAPIサーフェスを高く評価するでしょう。
