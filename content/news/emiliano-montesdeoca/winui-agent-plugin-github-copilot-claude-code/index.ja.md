---
title: "GitHub CopilotとClaude Code向けWinUIエージェントプラグイン"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "MicrosoftがWinUI開発向けエージェントスキルをリリース：スキャフォールド、ビルド、実行、テスト、反復、すべてGitHub Copilot CLIまたはClaude Codeで。核心的な革新：WinUI固有の事実にエージェントを根付かせる専用ツール。"
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

MicrosoftがWinUIアプリケーション開発向けのオープンソースのエージェントスキルセットを公開しました。[aka.ms/winui-skills](https://aka.ms/winui-skills)で入手できます。

## インストールとセットアップ

`/plugin install winui@awesome-copilot`でプラグインをインストールし、次に`/winui:winui-setup`で初期セットアップを実行します。セットアッププロセスは前提条件を確認し、必要な依存関係をインストールし、WinUIアプリケーション開発の環境を構成します。

## エンドツーエンド開発ループ

スキルは完全な開発サイクルをカバーします：

- **スキャフォールド：** 適切なパラメータで`dotnet new WinUI`を使用して正しいプロジェクトテンプレートを生成します — エージェントは正しいテンプレートとデフォルト設定値を知っています。
- **ビルド：** WinUIアプリケーションが必要とするパッケージ化された実行モデルを管理し、パッケージ署名とマニフェスト設定を含みます。
- **インタラクションと検証：** アプリケーションを起動し、インタラクションを行い、動作を検証します。
- **コンパイルエラーの修正：** エージェントはWinUI固有のエラーメッセージを理解し、解決方法を知っています。

## 専用ツールによるトークン効率

核心的な革新は、スキルに要求に応じて具体的な参照データを取得する専用ツールが含まれていることです：

- WinUIとFluent DesignのAPIの詳細
- MVVMパターンとベストプラクティス
- MSIXパッケージング、コード署名、Storeへの提出
- アクセシビリティ、テーマ、UIオートメーション

WinUIドキュメント全体をコンテキストに注入する代わりに、ツールはエージェントが必要とするものを必要な時に正確に取得します。これにより、エージェントがビルドサイクルやテストスイートを実行する際のコンテキスト使用を効率的に保ち、専門的なドメインでの精度を向上させます。

## 専用スキルが重要な理由

汎用言語モデルはWinUI固有のニュアンスについて限られた知識しか持ちません：パッケージ化された実行モデル、Fluent Design API、MSIX統合、またはWindows App SDKがWin32機能をラップする特定の方法。専用ツールは、潜在的に古いまたは誤ったモデルの知識ではなく、検証されたWinUIの事実にエージェントを根付かせることでこれを解決します。

同じパターンは、一般的な開発パターンとは異なる独自の規則と要件を持つ専門的なフレームワークやSDKにも適用されます。

元の投稿：[A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
