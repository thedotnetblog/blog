---
title: "GitHub Copilot 和 Claude Code 的 WinUI 智能体插件"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft 发布了用于 WinUI 开发的智能体技能：脚手架、构建、运行、测试、迭代，全部通过 GitHub Copilot CLI 或 Claude Code 完成。核心创新：专用工具将智能体锚定在 WinUI 特定的事实中。"
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft 发布了用于 WinUI 应用程序开发的开源智能体技能集，可在 [aka.ms/winui-skills](https://aka.ms/winui-skills) 获取。

## 安装与配置

使用 `/plugin install winui@awesome-copilot` 安装插件，然后使用 `/winui:winui-setup` 运行初始配置。设置过程会验证前提条件、安装必要的依赖项并为 WinUI 应用程序开发配置环境。

## 端到端开发循环

这些技能涵盖完整的开发周期：

- **脚手架：** 使用 `dotnet new WinUI` 和适当的参数生成正确的项目模板 — 智能体知道正确的模板和默认配置值。
- **构建：** 管理 WinUI 应用程序所需的打包执行模型，包括包签名和清单配置。
- **交互与验证：** 启动应用程序、与其交互并验证行为。
- **修复编译错误：** 智能体理解 WinUI 特定的错误消息，并知道如何解决它们。

## 通过专用工具提高令牌效率

核心创新在于这些技能包含专用工具，可按需获取具体的参考数据：

- WinUI 和 Fluent Design API 详情
- MVVM 模式和最佳实践
- MSIX 打包、代码签名和 Store 提交
- 可访问性、主题和 UI 自动化

工具不是将所有 WinUI 文档注入上下文，而是在智能体需要时精确获取所需内容。这在智能体运行可能产生数千行输出的构建周期或测试套件时保持上下文使用的高效性，并提高专业领域的精度。

## 为什么专用技能很重要

通用语言模型对 WinUI 特定的细节了解有限：打包执行模型、Fluent Design API、MSIX 集成或 Windows App SDK 包装 Win32 功能的特定方式。专用工具通过将智能体锚定在已验证的 WinUI 事实中来解决这个问题，而不是依赖可能过时或不正确的模型知识。

同样的模式适用于任何具有自身规范和要求（与通用开发模式不同）的专业框架或 SDK。

原始文章：[A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
