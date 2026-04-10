---
title: "エージェンティックなプラットフォームエンジニアリングが現実になりつつある — Git-APEがその方法を示す"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "MicrosoftのGit-APEプロジェクトがエージェンティックなプラットフォームエンジニアリングを実践 — GitHub CopilotエージェントとAzure MCPを使って自然言語のリクエストを検証済みクラウドインフラに変換します。"
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "agentic-platform-engineering-git-ape" >}})をご覧ください。*

プラットフォームエンジニアリングは、カンファレンスでは素晴らしく聞こえるけど、実際には「内部ポータルとTerraformラッパーを作りました」という意味になりがちな用語の一つです。本当の約束 — 安全で、ガバナンスが効いていて、高速なセルフサービスインフラ — はいつもあと数歩先にありました。

Azureチームが[エージェンティックなプラットフォームエンジニアリングシリーズのパート2](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/)を公開しました。今回はハンズオンの実装がテーマです。彼らはこれを**Git-APE**と呼んでいます（はい、頭字語は意図的です）。これはGitHub CopilotエージェントとAzure MCPサーバーを使って、自然言語のリクエストを検証済みでデプロイされたインフラに変換するオープンソースプロジェクトです。

## Git-APEが実際にやること

コアアイデア：開発者がTerraformモジュールを学んだり、ポータルUIをナビゲートしたり、プラットフォームチームにチケットを切る代わりに、Copilotエージェントに話しかけます。エージェントが意図を解釈し、Infrastructure-as-Codeを生成し、ポリシーに対して検証し、デプロイします — すべてVS Code内で。

セットアップはこちら：

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

VS Codeでワークスペースを開くと、エージェント設定ファイルがGitHub Copilotによって自動検出されます。エージェントと直接やり取りします：

```
@git-ape deploy a function app with storage in West Europe
```

エージェントは内部でAzure MCPサーバーを使ってAzureサービスとやり取りします。VS Code設定のMCP構成で特定の機能を有効にします：

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## なぜこれが重要か

Azureで構築している私たちにとって、これはプラットフォームエンジニアリングの議論を「ポータルをどう構築するか」から「ガードレールをどうAPIとして記述するか」にシフトさせます。プラットフォームのインターフェースがAIエージェントになると、制約とポリシーの品質がプロダクトになります。

パート1のブログは理論を提示しました：よく記述されたAPI、コントロールスキーマ、明示的なガードレールがプラットフォームをエージェント対応にします。パート2は実際のツールを提供することでそれが機能することを証明しています。エージェントはリソースを盲目的に生成するのではなく、ベストプラクティスに対して検証し、命名規則を尊重し、組織のポリシーを適用します。

クリーンアップも同様に簡単です：

```
@git-ape destroy my-resource-group
```

## 私の見解

正直に言うと、これは特定のツールよりもパターンについてです。Git-APE自体はデモ/リファレンスアーキテクチャです。しかし根底にあるアイデア — プラットフォームへのインターフェースとしてのエージェント、プロトコルとしてのMCP、ホストとしてのGitHub Copilot — これがエンタープライズの開発者体験が向かう方向です。

内部ツールをエージェントフレンドリーにする方法を探しているプラットフォームチームなら、これ以上の出発点はありません。そして.NET開発者として自分の世界とどう繋がるか気になるなら：Azure MCPサーバーとGitHub Copilotエージェントはどんなのワークロードでも動作します。ASP.NET Core API、.NET Aspireスタック、コンテナ化されたマイクロサービス — すべてがエージェンティックなデプロイフローのターゲットになり得ます。

## まとめ

Git-APEは、エージェンティックなプラットフォームエンジニアリングの実践における初期だが具体的な姿です。[リポジトリ](https://github.com/Azure/git-ape)をクローンし、デモを試し、プラットフォームのAPIとポリシーがエージェントに安全に使われるためにどうあるべきか考え始めてください。

[完全な記事](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/)でウォークスルーとデモ動画をご覧ください。
