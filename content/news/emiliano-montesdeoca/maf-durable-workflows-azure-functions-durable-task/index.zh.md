---
title: "Microsoft Agent Framework中的持久工作流：从内存到Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAF的工作流编程模型现在支持由Durable Task支持的持久执行——以下是如何构建可组合的代理工作流，这些工作流能够在进程重启后继续运行并在Azure Functions上扩展。"
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

早期AI代理工作流的痛点之一：它们很脆弱。绑定到单个进程的长时间运行多步骤工作流意味着进程重启 = 状态丢失。对于简单的演示这没问题。对于生产工作负载则不然。

Microsoft Agent Framework的工作流编程模型现在支持**持久执行**，由Durable Task框架支持，通过Azure Functions托管。以下是编程模型的工作原理以及持久性为何重要。

## 核心构建块

**Executor**是工作的基本单元。每个都是类型化的——接受特定输入并生成特定输出：

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // 查找订单，返回它
        return new Order(Id: message.OrderId, ...);
    }
}
```

**工作流**使用流畅构建器将执行器连接成有向图。框架处理执行、步骤之间的数据流和错误传播。

您可以建模：
- 顺序链（步骤A → 步骤B → 步骤C）
- 并行fan-out/fan-in（并行运行代理A、B、C，聚合结果）
- 条件分支
- 人在回路审批（暂停工作流，等待外部信号）

## 本地开发的内存运行器

入门很快：

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

核心包包含轻量级进程内运行器。无外部依赖，无数据库，无Azure资源。非常适合本地开发和单元测试。

## 使用Durable Task添加持久性

当工作流需要在进程重启后继续运行时——因为它运行时间长，因为它有人在回路步骤，因为它分散在许多并行代理调用中——内存运行器不够用。

MAF的Durable Task集成将工作流状态存储在Azure Storage中。如果进程重启，工作流从中断处继续。编程模型保持不变；只需替换运行器。

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

相同的执行器，相同的工作流图——由持久状态支持。

## Azure Functions托管

第三层是Azure Functions托管。您的工作流成为Function应用：通过HTTP端点触发工作流，持久运行时处理扩展、状态和可靠性。

这意味着具有并行调用、条件分支和人工审批的多代理工作流可以在无服务器Functions环境中扩展，无需自定义状态管理。

## 为什么这很重要

这种组合对真实AI系统很重要：

- **并行代理调用**——同时分发给多个专门代理而不阻塞，所有代理完成时聚合结果
- **长时间运行进程**——涉及人工审批或外部事件的工作流可以跨小时或天暂停和恢复
- **扩展性**——Azure Functions水平扩展执行；Durable Task框架管理并行状态协调

如果您正在构建超越简单本地演示的MAF工作流，这就是走向生产质量执行的道路。

原始文章：[Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
