---
title: "Foundry Local 1.1：实时转录、Embeddings 和 Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 新增实时麦克风转录、文本 embeddings 和 Responses API 支持——全部在本地运行，无云依赖、无网络延迟、无每令牌费用。"
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 已证明了这一概念：通过开发者友好的 SDK 在 Windows、macOS（Apple Silicon）和 Linux x64 上本地运行 AI 模型。1.1 版本新增三项功能，涵盖了许多真实的生产用例。

## 实时音频转录

最重要的新功能：直接从麦克风进行实时语音转文字流式处理。字幕、语音 UI、会议转录、无障碍工具——全部在本地运行，无任何云依赖。

API 基于会话，结果一到达即流式传输，使用 `is_final` 标记区分中间文本和最终文本。适用于所有语言绑定：JavaScript、C#、Python 和 Rust。

从目录加载流式语音模型，使用音频设置（采样率、声道、语言）创建会话，启动它，推送原始 PCM 音频块，并消费结果的异步流。文章中有完整的 Python 和 C# 示例。

## 文本 Embeddings

语义搜索、RAG 管道、聚类、相似性匹配——这些都需要 embeddings。Foundry Local 1.1 新增 embedding 模型支持，让你可以直接从同一 SDK 本地生成向量，无需将数据发送到云端。

对于数据驻留地很重要或需要处理敏感内容的应用程序，本地 embedding 生成是一项有意义的功能。

## Responses API

Foundry Local 现已支持 [Responses API](https://platform.openai.com/docs/api-reference/responses)——专为代理式交互设计的结构化接口。这新增了：

- **工具调用**——让本地运行的模型调用你定义的工具
- **多模态视觉-语言输入**——向视觉模型传递图像 + 文本
- 与标准 API 格式兼容，因此针对 OpenAI Responses API 的现有 agent 可以直接对接本地模型

## 包大小改进

两项更改减少了 JavaScript 包大小：
- `koffi` FFI 层已替换为自定义 Node-API C 插件
- WebGPU 执行提供程序作为单独插件提供，不需要 GPU 加速的应用无需承担额外的大小开销

C# SDK 现在针对更低的框架版本，以获得更广泛的 .NET 兼容性。

## 为什么重要

三项功能组合——转录、embeddings、工具调用——涵盖了许多 AI 应用程序的核心构建块。在本地运行它们意味着：
- 无需互联网
- 无每令牌费用
- 数据不离开设备
- 无论网络状况如何，延迟保持一致

Foundry Local 是边缘场景、隐私敏感工作负载、离线应用程序或任何希望在开发过程中避免云依赖的场景的正确选择。

原文：[Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
