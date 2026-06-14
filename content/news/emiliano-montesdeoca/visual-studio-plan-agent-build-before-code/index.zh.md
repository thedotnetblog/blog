---
title: "Visual Studio 中的新 Plan agent 解决了一个非常真实的 AI 工作流问题"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "Visual Studio 的新 Plan agent 很重要，因为它在实现之前建立了一个结构化的规划阶段，而这正是大型功能和重构经常需要的。"
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "visual-studio-plan-agent-build-before-code.md" >}})。*

最让人沮丧的 AI 编码工作流之一，就是实现开始得太快。

代码从技术上说甚至可能没错，但它解决的是你脑海里那个问题的错误版本。

你想要的是 refactor，它却开始 rewrite。
你想要的是一个范围明确的改进，它却碰到了项目的一半。
你想讨论选项，它却直接跳到了文件修改。

这就是为什么 Visual Studio 中这个新的 **Plan agent** 如此有用。

## 这解决的是一个真实的工作流问题，而不只是表面问题

原文描述了一个非常熟悉的场景："**代码并不错……只是它不是你想要的。**"

这句话非常准确。

因为很多 AI-assisted development 的薄弱点，不在于模型能不能生成代码，而在于工作流是否在实现开始之前，为就工作的预期形态达成一致提供了足够空间。

这对以下情况尤其重要：

- 大型功能
- 不熟悉的 codebase
- 非平凡的 refactor
- 对架构敏感的变更
- 在开始编辑之前需要团队 review 的工作

在这些场景里，直接跳到实现通常是错误的做法。

## 当任务是真实需求时，planning 不是 overhead

我觉得团队有时会低估，过早开始实现会浪费多少时间。

如果 agent：

- 触碰了错误的 file
- 选择了错误的方法
- 漏掉了关键约束
- 忽略了必要的 edge case

那么所谓“快速”的开始，最终会变成一个更慢的整体 workflow。

这就是我喜欢这个功能的原因。

它为以下内容留出了空间：

- 澄清问题
- 起草计划
- 直接编辑计划
- 在代码更改开始前分享计划

这不是 bureaucracy。很多时候它只是好的 engineering。

## markdown plan file 是一个聪明的选择

我特别喜欢的一点是，每个 plan 都会保存到 `.copilot/plans/plan-{title}.md`。

这让 planning 步骤变得可触摸。

也就是说，plan 不会被困在 chat transcript 里。它会变成你可以：

- review
- edit
- mentally version 管理
- 与队友讨论
- 更有意识地交给 implementation

这让这个功能感觉比“生成代码前的一段临时前言”要严肃得多。

## 这就是 AI workflow 开始尊重团队流程的地方

我认为这也是这些工具正在成熟的一个强烈信号。

最好的 AI developer workflow 不是把所有中间步骤都去掉，而是改进正确的中间步骤。

而 planning 就是其中之一。

如果 plan 足够强，implementation 就更容易。
如果 plan 很弱，implementation 就会变得嘈杂。

这个功能直接承认了这一点。

## 我的看法

这不只是一个 AI nicety。

这是 workflow 改进。

对于真实的功能和真实的 refactor 来说，这正是那种可以节省大量不必要 churn、review noise，以及“这不是我想表达的意思”式 rework 的改进。

我认为，越来越多的 agent experience 最终都会需要类似的东西。

Visual Studio 更早地做到这一点，而且方式很实用。

原文：[在构建前先规划：介绍 Visual Studio 中的 Plan agent](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)