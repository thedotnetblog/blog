---
title: "dotnet new WinUI：无需 Visual Studio 即可创建 Windows 应用"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI 项目模板现在可以通过 dotnet new 使用——空白应用、NavigationView 模式等。支持 VS Code，无需 Visual Studio，内置 Fluent Design 默认设置。"
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI 开发过去需要 Visual Studio。这一情况正在改变：Microsoft 发布了适用于 WinUI 的开源项目和项目模板，这些模板可与 `dotnet new` 配合使用，将 Windows 应用开发纳入标准 CLI 工作流。

## 三条命令即可开始

```shell
# 安装模板
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# 创建 NavigationView 应用
dotnet new winui-navview -n MyApp

# 运行
cd MyApp
dotnet run
```

无需 Visual Studio，无需手动配置项目。应用通过 `dotnet run` 运行。

## 包含的内容

**空白模板**（`dotnet new winui`）——现代化的起点，已连接 Fluent 标题栏，包含带 `.ico` 资源的更新默认应用图标，以及正确的浅色/深色模式默认值。比旧版空白模板更好，后者需要你自己配置基础设置。

**NavigationView 模板**（`dotnet new winui-navview`）——主从导航模式，完整连接了 NavigationView、现代标题栏和多页导航结构。遵循基于导航的应用的标准 Windows 应用轮廓。如果你要构建带侧边导航的应用，请从这里开始。

两个模板都开箱即遵循 [Windows 应用轮廓](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette)——用于布局、导航和视觉结构的现代 Fluent Design 模式。

## 为什么对非 Visual Studio 开发者很重要

使用 VS Code、Rider 或命令行工具的 WinUI 开发者一直处于不利地位。现有的 Visual Studio 模板无法在 VS 之外使用——必须手动重建项目结构并配置基础内容。

这些模板是开源的（参见 [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)），基于[社区反馈](https://github.com/microsoft/microsoft-ui-xaml/issues/10388)开发，现已可用。Visual Studio 支持正在开发中——这些相同的模板最终也将在那里运行。

对于希望自动化 WinUI 项目设置、将其集成到 CI 中，或者只是想使用 Visual Studio 以外的编辑器的团队来说，这是一个有意义的改进。

原文：[Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
