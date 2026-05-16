---
title: "Agentic Platform Engineering で移行の繰り返し作業をなくす"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape が実際の AWS Terraform デプロイメントを Azure Bicep に移行する過程を紹介します — 1:1 の構文変換ではなく、デプロイメントの意図を抽出してアーキテクチャを再マッピングします。"
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — Git-Ape（git アジェンティック・プラットフォーム・エンジニアリングツール）が実際の AWS Terraform リポジトリを Azure に移行するウォークスルーで、行単位の変換ではなくデプロイメントの意図抽出に焦点を当てています。

## 入力: contoso-migration

ソースは、AWS 上に Next.js アプリをデプロイする実際の Terraform プロジェクト（`contoso-migration`）です — コンピュートに EC2、ロードバランシングに ALB、アーティファクトに S3、アイデンティティに IAM キー。コスト: 月額約 34 ドル。目標は Azure で同じインフラを再現することではなく、デプロイメントが実際に何をしようとしているのかを把握し、Azure ネイティブサービス上でそれを再構築することです。

## ステップ 1: 検証と認証

Git-Ape は、何かに触れる前にすべての必要な CLI ツール — `az`、`aws`、`gh`、`jq`、`git` — を検証し、アクティブな認証セッションを確認することから始めます。部分的な実行はありません。

## ステップ 2: 意図の抽出

エージェントは GitHub API を通じてソースリポジトリ全体を読み込み、デプロイメントの意図を抽出します: ランタイム (Node.js)、コンピュートタイプ、イングレスパターン、アーティファクト処理、アイデンティティモデル、ネットワーキング、そしてモニタリング。これが重要なステップです — Terraform のキーワードではなく、デプロイメントが何をするかのセマンティックモデルを構築しています。

## ステップ 3: サービスマッピング

AWS サービスが Azure の同等物にマッピングされます:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → App Service 組み込みロードバランシング
- IAM ロール/キー → Managed Identity
- Terraform → Bicep + GitHub Actions

## ステップ 4: 批評エージェント

出力を生成する前に、批評エージェントが実行され、2 つのブロッキング問題を検出します:

1. **起動時ビルドのアンチパターン** — 元の Terraform は EC2 の起動時に `npm install && npm run build` を実行していました。修正: CI でビルドし、準備済みアーティファクトをデプロイする。
2. **不要な Blob Storage** — S3 は適切な CI/CD で排除できるアーティファクトステージングに使用されていました。批評エージェントがそれを完全に削除しました。

## ステップ 5: 生成された出力

結果は元の 200 行以上の Terraform の代わりに約 80 行の Bicep です。エージェントは `infra/main.bicep` と `.github/workflows/deploy.yml` を含む新しい GitHub リポジトリを作成し、すべての AWS 固有ファイルを削除しました。

## セキュリティ体制の比較

移行により、セキュリティも大幅に改善されました:

| AWS オリジナル | Azure 出力 |
|---|---|
| HTTP のみ | HTTPS のみ、TLS 1.2 |
| SSH が 0.0.0.0/0 に開放 | SSH 露出なし |
| IAM アクセスキー | OIDC + Managed Identity |
| モニタリングなし | Application Insights |

コスト: 元の 34 ドル/月に対して約 13 ドル/月。

## 構文コンバーターとの違い

批評エージェントのステップが、これを機械的な変換と区別するものです。AWS では機能するが Azure では誤りとなるパターンを検出し、それを複製する代わりに修正しました。出力は「Azure 構文の AWS」ではなく、同じ目標をよりクリーンに達成する Azure ネイティブのデプロイメントです。

完全なエージェントトレースと生成されたファイルについては、[完全なウォークスルー](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/)をご覧ください。
