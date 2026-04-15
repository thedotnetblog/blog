---
title: ".NET 2026年4月サービシング — 今すぐ適用すべきセキュリティパッチ"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "2026年4月のサービシングリリースは、.NET 10、.NET 9、.NET 8、.NET Frameworkにわたる6件のCVEを修正します — リモートコード実行の脆弱性2件を含みます。"
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *この記事は自動翻訳されています。オリジナル版は[こちら]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}})をご覧ください。*

.NETと.NET Frameworkの[2026年4月サービシングアップデート](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/)がリリースされました。今回はすぐに適用したいセキュリティ修正が含まれています。6件のCVEがパッチされ、そのうち2件はリモートコード実行（RCE）の脆弱性です。

## パッチされた内容

簡単なまとめはこちらです：

| CVE | 種類 | 影響範囲 |
|-----|------|----------|
| CVE-2026-26171 | セキュリティ機能のバイパス | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **リモートコード実行** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **リモートコード実行** | .NET 10, 9, 8 |
| CVE-2026-32203 | サービス拒否 | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | サービス拒否 | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | サービス拒否 | .NET Framework 2.0–4.8.1 |

2件のRCE CVE（CVE-2026-32178とCVE-2026-33116）は最も広範囲の.NETバージョンに影響し、優先的に対応すべきです。

## 更新されたバージョン

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

すべて通常のチャネルから入手できます — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0)、MCR上のコンテナイメージ、Linuxパッケージマネージャー。

## 対応すべきこと

プロジェクトとCI/CDパイプラインを最新のパッチバージョンに更新してください。コンテナを使用している場合は、最新のイメージをプルしてください。.NET Frameworkを使用している場合は、対応するパッチについて[.NET Frameworkリリースノート](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes)を確認してください。

.NET 10を本番環境で実行している方（現行リリースです）にとって、10.0.6は必須アップデートです。LTSトラックの.NET 9.0.15や.NET 8.0.26も同様です。2件のRCE脆弱性は後回しにできるものではありません。
