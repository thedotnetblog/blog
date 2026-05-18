---
title: "WinApp VS Code拡張機能：エディターを離れずにWindowsアプリを実行、デバッグ、パッケージ化"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "WinApp VS Code拡張機能は、Windows App Development CLIの全機能をVS Codeに直接統合します。Visual Studioなしで、WPF、WinUI、.NET、C++アプリをパッケージIDで実行、デバッグ、パッケージ化、署名できます。"
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})からご覧いただけます。*

VS CodeでWindowsアプリを開発しようとしたことがある人なら、あの瞬間を知っているはずです。好みのエディターでコードを書いていると、突然Windows APIのためにパッケージIDが必要になる。あるいはMSIXを作成したり、パッケージを署名したりする必要が出てくる。気づけばVisual Studioを開いていたり、夜11時に「msix packaging without visual studio」をGoogle検索していたりする。

そのような摩擦はもうなくなりました。[WinApp VS Code拡張機能](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp)がパブリックプレビューになりました。これは[Windows App Development CLI](https://github.com/microsoft/WinAppCli)の全機能がVS Codeに直接統合されたものです。別途インストール不要、Visual Studio不要。

## F5でパッケージID

Windows API — 通知、バックグラウンドタスク、オンデバイスAI機能、シェアターゲット — の多くは、アプリが**パッケージID**を持っている必要があります。これがないと、それらのAPIは動作しません。

従来、パッケージIDを取得するには完全なMSIXインストーラーを作成するか、Visual Studioから実行する必要がありました。WinApp拡張機能は、カスタム`winapp`デバッグタイプによってこれを完全に変えます。

`launch.json`にこれを追加します：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

F5を押すだけ。拡張機能がビルド出力とマニフェストを見つけ、`winapp run`でアプリにパッケージIDを付与し、デバッガーをアタッチします。.NETアプリは`coreclr`（C# Dev Kit必要）、C/C++は`cppvsdbg`、Node/Electronは組み込みデバッガーを使用します。

`preLaunchTask`を設定すれば、F5を押す前に自動的にビルドされます。Visual Studioと同じビルド&ランチフローがVS Codeで実現できます。

## コマンドパレットですべてを操作

`Ctrl+Shift+P`を開いて`WinApp`と入力すれば、完全なツールキットにアクセスできます：

- **Initialize Project** — Windows SDKおよび/またはWindows App SDKでプロジェクトを設定
- **Run Application** — パッケージIDを持つルースレイアウトパッケージアプリとして起動
- **Create MSIX Package** — 証明書とランタイムオプションでアプリをパッケージ化
- **Update Manifest Assets** — 単一のソース画像から必要なすべてのアプリアイコンを自動生成
- **Generate / Install Certificate** — 開発証明書の管理
- **Sign Package** — MSIXまたは実行可能ファイルに署名
- **Run SDK Tool** — `makeappx`、`signtool`、`mt`、`makepri`を直接実行

WinApp CLIのインストールも不要です。拡張機能にバンドルされています。

## 多くのフレームワークに対応

.NET WPF/WinUI専用のツールではありません。拡張機能は以下と連携します：

- **.NET**: WPF、WinForms、Console、WinUI 3
- **C/C++**: Win32、CMake、MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

この広さは意図的なものです。VS Codeはウェブやクロスプラットフォームの開発者が集まる場所です。Windowsパッケージングが必要なTauriやElectronアプリを開発している場合も、Visual Studioを採用することなくこの拡張機能でカバーできます。

## .NET開発者にとっての重要性

私はVS Codeで多くの作業をします。Markdownを書いたり、設定を管理したり、小さなプロジェクトを編集したり、ターミナルを実行したりする場所です。しかし.NET Windowsデスクトップ開発においては、パッケージング関連の作業が必要な瞬間、Visual Studioが唯一の選択肢でした。

この拡張機能がそのギャップを埋めます。VS Codeを離れることなく、.NET Windowsデスクトップ開発の完全なサイクル — 編集、ビルド、パッケージIDで実行、デバッグ、パッケージ化、署名 — が完結します。これは本物の生産性向上です。

## はじめに

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

または拡張機能ビュー（`Ctrl+Shift+X`）で**WinApp**を検索します。

要件：
- Windows 10以降
- VS Code 1.109.0以降
- アプリの言語に対応したデバッガー拡張機能

詳細は[Chiara Mooneyのフルアナウンス](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/)をご覧ください。

## まとめ

WinApp VS Code拡張機能は、VS Codeを使いながらパッケージング作業のためにVisual Studioに切り替えていた.NET Windowsデスクトップ開発者にとって待望の追加機能です。F5でパッケージID、コマンドパレットからMSIXパッケージ化、証明書管理の統合 — 正しい機能セットが揃っています。

次のWPFまたはWinUIプロジェクトで試してみてください。これまで回避してきた摩擦が大幅に軽減されます。
