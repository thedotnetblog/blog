---
title: "1日68分もコードを再説明している？解決策があります"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "コンテキストロットは現実です — AIエージェントは30ターン後に迷子になり、毎時間コンパクション税を支払っています。auto-memoryはGitHub Copilot CLIに何千ものトークンを消費せずに外科的な記憶を与えます。"
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*この投稿は自動翻訳されています。オリジナル版は[こちら](https://thedotnetblog.com/posts/emiliano-montesdeoca/auto-memory-stop-re-explaining-code-to-copilot/)をクリックしてください。*

Copilotセッションが`/compact`に達し、エージェントが何をしていたか完全に忘れてしまう瞬間を知っていますか？次の5分間、ファイル構造、失敗したテスト、すでに試した3つのアプローチを再説明します。そしてまた同じことが起きます。

Desi Villanueva が計測しました：**1日68分** — 再オリエンテーションだけに。コードを書くのでも、PRをレビューするのでもなく、AIがすでに知っていたことを再び教えるだけに。

## コンテキストウィンドウの嘘

実際の計算：200Kのうち、MCAツールで65K、インストラクションファイルで10K消費され、**言葉を入力する前に125K**しか残りません。そして60%の容量で壁に当たります。

有効な制限：**45Kトークン** — これが実際の制約です。

## コンパクション税

残酷な部分：**記憶はすでに存在します。** Copilot CLIは`~/.copilot/session-store.db`にすべてのセッションを書き込みます。エージェントはただ読めないだけです。

## auto-memory：リコールレイヤー

```bash
pip install auto-memory
```

~1,900行のPython。依存関係ゼロ。30秒でインストール完了。

grepの洪水の代わりに、**10,000トークンではなく50トークン**で昨日触れたファイルへの外科的アクセスを提供します。

## まとめ

コンテキストロットは本物のアーキテクチャ的制約です。auto-memoryはエージェントに安価で正確なリコールメカニズムを与えることでこれを回避します。

チェックしてみてください：[GitHubのauto-memory](https://github.com/dezgit2025/auto-memory)。オリジナル記事（Desi Villanueva著）：[I Wasted 68 Minutes a Day](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/)。
