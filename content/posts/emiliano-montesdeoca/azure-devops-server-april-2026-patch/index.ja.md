---
title: "Azure DevOps Server 2026年4月パッチ — PRの完了修正とセキュリティアップデート"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Serverがパッチ3を取得。PR完了の失敗修正、サインアウト時の検証改善、GitHub Enterprise Server PATの接続復元が含まれます。"
tags:
  - azure-devops
  - devops
  - patches
---

> *この記事は自動翻訳されています。オリジナル版は[こちら]({{< ref "azure-devops-server-april-2026-patch.md" >}})をご覧ください。*

セルフホストでAzure DevOps Serverを運用しているチームへの簡単なお知らせです。Microsoftが[2026年4月のパッチ3](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/)をリリースしました。3つの修正が含まれています。

## 修正内容

- **Pull Requestの完了失敗** — ワークアイテムの自動完了時にnull参照例外が発生し、PRのマージが失敗することがありました。ランダムなPR完了エラーに遭遇した方は、これが原因の可能性が高いです
- **サインアウト時のリダイレクト検証** — 悪意のあるリダイレクトを防止するため、サインアウト時の検証が改善されました。早めに適用すべきセキュリティ修正です
- **GitHub Enterprise Server PATの接続** — GitHub Enterprise ServerへのPersonal Access Tokenの接続作成が壊れていましたが、復元されました

## アップデート方法

[パッチ3](https://aka.ms/devopsserverpatch3)をダウンロードしてインストーラーを実行してください。パッチが適用されたことを確認するには：

```bash
<patch-installer>.exe CheckInstall
```

Azure DevOps Serverをオンプレミスで運用している場合、Microsoftはセキュリティと信頼性の両面から、最新のパッチを維持することを強く推奨しています。詳細は[リリースノート](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026)をご確認ください。
