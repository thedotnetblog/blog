---
title: "Windows App Dev CLI v0.3: ターミナルからF5デバッグとエージェント向けUIオートメーション"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3では、ターミナルからデバッグ起動できるwinapp run、UIオートメーション機能のwinapp ui、そしてパッケージアプリでdotnet runを使えるNuGetパッケージが追加されました。"
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をクリックしてください。*

Visual StudioのF5体験は素晴らしいです。しかし、パッケージ化されたWindowsアプリを起動してデバッグするためだけにVSを開くのは、CIパイプライン、自動化ワークフロー、またはAIエージェントがテストを実行しているときには過剰です。

Windows App Development CLI v0.3が[リリースされ](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)、2つの主要機能でこれに直接対応します：`winapp run`と`winapp ui`です。

## winapp run: どこからでもF5

`winapp run`はアンパッケージのアプリフォルダーとマニフェストを受け取り、VSがデバッグ起動時に行うすべてを実行します：ルーズパッケージを登録し、アプリを起動し、再デプロイ間で`LocalState`を保持します。

```bash
# アプリをビルドし、パッケージアプリとして実行
winapp run ./bin/Debug
```

WinUI、WPF、WinForms、コンソール、Avaloniaなどで動作します。各モードは開発者と自動化ワークフローの両方を想定しています：

- **`--detach`**: 起動後すぐにターミナルに制御を返します。CI/自動化に最適です。
- **`--unregister-on-exit`**: アプリ終了時に登録済みパッケージを削除します。
- **`--debug-output`**: `OutputDebugString`メッセージと例外をリアルタイムでキャプチャします。

## 新しいNuGetパッケージ: パッケージアプリ向けdotnet run

.NET開発者向けに新しいNuGetパッケージが登場しました：`Microsoft.Windows.SDK.BuildTools.WinApp`。インストール後は、`dotnet run`がインナーループ全体を処理します：ビルド、ルーズレイアウトパッケージの準備、Windowsへの登録、起動 — すべて1ステップで。

```bash
winapp init
# または
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: コマンドラインからUIオートメーション

エージェント型シナリオを切り開くのがこの機能です。`winapp ui`はターミナルから、実行中のあらゆるWindowsアプリ（WPF、WinForms、Win32、Electron、WinUI3）への完全なUIオートメーションアクセスを提供します。

できること：

- すべてのトップレベルウィンドウを一覧表示
- ウィンドウの完全なUIオートメーションツリーをナビゲート
- 名前、タイプ、オートメーションIDで要素を検索
- クリック、呼び出し、値の設定
- スクリーンショットの取得
- 要素の表示を待機 — テスト同期に最適

`winapp ui`と`winapp run`を組み合わせると、ターミナルから完全なビルド→起動→検証ワークフローが実現します。エージェントがアプリを実行し、UIの状態を検査し、プログラムで操作して結果を検証できます。

## その他の新機能

- **`winapp unregister`**: テスト終了後にサイドロードされたパッケージを削除します。
- **`winapp manifest add-alias`**: ターミナルからアプリ名で起動できるエイリアスを追加します。
- **タブ補完**: 1つのコマンドでPowerShell補完を設定します。

## インストール方法

```bash
winget install Microsoft.WinAppCli
# または
npm install -g @microsoft/winappcli
```

CLIはパブリックプレビュー中です。完全なドキュメントは[GitHubリポジトリ](https://github.com/microsoft/WinAppCli)を、すべての詳細は[元のアナウンス](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)をご覧ください。
