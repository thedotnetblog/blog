---
title: "Agent Harness、Hosted Agents 和 CodeAct：这就是我会重点关注的 Agent Framework 更新"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Build 2026 的 Agent Framework 公告信息量很大，但最值得关注的主线是 harness 模型、Foundry 托管的 hosted agents，以及用于降低编排开销的 CodeAct。"
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Build 上这次 Agent Framework 的大公告涵盖很多内容，但有三条主线最先吸引我：

- **harness 正在成为更接近一等公民的运行时能力**
- **Foundry 托管的 hosted agents 提供了一条走向生产的路径**
- **CodeAct 正在减少多步骤编排的开销**

这些就是我会一直盯着的部分。

## harness 正在成为真正的重心

原文把 harness 描述为模型推理与真实执行交汇的层。

这个描述非常准确，也正因为如此，我认为这一部分比很多单独的功能点都更重要。

一旦 agent 需要：

- 文件访问
- Shell 执行
- 规划模式
- 待办事项
- 会话记忆
- 审批工作流

你谈的就不再只是 prompt 加 model。

你谈的是运行时行为。

这正是框架要么真正有用、要么沦为玩具的分界线。

而 Microsoft Agent Framework 显然正在努力让这一层变得更有用。

## Hosted agents 才是本地到生产故事真正落地的地方

我也认为 hosted agents 这一部分是本次公告里战略意义很强的一部分。

原文明确说，这是一种把那个 agent 送上生产环境的最简单方式。

这句话很重要，因为大多数 agent framework 目前在本地实验上仍然远强于真正的运营部署。

如果 Foundry 的 hosted agents 真的能让从本地开发迁移到以下这些能力更容易：

- 扩展
- 可观测性
- 托管身份
- 会话处理
- 版本管理

那它就补上了当前 agent 生态里最大的缺口之一。

这是一个实打实的提升。

## CodeAct 是这次更新里最令人兴奋的技术思路

如果要我挑最有意思的技术概念，我大概率会选 CodeAct。

它要解决的问题很真实：太多多步骤 agent 工作流之所以昂贵，是因为编排循环本身就消耗了太多 model 轮次。

所以当原文给出这样的结果时：

- 52.4% faster
- 63.9% fewer tokens

我会立刻注意。

当然，这些是和代表性工作负载绑定的基准数据，不是普遍规律。但更大的想法依然很有吸引力。

如果模型能把工具调用链压缩成更高效的执行形态，agent 系统的经济性就会明显改变。

## 我认为开发者真正应该从这次更新中带走什么

重要的不是发布了多少功能。

更重要的是，框架正在这些真实应用最需要的地方变强：

- 运行时层
- 部署路径
- 执行效率
- 内建的运维模式

这类成熟度信号，比再来一份表面的 AI 功能清单更值得我关注。

## 我的看法

这次更新之所以重要，不只是因为它增加了更多表面能力。

它在强化围绕 agent 的 runtime 和 deployment 故事，而且这种强化应该对真正的应用场景有意义，尤其是那些想从本地实验走向可实际运行、可维护系统的团队。

这就是 framework 变得更有吸引力的地方。

如果我要紧盯这次发布，harness、hosted agents 和 CodeAct 一定是我最关注的部分。

原文： [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
