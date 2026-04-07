---
title: "MCP AppsにFluent APIが登場 — .NETでリッチなAIツールUIを3ステップで構築"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Azure Functions上のMCP Apps向け新しいFluent設定APIにより、あらゆる.NET MCPツールをビュー、パーミッション、CSPポリシーを備えた完全なアプリに、わずか数行のコードで変換できます。"
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}})をご覧ください。*

MCPツールはAIエージェントに機能を与えるのに最適です。でも、ツールがユーザーに何かを表示する必要がある場合はどうでしょう？ ダッシュボード、フォーム、インタラクティブなビジュアライゼーション。そこで登場するのがMCP Appsで、構築がずっと簡単になりました。

Azure SDKチームのLilian Kasemが、.NET Azure Functions上のMCP Apps向け[新しいFluent設定APIを発表](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)しました。なぜ最初からこんなにシンプルじゃなかったのかと思うような、開発者体験の改善です。

## MCP Appsとは？

MCP AppsはModel Context Protocolを拡張し、ツールが独自のUIビュー、静的アセット、セキュリティコントロールを持てるようにします。テキストを返すだけでなく、MCPツールは完全なHTMLエクスペリエンスをレンダリングできます — インタラクティブなダッシュボード、データビジュアライゼーション、設定フォーム — すべてAIエージェントから呼び出し可能で、MCPクライアントを通じてユーザーに表示されます。

問題は、これらを手動で配線するにはMCP仕様を深く理解する必要があったことです：`ui://` URI、特殊なMIMEタイプ、ツールとリソース間のメタデータ調整。難しくはないけど、面倒でした。

## Fluent APIの3ステップ

**ステップ1：関数を定義する。** 標準的なAzure Functions MCPツール：

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**ステップ2：MCP Appに昇格させる。** プログラムのスタートアップで：

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**ステップ3：HTMLビューを追加する。** 必要なUIで`assets/hello-app.html`を作成します。

以上です。Fluent APIがMCPプロトコルの配管をすべて処理します — 合成リソース関数の生成、正しいMIMEタイプの設定、ツールとビューを接続するメタデータの注入。

## APIの設計が秀逸

特に気に入っている点がいくつかあります：

**ビューソースが柔軟。** ディスク上のファイルからHTMLを提供したり、自己完結型デプロイのためにリソースをアセンブリに直接埋め込んだりできます：

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSPがコンポーザブル。** 最小権限の原則に従い、アプリが必要とするオリジンを明示的に許可します。`WithCsp`を複数回呼び出すとオリジンが蓄積されます：

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**可視性制御。** ツールをLLMのみ、ホストUIのみ、または両方に表示できます。UIのみをレンダリングし、モデルから呼び出されるべきでないツールが欲しい場合は簡単：

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## 始め方

プレビューパッケージを追加：

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

すでにAzure FunctionsでMCPツールを構築している場合、これはパッケージの更新だけです。コンセプトが初めての方は[MCP Appsクイックスタート](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp)が最適な出発点です。

## まとめ

MCP AppsはAIツーリング分野で最もエキサイティングな開発の一つです — 物事を*行う*だけでなく、ユーザーに物事を*見せる*ことができるツール。Fluent APIはプロトコルの複雑さを取り除き、重要なことに集中させてくれます：ツールのロジックとそのUI。

完全なAPIリファレンスと例については[完全な記事](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)をお読みください。
