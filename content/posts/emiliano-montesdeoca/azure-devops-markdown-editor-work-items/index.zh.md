---
title: "Azure DevOps终于修好了所有人都在抱怨的Markdown编辑器"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure DevOps的工作项Markdown编辑器获得了更清晰的预览与编辑模式区分。一个小改动，却解决了一个真正恼人的工作流问题。"
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *本文为自动翻译。查看原始版本，请[点击这里]({{< ref "azure-devops-markdown-editor-work-items.md" >}})。*

如果你使用Azure Boards，你可能经历过这种情况：你在阅读一个工作项描述，也许在检查验收标准，然后不小心双击了。砰——你进入了编辑模式。你根本不想编辑任何东西。你只是在阅读。

Dan Hellem [宣布了这个修复](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/)，这是那种听起来很小但确实从日常工作流中消除了真正摩擦的改动。

## 什么变了

工作项文本字段的Markdown编辑器现在**默认以预览模式打开**。你可以阅读和交互内容——跟随链接、检查格式——不用担心意外进入编辑模式。

当你真的想要编辑时，点击字段顶部的编辑图标。完成后，显式退出到预览模式。简单、有意图、可预测。

## 为什么这比听起来更重要

[社区反馈帖子](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496)很长。双击编辑的行为是在2025年7月随Markdown编辑器引入的，投诉几乎立刻开始了。

对于使用Azure Boards进行冲刺计划、需求梳理或代码审查的团队来说，这种微摩擦会累积。

## 部署状态

已经在向部分客户推出，将在未来两到三周内扩展到所有人。

## 总结

不是每个改进都需要成为头条功能。有时候最好的更新就是简单地移除恼人的东西。这就是其中之一——一个小小的UX修复，让Azure Boards对只想安静阅读工作项的人变得不再那么敌意。
