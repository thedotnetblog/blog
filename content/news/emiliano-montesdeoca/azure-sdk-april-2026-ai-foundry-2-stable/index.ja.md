---
title: "Azure SDK 2026年4月: AI Foundry 2.0と.NET開発者が知るべきこと"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "2026年4月のAzure SDKリリースは、重要な破壊的変更を伴うAzure.AI.Projects 2.0.0安定版、Cosmos DBの重大なセキュリティ修正、および.NET向けの新しいProvisioningライブラリを提供します。"
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*この投稿は自動翻訳されています。オリジナル版は[こちら](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-sdk-april-2026-ai-foundry-2-stable/)をクリックしてください。*

月次SDKリリースはよく見落とされがちですが、今回は特に注意すべき点があります。

## Azure.AI.Projects 2.0.0 — 意味のある破壊的変更

`Azure.AI.Projects` NuGetパッケージが安定版2.0.0に到達。名前空間の分割、型の名前変更、ブール値プロパティの`Is*`規則の統一。

## Cosmos DB Java: 重大なセキュリティ修正（RCE）

バージョン4.79.0で**リモートコード実行脆弱性（CWE-502）**の重大な修正。Azure Cosmos DBを使用しているJavaサービスがあれば直ちに更新してください。

## .NET向け新しいProvisioningライブラリ

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

オリジナルポスト: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/)。
