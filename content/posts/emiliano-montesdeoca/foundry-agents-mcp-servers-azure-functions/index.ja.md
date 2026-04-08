---
title: "Azure FunctionsのMCPサーバーをFoundryエージェントに接続する方法"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "MCPサーバーを一度構築し、Azure Functionsにデプロイして、適切な認証付きでMicrosoft Foundryエージェントに接続。ツールはどこでも動作します — VS Code、Cursor、そして今やエンタープライズAIエージェントでも。"
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}})をご覧ください。*

MCPエコシステムで私が大好きなことがあります：サーバーを一度構築すれば、どこでも動作するということです。VS Code、Visual Studio、Cursor、ChatGPT — すべてのMCPクライアントがあなたのツールを発見して使用できます。そして今、Microsoftはそのリストにもう一つの消費者を追加しています：Foundryエージェントです。

Azure SDKチームのLily Maが、Azure FunctionsにデプロイされたMCPサーバーをMicrosoft Foundryエージェントに接続する[実践ガイドを公開](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/)しました。すでにMCPサーバーをお持ちなら、これは純粋な付加価値です — 再構築は不要です。

## この組み合わせが理にかなう理由

Azure Functionsは、MCPサーバーのホスティングにスケーラブルなインフラ、組み込みの認証、サーバーレス課金を提供します。Microsoft Foundryは、推論、計画、行動ができるAIエージェントを提供します。この2つを接続すると、カスタムツール — データベースのクエリ、ビジネスAPIの呼び出し、バリデーションロジックの実行 — がエンタープライズAIエージェントが自律的に発見して使用できる機能になります。

重要なポイント：MCPサーバーはそのままです。Foundryをもう一つの消費者として追加するだけです。VS Codeのセットアップで動作している同じツールが、チームや顧客が対話するAIエージェントを動かすようになります。

## 認証オプション

ここが記事の真価が発揮されるところです。シナリオに応じた4つの認証方法：

| 方法 | ユースケース |
|------|------------|
| **キーベース**（デフォルト） | 開発またはEntra認証なしのサーバー |
| **Microsoft Entra** | マネージドIDによる本番環境 |
| **OAuthアイデンティティパススルー** | 各ユーザーが個別に認証する本番環境 |
| **認証なし** | 開発/テストまたは公開データのみ |

本番環境では、エージェントIDを使用したMicrosoft Entraが推奨パスです。OAuthアイデンティティパススルーは、ユーザーコンテキストが重要な場合に使用します — エージェントがユーザーにサインインを求め、各リクエストがユーザー自身のトークンを運びます。

## セットアップ

大まかな流れ：

1. **MCPサーバーをAzure Functionsにデプロイ** — [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)、Python、TypeScript、Javaのサンプルが利用可能
2. **Function Appで組み込みMCP認証を有効化**
3. **エンドポイントURLを取得** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **FoundryにMCPサーバーをツールとして追加** — ポータルでエージェントに移動し、新しいMCPツールを追加、エンドポイントとクレデンシャルを提供

その後、Agent Builderのプレイグラウンドでツールをトリガーするプロンプトを送信してテストします。

## 私の見解

ここでのコンポーザビリティの話は本当に強力になっています。MCPサーバーを.NET（またはPython、TypeScript、Java）で一度構築し、Azure Functionsにデプロイすれば、すべてのMCP互換クライアントが使用できます — コーディングツール、チャットアプリ、そして今やエンタープライズAIエージェント。実際に機能する「一度書いて、どこでも使う」パターンです。

特に.NET開発者にとって、[Azure Functions MCP拡張機能](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)がこれを簡単にしてくれます。ツールをAzure Functionsとして定義し、デプロイすれば、Azure Functionsが提供するすべてのセキュリティとスケーリングを備えた本番グレードのMCPサーバーが手に入ります。

## まとめ

Azure FunctionsでMCPツールを実行している場合、Foundryエージェントへの接続はクイックウィンです — カスタムツールが適切な認証付きでエンタープライズAI機能になり、サーバー自体のコード変更は不要です。

各認証方法のステップバイステップの手順は[完全ガイド](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/)を、本番セットアップについては[詳細ドキュメント](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry)をご覧ください。
