---
title: "Visual Studio 在 Build 2026 上最有意思的公告，是关于减少摩擦"
date: 2026-06-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 在 Build 2026 的公告指向了一个清晰方向：更强的 AI 集成、更好的 merge conflict 处理、改进的现代化流程，以及更少打断 inner loop 的小中断。"
tags:
  - Visual Studio
  - GitHub Copilot
  - Microsoft Build
  - AI
  - Modernization
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "visual-studio-build-2026-announcements-what-matters.md" >}})。*

Visual Studio Build 的最新公告，可以用一句话概括：**把摩擦从真正的工作里拿掉**。

这一点体现在很多地方：

- 处理 debugging、profiling 和 testing 的智能体
- 在 build 开始前更早的反馈
- AI 辅助的 merge conflict 处理
- 帮助老旧 .NET 应用现代化
- 更灵活的模型和 key 选择

## 这份 roadmap 比很多 AI 话术更落地

我最欣赏原始公告的一点，是它始终贴近开发者真实的痛点。

甚至还有一句话直接点中了核心：

> "**Code 是资产，不只是制品。**"

这比大多数泛泛的 AI 工具口号都更好的 framing。

因为一旦你接受 code 是资产，接下来的问题就很自然：到底有哪些工具真的能帮助你把这个资产保持健康、易懂，并且更容易演进？

这份 roadmap 正在朝那个方向走。

## 最有说服力的部分仍然是 debugger/profiler/test 连接

我一直觉得，Visual Studio 最好的 AI 故事不是孤立的代码生成。

而是 AI 与 Visual Studio 原本就擅长的能力并肩工作：

- debugging
- profiling
- testing
- 大型 codebase 的诊断

这也是为什么那个关于 agents 可以“debug、profile 和 test”的公告特别有意思。

因为如果 Visual Studio 能把 runtime signals 和 agent assistance 连接到一个真正帮助团队更快解决真实问题的 workflow 里，那它的价值会远高于又一个 autocomplete demo。

## merge conflict 帮助是人们真正会感受到的功能

AI 辅助冲突解决也是一个很好的例子。

没有人会满怀期待地醒来，想着要去解决 merge conflict。

所以如果工具能减少手工劳动，又不会对开发者隐藏太多，那就是实打实的体验提升。这类功能不会霸占头条，但会让日常工作少一些烦躁。

## 现代化方向也非常实用

我也喜欢 Visual Studio 持续推进 modernizaton，而且方式更偏渐进而不是戏剧化。

如果团队能够用 AI 辅助 workflow 去：

- 推进老应用
- 把 Aspire 带入现有系统
- 更安全地迁移旧 web stack

那么价值就会更容易在内部解释。

这比那种模糊的“AI 改变一切”说法更有说服力。

## 我的看法

我最喜欢这里的一点，是方向始终贴着开发者每天的痛点，而不是抽象的 AI 野心。

这让 roadmap 更可信。

这个公告里最好的部分，是那些减少真实工作摩擦的内容：修 bug、处理冲突、现代化现有应用，以及压缩分析到行动之间的循环。

这正是 Visual Studio 应该投资的地方。

原文：[Visual Studio 接下来会有什么：我们的 Microsoft Build 2026 公告](https://devblogs.microsoft.com/visualstudio/whats-coming-next-in-visual-studio-our-microsoft-build-2026-announcements/)