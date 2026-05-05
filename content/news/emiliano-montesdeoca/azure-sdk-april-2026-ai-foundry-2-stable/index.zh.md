---
title: "Azure SDK 2026年4月：AI Foundry 2.0及.NET开发者须知"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "2026年4月Azure SDK发布带来了Azure.AI.Projects 2.0.0稳定版（包含重大破坏性变更）、Cosmos DB关键安全修复以及.NET的新Provisioning库。"
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*本文已自动翻译。要查看原始版本，请[点击这里](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-sdk-april-2026-ai-foundry-2-stable/)。*

月度SDK发布通常容易被忽略。这次有几件事值得关注——特别是如果你在使用AI Foundry、Java版Cosmos DB或从.NET代码进行基础设施配置。

## Azure.AI.Projects 2.0.0 — 有意义的破坏性变更

命名空间拆分、类型重命名、布尔属性统一使用`Is*`命名规则。

## Cosmos DB Java：关键安全修复（RCE）

4.79.0版本修复了**远程代码执行漏洞（CWE-502）**。立即更新。

## .NET的新Provisioning库

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

原始文章：[Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/)。
