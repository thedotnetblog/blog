---
title: "Microsoft Foundry 2026年3月 — GPT-5.4、Agent Service GA，以及改变一切的SDK刷新"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry 2026年3月更新非常重大：Agent Service正式GA，GPT-5.4带来可靠推理，azure-ai-projects SDK在所有语言中稳定发布，Fireworks AI将开放模型引入Azure。"
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}})。*

每月的"Microsoft Foundry新动态"文章通常是增量改进和偶尔亮点功能的混合。[2026年3月版](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)呢？基本上全是亮点功能。Foundry Agent Service正式GA，GPT-5.4投入生产，SDK获得重要的稳定版本发布，Fireworks AI将开放模型推理引入Azure。让我来解析对.NET开发者来说什么最重要。

## Foundry Agent Service已准备好投入生产

这是最大的新闻。新一代代理运行时已正式发布 — 构建在OpenAI Responses API之上，与OpenAI代理协议兼容，并向多个提供商的模型开放。如果您今天正在使用Responses API构建，迁移到Foundry将在您现有的代理逻辑之上添加企业级安全性、私有网络、Entra RBAC、完整追踪和评估功能。

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

关键新增功能：端到端私有网络、MCP认证扩展（包括OAuth透传）、语音对语音代理的Voice Live预览，以及在6个新区域托管代理。

## GPT-5.4 — 可靠性优于纯粹的智能

GPT-5.4不是为了变得更聪明，而是为了变得更可靠。在长时间交互中更强的推理能力、更好的指令遵循性、更少的工作流中途故障，以及集成的计算机使用功能。对于生产环境的代理来说，这种可靠性比基准测试分数重要得多。

| 模型 | 价格（每百万token） | 最佳用途 |
|------|-------------------|---------|
| GPT-5.4 (≤272K) | $2.50 / $15 输出 | 生产代理、编码、文档工作流 |
| GPT-5.4 Pro | $30 / $180 输出 | 深度分析、科学推理 |
| GPT-5.4 Mini | 经济实惠 | 分类、提取、轻量级工具调用 |

聪明的策略是路由：GPT-5.4 Mini处理高吞吐量、低延迟的工作，而GPT-5.4负责推理密集型的请求。

## SDK终于稳定了

`azure-ai-projects` SDK在所有语言中发布了稳定版 — Python 2.0.0、JS/TS 2.0.0、Java 2.0.0和.NET 2.0.0（4月1日）。`azure-ai-agents`依赖已经消失 — 一切都在`AIProjectClient`下。使用`pip install azure-ai-projects`安装，包中直接捆绑了`openai`和`azure-identity`作为依赖项。

对于.NET开发者来说，这意味着一个NuGet包就能覆盖Foundry的全部功能。不再需要在多个代理SDK之间来回切换。

## Fireworks AI将开放模型引入Azure

也许是架构上最有趣的新增：Fireworks AI每天处理超过13万亿token，速度达到~180K请求/秒，现在可以通过Foundry使用。DeepSeek V3.2、gpt-oss-120b、Kimi K2.5和MiniMax M2.5在发布时可用。

真正的故事是**自带权重** — 从任何地方上传量化或微调的权重，无需更改服务栈。通过无服务器按token付费或预配置吞吐量进行部署。

## 其他亮点

- **Phi-4 Reasoning Vision 15B** — 针对图表、图形和文档布局的多模态推理
- **Evaluations GA** — 开箱即用的评估器，配合持续生产监控，直接接入Azure Monitor
- **Priority Processing**（预览）— 面向延迟敏感型工作负载的专用计算通道
- **Voice Live** — 直接连接到Foundry代理的语音对语音运行时
- **Tracing GA** — 具有排序和过滤功能的端到端代理追踪检查
- **PromptFlow弃用** — 在2027年1月前迁移到Microsoft Framework Workflows

## 总结

2026年3月是Foundry的转折点。Agent Service GA、所有语言的稳定SDK、用于可靠生产代理的GPT-5.4，以及通过Fireworks AI实现的开放模型推理 — 该平台已准备好应对严肃的工作负载。

阅读[完整汇总](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)并[构建您的第一个代理](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code)来开始吧。
