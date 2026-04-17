---
title: "别再盯着终端了：Aspire 的分离模式改变了工作流程"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 让你在后台运行 AppHost 并释放终端。结合新的 CLI 命令和代理支持，这比听起来重要得多。"
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "aspire-detached-mode-free-your-terminal" >}})。*

每次运行 Aspire AppHost，你的终端就没了。被锁住了。一直占用到你按 Ctrl+C 为止。需要快速运行个命令？打开另一个标签页。想查看日志？再开一个标签页。这是一种小摩擦，但积少成多。

Aspire 13.2 解决了这个问题。James Newton-King [写了完整的详情](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/)，说实话，这是那种一用就立刻改变工作方式的功能。

## 分离模式：一条命令，终端回来了

```bash
aspire start
```

这是 `aspire run --detach` 的简写。你的 AppHost 在后台启动，终端立即回到你手中。不需要额外的标签页。不需要终端多路复用器。就是你的提示符，随时可用。

## 管理正在运行的进程

关键在于——在后台运行只有在你能管理那些进程时才有用。Aspire 13.2 为此提供了一整套 CLI 命令：

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

这让 Aspire CLI 变成了一个真正的进程管理器。你可以启动多个 AppHost，检查它们的状态，跟踪日志，然后关闭它们——全部在一个终端会话中完成。

## 与隔离模式结合使用

分离模式与隔离模式天然搭配。想在后台运行同一个项目的两个实例而不产生端口冲突？

```bash
aspire start --isolated
aspire start --isolated
```

每个实例都会获得随机端口、独立的密钥和自己的生命周期。用 `aspire ps` 查看两者，用 `aspire stop` 停掉不需要的那个。

## 为什么这对编码代理意义重大

这才是真正有趣的地方。在你的终端中工作的编码代理现在可以：

1. 用 `aspire start` 启动应用
2. 用 `aspire describe` 查询状态
3. 用 `aspire logs` 检查日志来诊断问题
4. 完成后用 `aspire stop` 停止应用

所有操作都不会失去终端会话。在分离模式之前，运行你的 AppHost 的代理会把自己锁在终端里。现在它可以启动、观察、迭代和清理——这正是你期望自主代理的工作方式。

Aspire 团队在这方面下了功夫。运行 `aspire agent init` 会设置一个 Aspire 技能文件，教会代理这些命令。这样，像 Copilot 的编码代理这样的工具就能直接管理你的 Aspire 工作负载。

## 总结

分离模式是一个伪装成简单标志的工作流升级。你不再需要在终端之间切换上下文，代理不再阻塞自己，新的 CLI 命令让你真正看到正在运行的内容。它实用、干净，让日常开发循环明显更顺畅。

阅读[完整文章](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/)了解所有详情，并通过 `aspire update --self` 获取 Aspire 13.2。
