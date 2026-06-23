---
title: "OpenEnv 和 Foundry 正把讨论推进到静态智能体之外"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "OpenEnv 和 Foundry 的新故事远不只是 reinforcement learning 这类流行词。它真正指向的是这样一种智能体系统：可以根据真实业务结果，随着时间推移被评估、优化并持续改进。"
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}})。*

大多数智能体讨论仍然停留在推理阶段。

模型能回答提示吗？它能调用工具吗？它能把任务完成一次吗？

新的 **OpenEnv + Foundry** 讨论之所以有意思，是因为它想把话题推进到更有雄心的方向：**如何构建一个真正会随着时间不断变好的智能体系统？**

这才是一个好得多的问题。

## 关键转变是从响应走向学习闭环

Foundry 这篇文章把问题放在 environment、evals、rubrics、optimization 和 post-training 这些概念上。

可以用一句话概括：

**目标不再只是运行一个智能体，而是拥有一个能根据真实结果对智能体进行度量和改进的闭环。**

这正是我认为开发者应该关注的地方。

因为一旦你这样看，持久的资产就不只是模型或 prompt 了，而是它周围的系统：

- 它运行的 environment
- 给它打分的 rubric
- 解释发生了什么的 traces
- 改进配置的 optimizer

这是一种更适合企业的思考方式。

## 即使你不做 RL 研究，这也很重要

说实话，OpenEnv、post-training、world-modeling 这些术语很容易让很多开发者立刻失去兴趣。

但实际结论比术语简单得多。

即使你从不直接碰训练闭环，这项工作也在塑造未来智能体开发的平台故事：

- evaluations 变成 first-class
- optimization 从偶尔发生变成持续发生
- environments 变成可复用资产
- 更好的智能体行为变成可度量的东西，而不只是“demo 里感觉更好”

这是向前迈出的一大步。

## 我的看法

这次公告最聪明的地方不是某个具体研究细节。

而是 framing。

Microsoft 显然正在把生态从静态 prompt engineering 推向 **outcome-driven 智能体系统**。这些系统可以被评估、调优、治理，并逐步改进。

真正的平台价值就在这里。

如果你今天正在构建智能体，哪怕只是在应用层，也值得关注这个方向会走向哪里。

原文：[面向结果的学习系统：借助 OpenEnv 和 Foundry 的企业级 RL](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)