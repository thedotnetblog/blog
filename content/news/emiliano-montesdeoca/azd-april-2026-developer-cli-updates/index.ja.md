---
title: "Azure Developer CLI (azd) 2026年4月アップデート"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd は2026年4月に5つのリリースを公開しました。Python、JavaScript、TypeScript、.NET に対応したマルチ言語フックサポート、azd update のパブリックプレビュー、AI クォータのプリフライトチェックなどが含まれます。"
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[Azure Developer CLI (azd) は2026年4月に5つのリリースを公開しました](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/)（1.23.14 から 1.24.2 まで）。最大のテーマは、Bash と PowerShell だけでなく Python、JavaScript、TypeScript、.NET でも実行できるようになったフックです。

## azure.yaml のマルチ言語フック

フックはシェルスクリプトに加えて `.py`、`.js`、`.ts`、`.cs` ファイルを指定できるようになりました。各言語で依存関係の自動解決が行われます。

- **Python** — `requirements.txt` または `pyproject.toml` を検出し、virtualenv を作成して実行前に依存関係をインストールします。env 名は `virtualEnvName` で設定します。
- **JavaScript / TypeScript** — `package.json` を検出して `npm install` を自動実行します。TypeScript はコンパイル不要で `npx tsx` 経由で実行されます。パッケージマネージャは `packageManager` 設定ブロックで選択できます。
- **.NET** — `.cs` ファイルを `dotnet run` で実行します。.NET 10+ ではシングルファイルスクリプトをサポートします。ターゲットフレームワークは `configuration/framework` ブロックで設定します。

これにより、これらの言語ですでに作業しているチームは、プロビジョニングのライフサイクルイベントを接続するためだけに別の Bash または PowerShell フックを管理する必要がなくなります。

## azd update がパブリックプレビューに

`azd update` がすべてのプラットフォームでパブリックプレビューに移行しました。azd が最初にどのようにインストールされたかに関わらず、単一のコマンドでアップデートを処理できます。Homebrew、WinGet、MSI のパスを個別に追跡する必要はありません。

## AZD_NON_INTERACTIVE による非インタラクティブモード

`AZD_NON_INTERACTIVE=true` を設定する（または `--non-interactive` / `--no-prompt` を使用する）と、必要な入力を自動的に解決できない場合に CI/CD パイプラインで一貫した決定論的な失敗が発生するようになりました。以前はコマンドごとに動作が一致していませんでした。

## AI モデルクォータのプリフライトチェック

`azd provision` は AI モデルリソースのプロビジョニングを試みる前に Azure Cognitive Services のクォータを検証します。クォータ制限により失敗するデプロイは、プロビジョニングの途中ではなく、プロセスの早い段階でエラーが表示されるようになりました。

## Copilot トラブルシューティングの「このエラーを修正する」

azd の Copilot トラブルシューティング統合が、提案された修正を直接適用する機能を獲得しました。説明するだけでなく、エージェントが修正可能な問題を特定した場合、その場で変更を加えることができます。

## カスタムプロビジョニングプロバイダーと Key Vault シークレットリゾルバー

拡張機能の作成者は `WithProvisioningProvider()` を使用して代替インフラストラクチャバックエンドを登録できるようになりました。また、azd は設定を拡張機能に渡す前に `@Microsoft.KeyVault(...)` 参照を自動的に解決するため、カスタムプロバイダーでの手動シークレット解決が不要になります。

## テンプレートと watch モードの除外

2 つの新しい ignore ファイルでファイル処理をより細かく制御できます。
- **`.azdignore`** — コントリビューター専用のファイル（ドキュメント、CI 設定）をテンプレートのコピーから除外し、エンドユーザーがクリーンなプロジェクトスキャフォルドを取得できるようにします。
- **`.azdxignore`** — `azd x watch` 中のリビルドトリガーからディレクトリを除外し、反復開発中のノイズを軽減します。

## 予約名プリフライトと docker.network オプション

azd はプロビジョニング開始前に、予測されるリソース名が Azure の予約語（`MICROSOFT`、`WINDOWS`、または `LOGIN` プレフィックス）を含む場合に警告するようになりました。新しい `docker.network` オプションは `docker build` に `--network` を渡します。これは特定の Docker ネットワークを必要とする企業プロキシ環境で役立ちます。

## セキュリティ修正

Windows MSI パッケージにコード署名検証が追加されました。別の修正で、拡張機能コマンドの境界をまたいで値が漏洩する可能性のある環境変数リークが解消されました。

---

忙しい月でした。特にマルチ言語フックサポートは、主に Bash で作業しないチームにとっての真の摩擦点を解消します。5 つのリリースすべての完全な変更履歴については[完全なリリースノート](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/)を参照してください。
