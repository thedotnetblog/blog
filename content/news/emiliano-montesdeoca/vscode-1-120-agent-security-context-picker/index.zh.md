---
title: "VS Code 1.120：密码提示、上下文大小选择器、Agent Host 中的 GitHub 元数据"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 是面向 Copilot 用户的专注版本：安全密码提示处理、模型上下文大小选择器、代理会话中的 GitHub PR 元数据以及会话存档管理。"
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 带来了一系列 Copilot 代理改进，单独来看很小，但在日常使用中明显更好。

## 代理终端中的安全密码提示检测

当 Copilot 代理运行触发密码或密码短语提示的终端命令时，VS Code 现在会检测到这一点并显示确认对话框。对话框会将焦点转移到终端，以便您可以直接输入密钥 — 关键是，密钥永远不会通过模型路由。

这是一项重大安全改进。以前，运行触发身份验证提示命令的代理可能会创建用户可能无意间暴露凭据的情况。屏幕阅读器公告意味着可访问性用户也会收到通知。

## 模型选择器中的上下文大小选择器

新的上下文大小选择器允许您选择模型在会话中使用多少上下文。不同的模型具有不同的上下文窗口大小，某些工作流程受益于限制它（更低的延迟、更低的成本）或最大化它（复杂的代码库、长时间运行的会话）。

## Agent Host 会话中的 GitHub PR 元数据

对于由 GitHub 存储库支持的会话，VS Code 现在在代理主机 UI 中显示 GitHub 元数据 — 包括拉取请求按钮。在处理 PR 时，减少了切换到浏览器或 GitHub 扩展的上下文切换。

## 聊天会话存档管理

会话 Quick Pick 的两项改进：
- 存档的会话默认隐藏（减少视觉混乱）
- 搜索仍然匹配存档的会话，因此您可以按标题恢复一个

会话也默认按最近顺序分组，使最近的工作更容易找到。

## Copilot CLI 插件发现

VS Code 现在自动从 `~/.copilot/installed-plugins/` 发现安装的 Copilot CLI 用户插件。如果您设置了 WinUI 或其他领域特定的代理技能，它们无需手动配置即可被识别。

## 自定义差异编辑器 API（预览）

对于扩展作者：新的提案 API `customDiffEditorProvider` 允许扩展在单个 webview 中呈现统一的差异，并可访问原始和修改的文档，而不是两个并排的自定义编辑器视图。

原始文章：[Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
