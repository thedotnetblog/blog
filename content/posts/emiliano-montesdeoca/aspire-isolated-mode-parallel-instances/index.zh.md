---
title: "Aspire的隔离模式解决了并行开发中端口冲突的噩梦"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2引入--isolated模式：随机端口、独立密钥，运行同一AppHost的多个实例时零冲突。完美适用于AI智能体、worktree和并行工作流。"
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "aspire-isolated-mode-parallel-instances" >}})。*

如果你曾试过同时运行同一个项目的两个实例，你就知道那种痛苦。端口8080已被占用。端口17370已被使用。杀掉进程、重启、摆弄环境变量 — 这是生产力杀手。

这个问题在变得更严重，而不是更好。AI智能体创建git worktree来独立工作。后台智能体启动独立环境。开发者为了功能分支两次checkout同一个仓库。每一个场景都撞上了同一堵墙：同一个应用的两个实例在争夺相同的端口。

Aspire 13.2用一个flag就解决了这个问题。Aspire团队的James Newton-King[写了完整的细节](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/)，这是那种"我们怎么之前没有这个"的功能。

## 解决方案：`--isolated`

```bash
aspire run --isolated
```

就这样。每次运行获得：

- **随机端口** — 实例间不再冲突
- **隔离的用户密钥** — 连接字符串和API密钥在每个实例间保持独立

不需要手动重新分配端口。不需要摆弄环境变量。每次运行自动获得一个干净的、无冲突的环境。

## 这个功能发光的真实场景

**多次checkout。** 你有一个功能分支在一个目录，一个bugfix在另一个：

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

两个都无冲突运行。仪表盘显示什么在运行以及在哪里运行。

**VS Code中的后台智能体。** 当Copilot Chat的后台智能体创建git worktree来独立处理你的代码时，它可能需要运行你的Aspire AppHost。没有`--isolated`，这就会和你的主worktree产生端口冲突。有了它，两个实例就能正常运行。

`aspire agent init`附带的Aspire技能会自动指导智能体在worktree中工作时使用`--isolated`。所以Copilot的后台智能体应该能原生处理这个问题。

**开发同时运行集成测试。** 需要在继续开发功能的同时对活跃的AppHost运行测试？隔离模式给每个上下文提供独立的端口和配置。

## 底层工作原理

当你传递`--isolated`时，CLI会为该运行生成一个唯一的实例ID。这驱动两个行为：

1. **端口随机化** — 不再绑定到AppHost配置中定义的可预测端口，隔离模式为所有内容选择随机可用端口 — 仪表盘、服务端点，全部。服务发现自动调整，所以服务能找到彼此，不管它们落在哪个端口上。

2. **密钥隔离** — 每个隔离运行获得自己的用户密钥存储，以实例ID为键。一次运行的连接字符串和API密钥不会泄露到另一次运行中。

你的代码不需要任何改动。Aspire的服务发现在运行时解析端点，所以不管端口分配如何，一切都能正确连接。

## 何时使用

当同时运行同一AppHost的多个实例时使用`--isolated` — 无论是并行开发、自动化测试、AI智能体还是git worktree。对于偏好可预测端口的单实例开发，常规的`aspire run`仍然可以正常使用。

## 总结

隔离模式是一个解决真实且越来越常见问题的小功能。随着AI辅助开发推动我们走向更多并行工作流 — 多个智能体、多个worktree、多个上下文 — 能够简单地启动另一个实例而不必争夺端口是必不可少的。

阅读[完整文章](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/)获取所有技术细节，并用`aspire update --self`获取13.2来试用。
