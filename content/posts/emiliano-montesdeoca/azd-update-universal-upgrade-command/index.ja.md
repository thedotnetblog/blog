---
title: "azd update — すべてのパッケージマネージャーを統べる一つのコマンド"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLIに、インストール方法を問わず動作するユニバーサルなアップデートコマンドが追加されました — winget、Homebrew、Chocolatey、インストールスクリプトのいずれでも対応。"
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *この記事は自動翻訳されています。オリジナル版は[こちら]({{< ref "azd-update-universal-upgrade-command.md" >}})をご覧ください。*

数週間ごとに表示される「azdの新しいバージョンが利用可能です」というメッセージ、知っていますか？ `azd`をwingetでインストールしたのか、Homebrewなのか、それとも半年前に実行したcurlスクリプトなのか思い出せなくて、つい無視してしまうあのメッセージです。ついに解決しました。

Microsoftが[`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/)をリリースしました — 元々のインストール方法に関係なく、Azure Developer CLIを最新バージョンにアップデートできる単一のコマンドです。Windows、macOS、Linux — 関係ありません。コマンド一つで完了です。

## 仕組み

```bash
azd update
```

これだけです。新機能に早くアクセスしたい場合は、デイリーのInsidersビルドに切り替えることもできます：

```bash
azd update --channel daily
azd update --channel stable
```

このコマンドは現在のインストール方法を自動検出し、裏側で適切なアップデートメカニズムを使用します。もう「この PC では winget を使ったっけ、choco だったっけ？」と悩む必要はありません。

## 一つだけ注意点

`azd update`はバージョン1.23.x以降で利用可能です。それより古いバージョンを使っている場合は、元のインストール方法で最後の手動アップデートを行う必要があります。その後は`azd update`がすべてのアップデートを引き受けてくれます。

`azd version`で現在のバージョンを確認してください。新規インストールが必要な場合は、[インストールドキュメント](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)を参照してください。

## なぜ重要なのか

これは小さなQOL改善ですが、AIエージェントやAspireアプリをAzureにデプロイするために`azd`を毎日使っている私たちにとって、最新の状態を保つことは「そのバグは最新バージョンで修正済みでした」という場面を減らすことを意味します。考えることが一つ減るのです。

詳細は[公式アナウンス](https://devblogs.microsoft.com/azure-sdk/azd-update/)とJon Gallantの[詳しい解説](https://blog.jongallant.com/2026/04/azd-update)をご覧ください。
