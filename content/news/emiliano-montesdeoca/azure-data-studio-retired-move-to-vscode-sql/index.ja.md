---
title: "Azure Data Studio は廃止されました：Azure SQL ワークフローを VS Code に移行する"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio は 2025 年 2 月 6 日に廃止され、サポートは 2026 年 2 月 28 日に終了します。MSSQL 拡張機能を使用した VS Code への完全な移行パスを紹介します。"
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[Azure Data Studio は 2025 年 2 月 6 日に廃止されました](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)。サポートは 2026 年 2 月 28 日に終了します。推奨される代替ツールは MSSQL 拡張機能を備えた VS Code です。

## インストールするもの

開始するために必要な 3 つのもの：

- **MSSQL 拡張機能** — VS Code Marketplace で「SQL Server (mssql)」を検索
- **SQL Database Projects 拡張機能** — コードとしてのスキーマ、ビルド検証、ガイド付き公開
- **.NET 8 SDK** — ビルドシステムに必要。SDK が見つからないのは初回起動時の最も一般的な問題

## ADS の接続と設定の移行

MSSQL 拡張機能には **ADS Migration Toolkit** が同梱されており、ガイド付きフローで一度きりの移行を処理します。保存された接続、接続グループ、設定、キーバインドがすべて自動的にインポートされます。

## F5 のクセを取り戻す

ADS ユーザーはクエリ実行に F5 を使用します。**MSSQL Database Management Keymap** 拡張機能をインストールすると、F5 を含む ADS スタイルのキーバインドが復元されます。

## SQL Database Projects：コードとしてのスキーマ

プロジェクトを右クリック → **公開** → ターゲットを設定 → 生成された T-SQL スクリプトを確認 → デプロイ。デプロイ前のスクリプトプレビューが主要な安全機能です。アイテムテンプレートはテーブル、ストアドプロシージャ、ビューのスタブを生成します。SSDT と同じワークフローです。

よくある問題：`.sqlproj` ファイルの**ターゲットプラットフォームの不一致**は、プロジェクトが別の SQL Server バージョン用に作成された場合にビルドエラーを引き起こします。

## Schema Compare と Schema Designer

拡張機能には **Schema Compare**（プロジェクトとデプロイ済みデータベースの差分）と **Schema Designer**（DDL を手書きせずに視覚的にスキーマを編集）も含まれています。

## Microsoft Fabric 開発者向け

セットアップは同一ですが、VS Code で開く前に **Fabric ポータル**からデータベースを Git に接続することから始めてください。Microsoft には専用ガイドがあります：*Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*。

## まとめ

移行は手動での再構築ではなく、一度きりのガイド付きフローです。3 つのツールをインストールし、ADS Migration Toolkit を実行し、キーバインドを復元すれば、10 分以内に通常の作業に戻れます。

ステップバイステップのスクリーンショットと Fabric 固有のウォークスルーについては、[完全な記事](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)をご覧ください。
