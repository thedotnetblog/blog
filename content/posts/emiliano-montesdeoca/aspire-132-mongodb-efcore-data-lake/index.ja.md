---
title: "Aspire 13.2にMongoDB EF CoreとAzure Data Lakeが追加 — 試す価値のある2つのインテグレーション"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2では、設定不要のヘルスチェックとサービスディスカバリを備えたMongoDB Entity Framework CoreとAzure Data Lake Storageのインテグレーションが追加されました。実際にどのように使えるか紹介します。"
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *この記事は自動翻訳されています。オリジナル版は[こちら]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}})をご覧ください。*

Aspire 13.2が[2つの新しいデータベースインテグレーション](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/)と共にリリースされました。注目すべきはMongoDB Entity Framework CoreとAzure Data Lake Storageです。AspireアプリでMongoDBとEF Coreを使いたかった方、あるいはサービスディスカバリ付きでData Lakeワークロードを接続したかった方にとって、今回のリリースはまさにそれを提供してくれます。

## AspireでMongoDBとEF Coreが出会う

これが一番ワクワクしているインテグレーションです。AspireはMongoDBを以前からサポートしていましたが、常に生のドライバーでした — EF Coreなし、`DbContext`なし、ドキュメントに対するLINQクエリなし。今回から、MongoDBでフルのEF Core体験が得られるようになり、さらにAspireの自動ヘルスチェックとサービスディスカバリも付いてきます。

セットアップは典型的なAspireパターンです。AppHostで：

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

次に、コンシューマープロジェクトでEF Coreインテグレーションを追加します：

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

そして`DbContext`を登録します：

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

あとは標準的なEF Coreです。エンティティを定義し、他のプロバイダーと同じように`DbContext`を使います。コネクションプーリング、OpenTelemetryトレース、ヘルスチェックはインテグレーションがバックグラウンドで処理します。

生のドライバーでMongoDBを使い、コネクション文字列を手動で設定していた.NET開発者にとって、これは嬉しい改善です。Aspireのサービスディスカバリを失うことなく、EF Coreの完全な抽象化が手に入ります。

## Azure Data Lake Storageが仲間入り

2つ目の大きな追加は[Azure Data Lake Storage（ADLS）インテグレーション](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/)です。データパイプライン、ETLプロセス、分析プラットフォームを構築しているなら、他のAspire依存関係と同じ方法でData Lakeリソースを接続できるようになりました。

AppHostで：

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

コンシューマープロジェクトで：

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

コネクション文字列の手動管理も、資格情報の探索も不要です。Aspireがリソースをプロビジョニングして注入します。オペレーショナルデータと分析ワークロードの両方を扱うクラウドネイティブな.NETアプリを構築している私たちにとって、Data LakeがAspireモデルのファーストクラスシチズンのように感じられるようになります。

## 地味だけど大事な修正

メイン機能以外にも、いくつかの改善が注目に値します：

- **MongoDBコネクション文字列の修正** — データベース名の前のスラッシュが正しく処理されるようになりました。ワークアラウンドを使っていた方は、もう不要です
- **SQL Serverエクスポート** — `Aspire.Hosting.SqlServer`が追加のサーバー構成オプションをエクスポートし、より細かい制御が可能に
- **エミュレーターの更新** — ServiceBusエミュレーター2.0.0、App Configurationエミュレーター1.0.2、CosmosDBのプレビューエミュレーターにレディネスチェックが追加
- **Azure Managed Redis** — デフォルトで`rediss://`（Redis Secure）を使用するようになり、接続が最初から暗号化されます

最後のポイントは地味ですが重要です — デフォルトで暗号化されたRedisは、本番環境で設定すべきことが1つ減ることを意味します。

## まとめ

Aspire 13.2はインクリメンタルなリリースですが、MongoDB EF CoreとData Lakeのインテグレーションは実際のギャップを埋めてくれます。AspireでのMongoDBに対する適切なEF Coreサポートを待っていた方、またはData Lakeをファーストクラスの依存関係として必要としていた方は、[13.2にアップグレード](https://get.aspire.dev)して試してみてください。`aspire add`コマンドで必要なものがすべてスキャフォールドされます。

[完全なリリースノート](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates)で詳細を確認し、[インテグレーションギャラリー](https://aspire.dev/integrations/gallery/)で完全なリストをチェックしてください。
