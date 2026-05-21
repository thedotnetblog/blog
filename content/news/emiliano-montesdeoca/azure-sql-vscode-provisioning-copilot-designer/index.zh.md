---
title: "VS Code 的 MSSQL 扩展正在悄悄变成一个更大的平台"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "最新的 MSSQL 扩展更新加入了 Azure SQL provisioning、Copilot 辅助的 schema 设计、Data API builder 和 notebooks。真正有意思的是，现在有多少数据库工作可以留在 VS Code 里完成。"
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*本文已自动翻译。要查看原文，请[点击此处]({{< ref "index.md" >}})。*

VS Code 的 MSSQL 扩展已经增长了一段时间，但这次最新更新把方向变得更清楚了。

它不再只是“连接然后跑几个查询”。

随着 **Azure SQL provisioning**、**Copilot 辅助的 Schema Designer**、**SQL Notebooks** 和 **Data API builder** 一起推进，这个扩展正在变成一个面向数据库开发的更完整工作区。

## 真正实用的切入点是直接在编辑器里进行 provisioning

原文说，你现在可以使用免费层级“直接从编辑器里、而且免费地”创建一个 fully managed 的云数据库。

这类功能看起来很小，直到你意识到它到底减少了多少配置摩擦。

对很多开发者来说，数据密集型实验最麻烦的部分不是 SQL 本身，而是下面这些之间的环境鸿沟：

- 想法
- 数据库
- schema
- API
- 可测试的 backend

如果这个鸿沟可以在一个工具里缩短，整个工作流就会更有吸引力。

## 这才是数据工作的更强 inner loop

我喜欢这个版本的一点是，它把更多数据库工作流留在了同一个地方：

- provisioning 数据库
- 设计 schema
- 审查变更
- 生成 ORM 脚本
- 暴露 API
- 测试 endpoints
- 通过 notebooks 做文档和查询

这比把 SQL 当成堆栈里一个分离的旁边工具要有说服力得多。

## Copilot 辅助的 schema 工作流，才是 AI 价值真正显现的地方

schema designer 的新增内容尤其有意思，因为它们似乎找到了不错的平衡。

价值不是“AI 设计你的 data model，然后你盲目信任它”。

价值是：

- 更快的起点
- 视觉审查
- 变更跟踪
- 面向迁移的输出
- 明确的接受/撤销控制

这比没有检查路径的全自动生成健康得多。

而对于数据库工作来说，可审查性非常重要。

## Data API builder 是一个安静的倍增器

另一个我不会忽视的功能是 Data API builder 的集成。

如果你能在同一个环境里从 schema 走到：

- REST
- GraphQL
- MCP endpoints

这就为 backend prototype 和内部工具创造了一条非常高效的路径。

这并不能取代更深入的 backend engineering，但它确实大大缩短了从数据库想法到可用接口的路径。

## 我的看法

这个版本让 MSSQL 扩展更像 VS Code 里的一个小型平台，而不是一个简单插件。

对于构建 API、数据工具、管理工具或基于 SQL 的 prototype 的开发者来说，这是一个有意义的变化。

如果 Microsoft 继续收紧这个循环，这个扩展的战略价值会比很多人现在以为的更高。

原始文章：[MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)