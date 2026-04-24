---
title: "Foundry Toolboxes: AIエージェントツールのための統一エンドポイント"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft FoundryがToolboxesをパブリックプレビューで公開した。AIエージェントツールを単一のMCP互換エンドポイントで管理・公開するための仕組みだ。"
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})をクリックしてください。*

退屈に聞こえるが実際に直面すると深刻な問題がある：組織が複数のAIエージェントを構築し、それぞれがツールを必要とし、各チームがゼロから設定している。同じWeb検索統合、同じAzure AI Searchの設定、同じGitHub MCPサーバーの接続 — でも別のリポジトリに、別のチームが、別の認証情報で、ガバナンスの共有なしに。

Microsoft FoundryがPublic Previewで[Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)を公開した。これはその問題への直接的な答えだ。

## Toolboxとは

ToolboxはFoundryで一度定義し、単一のMCP互換エンドポイントを通じて公開する、名前付きの再利用可能なツールバンドルだ。MCPを話す任意のエージェントランタイムが消費できる — Foundry Agentsへのロックインはない。

提案はシンプルだ：**build once, consume anywhere**。ツールを定義し、認証を一元設定（OAuthパススルー、Entraマネージドアイデンティティ）し、エンドポイントを公開する。そのツールが必要な各エージェントはエンドポイントに接続して全てを取得する。

## 4つの柱（今日は2つが利用可能）

| 柱 | ステータス | 何をするか |
|----|---------|-----------|
| **Discover** | 近日公開 | 手動検索なしで承認済みツールを発見 |
| **Build** | 利用可能 | ツールを再利用可能なバンドルにまとめる |
| **Consume** | 利用可能 | 単一MCPエンドポイントが全ツールを公開 |
| **Govern** | 近日公開 | 全ツール呼び出しの一元認証+可観測性 |

## 実践的な例

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="ドキュメントを検索し、GitHubのissueに対応する",
    tools=[
        {"type": "web_search", "description": "公開ドキュメントを検索"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

公開後、Foundryは統一エンドポイントを提供する。1回の接続で全ツールが使える。

## Foundry Agentsへのロックインはない

ToolboxはFoundryで**作成・管理**されるが、消費面はオープンなMCPプロトコルだ。Microsoft Agent FrameworkやLangGraphのカスタムエージェント、GitHub Copilotやその他のMCP対応IDE、あらゆるMCPランタイムから使用できる。

## 今なぜ重要か

マルチエージェントの波が本番環境に到達している。新しいエージェントが増えるたびに、重複した設定、古い認証情報、一貫性のない動作の新たな表面が生まれる。Build + Consumeの基盤は集中化を始めるには十分だ。Governの柱が来た時、エージェント全体に完全に可観測で一元管理されたツール層が得られる。

## まとめ

まだ早い段階だ — パブリックプレビュー、Python SDK優先。しかし、モデルは確かで、MCPネイティブな設計は既に構築しているツールで機能することを意味する。[公式発表](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)で詳細を確認しよう。
