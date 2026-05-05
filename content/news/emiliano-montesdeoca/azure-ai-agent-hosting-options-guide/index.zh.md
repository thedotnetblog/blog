---
title: "Azure上のAIエージェントはどこにホストすべき？実践的な判断ガイド"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure提供六种托管AI代理的方式——从原始容器到完全托管的Foundry Hosted Agents。以下是如何为你的.NET工作负载选择合适方案。"
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "azure-ai-agent-hosting-options-guide.md" >}})。*

如果你现在正在用.NET构建AI代理，你可能已经注意到一件事：在Azure上托管它们的方式*太多了*。Container Apps、AKS、Functions、App Service、Foundry Agents、Foundry Hosted Agents——在你真正需要选择之前，每个都听起来合理。Microsoft刚刚发布了一份[Azure AI代理托管综合指南](https://devblogs.microsoft.com/all-things-azure/hostedagent/)来澄清这个问题，我想从.NET开发者的实践角度来拆解它。

## 六种选项速览

以下是我对这个版图的总结：

| 选项 | 最适合 | 你需要管理 |
|------|--------|-----------|
| **Container Apps** | 无需K8s复杂性的完整容器控制 | 可观测性、状态、生命周期 |
| **AKS** | 企业合规、多集群、自定义网络 | 所有东西（这就是重点） |
| **Azure Functions** | 事件驱动的短时代理任务 | 几乎不需要——真正的无服务器 |
| **App Service** | 简单的HTTP代理、可预测的流量 | 部署、扩展配置 |
| **Foundry Agents** | 通过门户/SDK的无代码代理 | 几乎不需要 |
| **Foundry Hosted Agents** | 托管基础设施上的自定义框架代理 | 仅你的代理代码 |

前四个是通用计算——你*可以*在上面运行代理，但它们不是为此设计的。最后两个是代理原生的：它们将对话、工具调用和代理生命周期理解为一等概念。

## Foundry Hosted Agents——.NET代理开发者的最佳选择

这是引起我注意的地方。Foundry Hosted Agents正好处于中间位置：你获得运行自己代码的灵活性（Semantic Kernel、Agent Framework、LangGraph——随便什么），但平台处理基础设施、可观测性和对话管理。

关键部分是**Hosting Adapter**——一个将你的代理框架连接到Foundry平台的薄抽象层。对于Microsoft Agent Framework，看起来是这样的：

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

这就是你的整个托管方案。适配器自动处理协议转换、通过server-sent events的流式传输、对话历史和OpenTelemetry追踪。不需要自定义中间件，不需要手动配置。

## 部署真的很简单

我以前在Container Apps上部署过代理，虽然可以工作，但最后你会写很多胶水代码来处理状态管理和可观测性。使用Hosted Agents和`azd`，部署是：

```bash
# 安装AI代理扩展
azd ext install azure.ai.agents

# 从模板初始化
azd ai agent init

# 构建、推送、部署——完成
azd up
```

这个单独的`azd up`会构建你的容器、推送到ACR、配置Foundry项目、部署模型端点并启动你的代理。五个步骤压缩成一个命令。

## 内置对话管理

这是在生产中节省最多时间的部分。不需要构建自己的对话状态存储，Hosted Agents原生处理：

```python
# 创建持久对话
conversation = openai_client.conversations.create()

# 第一轮
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# 第二轮——上下文被保留
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

不需要Redis。不需要Cosmos DB会话存储。不需要自定义中间件来序列化消息。平台直接处理了。

## 我的决策框架

在审查了所有六个选项之后，这是我的快速心智模型：

1. **需要零基础设施？** → Foundry Agents（门户/SDK，无容器）
2. **有自定义代理代码但想要托管主机？** → Foundry Hosted Agents
3. **需要事件驱动的短期代理任务？** → Azure Functions
4. **需要不用K8s的最大容器控制？** → Container Apps
5. **需要严格合规和多集群？** → AKS
6. **有流量可预测的简单HTTP代理？** → App Service

对于大多数使用Semantic Kernel或Microsoft Agent Framework构建的.NET开发者来说，Hosted Agents可能是正确的起点。你能获得scale-to-zero、内置OpenTelemetry、对话管理和框架灵活性——无需管理Kubernetes或搭建自己的可观测性栈。

## 总结

Azure上的代理托管格局正在快速成熟。如果你今天要开始一个新的AI代理项目，我会在习惯性地使用Container Apps或AKS之前认真考虑Foundry Hosted Agents。托管基础设施节省实际时间，而hosting adapter模式让你保留框架选择。

查看[Microsoft的完整指南](https://devblogs.microsoft.com/all-things-azure/hostedagent/)和[Foundry Samples仓库](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents)获取可运行的示例。
