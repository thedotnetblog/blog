---
title: "Intelligent Terminal 0.1 是一次认真的 AI 原生 shell 体验起点"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Intelligent Terminal 0.1 加入了原生的 agent 面板、感知错误的帮助、后台任务，以及从 command palette 触发的 agent 流程。它仍然处于实验阶段，但方向非常有吸引力。"
tags:
  - Terminal
  - AI
  - GitHub Copilot
  - Developer Tools
  - Windows Terminal
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "index.md" >}})。*

我一直认为，终端是 AI 辅助开发最自然、也最有可能真正变得有用的地方之一。

因此，**Intelligent Terminal 0.1** 即使仍处于实验阶段，也让我觉得这是一个非常认真的发布。

有意思的地方不只是“在终端里聊天”，而是这些原生集成：

- agent 面板
- 错误检测
- 会话管理
- 后台任务
- 通过 command palette 启动的 agent 操作

它开始更像一个真正的 shell 体验，而不是贴在旁边的附加功能。

## 原文理解真正的痛点

原帖最好的地方之一，是它并没有从抽象的 AI 愿景开始。

它从一个非常普通的开发者体验开始：

> "**你有没有输入过一条 PowerShell 命令，结果报错，然后把它复制出来，打开浏览器，粘贴进去，再在多个论坛帖子之间来回跳转去修复它？**"

这个问题之所以成立，是因为它痛得太熟悉了。

终端里充满了这种小中断。

所以，如果 AI 要出现，它最应该出现的位置，就是这些中断的旁边。

## 为什么它比大多数终端 AI 演示更扎实

让它变得有意思的，不只是有一个 agent。

而是终端体验正在围绕开发者真实的工作方式被重新设计：

- 持久的 agent surface
- 来自 shell 输出的 context
- 错误出现时的快速帮助
- 后台任务启动
- 会话恢复
- 作为入口点的 command palette

这比一个挂在 shell 窗口上的漂浮 chatbot 更接近可用的 workflow。

## 这里真正的产品是 agent 面板

如果让我选设计里最重要的一部分，那可能就是 agent 面板。

为什么？因为它在两个不太好用的模式之间创造了一个中间地带：

- 完全离开终端
- 或者把所有交互都塞进 inline shell text

这是一个很好的设计选择。

它尊重终端作为工作表面的角色，同时也给 agent 留出了足够空间，让它不只是 autocomplete。

## 错误检测正是价值开始显现的地方

自动错误检测也正是这里该有的功能。

终端已经拥有 context。
错误已经发生。
而开发者仍然在 flow 里。

这让 shell 成为下面这些事情最适合的地方之一：

- 立即诊断
- 修复建议
- 快速迭代
- 不离开当前环境的后续推理

这不是魔法。只是把 workflow 放到了正确的位置。

## 我的看法

这还很早，但它是我目前见过的、关于终端 AI 最有说服力的方向之一。

不是因为它承诺魔法。
而是因为它始终贴近开发者已经在 shell 中工作的方式。

如果它继续朝这个方向演进，我认为它可能会成为 Microsoft 工具组合里最有趣的 AI native 开发体验之一。

原文：[Announcing Intelligent Terminal 0.1](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/)
