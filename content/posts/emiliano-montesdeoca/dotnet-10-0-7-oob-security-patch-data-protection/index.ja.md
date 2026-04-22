---
title: "今すぐパッチを: .NET 10.0.7 OOBセキュリティアップデート (ASP.NET Core Data Protection)"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7はMicrosoft.AspNetCore.DataProtectionのセキュリティ脆弱性を修正するOut-of-Bandリリース — 管理された認証暗号化機がペイロードの誤ったバイトでHMACを計算し、権限昇格につながる可能性がありました。"
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*この投稿は自動翻訳されています。オリジナル版は[こちら](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/)をクリックしてください。*

このアップデートはオプションではありません。アプリケーションが`Microsoft.AspNetCore.DataProtection`を使用している場合、10.0.7に更新する必要があります。

## 何が起きたか

Patch Tuesday `.NET 10.0.6`リリース後、一部のユーザーが復号化の失敗を報告しました。調査中に**CVE-2026-40372**が発見されました：HMAC検証タグが**誤ったバイト**で計算されており、権限昇格につながる可能性がありました。

## 修正方法

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

その後、アプリケーションを**再ビルドして再デプロイ**してください。

Rahul Bhandariによるオリジナルアナウンス: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/)。
