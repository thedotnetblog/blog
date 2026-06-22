---
title: "在 Visual Studio 里面审查 pull request，正是我喜欢的那种减少摩擦"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio 现在可以在不离开 IDE 的情况下，从头到尾审查 pull request。它听起来可能只是增量改进，但对于整天都待在 Visual Studio 里的团队来说，它能减少很多不必要的上下文切换。"
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}})。*

浏览器在 code review 工作流中占用了太多太久的比重。

所以我非常高兴看到 Visual Studio 继续向 **在 IDE 内端到端审查 pull request** 迈进。

这类功能也许不会制造巨大头条，但它确实能改善日常开发体验。

## 主要价值很简单：更少的 context switching

当你的 review loop 一部分在 IDE 里，一部分在浏览器里时，摩擦就会累积：

- 在别处打开 PR
- 用一个工具检查变更
- 回到 solution 深入调查
- 再切一次去评论或批准

这不算灾难，只是效率不高。

如果 Visual Studio 能让你在同一个工作环境里打开、检查、评论、批准并 merge，这就是真正的生产力提升。

## “不 checkout 就 review” 这个选项尤其好

我特别喜欢的一点，是可以在不 checkout PR 分支的情况下进行 review。

这听起来很小，但它特别适合：

- 快速 review pass
- 被打断时收到的反馈请求
- 保持当前分支和本地状态不变

这正是优秀 code review 工具需要的灵活性。

## 我的看法

这不是一个革命性的功能。

它更好：它很实用。

对于大部分时间都待在 Visual Studio 里的团队来说，更紧密的 PR review 支持意味着更少的 workflow 中断，以及从检查到行动更顺畅的路径。

在我看来，这样的改进很值得。

原文：[无需离开 Visual Studio 即可审查 pull request](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)