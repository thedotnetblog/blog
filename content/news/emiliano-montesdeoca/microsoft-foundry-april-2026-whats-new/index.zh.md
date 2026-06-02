---
title: "Microsoft Foundry 2026年4月：Foundry Local GA、GPT-5.5、Hyperlight上的CodeAct"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "4月的Foundry回顾内容丰富：Foundry Local达到GA，GPT-5.5到来，Agent Framework获得OpenTelemetry追踪，CodeAct在Hyperlight微型虚拟机中运行Python，以及代理监控仪表板上线。"
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

微软Foundry迎来了繁忙的一个月。以下是最重要的公告。

## Foundry Local正式发布

Foundry Local — 微软的跨平台本地AI运行时 — 在Windows、macOS（Apple Silicon）和Linux x64上从预览版升级为GA版本。具备开发者友好SDK的生产就绪本地模型推理。1.1版本增加了转录、embeddings和Responses API支持。

## GPT-5.5

GPT-5系列的最新模型现已在Foundry中提供。Tier 5和Tier 6订阅的默认配额。如果您一直在使用早期的GPT-5变体，值得针对您的用例进行评估。

## Foundry中的Agent Framework追踪

本月有两项追踪功能以预览形式发布：

**Microsoft Agent Framework追踪** — MAF代理现在可以向Foundry发送OpenTelemetry追踪。调试代理行为，追踪多步骤执行，显示工具调用中的延迟和错误。这填补了一个真实的空白：知道*代理在生产中实际做了什么*，而不仅仅是它返回了什么。

**托管代理追踪** — 托管代理的会话、工具调用和运行步骤也出现在Foundry追踪中。相同的可观测性能力延伸到托管层。

## Hyperlight上的CodeAct（Alpha）

这是技术上最有趣的新增功能：Agent Framework现在可以在[Hyperlight](https://github.com/hyperlight-dev/hyperlight)微型虚拟机中执行Python代码。

CodeAct是代理将Python代码作为工具生成并执行的模式。显而易见的担忧是安全性 — 您正在运行模型生成的代码。Hyperlight的微型VM以接近原生的启动时间提供进程级隔离，使沙盒代码执行变得实用，而无需完整容器或VM的开销。

对于需要代码执行的代理工作流，这是相比在宿主进程中运行代码的重大安全改进。

## 代理监控仪表板（预览）

统一的操作仪表板，在一个视图中结合了令牌使用情况、延迟、运行成功率和评估器分数。与常规可观测性仪表板的区别：它在操作指标旁边包含评估结果，因此您可以将"代理变慢了"与"评估器分数下降了"关联起来 — 或确认它们无关。

## 持续评估自定义评估器（预览）

您现在可以将自己的基于代码或提示的评估器带入持续评估管道。以前，持续评估仅限于内置评估器。自定义评估器让您在生产监控循环中执行团队特定的质量标准。

## 控制平面中的代理清单

Foundry控制平面的Operate视图现在显示订阅中所有受支持的代理：Foundry代理、Azure SRE Agent、Logic Apps代理循环和已注册的自定义代理。一个视图来了解部署了什么以及在哪里。

原始帖子：[What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
