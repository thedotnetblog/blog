---
title: "为什么 Microsoft Agent Framework 的分层设计真的很重要"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 新的分层 SDK 解释不只是架构层面的讨论。它展示了微软希望开发者如何从简单循环走向生产级编排，而不用把一切推倒重来。"
tags:
  - Agent Framework
  - AI
  - .NET
  - Architecture
  - Developer Tools
---

> *本文已自动翻译。如需查看原文，请[点击此处]({{< ref "index.md" >}})。*

框架公告通常先讲功能。

这次先讲的是 **设计哲学**，我觉得这正是它重要的原因。

微软对 Microsoft Agent Framework 如何围绕 **agent loops**、**workflows** 和 **harnesses** 进行组织的最新说明，给出的信号比另一张功能清单要强得多。它告诉我们团队预期真实应用会怎样成长。

而对于任何在 .NET 上构建 agent 的人来说，这才是最有价值的部分。

## 大多数 agent 应用很快就会超出它们最初的架构

你从一个 model call 开始。

然后加上 tools。

然后是 memory。

然后是 planner。

然后是 retries、telemetry、approvals、专用 agents，以及一些 workflow 逻辑，因为单个 loop 已经不够用了。

很多 AI 应用就是在这里变得一团糟。第一个版本能跑，但每一项新能力都是从不同的抽象层硬拼上去的。

我喜欢 Agent Framework 这篇说明的一点，是它把这些层次讲得很明确：

- **loops** 用于核心执行循环
- **workflows** 用于结构化编排
- **harnesses** 用于围绕 agent 的可复用 runtime 能力

这听起来一开始可能有点学院派，但它解决的是一个非常实际的问题：**你可以在不每次重写心智模型的情况下，让应用随着复杂度提升而演进**。

## harness 的概念尤其重要

如果要我选一个我认为会越来越重要的部分，那就是 **harness** 这个想法。

harness 是 agent 开发从提示词工作变成工程工作的地方。

到了这一层，你开始关心：

- tools 和 middleware
- 规划行为
- memory 集成
- observability
- 控制和治理
- 可重复的 runtime 行为

这也是这个设计能和微软技术栈其他部分很好结合的原因。Foundry、治理工具、hosted agents、评估，以及工具生态，在把模型周围的 runtime 外壳当作一等公民时才更合理。

## 这对 .NET 开发者来说是个好信号

在这类生态里，我总会看一件事：framework 在第一次演示之后是否仍然好用。

分层方法表明微软在考虑完整路径：

1. 构建一个简单的 agent loop
2. 在不混乱的情况下添加结构化能力
3. 当应用需要时，转向更正式的 workflows
4. 让 runtime 保持足够可组合，以便集成企业系统

这比“给你一个单体抽象，祝你好运”健康得多。

而且它和 .NET 开发者平时喜欢的工作方式非常一致：分层系统、显式组合、可测试的边界，以及强大的 runtime 控制。

## 我的看法

这篇文章很容易被低估，因为它没有炫目的截图，也没有大规模的 API 列表。

但像这样的架构笔记，往往更能预测一个 framework 六个月后是否还能站得住。

Microsoft Agent Framework 显然不想只做 model call 外面一个玩具式包装器。这个分层 SDK 的故事说明，团队是在为那段最麻烦的中间地带而构建：agent 需要 orchestration、tools、runtime services 和 production discipline 的地方。

这正是我关心的区域。

原文：[ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK]({{< ref "index.md" >}})
