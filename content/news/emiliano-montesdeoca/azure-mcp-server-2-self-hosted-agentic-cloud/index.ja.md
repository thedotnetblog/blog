---
title: "Azure MCP Server 2.0 がリリース — セルフホスト型エージェンティック クラウド オートメーションがここに"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 は、セルフホスト型のリモート展開、57 の Azure サービス全体で 276 のツール、エンタープライズグレードのセキュリティを備え、安定版となりました。エージェンティック ワークフローを構築する .NET 開発者にとって重要な点をここに紹介します。"
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

*この記事は自動翻訳されています。オリジナル版は[こちら]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud.md" >}})をご覧ください。*

最近 MCP と Azure で何かを構築している人なら、ローカル環境での体験がうまく機能していることはご存じでしょう。MCP サーバーを接続して、AI エージェントが Azure リソースと通信できるようにして、先へ進む。しかし、その設定をチーム全体で共有する必要が出た瞬間？そこが複雑になっていました。

もうそんなことはありません。Azure MCP Server が [2.0 安定版をリリース](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)し、見出し機能はまさにエンタープライズ チームが要望していたものです：**セルフホスト型リモート MCP サーバー サポート**。

## Azure MCP Server とは？

簡単なおさらいです。Azure MCP Server は [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) 仕様を実装し、Azure 機能を構造化された検出可能なツールとして公開します。AI エージェントがこれらを呼び出せます。これをエージェントと Azure 間の標準化された橋と考えてください — プロビジョニング、デプロイメント、監視、診断、すべて 1 つの一貫したインターフェース経由で。

数字を見ればわかります：**57 の Azure サービス全体で 276 の MCP ツール**。これは本格的なカバレッジです。

## 大きな変化：セルフホスト型リモート展開

ここが重要な点です。ローカルでマシン上で MCP を実行することは開発と実験には問題ありませんが、実際のチーム シナリオでは以下が必要です：

- 開発者と内部エージェント システム向けの共有アクセス
- 集中管理構成（テナント コンテキスト、サブスクリプション デフォルト、テレメトリ）
- エンタープライズ ネットワークとポリシー境界
- CI/CD パイプラインへの統合

Azure MCP Server 2.0 はこれらすべてに対応しています。HTTP ベースのトランスポート、適切な認証、一貫した統治を備えた集中管理内部サービスとしてデプロイできます。

認証には 2 つの確実なオプションがあります：

1. **マネージド ID** — [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) と並行して実行している場合
2. **On-Behalf-Of（OBO）フロー** — サインインしたユーザーのコンテキストを使用して Azure API を呼び出す OpenID Connect 委譲

この OBO フロー は .NET 開発者にとって特に興味深いものです。これは、エージェンティック ワークフローが過度な特権を持つサービス アカウントではなく、ユーザーの実際のアクセス許可で動作できることを意味します。最小権限の原則が組み込まれています。

## セキュリティの強化

これは単なる機能リリースではなく、セキュリティ リリースでもあります。2.0 リリースは以下を追加します：

- より強いエンドポイント検証
- クエリ指向ツールのインジェクション パターンに対する保護
- 開発環境用のより厳密な分離制御

MCP を共有サービスとして公開する場合、これらのセーフガードは重要です。本当に重要です。

## どこで使用できますか？

クライアント互換性の状況は幅広いです。Azure MCP Server 2.0 は以下で動作します：

- **IDE**：VS Code、Visual Studio、IntelliJ、Eclipse、Cursor
- **CLI エージェント**：GitHub Copilot CLI、Claude Code
- **スタンドアロン**：シンプルなセットアップ用のローカル サーバー
- **セルフホスト型リモート**：2.0 の新しいスター

さらに、Azure US Government と 21Vianet が運用する Azure のソブリン クラウド サポートもあります。これは規制対象のデプロイメントに重要です。

## .NET 開発者にとってこれが重要な理由

.NET でエージェンティック アプリケーションを構築している場合 — Semantic Kernel、Microsoft Agent Framework、または独自のオーケストレーションのいずれであっても — Azure MCP Server 2.0 は、エージェントが Azure インフラストラクチャと対話するための本番環境対応の方法を提供します。カスタム REST ラッパーは不要です。サービス固有の統合パターンは不要です。MCP があるだけです。

数日前にドロップされた [MCP Apps 向けの Fluent API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) と組み合わせると、.NET MCP エコシステムは急速に成熟しています。

## はじめに

パスを選択してください：

- **[GitHub リポジトリ](https://aka.ms/azmcp)** — ソース コード、ドキュメント、すべて
- **[Docker イメージ](https://aka.ms/azmcp/download/docker)** — コンテナ化されたデプロイメント
- **[VS Code 拡張機能](https://aka.ms/azmcp/download/vscode)** — IDE 統合
- **[セルフホスティング ガイド](https://aka.ms/azmcp/self-host)** — 2.0 の旗艦機能

## まとめ

Azure MCP Server 2.0 は、デモでは派手に見えないけれど、実際には万能を変えるようなインフラストラクチャ アップグレードです。適切な認証、セキュリティ強化、ソブリン クラウド サポートを備えたセルフホスト型リモート MCP は、Azure でエージェンティック ワークフローを構築している実際のチームに MCP が対応していることを示しています。「エンタープライズ対応」シグナルを待っていたなら — これです。
