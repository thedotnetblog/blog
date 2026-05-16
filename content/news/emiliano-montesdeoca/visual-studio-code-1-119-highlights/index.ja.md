---
title: "VS Code 1.119：エージェントセッションの OpenTelemetry、ブラウザー統合、セキュリティ"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (2026 年 5 月) でエージェントセッションの OpenTelemetry トレーシング、ブラウザータブ共有、信頼とセキュリティの改善、1.119.1 セキュリティパッチが追加。"
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) は 2026 年 5 月 6 日にリリースされました（その後すぐに 1.119.1 セキュリティパッチも公開）。このリリースはエージェントの可観測性、ブラウザーとの連携、割り込みの削減に重点を置いています。

## エージェントセッションの OpenTelemetry トレーシング

本番環境でエージェントを実行している方や、エージェントワークフローをデバッグしている方にとって注目の機能です。2 つの設定で有効化します：

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

トレースは GenAI セマンティック規約に従います。各エージェントリクエストは `invoke_agent` ルートスパンを生成し、ネストされた子スパン（`chat`、`execute_tool`、`execute_hook`）を持ちます。トークン使用量はリクエストごとに報告されます — キャッシュ読み取りと作成のカウントも含みます。

ローカルエージェント、Copilot CLI バックグラウンドエージェント、Claude エージェントと連携します。OTLP 対応バックエンドでトレースを受信できます — ローカル開発には [Aspire Dashboard スタンドアロン](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone)が便利です。

## エージェントがブラウザータブにアクセス可能に

エージェントは統合ブラウザーのタブへのアクセスを要求できるようになりました — ただし自動ではありません。コンテキストピッカー、ドラッグアンドドロップ、または提案されたコンテキストを通じてタブを明示的に共有する必要があります。ブラウザーにアクセスを取り消すための共有ボタンがあります。エージェントが既に開いている（共有されていない）タブと同じドメインの新しいタブを開こうとすると、VS Code は既存のタブを再利用するよう促します。

## トークン使用量の最適化

実験的な軽量モデルがエージェントのタスクリスト管理を担うようになり、この管理作業を高コストなメインモデルから切り離します。フルの推論能力を必要としないタスクのトークン消費を削減します。

## 信頼とセキュリティ

割り込みの削減：VS Code 1.119 はエージェントによるネットワークアクセス要求と一時フォルダーへの書き込みのプロンプトを削減します。1.119.1 パッチは特定のセキュリティ問題に対処しています — まだ更新していない場合は更新することをお勧めします。

## Markdown プレビューへのクイックスワップ

小さいながら便利：ナビゲートせずに現在のエディターを Markdown プレビューに素早く切り替えられるようになりました。

## VS Code Agents (Insiders プレビュー)

再設計されたエージェントセッション UI — 新しいリポジトリピッカー（ローカル/リポジトリ/リモート）、サブセッションの改善、Web とモバイルの改善、進捗アニメーション — は Insiders の [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents) で利用可能です。

完全な変更履歴：[code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119)。
