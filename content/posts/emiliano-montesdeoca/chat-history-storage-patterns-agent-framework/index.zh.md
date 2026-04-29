---
title: "你的 Agent 在哪里记住事情？聊天历史存储实践指南"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "服务管理还是客户端管理？线性还是分叉？这个架构决策决定了你的 AI Agent 能做什么——附 C# 和 Python 代码示例。"
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*本文已自动翻译。如需查看原文，请[点击此处]({{< ref "index.md" >}})。*

在构建 AI Agent 时，你把大部分精力花在模型、工具和提示词上。*对话历史存储在哪里*这个问题看起来像是实现细节——但实际上是你将做出的最重要的架构决策之一。

它决定了用户能否分叉对话、撤销回答、重启后恢复会话，以及数据是否会离开你的基础设施。[Agent Framework 团队发布了一篇深度分析](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/)。

## 两种基本模式

**服务管理型**：AI 服务存储对话状态。你的应用保持一个引用，服务自动在每次请求中包含相关历史记录。更简单，控制更少。

**客户端管理型**：你的应用维护完整历史记录，并在每次请求时发送相关消息。服务无状态。你控制一切。

## Agent Framework 如何抽象这一切

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("我叫 Alice。", session);
var second = await agent.RunAsync("我叫什么名字？", session);
```

```python
session = agent.create_session()
first = await agent.run("我叫 Alice。", session=session)
second = await agent.run("我叫什么名字？", session=session)
```

Session 处理底层差异。无论切换什么提供商，应用代码不变。

## 提供商快速参考

| 提供商 | 存储位置 | 模式 | 压缩 |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | 客户端 | N/A | 你 |
| Foundry Agent Service | 服务端 | 线性 | 服务端 |
| Responses API（默认） | 服务端 | 分叉型 | 服务端 |
| Anthropic Claude, Ollama | 客户端 | N/A | 你 |

## 如何选择

1. **需要分叉对话或"撤销"？** → 服务管理型 Responses API
2. **需要数据主权？** → 带数据库后端的客户端管理型
3. **只是简单聊天机器人？** → 服务管理型线性即可

阅读[完整文章](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/)了解完整决策树。
