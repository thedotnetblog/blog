---
title: "Azure MCP Server が .mcpb になった — ランタイムなしでインストール"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server が MCP Bundle (.mcpb) として利用可能になりました — ダウンロードして Claude Desktop にドラッグするだけ。Node.js、Python、.NET 不要。"
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をご覧ください。*

MCP サーバーのセットアップで面倒だったこと、ご存知ですか？ランタイムが必要でした。npm 版には Node.js、pip/uvx には Python、dotnet 版には .NET SDK。

[Azure MCP Server がその問題を解決しました](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)。`.mcpb` — MCP Bundle — として利用可能になり、セットアップはドラッグ＆ドロップです。

## MCP Bundle とは？

VS Code 拡張機能（`.vsix`）やブラウザ拡張機能（`.crx`）のようなものですが、MCP サーバー用です。`.mcpb` ファイルはサーバーバイナリとすべての依存関係を含む自己完結型の ZIP アーカイブです。

## インストール方法

**1. プラットフォーム用バンドルをダウンロード**

[GitHub Releases ページ](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) で、OS とアーキテクチャに合った `.mcpb` ファイルをダウンロードします。

**2. Claude Desktop にインストール**

最も簡単な方法：拡張機能の設定ページ（`☰ → ファイル → 設定 → 拡張機能`）を開きながら、`.mcpb` ファイルを Claude Desktop ウィンドウにドラッグ＆ドロップします。サーバーの詳細を確認し、インストールをクリックして確認します。

**3. Azure で認証**

```bash
az login
```

以上です。Azure MCP Server は既存の Azure 認証情報を使用します。

## できること

AI クライアントから直接 100 以上の Azure サービスツールにアクセス：
- Cosmos DB、Storage、Key Vault、App Service、Foundry のクエリと管理
- 任意のタスクの `az` CLI コマンド生成
- Bicep・Terraform テンプレートの作成

## はじめるには

- **ダウンロード**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **リポジトリ**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **ドキュメント**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

[完全な記事](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)もご確認ください。
