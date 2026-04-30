---
title: "GPT-5.5 已来到 Azure Foundry — .NET 开发者需要了解的一切"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 在 Microsoft Foundry 正式发布。从 GPT-5 到 5.5 的演进、真正改进了什么，以及今天如何在你的 Agent 中开始使用它。"
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*本文已自动翻译。如需查看原文，请[点击此处]({{< ref "index.md" >}})。*

微软刚刚宣布 [GPT-5.5 在 Microsoft Foundry 正式发布](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)。如果你一直在 Azure 上构建 Agent，这就是你一直等待的更新。

## GPT-5 的演进

- **GPT-5**：将推理与速度统一到单一系统中
- **GPT-5.4**：更强的多步推理，面向企业的早期 Agent 能力
- **GPT-5.5**：更深入的长上下文推理，更可靠的 Agent 执行，更好的 Token 效率

## 真正发生了什么变化

**Agent 编码改进**：GPT-5.5 在大型代码库中保持上下文，诊断架构级故障，并预测测试需求。模型在行动前推理*修复还会影响什么*。

**Token 效率**：更少的 Token 和更少的重试产生更高质量的输出。生产部署的成本和延迟直接降低。

**长上下文分析**：处理大量文档和多会话历史记录而不失去线索。

## 定价

| 模型 | 输入 ($/M tokens) | 缓存输入 | 输出 ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

## 为什么 Foundry 很重要

Foundry Agent Service 允许你在 YAML 中定义 Agent，或与 Microsoft Agent Framework、GitHub Copilot SDK、LangGraph 或 OpenAI Agents SDK 连接——并将它们作为具有持久文件系统、独立 Microsoft Entra 身份和零扩展定价的隔离托管 Agent 运行。

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "你是一个有用的助手。", name: "我的Agent");
```

查看[完整公告](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)了解所有详情。
