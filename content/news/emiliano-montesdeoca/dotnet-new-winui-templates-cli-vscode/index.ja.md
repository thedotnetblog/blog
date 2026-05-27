---
title: "dotnet new WinUI: Visual Studio なしで Windows アプリを作成"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI プロジェクトテンプレートが dotnet new で使えるようになりました — 空のアプリ、NavigationView パターンなど。VS Code 対応、Visual Studio 不要、Fluent Design のデフォルト設定が組み込まれています。"
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI 開発にはかつて Visual Studio が必要でした。それが変わりつつあります: Microsoft が `dotnet new` で動作する WinUI 向けのオープンソースのプロジェクトテンプレートとアイテムテンプレートを公開し、Windows アプリ開発を標準的な CLI ワークフローに組み込んでいます。

## 3 つのコマンドで始める

```shell
# テンプレートをインストール
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# NavigationView アプリを作成
dotnet new winui-navview -n MyApp

# 実行
cd MyApp
dotnet run
```

Visual Studio 不要、手動のプロジェクト設定も不要。アプリは `dotnet run` で実行できます。

## 含まれているもの

**空のテンプレート** (`dotnet new winui`) — Fluent タイトルバーがすでに設定されたモダンな出発点。`.ico` アセット付きの更新されたデフォルトアプリアイコン、適切なライト/ダークモードのデフォルト設定を含みます。自分で基本設定をしなければならなかった古い空のテンプレートより優れています。

**NavigationView テンプレート** (`dotnet new winui-navview`) — マスター-詳細ナビゲーションパターン。NavigationView、モダンなタイトルバー、マルチページナビゲーション構造が完全に設定されています。ナビゲーションベースのアプリに対する標準的な Windows アプリシルエットに従っています。サイドナビゲーションのあるものを作る場合はここから始めましょう。

両テンプレートは [Windows アプリシルエット](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — レイアウト、ナビゲーション、視覚構造のためのモダンな Fluent Design パターン — にすぐに従います。

## Visual Studio 以外の開発者にとって重要な理由

VS Code、Rider、またはコマンドラインツールを使用している WinUI 開発者は不遇に扱われてきました。既存の Visual Studio テンプレートは VS 外では使えず、プロジェクト構造を手動で再作成し、基本を設定し直す必要がありました。

これらのテンプレートはオープンソースです ([WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407) を参照)。[コミュニティのフィードバック](https://github.com/microsoft/microsoft-ui-xaml/issues/10388)から開発され、今すぐ利用可能です。Visual Studio サポートも進行中 — これらの同じテンプレートはいずれそちらでも動作するようになります。

WinUI プロジェクトのセットアップをスクリプト化したい、CI に組み込みたい、または Visual Studio 以外のエディタを使いたいチームにとって、これは意味のある改善です。

元の記事: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
