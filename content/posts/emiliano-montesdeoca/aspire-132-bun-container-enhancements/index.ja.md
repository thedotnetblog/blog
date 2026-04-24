---
title: "Aspire 13.2: Bun サポート、コンテナ改善、デバッグの摩擦軽減"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2はViteアプリへのBunサポートをファーストクラスで追加し、Yarnの信頼性を修正し、ローカル開発の動作をより予測可能にするコンテナ改善を提供します。"
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*この投稿は自動翻訳されています。オリジナル版は[こちら](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/)をクリックしてください。*

.NETバックエンドとJavaScriptフロントエンドをAspireで構築しているなら、13.2は静かにあなたの一日を良くする種類のアップデートです。

## Bunがファーストクラスになりました

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

チームがすでにBunを使用している場合、Aspireはもはや逆流を強いません。

## Yarnの信頼性向上

`withYarn()`と`addViteApp()`での謎のエラーが減少します。

## コンテナの改善

`ImagePullPolicy.Never`でレジストリに行かずにローカルイメージを使用。PostgreSQL 18+のデータボリュームが正しく動作するようになりました。

## デバッグの改善

コアタイプへの`DebuggerDisplayAttribute`、`WaitFor`の改善されたエラーメッセージ、適切なタイミングで発火する`BeforeResourceStartedEvent`。

オリジナルポスト（David Pine著）: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/)。
