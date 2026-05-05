---
title: "VS Code 1.116 — Agents应用获得键盘导航和文件上下文补全"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116专注于Agents应用的优化 — 专属快捷键、辅助功能改进、文件上下文补全，以及CSS @import链接解析。"
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "vscode-1-116-agents-app-updates.md" >}})。*

VS Code 1.116是2026年4月的版本，虽然比最近的一些更新更轻量，但变化是有针对性且有意义的 — 尤其是如果你每天都在使用Agents应用。

以下是基于[官方发行说明](https://code.visualstudio.com/updates/v1_116)的更新内容。

## Agents应用改进

Agents应用继续通过可用性优化不断成熟，这些改进在日常工作流中产生了真正的影响：

**专属快捷键** — 现在你可以用专属命令和键盘快捷键来聚焦更改视图、更改中的文件树，以及聊天自定义视图。如果你之前一直在Agents应用中到处点击来导航，这带来了完全由键盘驱动的工作流。

**辅助功能帮助对话框** — 在聊天输入框中按`Alt+F1`现在会打开一个辅助功能帮助对话框，显示可用的命令和快捷键。屏幕阅读器用户还可以控制播报的详细程度。良好的辅助功能让每个人受益。

**文件上下文补全** — 在Agents应用聊天中输入`#`来触发限定在当前工作区范围内的文件上下文补全。这是那些加速每次交互的小型生活质量改进之一 — 不再需要在引用代码时输入完整的文件路径。

## CSS `@import`链接解析

前端开发者的好消息：VS Code现在可以解析使用node_modules路径的CSS `@import`引用。当使用打包工具时，你可以通过`Ctrl+点击`跳转到像`@import "some-module/style.css"`这样的导入。虽小但消除了CSS工作流中的一个摩擦点。

## 总结

VS Code 1.116是关于改进的 — 让Agents应用更易导航、更易访问、更友好的键盘操作。如果你在Agents应用中花费大量时间（我猜很多人都是如此），这些变化会累积起来。

查看[完整发行说明](https://code.visualstudio.com/updates/v1_116)获取完整列表。
