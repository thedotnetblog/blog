---
title: "Visual Studioの3月アップデートでカスタムCopilotエージェントが作成可能に — find_symbolが大きな進化"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studioの2026年3月アップデートがカスタムCopilotエージェント、再利用可能なスキル、言語対応のfind_symbolツール、Test ExplorerからのCopilotプロファイリングを提供。"
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *この記事は自動翻訳されました。オリジナル版は[こちら]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}})をご覧ください。*

Visual Studioが最も重要なCopilotアップデートを受けました。Mark Downieが[3月リリースを発表](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/)し、見出しはカスタムエージェントですが、正直なところ`find_symbol`ツールがワークフローを最も変える機能かもしれません。

## リポジトリ内のカスタムCopilotエージェント

Copilotにチームのコーディング標準に従わせたい？カスタムエージェントはリポジトリの`.github/agents/`に`.agent.md`ファイルとして定義されます。各エージェントはワークスペース認識、コード理解、ツール、優先モデル、MCP接続へのフルアクセスを持ちます。

## エージェントスキル：再利用可能なインストラクションパック

スキルはリポジトリの`.github/skills/`またはプロファイルの`~/.copilot/skills/`から自動的にロードされます。

## find_symbol：言語対応ナビゲーション

新しい`find_symbol`ツールはCopilotのエージェントモードに言語サービスベースのシンボルナビゲーションを提供します。テキスト検索の代わりに、シンボルのすべての参照を見つけ、型情報やスコープにアクセスできます。

.NET開発者にとって、これは大きな改善です — 深い型階層を持つC#コードベースが大きく恩恵を受けます。

## Copilotでテストをプロファイル

Test Explorerのコンテキストメニューに**Profile with Copilot**が追加されました。Profiling Agentがテストを実行し、パフォーマンスを自動分析します。

## ライブデバッグ中のPerf Tips

パフォーマンス最適化がデバッグ中に行われるようになりました。Visual Studioがインラインで実行時間を表示します。遅い行を見つけたら、Perf Tipをクリックして最適化の提案をCopilotに依頼できます。

## Solution ExplorerからNuGet脆弱性を修正

NuGetパッケージの脆弱性が検出されると、Solution Explorerに直接**Fix with GitHub Copilot**リンクが表示されます。

## まとめ

カスタムエージェントとスキルが見出しですが、`find_symbol`が隠れた逸品です — .NETコードのリファクタリング時のCopilotの精度を根本的に変えます。[Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/)をダウンロードしてお試しください。
