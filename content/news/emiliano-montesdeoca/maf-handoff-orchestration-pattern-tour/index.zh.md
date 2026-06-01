---
title: "Handoff 模式：当一个智能体不够用时"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 的 Handoff 编排模式让智能体能够决定由谁处理下一轮对话——而不会丢失对话上下文或违反拓扑规则。"
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

在某个时刻，每个多智能体系统都会超越一个简单的路由器。第一个信号通常是当一个专业智能体需要提出后续问题时，或者在轮次中途意识到另一个智能体应该继续时。固定管道在那里失败。单次路由器在那里失败。

这正是 Microsoft Agent Framework 中 Handoff 编排模式设计解决的问题。

## Handoff 如何工作

开发者声明一个图：这些是智能体，这些是它们之间的边。框架完成其余工作——为每条出边合成一个 handoff 工具并将其注入每个智能体。当智能体决定交出控制权时，它调用该工具。框架强制执行拓扑结构。

三件事使这与简单地让智能体互相调用不同：

1. **共享转录** — 接收智能体看到完整的对话历史。不需要从头开始。
2. **拓扑强制执行** — 智能体只能将控制权交给声明的目标。路由错误在创作时被捕获，而不是在生产中。
3. **自然终止** — 当活跃智能体在没有调用 handoff 工具的情况下结束其轮次时，工作流让位给用户。无需轮询，无需显式退出条件。

## 最小示例

在 .NET 中，构建 handoff 工作流看起来像这样：

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage 可以发送给任一专家。两个专家都可以发送回 triage。图支持无环，但在需要时支持后向边（"我需要更多信息" → 返回研究）。

## 何时使用 Handoff（何时不使用）

Handoff 是好的选择，当：

- **所有权可能在对话中途改变** — 智能体可能意识到自己是错误的专家
- **后向边很重要** — 可能需要在不重启的情况下重新访问之前的步骤
- **路由决策是细微的** — handoff 的决定是上下文相关的，最好由模型而不是类型化谓词来做出

*不是*正确选择，当：

- 管道是固定且顺序的 — 为此使用 `Sequential` 工作流
- 每个步骤都是独立的 — 智能体共享一个只有一个需要的转录只是噪音
- 需要严格的处理保证 — 模型驱动路由的不确定性不是你想要的

## 后向边和 Human-in-the-Loop

Handoff 允许的最有趣的形式之一是真正的后向边。智能体可以决定"我没有足够的信息"并路由回研究步骤——不是使用硬编码循环，而是因为模型决定这是正确的决定。

Human-in-the-loop 交互也自然地组合。当专家需要用户输入时，工作流通过默认的轮次循环让位给用户，收集响应，并以完整上下文恢复。智能体从未丢失对话。

## 总结

Handoff 是那些看起来简单但一旦内化就能实现很多功能的模式之一：分散路由、共享上下文、强制拓扑、自然终止。当你的智能体开始说"实际上，应该由其他人来处理这个"时，这是正确的下一步。

在原始帖子中阅读完整演练：[A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
