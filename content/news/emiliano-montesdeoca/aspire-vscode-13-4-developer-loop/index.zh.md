---
title: "VS Code 中的 Aspire 13.4 以恰到好处的方式收紧了开发者循环"
date: 2026-06-16
author: "Emiliano Montesdeoca"
description: "VS Code 中的 Aspire 13.4 不仅仅是一个功能更新。它通过更好的调试、资源可见性、面板集成和 TypeScript AppHost 支持，切实改善了日常开发循环。"
tags:
  - Aspire
  - VS Code
  - .NET
  - Developer Experience
  - TypeScript
---

最好的工具更新是那些用了几天后就能感受到的，而不是那些只在发布说明中看起来不错的。

这就是我对 **VS Code 中的 Aspire 13.4** 的感受。

这次更新全部关于收紧内循环：更快地创建项目、更自然地调试混合语言资源、直接在编辑器中显示健康状态和命令、保持仪表盘触手可及但又不让它成为唯一的工作空间。

这是一个非常好的方向。

## 最大的胜利是减少上下文切换

如果你认真使用 Aspire，你通常需要在多个界面之间切换：

- AppHost 代码
- 终端
- 仪表盘
- 日志
- 调试会话
- 服务端点

13.4 做得好的地方在于减少了这些界面之间的摩擦。

新的 VS Code 体验让你在你已经在工作的地方就能看到更多的应用状态：

- 编辑器中的资源健康状态
- 资源声明旁边的命令
- 更便捷的仪表盘访问
- 从 AppHost 上下文中访问日志
- 即使在完整调试开始之前也有用的面板

这听起来很小，直到你每天都要用到它。

## 混合栈调试比人们想象的更重要

这次更新中最强大的部分之一，是在一个 Aspire 驱动的流程中更自然地调试 **C#、TypeScript、Python、Go、浏览器应用和 Azure Functions**。

这反映了现代应用的真实形态，远好于假装所有东西都运行在同一个运行时中。

对 .NET 开发者来说尤其有价值，因为我们中的许多人现在正在构建混合 API 项目、前端、工作进程和不同语言的 AI 相关服务的系统。

Aspire 在 VS Code 内部让这一切感觉更统一，是一个非常实际的改进。

## TypeScript AppHost 支持达到 GA 也很有意义

我不会忽视该版本中的 TypeScript AppHost 方面。

Aspire 对 C# 和 TypeScript 都变得更加自然，扩大了可以在同一系统模型中工作的人员范围，而无需奇怪的一等公民处理方式。这对于平台代码、前端代码和服务编排紧密共存的团队来说很重要。

## 我的看法

VS Code 中的 Aspire 13.4 不是关于一个杀手级功能。它关于打磨日常开发循环中的粗糙边缘：

- 更快地启动
- 在你写代码的地方看到更多状态
- 更自然地调试
- 只在需要时才跳转到日志和仪表盘

这正是好的工具应有的演进方式。

如果你已经在使用 Aspire，这次更新值得安装。如果你还在犹豫 VS Code 是否是 Aspire 开发的可靠环境，答案正变得越来越明显。

原文：[Aspire in VS Code: the 13.4 developer loop](https://devblogs.microsoft.com/aspire/aspire-vscode-extension-13-4/)