---
title: "Foundry Toolboxes：AI Agent工具的统一端点"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry已推出公开预览版Toolboxes——一种通过单一MCP兼容端点管理和公开AI Agent工具的方式，无需在每个Agent中重新配置所有内容。"
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*本文已自动翻译。如需查看原始版本，请[点击此处]({{< ref "index.md" >}})。*

有一个问题听起来无聊，直到你真正遇到它：你的组织在构建多个AI Agent，每个都需要工具，每个团队都从头开始配置。相同的Web搜索集成、相同的Azure AI Search配置、相同的GitHub MCP服务器连接——但在不同的仓库里，由不同的团队，使用不同的凭据，没有任何共享治理。

Microsoft Foundry刚刚以公开预览版发布了[Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)，这是对该问题的直接回应。

## 什么是Toolbox

Toolbox是一个有命名的、可复用的工具包，在Foundry中定义一次，通过单一MCP兼容端点公开。任何能够使用MCP的Agent运行时都可以消费它——不受限于Foundry Agents。

承诺很简单：**build once, consume anywhere**。定义工具，集中配置身份验证（OAuth直通、Entra托管标识），发布端点。需要这些工具的每个Agent连接到端点即可获取全部工具。

## 四个支柱（今天两个可用）

| 支柱 | 状态 | 功能 |
|------|------|------|
| **Discover** | 即将推出 | 无需手动搜索即可发现已批准的工具 |
| **Build** | 现已可用 | 将工具整合到可复用包中 |
| **Consume** | 现已可用 | 单一MCP端点公开所有工具 |
| **Govern** | 即将推出 | 集中身份验证+所有工具调用的可观测性 |

## 实践示例

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="搜索文档并回应GitHub issues",
    tools=[
        {"type": "web_search", "description": "搜索公开文档"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

发布后，Foundry提供统一端点。一次连接，获取所有工具。

## 不受限于Foundry Agents

Toolboxes在Foundry中**创建和管理**，但消费面是开放的MCP协议。可以从使用Microsoft Agent Framework或LangGraph的自定义Agent、GitHub Copilot和其他MCP兼容IDE以及任何支持MCP的运行时中使用它们。

## 为什么现在重要

多Agent浪潮正在进入生产环境。每个新Agent都是重复配置、过期凭据和不一致行为的新风险面。Build + Consume基础足以开始集中化。当Govern支柱推出时，你将拥有对整个Agent群完全可观测、集中控制的工具层。

## 总结

还是早期阶段——公开预览，Python SDK优先，Discover和Govern仍在路上。但模型是稳固的，MCP原生设计意味着它可以与你已经在构建的工具配合使用。查阅[官方公告](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)了解详情。
