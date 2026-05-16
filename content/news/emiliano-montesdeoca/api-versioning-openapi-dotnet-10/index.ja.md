---
title: ".NET 10 で API バージョニングと OpenAPI を組み合わせる"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 は .NET 10 と Microsoft.AspNetCore.OpenApi の両方を公式サポートする初のバージョンで、API バージョンごとに個別の OpenAPI ドキュメントを生成します。"
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[.NET 10 で API バージョニングと OpenAPI を組み合わせる](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — Microsoft MVP の Sander ten Brinke によるゲスト記事 — は、新パッケージ `Asp.Versioning` v10 を解説しています。これは .NET 10 と、.NET 9 でデフォルトとして Swashbuckle を置き換えた組み込みライブラリ `Microsoft.AspNetCore.OpenApi` に特化して設計された初のバージョンです。

## Asp.Versioning v10: 新しい OpenAPI スタックのために設計

従来の `Asp.Versioning` v8.x は暗黙的なロールフォワードにより .NET 10 でも動作しますが、v10 は `Microsoft.AspNetCore.OpenApi` に特化して設計された初のバージョンです。基本的なセットアップは `AddApiVersioning` を `AddApiExplorer` とチェーンし、公開したいバージョンごとに `AddOpenApi` を個別に呼び出すことです:

```csharp
builder.Services.AddApiVersioning(options => {
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
})
.AddApiExplorer(options => {
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

builder.Services.AddOpenApi("v1");
builder.Services.AddOpenApi("v2");
```

これにより `/openapi/v1.json` と `/openapi/v2.json` にそれぞれ個別のドキュメントが生成されます。

## バージョニング戦略: URL パス、クエリ文字列、ヘッダー、メディアタイプ

パッケージは 4 つの戦略をサポートします。URL パスバージョニング (`/api/v1/resource`) はパブリック API で最も一般的です。クエリ文字列 (`?version=1.0`) とカスタムヘッダー (`X-API-Version`) は内部サービスで人気があります。`Accept` ヘッダーを使ったメディアタイプバージョニングは、GitHub が REST API に採用しているアプローチです。

## Minimal APIs と Controllers の両方に対応

Minimal APIs では、バージョンセットを作成して各ルートを特定のバージョンにマップします:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Controllers では、クラスとアクションレベルに `[ApiVersion("1.0")]` および `[MapToApiVersion("1.0")]` 属性を適用します。

## SwaggerUI と Scalar はすぐに動作

`Swashbuckle.AspNetCore.SwaggerUI` と `Scalar.AspNetCore` はどちらもスムーズに統合できます — バージョンごとのドキュメント URL を指定するだけで、追加の設定なしにバージョン対応 UI が得られます。

## コード例は .NET 10 のファイルベースアプリを使用

記事のサンプルは C# 14 / .NET 10 の新しいファイルベースアプリ機能を使用しています: プロジェクトファイル不要で、`dotnet <ファイル名>.cs` で単一の `.cs` ファイルを実行します。スニペットが自己完結していてローカルで簡単に試せます。

## まとめ

.NET 10 を使用していて、サードパーティミドルウェアを追加せずにクリーンなバージョン付き OpenAPI コントラクトを実現したい場合、`Asp.Versioning` v10 が公式の選択肢です。

記事全文を読む: [.NET 10 で API バージョニングと OpenAPI を組み合わせる](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
