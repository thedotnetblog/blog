---
title: "Deep Agents + Cosmos DB 展示了一个针对实时运维数据的实用模式"
date: 2026-06-22
author: "Emiliano Montesdeoca"
description: "Deep Agents 与 Azure Cosmos DB 的示例之所以有趣，是因为它展示了一个智能体直接对运维数据进行操作、跨多步规划、验证写入并始终与企业已经在使用的数据存储保持连接的模式。"
tags:
  - Azure Cosmos DB
  - AI
  - Agents
  - Azure
  - Architecture
---

我喜欢那些贴近真实运维工作流的智能体示例。

这个新的 **Deep Agents + Azure Cosmos DB** 示例正是如此。

它没有发明一个脱离实际的演示世界，而是将智能体放在一个存储在 Cosmos DB 中的支持工单队列之上，让它做团队真正关心的事情：

- 分类工作
- 检测模式
- 更新记录
- 验证结果

这对于一个智能体系统来说是一个更有用的形态。

## 真正价值不在于"AI 与数据库对话"

我们已经见过那种故事了。

这个示例更好的地方在于围绕它的运维纪律：

- 智能体使用特定的工具
- 写入通过受控路径进行
- 读后写验证是流程的一部分
- 分区和查询成本被纳入考量
- 系统处理的是实时风格的运维数据，而非假装是现实的侧缓存

这种组合让这个模式变得有趣。

## 为什么 Cosmos DB 很适合这里

Cosmos DB 非常适合这类工作负载，因为数据本身就是动态的、文档形态的和运维性的。

智能体可以：

- 直接读取工单
- 在需要时运行队列范围查询
- 打补丁特定项目
- 将状态和历史紧邻数据本身保存

对于智能体场景来说，这通常比先强制所有数据通过一个单独的分析层更有用。

## 我的看法

这里最大的收获是，当智能体系统操作于企业已经依赖的相同数据和相同工作流时，它们会变得更有说服力。

这就是这个示例做对的地方。

它把智能体当作一个具有明确工具边界的运维参与者，而不是一个假装在帮忙的脱节聊天界面。

这是一个值得学习研究的模式。

原文：[How to Use Deep Agents with Azure Cosmos DB – Plan, act, and verify against operational data](https://devblogs.microsoft.com/cosmosdb/deep-agents-to-plan-act-verify-against-operational-data/)