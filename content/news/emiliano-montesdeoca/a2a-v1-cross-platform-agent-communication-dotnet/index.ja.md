---
title: "A2A v1 登場: Microsoft Agent Framework for .NET でのクロスプラットフォームエージェント通信"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "A2A プロトコル v1.0 がリリースされ、Microsoft Agent Framework の .NET パッケージが更新されました — AIエージェントをプロバイダー間で接続・公開するための安定した相互運用性標準。"
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[A2A v1 登場: Microsoft Agent Framework for .NET でのクロスプラットフォームエージェント通信](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — A2A プロトコルが v1.0 に到達し、.NET の A2A Agent（クライアント）と A2A Hosting（サーバー）パッケージが更新されました。

## A2A v1 の実体

A2A は、AWS、Cisco、Google、IBM Research、Microsoft、Salesforce、SAP、ServiceNow の代表者からなるテクニカルステアリングコミッティが支援するAIエージェント向けオープン相互運用プロトコルです。v1 ラベルは、これが安定した本番対応の標準になったことを意味します。実装する SDK と Agent Framework パッケージはまだプレビュー段階ですが、プロトコル自体は確定しています。

v1 は v0.3 からマルチテナントサポート、暗号化IDのための署名付き Agent Cards、改善されたセキュリティフロー、ウェブ整合アーキテクチャを追加しました。

## リモート A2A エージェントへの接続

リモート A2A エージェントはコード内では単なる `AIAgent` です — 同じ `RunAsync`、同じストリーミング、同じセッション管理：

```csharp
// Well-known URI による探索
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// 直接設定
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// ストリーミングも同様
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## エージェントを A2A エンドポイントとして公開

Microsoft Foundry、Azure OpenAI、OpenAI、Anthropic、AWS Bedrock で構築した任意の `AIAgent` を、ASP.NET Core の 2 行で A2A エンドポイントとして公開できます：

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

エージェントカードは `/.well-known/agent-card.json` で自動的に提供されます。

## 実際に何を意味するか

安定した v1 プロトコルにより、breaking changes を心配せずに .NET エージェントを Python、Java、その他の言語で構築されたエージェントと接続できます。署名付き Agent Cards の暗号化 ID は、エージェント間の信頼検証の基盤も提供します。

完全な変更履歴と v0.3 からの移行メモについては、[完全な記事](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/)をご覧ください。
