---
title: "Foundry Agent Service 正式发布：对 .NET 代理开发者真正重要的是什么"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "微软的 Foundry Agent Service 刚刚正式发布，带来了私有网络、Voice Live、生产评估和开放的多模型运行时。这是你需要知道的。"
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

说实话 — 构建一个 AI 代理原型是简单的部分。困难的是之后的一切：用适当的网络隔离投入生产、运行真正有意义的评估、处理合规要求，以及不在凌晨 2 点搞崩东西。

[Foundry Agent Service 刚刚正式发布](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)，这个版本像激光一样聚焦在"之后一切"的鸿沟上。

## 构建在 Responses API 之上

标题新闻：新一代 Foundry Agent Service 构建在 OpenAI Responses API 之上。如果你已经在用这个 wire protocol 构建，迁移到 Foundry 只需最少的代码改动。你获得的：企业安全、私有网络、Entra RBAC、完整追踪和评估 — 在你现有的代理逻辑之上。

架构是有意开放的。你不被锁定在一个模型提供商或一个编排框架上。用 DeepSeek 做规划、OpenAI 做生成、LangGraph 做编排 — 运行时处理一致性层。

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> 如果你从 `azure-ai-agents` 包迁移过来，代理现在是 `azure-ai-projects` 中 `AIProjectClient` 的一等操作。移除独立依赖，使用 `get_openai_client()` 来驱动响应。

## 私有网络：企业阻碍已移除

这是解锁企业采用的功能。Foundry 现在支持完整的端到端私有网络配合 BYO VNet：

- **无公共出口** — 代理流量永远不会触及公共互联网
- **容器/子网注入**到你的网络以实现本地通信
- **工具连接也包含在内** — MCP 服务器、Azure AI Search、Fabric 数据代理都通过私有路径运作

最后一点至关重要。不只是推理调用保持私有 — 每个工具调用和检索调用也都留在你的网络边界内。对于在数据分类策略下禁止外部路由的团队来说，这就是缺失的那块。

## MCP 认证做对了

MCP 服务器连接现在支持完整的认证模式谱系：

| 认证方式 | 何时使用 |
|----------|----------|
| 基于密钥 | 组织范围内部工具的简单共享访问 |
| Entra Agent Identity | 服务间；代理以自身身份认证 |
| Entra Managed Identity | 按项目隔离；无凭证管理 |
| OAuth Identity Passthrough | 用户委托访问；代理代表用户行事 |

OAuth Identity Passthrough 是有趣的那个。当用户需要授予代理访问他们的个人数据 — 他们的 OneDrive、Salesforce 组织、按用户范围的 SaaS API — 代理使用标准 OAuth 流程代表他们行事。没有假装是所有人的共享系统身份。

## Voice Live：无需管道工程的语音对语音

给代理添加语音曾经意味着拼凑 STT、LLM 和 TTS — 三个服务、三次延迟跳转、三个计费面，全部手动同步。**Voice Live** 将这一切压缩为单个托管 API：

- 语义语音活动和轮次结束检测（理解含义，不仅仅是沉默）
- 服务端噪声抑制和回声消除
- 插话支持（用户可以在响应中途打断）

语音交互通过与文本相同的代理运行时。相同的评估器、相同的追踪、相同的成本可见性。对于客户支持、现场服务或无障碍场景，这取代了以前需要自定义音频管道的方案。

## 评估：从勾选框到持续监控

这是 Foundry 认真对待生产质量的地方。评估系统现在有三层：

1. **开箱即用评估器** — 连贯性、相关性、扎实度、检索质量、安全性。连接到数据集或实时流量获取分数。

2. **自定义评估器** — 编码你自己的业务逻辑、语调标准和领域特定合规规则。

3. **持续评估** — Foundry 采样实时生产流量，运行你的评估器套件，并在仪表板中显示结果。设置 Azure Monitor 告警以监控扎实度下降或安全阈值突破。

一切发布到 Azure Monitor Application Insights。代理质量、基础设施健康、成本和应用遥测 — 全在一处。

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## 六个新区域支持托管代理

托管代理现在在 East US、North Central US、Sweden Central、Southeast Asia、Japan East 等区域可用。这对数据驻留要求很重要，也有助于在代理靠近数据源运行时压缩延迟。

## 为什么这对 .NET 开发者重要

虽然 GA 公告中的代码示例是 Python 优先的，但底层基础设施是语言无关的 — `azure-ai-projects` 的 .NET SDK 遵循相同的模式。Responses API、评估框架、私有网络、MCP 认证 — 这些都可以从 .NET 使用。

如果你一直在等 AI 代理从"酷炫演示"变成"我真的可以在工作中交付"，这个 GA 版本就是信号。私有网络、适当的认证、持续评估和生产监控是缺失的那些拼图。

## 总结

Foundry Agent Service 现在可用。安装 SDK，打开[门户](https://ai.azure.com)，开始构建。[快速入门指南](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code)带你在几分钟内从零到运行中的代理。

包含所有代码示例的完整技术深度分析，请查看 [GA 公告](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)。
