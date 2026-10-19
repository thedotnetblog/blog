---
title: "Aspire + Agent Framework 开始看起来像是真正的多智能体技术栈"
date: 2026-06-13
author: "Emiliano Montesdeoca"
description: "新的 AlpineAI 示例展示了当 Aspire 和 Microsoft Agent Framework 被用于一个真正的分布式多智能体系统时的样子。重要的不是滑雪演示，而是其背后的架构模式。"
tags:
  - Aspire
  - Agent Framework
  - .NET
  - Microsoft Foundry
  - Architecture
---

多智能体演示现在到处都是。

问题是，很多演示正好在现实中最痛苦的部分之前停下来：部署形态、服务连接、健康状态、遥测、运行时边界以及分布式系统的纯粹混乱。

这就是为什么新的 **Aspire + Microsoft Agent Framework** 示例值得关注。

不，有趣的部分不是滑雪度假村礼宾场景。

有趣的部分是这个示例展示了一个更现实的模式来构建分布式智能体系统，具备：

- 定制托管智能体
- 提示智能体
- 多个运行时
- 服务引用
- 实时数据源
- 可观测性和部署结构

这才是真正的故事。

## 这不仅仅是"一个使用工具的智能体"

示例中的架构超越了熟悉的单循环智能体模型。

你拥有：

- 职责狭窄的专家智能体
- 协调它们的顾问智能体
- Foundry 管理的资源
- 同一图中的 .NET、Python 和 Go 服务
- 语音和聊天入口

这更接近严肃智能体系统在实际中的真实面貌。

而这就是 Aspire 突然变得非常重要的地方。

## Aspire 在做人通常记在脑子里的困难部分

这里我最喜欢的甚至不是智能体逻辑。而是**应用图是显式的**这一事实。

Aspire 被用来描述：

- 哪些服务存在
- 它们依赖什么
- 它们需要哪些模型部署
- 每个服务使用哪个运行时
- 存在哪些健康和部署关系

这很重要，因为分布式智能体系统会迅速变得混乱。如果拓扑只存在于人们的头脑和随机的设置文档中，你的系统会立刻变得脆弱。

把拓扑放在 AppHost 中是迈向可复现性的巨大一步。

## 专家智能体即工具仍然是值得关注的模式

我最喜欢的架构部分之一，是专家智能体作为可调用能力暴露给编排器的方式。

这种模式反复出现是有原因的。它给你：

- 关注点分离
- 更好的领域边界
- 更清晰的可观测性
- 更容易替换一个专家而无需重写所有东西

对于 .NET 团队来说，这比构建一个无所不知的巨型智能体并希望提示词指令保持其稳定要健康得多。

## 我的看法

这个示例证明的重要事情不是多智能体应用是可能的——我们早就知道了。

它证明的是微软技术栈开始为下一个问题提供连贯的答案：

**如何构建仍然可运维的多智能体系统？**

Aspire 负责图。Agent Framework 负责运行时抽象。Foundry 负责托管 AI 资源和托管。这个组合开始感觉不那么实验性，而更像一个真实的平台故事。

这就是我会关注的方向。

原文：[Distributed multi-agent systems with Aspire and Microsoft Agent Framework](https://devblogs.microsoft.com/aspire/building-distributed-multi-agent-systems-with-aspire-and-microsoft-agent-framework/)