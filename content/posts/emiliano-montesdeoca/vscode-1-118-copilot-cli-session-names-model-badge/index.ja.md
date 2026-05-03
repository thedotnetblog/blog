---
title: "VS Code 1.118: Copilot CLI にセッション名、モデルバッジ、TypeScript 7.0 ナイトリーオプトイン"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Visual Studio Code 1.118 は Copilot CLI の改善に焦点を当てたリリース — セッション名、モデルバッジ、自動モデル選択、TypeScript 7.0 ナイトリーのオプトイン。"
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
  - TypeScript
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をご覧ください。*

[Visual Studio Code 1.118](https://code.visualstudio.com/updates/v1_118) は小さめで焦点を絞ったリリース — 主に Copilot CLI の改良 — ですが、いくつか注目すべき点があります。

## Copilot CLI: セッションに実際の名前が付く

Copilot CLI SDK のセッションタイトル API がセッション名の情報源として使用されるようになりました。自動生成されたラベルではなく、SDK の実際の名前が表示されます。

## キーボードショートカットで素早くセッション切り替え

Agents アプリに `Ctrl+1`、`Ctrl+2` などのセッション切り替えキーが割り当てられました。複数の Copilot CLI セッションを並行して実行している場合、マウスクリックが大幅に減ります。

## チャットにモデルバッジ表示

チャットパネルの Copilot CLI レスポンスにモデルバッジが表示されるようになりました — どのモデルが各リクエストを処理したかひと目でわかります。

## Copilot CLI に自動モデル選択

自動モデル選択機能 — 以前は Copilot の他の部分で使用可能だった — が Copilot CLI エージェントでも機能するようになりました。

## TypeScript 7.0 ナイトリーのオプトイン

VS Code の設定から TypeScript 7.0 ナイトリーをテストするオプトインが可能になりました。TypeScript 7.0 は大規模リリースです（[ベータ版が数日前にリリース](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)）。

[完全なリリースノート](https://code.visualstudio.com/updates/v1_118)をご確認ください。
