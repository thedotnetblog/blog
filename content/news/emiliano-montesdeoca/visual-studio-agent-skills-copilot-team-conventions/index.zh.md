---
title: "Visual Studio中的Agent Skills：教Copilot了解你的团队真正的工作方式"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio现在支持Agent Skills——可重用的指令集，教会Copilot你团队特定的工作流程、编码标准和约定。定义一次，自动应用。"
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

AI编程助手长期存在的一个挫折：它们了解一般编程，但不了解*你*团队的特定约定、内部API或偏好的模式。每次会话，你都要重新解释上下文。Visual Studio中的Agent Skills旨在解决这个问题。

## 什么是Agent Skills

在`SKILL.md`文件中定义的可重用指令集——教会Copilot代理如何处理特定任务。为"如何运行我们的构建管道"、"如何为我们的服务层生成样板代码"或"我们的代码审查清单"定义一个技能。代理在相关时自动应用技能。

这不是一个新概念（`.github/copilot-instructions.md`已经存在了一段时间），但Visual Studio集成使它们成为具有发现UI的一等对象。

## 在Visual Studio中创建Skills

集成UI流程：点击Copilot Chat中的工具图标，打开技能面板，点击`+`。你选择全局（个人）或解决方案级别范围，选择名称，Visual Studio生成模板。然后Copilot代理模式可以帮助你填写模板——使用代理为代理编写技能。

目前在Insiders频道，即将在Release中推出。

你也可以手动创建技能：

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## 发现位置

技能从标准路径自动发现：

**解决方案级别（通过仓库共享）：** `.github/skills/`、`.claude/skills/`、`.agents/skills/`

**全局/个人（你的用户配置文件，随处可用）：** `~/.copilot/skills/`、`~/.agents/skills/`

多位置支持意味着相同的约定适用于GitHub Copilot、Claude Code和其他代理框架——定义一次技能，随处使用。

## 格式

技能遵循[agentskills.io/specification](https://agentskills.io/specification)格式——基于Markdown的规范，既人类可读又机器可解析。你可以在`SKILL.md`旁边包含脚本、模板和示例。

## 实际价值

真正的力量不在于单个功能——而在于团队共享技能（通过`.github/skills/`）和个人技能（通过`~/.agents/skills/`）的组合。团队技能编码你的组织如何做事。个人技能编码你具体如何工作。代理自动获得两个上下文。

对于已经大量使用Copilot的组织，这是使工具真正了解你的代码库特定约定而不是给出通用建议的重要一步。

原始帖子：[Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
