---
title: "Visual Studio 2026 4 月アップデート：クラウドエージェント、カスタムエージェント、デバッガーエージェント"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026 (18.5) の 4 月アップデートでクラウドエージェント統合、ユーザーレベルのカスタムエージェント、C++ ツール GA、実際のランタイム動作に対して修正を検証するデバッガーエージェントが追加。"
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[Visual Studio 2026 (18.5) の 4 月アップデート](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/)では、クラウドエージェント統合、ユーザーレベルのカスタムエージェント、GA に到達する C++ ツール、新しいデバッガーエージェントが提供されます。

## クラウドエージェント：リモート Copilot セッションに作業を委任

Chat ウィンドウのエージェントピッカーで **Cloud** を選択すると、リモートの Copilot コーディングエージェントにタスクを委任できます。作業を説明すると、エージェントはリポジトリに GitHub issue を作成し、完了したら PR を開きます。"View PR" / "Open in browser" の通知が届きます — コーディングを続けながら、または IDE を閉じた状態でも動作します。

## カスタムエージェントがどこへでもついてくる

`%USERPROFILE%/.github/agents/` に保存されたユーザーレベルのカスタムエージェントはリポジトリに限定されなくなりました — プロジェクトをまたいで追従します。保存パスは Tools > Options > GitHub > Copilot > Chat で設定可能です。エージェントピッカーの `+` ボタンで直接新しいエージェントを作成できます。リポジトリスコープのエージェントと同じ機能を持ちます：ワークスペース認識、ツール、モデル選択、MCP 接続。

組み込みエージェント：Agent、Ask、Copilot CLI、Debugger、Modernize、Profiler。

## C++ コード編集ツールが GA に

2 つのツール — `get_symbol_call_hierarchy` と `get_symbol_class_hierarchy` — がデフォルトで有効になりました。C++ コードベースの継承階層や関数呼び出しチェーンを Copilot が言語認識ナビゲーションで探索できます。Copilot Chat のツールアイコンから有効化します。ツール呼び出し対応モデルで最も効果的です。

## デバッガーエージェント：実際のランタイム動作に対して修正を検証

GitHub または Azure DevOps の issue（または自然言語での説明）から開始し、Debugger モードに切り替えると、エージェントは：

1. 最小限の再現手順を作成
2. 失敗の仮説を生成
3. トレースポイントと条件付きブレークポイントでアプリを計測
4. 実際のデバッグセッションを実行
5. ライブテレメトリを分析
6. 正確な修正を提案

プロセス全体を通じてループに留まれます — インタラクティブで、完全自律ではありません。

## IntelliSense 優先度の修正

IntelliSense リストがアクティブな間、VS は Copilot の補完を抑制するようになりました。一度に 1 つの提案のみ。頻繁な摩擦ポイントであり、デフォルトで有効になりました。

完全なリリースノートとダウンロードは [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) で。
