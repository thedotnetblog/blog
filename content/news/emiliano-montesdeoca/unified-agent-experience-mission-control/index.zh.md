---
title: "编码代理的任务控制：VS Code 中的统一体验"
description: "VS Code 将本地、云端、CLI 和第三方编码代理引入代理会话中，使开发人员可以跟踪、中断和协调自主工作。"
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}})。*

# 编码代理的任务控制：VS Code 中的统一体验

单个编码助手很容易理解。多个代理在不同的地方工作就不是这样了。

一个代理在 VS Code 中本地运行。另一个在云端处理 GitHub 问题。一个 CLI 代理驻留在终端中。第三方编码代理可能有不同的会话模型和不同的限制。没有共享的视图，开发人员花费的时间更多是在追踪工作而不是监督工作。

VS Code 的统一代理体验通过代理会话解决了这个协调问题：一个地方可以启动代理、查看它们的状态、打开它们的对话，以及在计划改变时进行干预。

这不太是关于添加另一个代理，而是关于使多个代理更易管理。

## 一个不同工作类型的视图

源文章描述了四个不同的参与者：本地 GitHub Copilot、云中的 Copilot 编码代理、GitHub Copilot CLI 和符合条件的 Copilot 订阅者的 OpenAI Codex。

它们各有各的优势：

- 本地代理可以检查当前工作区并快速进行更改。
- 云编码代理可以异步处理问题并打开拉取请求。
- CLI 代理适合终端繁重的工作流和操作命令。
- 另一个提供商可以提供不同的模型或推理风格。

代理会话为这些任务提供了一个公共的家园。您可以看到正在运行的是什么、正在做什么，以及在哪里继续对话。

这种可见性很重要，因为自主工作不会消除协调。它使协调成为一项一流的工程任务。

## 中断是工作流的一部分

源文章提出了一个简单的观察："发送提示后意识到遗忘了什么重要的事情是很常见的。"以前，选择通常是等待或取消。使用聊天编辑器，您可以打开活跃的会话并在代理工作时添加信息。

这更接近真正的协作。需求改变。测试揭示了一个假设。审阅者注意到 API 必须保持向后兼容。有用的代理不是从不需要纠正的代理；而是能够吸收纠正而不失去整个任务的代理。

对于 .NET 工作，中断可能就像这样简单：

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

指令很短，因为存储库已经包含了更大的上下文。会话是纠正方向的地方，而不是重申整个系统。

## 自定义代理将团队习惯转变为角色

VS Code 还引入了专门的代理，例如 Plan。与其立即实施，规划代理在生成实现规范之前询问有关范围、组件、库和约束的问题。

这种模式对于内置代理之外的用途很有用。团队可以定义重点角色：

- **研究** 收集证据并撰写简短的决策记录。
- **审查** 根据存储库约定检查更改。
- **测试** 识别缺失的案例并提出测试计划。
- **架构** 比较选项而不修改文件。

一个小的自定义代理定义可能看起来像这样：

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

有用的部分不是 YAML。而是明确分离责任。规划代理不应该悄悄编辑生产代码。审查代理不应该重写它应该评估的设计。

## 子代理减少上下文冲突

长对话积累了无关的上下文。子代理为有界的研究任务提供了一个隔离的工作区，然后将结果返回到主会话。

这很适合问题，例如：

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

主代理保持专注于实现，而研究代理处理一个更狭隘的问题。相同的原则适用于团队：明确的委派比启动多个代理具有重叠权限会产生更好的结果。

## 警告：更多代理意味着更多协调

代理会话可以显示活动，但它无法解决冲突的所有权。两个代理编辑同一区域仍然可以创建合并问题。云代理和本地代理可以做出不兼容的假设。自定义代理可以产生另一个代理忽视的建议。

设置边界：

1. 一个代理对给定分支的实现拥有所有权。
2. 研究代理返回工件，不跟踪编辑。
3. 拉取请求保持审查边界。
4. 代理名称和提示说明它们可能会改变什么。
5. 会话输出在解释重要决策时被保留。

## 我的看法

多代理的未来不是一队聊天窗口。这是一个小团队，有角色、交接和问责制。

代理会话很有价值，因为它承认这一现实。它为开发人员提供了一个控制表面，用于已经在编辑器、终端和云中发生的工作。下一个生产力增益将来自更少的代理数量和更多的代理边界清晰度。

对于 .NET 团队，我会从一个规划代理和一个实现代理开始。使用规划输出作为问题或拉取请求规范，然后让实现代理在该边界内工作。在添加更多角色之前测量返工。

最好的任务控制仍然是使所有权明显的那一个。
