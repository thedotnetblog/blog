---
title: "Azure DevOps Server 2026年4月补丁 — PR完成修复和安全更新"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server 发布补丁3，修复了PR完成失败问题，改进了注销验证，并恢复了GitHub Enterprise Server PAT连接。"
tags:
  - azure-devops
  - devops
  - patches
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "azure-devops-server-april-2026-patch.md" >}})。*

给运行自托管Azure DevOps Server的团队快速提个醒：Microsoft发布了[2026年4月补丁3](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/)，包含三个针对性修复。

## 修复内容

- **Pull Request完成失败** — 工作项自动完成期间的空引用异常可能导致PR合并失败。如果你遇到过随机的PR完成错误，这很可能就是原因
- **注销重定向验证** — 改进了注销期间的验证，以防止潜在的恶意重定向。这是一个值得尽快应用的安全修复
- **GitHub Enterprise Server PAT连接** — 创建到GitHub Enterprise Server的Personal Access Token连接之前无法正常工作，现在已恢复

## 如何更新

下载[补丁3](https://aka.ms/devopsserverpatch3)并运行安装程序。要验证补丁是否已应用：

```bash
<patch-installer>.exe CheckInstall
```

如果你在本地运行Azure DevOps Server，Microsoft强烈建议保持最新补丁，以确保安全性和可靠性。查看[发行说明](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026)了解完整详情。
