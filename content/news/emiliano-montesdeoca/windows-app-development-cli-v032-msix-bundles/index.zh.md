---
title: "Windows App Development CLI 正在成为实际打包工作的更实用工具"
date: 2026-06-19
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3.2 增加了 MSIX bundle 支持、更智能的项目初始化以及更好的自动化行为。对于专注 Windows 的 .NET 团队来说，这让它更适合成为真实打包工作流的一部分。"
tags:
  - Windows
  - .NET
  - WinUI
  - WPF
  - Developer Tools
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "windows-app-development-cli-v032-msix-bundles.md" >}})。*

我喜欢那些能去掉没人愿意手动做的烦人步骤的工具更新。

这基本上就是 **Windows App Development CLI v0.3.2** 的故事。

这个版本增加了更好的 bundling、更智能的初始化、更干净的截图支持，以及更可靠的非交互式行为。单独看这些都不算炫，但放在一起，它让这个 CLI 对于真正做 Windows 应用打包和交付的团队来说更值得信赖。

## MSIX bundle 支持成为重点是有原因的

这里最强的新增功能是 **MSIX bundle 支持**。

如果你要把 Windows 应用发布到多个架构，一个更简单的路径生成正确的 `.msixbundle` 很重要。Microsoft Store 的流程、打包流程以及多架构交付，都会在 CLI 能直接承担更多这部分工作时变得不那么麻烦。

这就是那种能让工具从“有趣的 preview" 变成“也许我真的会把它留在 toolchain 里”的功能。

## 更智能的 `winapp init` 也比听起来更重要

`winapp init` 的改进属于那种人们会在亲自踩到痛点之前低估的东西。

自动检测兼容项目、更干净地处理多种项目类型，以及在非交互式 shell 中表现更好，让这个 CLI 对脚本驱动和 CI 驱动的 setup 更加现实。

这对严肃的团队来说很重要。

## 为什么这对 .NET 开发者相关

如果你处在 .NET 世界中仍然非常关注以下内容，那尤其值得跟进：

- WPF
- WinUI
- desktop packaging
- Store 提交
- Windows-native 分发

这些领域并不总能得到和 cloud 或 AI tooling 相同程度的热度，但它们对真实产品仍然非常重要。

## 我的看法

Windows App Development CLI 仍然处于早期，但像这样的版本正是工具赢得信任的方式。

更好的打包、更好的初始化行为，以及更好的自动化支持，正是会让一个 preview tool 开始真正显得有用的那类改进。

原文：[Windows App Development CLI v0.3.2 — bundling 支持、更智能的初始化，以及更多](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-2-bundling-support-smarter-initialization-and-more/)