---
title: "Cosmos DB 的不可变备份是那种你会很晚才感激的功能"
date: 2026-06-27
author: "Emiliano Montesdeoca"
description: "Azure Backup for Azure Cosmos DB 现在在公开预览中增加了不可变备份和长期保留。关键点不仅在于恢复，还在于改善受监管或高风险工作负载的弹性和证据保存。"
tags:
  - Azure Cosmos DB
  - Azure
  - Backup
  - Security
  - Resilience
---

备份功能很容易被忽视——直到它们变成房间里最重要的事情。

这就是为什么我认为新的 **Azure Backup for Azure Cosmos DB** 预览版值得关注。

有趣的部分不仅仅是一个"另一个备份选项"。而是增加了**不可变恢复点**和**长期保留**，其模式与勒索软件防御、可审计性和受监管的恢复需求更加契合。

## 不可变改变了对话

当攻击者针对生产系统时，下一个问题不再只是"我们有备份吗？"

而是：

- 备份可信吗？
- 它能否被修改或删除？
- 事故开始后我们是否还有受保护的恢复点？

这就是为什么不可变备份很重要。它改善了当周围环境不再可信时的恢复路径。

## 我的看法

这不是那种会让人人兴奋的公告。

但对于在 Cosmos DB 上运行关键工作负载的团队来说，它正是那种会在季度最糟糕的那一天成为中心的能力。

而这些往往是最值得跟踪的功能。

原文：[Azure Backup for Azure Cosmos DB Public Preview Adds Immutable Backups and Long-Term Retention](https://devblogs.microsoft.com/cosmosdb/azure-backup-for-azure-cosmos-db-public-preview-adds-immutable-backups-and-long-term-retention/)