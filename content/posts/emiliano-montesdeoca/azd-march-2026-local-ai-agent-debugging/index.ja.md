---
title: "azdでAIエージェントをローカル実行・デバッグ可能に — 2026年3月の変更点まとめ"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLIが2026年3月に7つのリリースを公開。ハイライト：AIエージェントのローカル実行＆デバッグループ、GitHub Copilotのプロジェクトセットアップ統合、Container App Jobsサポート。"
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *この記事は自動翻訳されました。オリジナル版は[こちら]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}})をご覧ください。*

1ヶ月で7つのリリース。これがAzure Developer CLI（`azd`）チームが2026年3月に出荷したもので、メイン機能は私が待っていたもの：**AIエージェントのローカル実行＆デバッグループ**です。

PC Chanが[完全なまとめを公開](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/)しましたが、内容が多いので、AI搭載アプリを構築する.NET開発者にとって本当に重要なことにフィルタリングしましょう。

## デプロイなしでAIエージェントを実行・デバッグ

これが一番大きいです。新しい`azure.ai.agents`拡張機能がAIエージェントの適切なインナーループ体験を提供するコマンドを追加します：

- `azd ai agent run` — エージェントをローカルで起動
- `azd ai agent invoke` — メッセージを送信（ローカルまたはデプロイ済み）
- `azd ai agent show` — コンテナのステータスとヘルスを表示
- `azd ai agent monitor` — コンテナログをリアルタイムでストリーミング

以前は、AIエージェントのテストは変更するたびにMicrosoft Foundryへのデプロイを意味しました。今ではローカルで反復し、エージェントの動作をテストし、準備ができたときだけデプロイできます。

## GitHub Copilotがazdプロジェクトをセットアップ

`azd init`に「Set up with GitHub Copilot (Preview)」オプションが追加されました。プロジェクト構造についてのプロンプトに手動で回答する代わりに、Copilotエージェントが設定を生成します。コマンドが失敗した場合、`azd`がAI支援のトラブルシューティングを提供します。

## Container App Jobsとデプロイの改善

- **Container App Jobs**：`azd`が既存の`host: containerapp`設定で`Microsoft.App/jobs`をデプロイ可能に
- **設定可能なデプロイタイムアウト**：`azd deploy`の新しい`--timeout`フラグと`azure.yaml`の`deployTimeout`フィールド
- **リモートビルドフォールバック**：ACRビルドが失敗するとローカルDocker/Podmanビルドに自動フォールバック
- **ローカルプリフライト検証**：デプロイ前にBicepパラメータをローカルで検証

## DXの改善

- **pnpm/yarn自動検出** — JS/TSプロジェクト向け
- **pyproject.tomlサポート** — Pythonパッケージング向け
- **ローカルテンプレートディレクトリ** — `azd init --template`がファイルシステムパスを受け入れ
- **改善されたエラーメッセージ** — `--no-prompt`モード
- **ビルド環境変数** — すべてのフレームワークビルドサブプロセスに注入（.NET、Node.js、Java、Python）

## まとめ

ローカルAIエージェントデバッグループがこのリリースの主役ですが、デプロイ改善とDXポリッシュの積み重ねにより、`azd`はかつてないほど成熟しています。AzureにDotNetアプリをデプロイしているなら — 特にAIエージェント — このアップデートは価値があります。

[完全なリリースノート](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/)で全詳細をご確認ください。
