---
title: "Azure Developer CLI 正在持续变成更好的 inner loop 工具"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "2026 年 5 月和 6 月的 Azure Developer CLI 版本加入了很多内容，但最大的价值在于它们如何改进日常循环：更好的工具管理、更安全的 provisioning、更强的扩展支持，以及更实用的执行流程。"
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*本文已自动翻译。要查看原文，请[点击此处]({{< ref "index.md" >}})。*

大型 CLI 综述往往读起来很累，因为它们会把重要的工作流改进和小修小补混在一堵文字墙里。

所以这里给出我的简短版本：最近的 **Azure Developer CLI** 更新很重要，因为 `azd` 正在持续成为一个 **更好的 inner loop 工具**，而不只是 deployment 包装器。

这才是最重要的变化。

## 工具管理正在成为产品的一部分，而不是旁支任务

我最喜欢的新增内容之一是新的 `azd tool` 命令。

任何能降低配置摩擦的东西都值得关注，尤其是在工作环境依赖 SDK、CLI、Docker、Bicep 和扩展组合的项目里。

如果工具现在能够直接帮助发现、安装、检查和更新这些依赖，那么它就能去掉很多最先困扰新人的烦人失败模式。

这才是真正的价值。

## `azd exec` 也比名字听起来更重要

乍一看，`azd exec` 可能只是一个小小的便利功能。

我不这么看。

带着完整的 `azd` 环境上下文执行命令，包括 secret resolution，正是那种能让本地自动化和 scripting 变得更干净的能力。

这减少了额外 glue 脚本的需求，也有助于让不同环境之间的执行保持一致。

这是一种实实在在的提升。

## 更安全的 provisioning 和更好的取消行为是被低估的改进

这个版本还包括 provisioning dependency、取消处理和 deployment behavior 方面的变化。这些东西可能不显眼，但非常受欢迎。

交互式取消提示、更好的 dependency modeling，以及更清晰的 deployment 状态，正是会让 CLI 在处理真实 Azure 资源时显得可靠的那类改进。

而信任对于这样的工具来说非常重要。

## 我的看法

`azd` 在 setup、scripting、部署安全性和扩展支持方面越进步，它就越像一个你可以放在日常循环里的工具，而不是只在 deployment 前才碰一下的东西。

这才是正确方向。

对于在 Azure 上构建 cloud-native 或 AI-driven 应用的团队来说，这会让 CLI 在最重要的地方更有用：真实开发过程中。

原始文章：[Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)