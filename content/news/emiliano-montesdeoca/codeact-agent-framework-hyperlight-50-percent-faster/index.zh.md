---
title: "Agent Framework中的CodeAct：如何将智能体延迟减半"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct将多步骤工具链压缩为单个沙盒代码块——延迟降低52%，令牌使用量减少64%。了解它对您的智能体意味着什么以及何时使用它。"
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*本文已自动翻译。如需阅读原文，请[点击此处]({{< ref "index.md" >}})。*

在每个智能体项目中，都会有这样一个时刻：你查看追踪信息，心想："为什么这要花这么长时间？"模型没问题，工具也能运行，但为了获得一个本可一步计算出的结果，却需要七次往返请求。

这正是CodeAct解决的问题——[Agent Framework团队刚刚发布了Alpha支持](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)，通过新的`agent-framework-hyperlight`包实现。

## 什么是CodeAct？

[CodeAct模式](https://arxiv.org/abs/2402.01030)优雅而简单：不再给模型一个工具列表让它逐一调用，而是给它一个单一的`execute_code`工具，让它将*整个计划*表达为一个简短的Python程序。智能体只需编写一次代码，沙盒执行它，你就能得到一个统一的结果。

| 方式 | 时间 | 令牌 |
|--------|------|--------|
| 传统方式 | 27.81秒 | 6,890 |
| CodeAct | 13.23秒 | 2,489 |
| **提升** | **52.4%** | **63.9%** |

## 安全机制：Hyperlight微型虚拟机

`agent-framework-hyperlight`包使用[Hyperlight](https://github.com/hyperlight-dev/hyperlight)微型虚拟机。每次`execute_code`调用都在一个全新的微型VM中运行。启动时间以毫秒计算。隔离几乎是免费的。

你的工具仍在主机上运行。模型生成的*粘合代码*在沙盒中运行。这是正确的分工。

## 最小配置

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## 何时使用CodeAct（何时不用）

**使用CodeAct的情况：**
- 任务需要链接许多小型工具调用（查询、连接、计算）
- 延迟和令牌成本很重要
- 需要对模型生成的代码进行强隔离

**继续使用传统工具调用的情况：**
- 智能体每轮只进行一两次工具调用
- 每次调用都有需要单独审批的副作用
- 工具描述稀少或模糊

## 立即尝试

```bash
pip install agent-framework-hyperlight --pre
```

请查阅[Agent Framework博客的完整文章](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)获取更深入的介绍。
