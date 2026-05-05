---
title: "那个你不知道的Visual Studio浮动窗口设置（但你应该知道）"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Visual Studio的一个隐藏设置让你完全控制浮动窗口 — 独立的任务栏条目、正确的多显示器行为，以及完美的FancyZones集成。一个下拉菜单改变一切。"
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "visual-studio-floating-windows-powertoys.md" >}})。*

如果你在Visual Studio中使用多个显示器（说实话，现在谁不用呢？），你可能经历过这种烦恼：浮动工具窗口在你最小化主IDE时消失，它们总是在所有窗口之上，而且不会在任务栏中显示为单独的按钮。这对某些工作流有效，但对多显示器设置来说很令人沮丧。

Visual Studio团队的Mads Kristensen [分享了一个鲜为人知的设置](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/)，它完全改变了浮动窗口的行为。一个下拉菜单。就这样。

## 设置

**Tools > Options > Environment > Windows > Floating Windows**

下拉菜单"These floating windows are owned by the main window"有三个选项：

- **None** — 完全独立。每个浮动窗口都有自己的任务栏条目，行为就像普通的Windows窗口。
- **Tool Windows**（默认）— 文档自由浮动，工具窗口保持与IDE绑定。
- **Documents and Tool Windows** — 经典的Visual Studio行为，所有窗口都绑定到主窗口。

## 为什么"None"是多显示器设置的最佳选择

将其设置为**None**，突然间你所有的浮动工具窗口和文档都像真正的Windows应用程序一样运行。它们出现在任务栏中，当你最小化Visual Studio主窗口时保持可见，并且不再强制自己始终在最前面。

将此与**PowerToys FancyZones**结合使用，效果惊人。在你的显示器上创建自定义布局，将解决方案资源管理器放在一个区域，调试器放在另一个区域，代码文件放在你想要的任何地方。一切都保持在原位，一切都可以独立访问，你的工作空间感觉有条理而不是混乱的。

## 快速建议

- **多显示器高级用户**：设置为**None**，搭配FancyZones
- **偶尔浮动的用户**：**Tool Windows**（默认）是不错的折中方案
- **传统工作流**：**Documents and Tool Windows**保持经典行为

专业提示：在任何工具窗口的标题栏上**Ctrl + 双击**即可立即浮动或停靠。更改设置后无需重启。

## 总结

这是那种"我不敢相信我之前不知道"的设置之一。如果Visual Studio中的浮动窗口曾经让你烦恼，现在就去改掉它。

阅读[完整文章](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/)获取详细信息和截图。
