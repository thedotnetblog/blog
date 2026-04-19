---
title: "VS Code 1.117：Agent 拥有了自己的 Git 分支，我举双手赞成"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 为 Agent 会话带来了 worktree 隔离、持久化 Autopilot 模式和子 Agent 支持。Agent 编码工作流变得更加真实了。"
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}})。*

"AI 助手"和"AI 队友"之间的界限越来越模糊。VS Code 1.117 刚刚发布，[完整的发行说明](https://code.visualstudio.com/updates/v1_117)内容丰富，但核心很明确：Agent 正在成为你开发工作流中的一等公民。

以下是真正重要的内容。

## Autopilot 模式终于能记住你的偏好了

以前，你每次开始新会话都得重新启用 Autopilot。很烦。现在你的权限模式会在会话之间持久化，你还可以配置默认值。

Agent Host 支持三种会话配置：

- **Default** — 工具在运行前会请求确认
- **Bypass** — 自动批准一切
- **Autopilot** — 完全自主，自己回答问题并继续执行

如果你正在搭建一个带有迁移、Docker 和 CI 的新 .NET 项目——设置一次 Autopilot 就行了。这个偏好会一直保持。

## Agent 会话的 worktree 和 git 隔离

这是重头戏。Agent 会话现在支持完整的 worktree 和 git 隔离。这意味着当一个 Agent 处理任务时，它会获得自己的分支和工作目录。你的主分支完全不受影响。

更好的是——Copilot CLI 会为这些 worktree 会话生成有意义的分支名称。不再是 `agent-session-abc123`。你会得到一个真正描述 Agent 正在做什么的名称。

对于管理多个功能分支或在长时间脚手架任务运行期间修复 bug 的 .NET 开发者来说，这是一个游戏规则的改变。你可以让一个 Agent 在一个 worktree 中构建 API 控制器，同时你在另一个 worktree 中调试服务层问题。没有冲突。没有 stash。没有混乱。

## 子 Agent 和 Agent 团队

Agent Host Protocol 现在支持子 Agent。一个 Agent 可以启动其他 Agent 来处理任务的各个部分。把它想象成委派——你的主 Agent 负责协调，专门的 Agent 处理各个部分。

这还处于早期阶段，但对 .NET 工作流的潜力显而易见。想象一下，一个 Agent 处理你的 EF Core 迁移，另一个设置你的集成测试。我们还没有完全到达那里，但协议支持现在落地意味着工具很快就会跟上。

## Agent 发送输入时终端输出自动包含

虽小但有意义。当 Agent 向终端发送输入时，终端输出现在会自动包含在上下文中。以前，Agent 需要额外的一个回合才能读取发生了什么。

如果你曾经看到一个 Agent 运行 `dotnet build`，失败了，然后又需要一次往返才能看到错误——这种摩擦消失了。它立即看到输出并做出反应。

## macOS 上的 Agents 应用自动更新

macOS 上的独立 Agents 应用现在可以自动更新了。不再需要手动下载新版本。它会自动保持最新。

## 值得了解的小改进

- **package.json 悬停提示**现在同时显示已安装版本和最新可用版本。如果你在 .NET 项目旁边管理 npm 工具，这很有用。
- **JSDoc 注释中的图片**在悬停和补全中正确渲染。
- **Copilot CLI 会话**现在会显示是由 VS Code 还是外部创建的——当你在终端之间切换时很方便。
- **Copilot CLI、Claude Code 和 Gemini CLI** 被识别为 shell 类型。编辑器知道你在运行什么。

## 总结

VS Code 1.117 不是一个花哨的功能堆砌。它是基础设施。Worktree 隔离、持久化权限、子 Agent 协议——这些是构建一个工作流的基石，在这个工作流中，Agent 可以处理真实的并行任务而不会干扰你的代码。

如果你正在用 .NET 开发，还没有尝试 Agent 工作流，说实话，现在就是开始的时候。
