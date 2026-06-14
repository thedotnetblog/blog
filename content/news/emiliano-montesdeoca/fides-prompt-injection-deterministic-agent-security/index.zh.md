---
title: "FIDES 正是我想看到更多的那种确定性代理安全故事"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Agent Framework 中新的 FIDES 能力之所以重要，是因为它们把对 prompt injection 的防御从启发式方法，转向基于标记内容和 middleware 检查、可强制执行的策略。"
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *本文已自动翻译。查看原文，请[点击这里]({{< ref "index.md" >}})。*

对 prompt injection 的防御常常让人感觉像是站在不稳的地面上。

你加入更强的 system prompt。你加入一个过滤器。你放上一些 allowlist。然后希望下一个奇怪输入不会破坏假设。

这就是 **FIDES** 有意思的地方。

这个故事最强的部分在于，它把安全性推向更具确定性的方向：

- 为内容打标签
- 标签在工作流中传播
- 在受权限工具执行前通过 middleware 强制执行
- 围绕不可信上下文可以影响什么，建立清晰的策略边界

## 原文的表达直截了当，而且很到位

它一开头就说 prompt injection 是 "**OWASP LLM Top 10 中的头号风险**"。

很好。

我喜欢这里这种直白，因为太多团队仍然把代理安全当成未来的问题，而不是当前的 runtime 设计问题。

接着文章给出了一个很实用的对比：当前大多数防御都是启发式的，而 FIDES 试图把系统推向策略和强制执行。

这正是正确的转变。

## 为什么它比另一篇安全 whitepaper 更有说服力

很多关于 AI 安全的文章都停留在抽象层面。

这篇文章做得更好。它围绕一个非常具体的例子展开：一个 GitHub issue triage agent、恶意 issue body、受权限的文件读取，以及试图通过 public comment 泄漏信息。

这很有用，因为它把整个讨论锚定到了真实的工作流里。

一旦你看到这个场景，确定性控制的价值就更容易理解了。

## 核心想法不是“让模型更聪明”

这里最重要的一点是，FIDES 并没有要求模型魔法般地更擅长发现攻击。

它在改变 runtime contract。

这意味着：

- 内容会被标记
- 标签会继续传播
- 工具会声明自己接受什么
- middleware 会在执行前阻止不安全路径

这是一种健康得多的方法。

因为一旦代理能够调用具有真实后果的工具，安全就不能只取决于模型今天状态好不好。

## 我的看法

这正是我想更多看到的代理安全方向。

不是“相信模型会忽略坏指令”，而是“把 policy fence 建进 runtime 里面”。

这是一种健康得多的模型。

而且如果代理框架想在生产环境中被认真对待，它们就需要更多这样的故事。

原文链接： [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)