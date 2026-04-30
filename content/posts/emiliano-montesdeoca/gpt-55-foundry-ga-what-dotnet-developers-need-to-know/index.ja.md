---
title: "GPT-5.5 が Azure Foundry に登場 — .NET 開発者が知っておくべきこと"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 が Microsoft Foundry で一般提供開始。GPT-5 から 5.5 への進化、実際に何が改善されたか、そして今日エージェントで使い始める方法。"
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をご覧ください。*

Microsoftは[GPT-5.5がMicrosoft Foundryで一般提供開始](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)したと発表しました。Azureでエージェントを構築してきた方にとって、これが待ち望んでいたアップデートです。

## GPT-5 の進化

- **GPT-5**: 推論と速度を1つのシステムに統合
- **GPT-5.4**: より強力なマルチステップ推論、企業向けエージェント機能
- **GPT-5.5**: より深い長コンテキスト推論、信頼性の高いエージェント実行、トークン効率の向上

## 実際に何が変わったか

**エージェントコーディングの向上**: GPT-5.5は大規模なコードベース全体でコンテキストを保持し、アーキテクチャ上の障害を診断し、テスト要件を予測します。修正が*他に何に影響するか*を行動前に推論します。

**トークン効率**: 少ないトークンと少ない再試行でより高品質な出力。本番デプロイメントでコストとレイテンシが直接削減されます。

**長コンテキスト分析**: 膨大なドキュメントやマルチセッション履歴をスレッドを失わずに処理。

## 価格

| モデル | 入力 ($/M tokens) | キャッシュ入力 | 出力 ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

## Foundry が重要な理由

Foundry Agent Serviceでは、YAMLでエージェントを定義するか、Microsoft Agent Framework、GitHub Copilot SDK、LangGraph、またはOpenAI Agents SDKで接続できます。永続的なファイルシステム、独自のMicrosoft Entraアイデンティティ、ゼロスケール価格を持つ孤立したホステッドエージェントとして実行します。

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "あなたは役立つアシスタントです。", name: "MyAgent");
```

完全な詳細は[完全発表](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)をご覧ください。
