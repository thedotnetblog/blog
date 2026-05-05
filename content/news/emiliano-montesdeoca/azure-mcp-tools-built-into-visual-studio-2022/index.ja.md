---
title: "Azure MCPツールがVisual Studio 2022に組み込まれました — 拡張機能のインストール不要"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCPツールがVisual Studio 2022のAzure開発ワークロードの一部として同梱されました。230以上のツール、45のAzureサービス、インストールする拡張機能はゼロ。"
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *この記事は自動翻訳されています。原文は[こちらをクリック]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}})してご覧ください。*

Visual Studioで別途拡張機能としてAzure MCPツールを使っていた方なら、あのお決まりの流れをご存知でしょう — VSIXをインストールし、再起動し、壊れないことを祈り、バージョンの不一致を管理する。その煩わしさはもう終わりです。

Yun Jung Choiが[発表](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/)したとおり、Azure MCPツールはVisual Studio 2022のAzure開発ワークロードの一部として直接同梱されるようになりました。拡張機能なし。VSIXなし。再起動の手間なし。

## これが実際に意味すること

Visual Studio 2022 バージョン17.14.30以降、Azure MCP ServerはAzure開発ワークロードにバンドルされています。すでにそのワークロードがインストールされていれば、GitHub Copilot Chatで有効にするだけで完了です。

45のAzureサービスにわたる230以上のツール — チャットウィンドウから直接アクセスできます。ストレージアカウントの一覧表示、ASP.NET Coreアプリのデプロイ、App Serviceの問題診断、Log Analyticsへのクエリ — すべてブラウザタブを開くことなく実行できます。

## なぜこれが見た目以上に重要なのか

開発ツールについて言えることはこれです：余分なステップはすべて摩擦であり、摩擦は普及を妨げます。MCPが別の拡張機能だった頃は、バージョンの不一致、インストールの失敗、そしてもう一つアップデートを管理するものが増えるということを意味していました。ワークロードへの組み込みは以下を意味します：

- **単一の更新パス** — Visual Studio Installerを通じて
- **バージョンのずれなし** — 拡張機能とIDEの間で
- **常に最新** — MCP Serverは通常のVSリリースと一緒に更新

Azureを標準化しているチームにとって、これは大きな前進です。ワークロードを一度インストールし、ツールを有効にすれば、毎回のセッションで利用可能です。

## これで何ができるか

ツールはCopilot Chatを通じて開発ライフサイクル全体をカバーします：

- **学ぶ** — Azureサービス、ベストプラクティス、アーキテクチャパターンについて質問
- **設計・開発** — サービスの推奨を取得、アプリコードの設定
- **デプロイ** — リソースのプロビジョニングとIDEからの直接デプロイ
- **トラブルシューティング** — ログのクエリ、リソースの正常性チェック、本番環境の問題診断

簡単な例として、Copilot Chatで以下を入力してみてください：

```
List my storage accounts in my current subscription.
```

Copilotは裏側でAzure MCPツールを呼び出し、サブスクリプションを照会し、名前、場所、SKUが記載されたフォーマット済みリストを返します。ポータルは不要です。

## 有効にする方法

1. Visual Studio 2022 **17.14.30**以降にアップデート
2. **Azure development**ワークロードがインストールされていることを確認
3. GitHub Copilot Chatを開く
4. **Select tools**ボタン（レンチアイコン）をクリック
5. **Azure MCP Server**をオンに切り替え

以上です。セッション間で有効な状態が維持されます。

## 注意点

ツールはデフォルトで無効になっています — オプトインが必要です。また、VS 2026固有のツールはVS 2022では利用できません。ツールの利用可能性はAzureサブスクリプションの権限にも依存します。ポータルと同じです。

## より大きな視点

これは明確なトレンドの一部です：MCPは開発者IDEにクラウドツールを提供するための標準になりつつあります。すでに[Azure MCP Server 2.0の安定版リリース](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)やVS Codeをはじめとする各種エディタでのMCP統合が進んでいます。Visual Studioのワークロードシステムへの組み込みは、その自然な進化です。

Visual Studioで日々開発している.NET開発者にとって、Azureポータルへのコンテキストスイッチの理由がまた一つ減りました。正直なところ、タブの切り替えは少なければ少ないほど良いですからね。
