---
title: "Visual Studio 五月更新真正关心的是如何更好地控制想法到变更之间的过程"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "Visual Studio 的五月更新加入了 Plan agent、更好的 skill 管理、context window 可见性，以及更强的多文件汇总 diff 体验。共同主题是更好地控制 AI-assisted inner loop。"
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}})。*

Visual Studio 五月更新最有意思的地方，不是某一个孤立功能。

而是它所呈现的共同方向。

这个版本持续改进的是以下几个阶段之间的空间：

- 一个想法
- 一个计划
- 一次生成的变更
- 一次 review
- 一个更精炼的结果

这正是 AI-assisted development 是否让人觉得可靠或混乱的关键。

## 功能列表很杂，但意图是统一的

从纸面上看，这个版本包含了很多东西：

- 新的 Plan agent
- skill 管理改进
- context window 可见性
- 多文件汇总 diff
- Copilot 相关 workflow 清理
- C++ 侧的 MSVC 更新

这看起来可能像一锅大杂烩。

我不这么认为。

主线其实很清楚：**Visual Studio 想让开发者在 AI-assisted 工作上拥有更多 control，同时又不拖慢他们。**

这正是应该追求的正确 trade-off。

## Plan agent 是这个版本的哲学中心

即使其他功能也很重要，我仍然认为 Plan agent 是这次更新中最能说明问题的部分。

它把很多人使用 coding agents 时都会有的感受明确了出来：

快速开始，并不总是等于有效推进。

这个版本通过让 planning、review 和 controlled implementation 成为更自然的顺序，强化了这一点。

这是健康的。

## multi-file diff 工作是一次悄无声息的大改进

我也认为 multi-file summary diff 值得更多认可，尽管它大概率不会得到很多关注。

当 agents 一次修改多个文件时，review experience 本身就成了产品。

如果 review changes 的感觉很乱，开发者对 workflow 的信任就会下降。

如果 review changes 的感觉连贯，开发者就更可能继续使用这个工具。

这就是统一 summary view 如此重要的原因。它降低了对生成工作说 yes 或 no 的认知成本。

## context window indicator 比听起来更聪明

我也喜欢 context usage 指示器。

这看起来可能只是一个小细节，但它解决了一个非常现实的 AI workflow 问题：不知道工具什么时候开始忘记对话前面的内容。

把这一点可视化是个很好的设计决定。

它不会神奇地扩大模型 context，但它让限制变得可观察，而这通常就是最好的下一步。

## 我的看法

这次更新真正关心的是，让开发者对 AI-assisted loop 拥有更多可见性和 control。

不是更多新奇。
不是更多混乱。
而是更多 control。

如果目标是在一个严肃的 IDE workflow 中让 AI tools 更值得信赖，那这正是应该投资的地方。

原文：[Visual Studio 五月更新——计划、review、refine](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)