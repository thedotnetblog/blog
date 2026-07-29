---
title: "智能体框架之所以重要，是因为提示词本身还不够"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "新的 Microsoft Agent Framework claw 和 harness 实践教程是一个有用的提醒：真正的智能体需要模型外的运行时外壳——工具、规划、记忆、会话以及一个实用的执行循环。"
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

智能体开发中最容易犯的错误之一，就是以为提示词就是产品本身。

其实不是。

新的 **agent harness 和 claw** 实践教程来自 Microsoft Agent Framework 团队，它的价值在于将焦点保持在真正决定智能体是否好用的部分上：模型的运行时外壳。

这包括：

- 工具
- 规划
- 会话状态
- 记忆
- 执行模式
- 可用的控制台或迭代交互界面

正是这些让智能体从巧妙的演示变成真正的软件。

## Harness 模式是一种实用的模式

我欣赏的是这个想法多么平易近人。

从一个聊天客户端开始。

然后将其包裹到带有指令和工具的 harness 中。

然后通过支持规划、待办事项、会话和流式交互的 shell 来运行它。

这是一个健康的模式，因为它清晰地区分了关注点：

- 模型负责推理
- harness 负责运行时行为
- 应用决定哪些工具和体验是重要的

## 这非常契合 .NET 开发者的构建方式

Harness 的概念也与 .NET 的思维方式完美匹配。

当运行时行为是显式的且可组合时，我们通常能做得更好。中间件、管道、选项、提供者和适配器在这个世界中都感觉很自然。

这就是为什么我认为 Agent Framework 有很大机会在 .NET 开发者中落地。它没有强迫每个人都进入一个神奇的抽象层，而是提供了你可以组合在一起的结构化运行时组件。

## 我的看法

这篇文章最有用的部分在于提醒我们，智能体需要的不仅仅是好的模型和巧妙的指令字符串。

它们需要一个提供结构、记忆、工具访问、规划以及可工作的开发者循环的运行时外壳。

这就是 harness 给你的。

老实说，这就是为什么这个模式值得关注。

原文：[Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)