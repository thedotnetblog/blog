---
title: "azd + GitHub Copilot: AIによるプロジェクトセットアップとスマートなエラー解決"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLIがGitHub Copilotと統合され、プロジェクトのスキャフォールディングとデプロイエラーの解決をターミナルから直接できるようになりました。"
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *この記事は自動翻訳されました。英語の原文は[こちら]({{< ref "index.md" >}})からご覧いただけます。*

既存のアプリをAzureにデプロイしようとして、空の `azure.yaml` を眺めながら「Express APIにはContainer AppsとApp Serviceのどちらを使えばいいんだっけ？」と頭を抱えた経験はありませんか？そんな場面が、これからは格段に短くなります。

Azure Developer CLI（`azd`）がGitHub Copilotと2つの形で統合されました。`azd init` 実行時のAIによるプロジェクトスキャフォールディングと、デプロイ失敗時のインテリジェントなエラートラブルシューティングです。どちらの機能もターミナル内で完結します。

## azd init でのCopilotセットアップ

`azd init` を実行すると、「Set up with GitHub Copilot (Preview)」という選択肢が表示されます。選択すると、Copilotがコードベースを分析し、実際のコードに基づいて `azure.yaml`、インフラテンプレート、Bicepモジュールを生成します。

```
azd init
# 選択: "Set up with GitHub Copilot (Preview)"
```

必要なもの：

- **azd 1.23.11以降** — `azd version` で確認、`azd update` で更新
- **有効なGitHub Copilotサブスクリプション**（Individual、Business、またはEnterprise）
- **GitHub CLI（`gh`）** — 必要に応じてログインを求められます

この機能の優れた点は双方向に機能することです。ゼロから構築する場合はAzureサービスの適切なセットアップを支援し、既存のアプリをデプロイしたい場合はコードを分析して設定を生成します。構造を変更する必要はありません。

### 実際に何をするのか

Node.js ExpressのAPIにPostgreSQLの依存関係がある場合を例にしましょう。Container AppsかApp Serviceかを手動で決め、BicepをゼロからT書く代わりに、Copilotはスタックを検出して以下を生成します：

- 適切な `language`、`host`、`build` 設定を持つ `azure.yaml`
- Azure Container Apps用のBicepモジュール
- Azure Database for PostgreSQL用のBicepモジュール

変更前に事前チェックも実行されます。gitの作業ディレクトリがクリーンかどうか確認し、MCPサーバーツールへの同意を事前に求めます。何が変わるか把握した上でのみ処理が進みます。

## Copilotによるエラートラブルシューティング

デプロイエラーは避けられません。パラメーターの欠落、権限の問題、SKUの可用性問題など。エラーメッセージが修正方法を教えてくれることはほとんどありません。

Copilotなしの場合のループ：エラーをコピー → ドキュメントを検索 → 関係ないStack Overflowの回答を3つ読む → `az` CLIコマンドを実行 → 再試行して祈る。`azd` にCopilotが統合されると、このループが消えます。`azd` コマンドが失敗すると、即座に4つの選択肢が提示されます：

- **Explain** — 何が起きたかをわかりやすく説明
- **Guidance** — 修正のステップバイステップの手順
- **Diagnose and Guide** — 完全な分析 + Copilotが修正を適用（承認後）+ 再試行オプション
- **Skip** — 自分で対処

重要な点：Copilotはすでにプロジェクト、失敗したコマンド、エラー出力のコンテキストを持っています。提案は *あなたの状況* に特化したものです。

### デフォルト動作の設定

常に同じオプションを選ぶなら、インタラクティブなプロンプトをスキップできます：

```
azd config set copilot.errorHandling.category troubleshoot
```

値：`explain`、`guidance`、`troubleshoot`、`fix`、`skip`。自動修正と再試行も有効にできます：

```
azd config set copilot.errorHandling.fix allow
```

いつでもインタラクティブモードに戻せます：

```
azd config unset copilot.errorHandling.category
```

## まとめ

`azd update` で最新バージョンに更新し、次のプロジェクトで `azd init` を試してみてください。本当に価値のあるCopilot統合です。

[元の発表はこちら](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/)をご覧ください。
