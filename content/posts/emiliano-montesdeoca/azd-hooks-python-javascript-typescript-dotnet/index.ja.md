---
title: "Python、TypeScript、.NETでazdフックを書く：シェルスクリプトとの決別"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLIがPython、JavaScript、TypeScript、.NETでのフック作成をサポート。マイグレーションスクリプトのためだけにBashへ切り替える必要はもうない。"
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})をクリックしてください。*

完全に.NETで書かれたプロジェクトを持ちながら、azdのフックのためにBashスクリプトを書かなければならなかった経験はないだろうか。あの苦痛を知っている人は多いはず。C#でプロジェクト全体を書いているのに、なぜpre-provisioningのステップだけシェル構文に切り替えなければならないのか。

その不満がついに公式に解決された。Azure Developer CLIが[フックのマルチ言語サポートを発表](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)し、想像通りの素晴らしい機能となっている。

## フックとは

フックは`azd`のライフサイクルの重要なポイントで実行されるスクリプト — プロビジョニング前、デプロイ後など。`azure.yaml`で定義され、CLIを変更せずにカスタムロジックを注入できる。

これまではBashとPowerShellのみサポートされていた。今や**Python、JavaScript、TypeScript、.NET**が使えるようになり、`azd`が残りを自動で処理する。

## 検出の仕組み

フックをファイルに向けるだけで、`azd`が拡張子から言語を推論する：

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

追加設定は不要。拡張子が曖昧な場合は`kind: python`（または対応する言語）を明示的に指定できる。

## 言語別の重要な詳細

### Python

スクリプトと同じディレクトリ（または親ディレクトリ）に`requirements.txt`や`pyproject.toml`を置くだけ。`azd`が自動的に仮想環境を作成し、依存関係をインストールしてスクリプトを実行する。

### JavaScriptとTypeScript

同じパターン — スクリプトの近くに`package.json`を置くと`azd`がまず`npm install`を実行する。TypeScriptの場合は`npx tsx`を使用し、コンパイルステップも`tsconfig.json`も不要。

### .NET

2つのモードが利用可能：

- **プロジェクトモード**：スクリプトの隣に`.csproj`があれば、`azd`が自動的に`dotnet restore`と`dotnet build`を実行。
- **シングルファイルモード**：.NET 10以降では、スタンドアロンの`.cs`ファイルを`dotnet run script.cs`で直接実行可能。プロジェクトファイル不要。

## エグゼキューター固有の設定

各言語はオプションの`config`ブロックをサポート：

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## .NET開発者にとっての重要性

フックはazd基盤のプロジェクトで言語切り替えを強制する最後の場所だった。これで、アプリコード、インフラスクリプト、ライフサイクルフックを含むデプロイパイプライン全体を1つの言語で管理できる。既存の.NETユーティリティをフックで再利用し、共有ライブラリを参照し、シェルスクリプトの保守から解放される。

## まとめ

小さな変更のように見えるが、azdの日常ワークフローから多くの摩擦を取り除く変更の一つ。フックのマルチ言語サポートは今すぐ利用可能 — [公式ポスト](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)で全ドキュメントを確認してほしい。
