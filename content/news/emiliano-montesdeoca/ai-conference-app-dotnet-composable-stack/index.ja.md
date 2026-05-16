---
title: ".NETのComposable StackでAI搭載カンファレンスアプリを構築する"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "MicrosoftはConferencePulseを構築しました — Microsoft.Extensions.AI、DataIngestion、VectorData、MCP、Agent Frameworkを組み合わせたライブカンファレンスBlazorアプリ。パーツがどう組み合わさるかを説明します。"
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[.NETのComposable StackでAI搭載カンファレンスアプリを構築する](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoftは、5つの.NET拡張ライブラリを組み合わせることで、ライブカンファレンスセッション向けのBlazor ServerアプリであるConferencePulseを構築しました。MVP Summitで使用されました。

## ConferencePulseの機能

ConferencePulseはライブセッション中に動作し、以下を提供します：セッションコンテンツからAIが生成するポール、ライブナレッジベースからRAGパイプラインで引き出す聴衆Q&A、自動生成されたインサイト、複数の同時AIエージェントが生成するセッションサマリー。スタックは.NET 10、Blazor Server、Aspireで、5つのプロジェクトに分割されています：Web、Core、Ingestion、Agents、Mcp、AppHost。

## Microsoft.Extensions.AI：すべてのための1つの抽象化

`IChatClient`は統合抽象化です — 一度セットアップすれば、同じインターフェイスがAzure OpenAI、OpenAI、Anthropic、または他のプロバイダーで動作します。関数呼び出し、OpenTelemetryトレーシング、ロギングミドルウェアを備えた完全設定クライアントを6行で取得できます：

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

同じ`IChatClient`は後でデータ取り込みのエンリッチメントステップに再利用されます — そのための別クライアントは不要です。

## DataIngestionパイプライン

セッションコンテンツはパイプラインを流れます：`MarkdownReader` → `HeaderChunker`（500トークン、50トークンオーバーラップ）→ `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter`（Qdrant）。エンリッチャーはインデックス作成前にサマリーを生成してキーワードを抽出するために同じ`IChatClient`を使用します。聴衆の質問、Q&Aペア、ポール結果はセッションが進むにつれてリアルタイムで取り込まれます — ナレッジベースはトーク中に成長します。

## VectorData：プロバイダーに依存しない検索

`VectorStoreCollection.SearchAsync()`は、バッキングストアがQdrantであるかAzure AI Searchであるかに関係なく同じように動作します。ハイブリッド検索（ベクトル + 全文）がサポートされています。聴衆Q&AのRAGパイプラインはこのコレクションをクエリし、チャットクライアントにコンテキストとして渡す関連チャンクを取得します。

## MCP：ツールとしてのセッションコンテンツ

セッションコンテンツはMCPを通じて公開されるため、MCPと互換性のあるクライアントからアクセスできます。サーバーとクライアントの両方が実装されています — サーバーはセッションの知識をMCPツールとして公開し、クライアントはエージェントパイプライン内からそれらのツールを呼び出すことを可能にします。

## Agent Framework：並列マルチエージェントサマリー

セッションサマリーは3つのエージェントが並行して実行されることで生成されます — `PollSummaryAgent`、`QuestionSummaryAgent`、`InsightSummaryAgent` — その後マージされます。これはMicrosoft Agent Frameworkのグループチャットまたは並列実行パターンを使用します。各エージェントが1つの関心事を担当し、オーケストレーターが出力をマージします。

## 設計原則

この投稿では覚えておく価値のある点が述べられています：最もシンプルなツールを使用する。シンプルな生成タスクには直接の`IChatClient`呼び出し。構造化データ抽出にはツール/関数呼び出し。自律的なマルチステップ推論が必要な場合のみフルエージェントを使用。ライブラリのレイヤリングがこれを強制します — フルAgent Frameworkを引き込まずに`Microsoft.Extensions.AI`を使用できます。

完全なプロジェクト構造とソースリンクについては、[フルポスト](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/)を参照してください。
