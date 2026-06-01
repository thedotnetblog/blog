---
title: "Model router 的 eval 是太多团队跳过的一步"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Foundry 中新的 model router evaluation repo 很重要，因为在团队把自动模型选择当成魔法之前，路由决策就应该先拿质量、延迟和成本来衡量。"
tags:
  - Microsoft Foundry
  - AI
  - Evaluations
  - Model Router
  - Cost Optimization
---

> *本文已自动翻译。原文请[点击这里]({{< ref "index.md" >}})。*

自动模型路由听起来很棒，直到你意识到，你仍然需要证明它对你的 workload 来说确实是正确选择。

这就是新的 **model router evaluation repo** 有用的原因。

它为团队提供了更具体的方式来回答那些真正重要的问题：

- 路由是否保留了质量？
- 它是否改善了成本？
- 它对延迟有什么影响？
- 如果我限制 model subset，会发生什么变化？

## 原文提出了正确的问题

我特别喜欢原文的一点是，它没有把 model router 当成理所当然的好东西。

相反，它提出了那些让人不舒服但正确的问题：

- "**在我的 prompts 上，model router 自动选择的 model 是否能与我原本会选择的 single model 持平甚至更好？**"
- "**我到底是真的在端到端节省钱，还是只是把支出从一个地方转移到另一个地方？**"

这才是正确的态度。

因为自动路由虽然很有吸引力，但它仍然是一个 system decision。而 system decision 应该被衡量，而不是被欣赏。

## 为什么这个 repo 比第一眼看到的更重要

在一个层面上，这只是一个 evaluation repo。

在另一个层面上，它是成熟度的信号。

它在说：如果你想采用自动路由，这里有一种更有纪律的测试方式：

- 质量
- 成本
- 延迟
- subset trade-off
- model distribution 行为

这比把 routing 当成一个有好品牌的黑盒要好得多。

## 我的看法

这是 AI platform 更需要的那类 tooling 的一个好例子：不是更多魔法，而是在信任魔法之前，提供更多验证它的方法。

这就是团队避免在未经测试的假设上建立昂贵信心的方式。

原文： [How to run evals for the model router](https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/)
