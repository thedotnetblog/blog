---
title: "智能体平台工程正在成为现实 — Git-APE展示了方法"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "微软的Git-APE项目将智能体平台工程付诸实践 — 使用GitHub Copilot智能体和Azure MCP将自然语言请求转化为经过验证的云基础设施。"
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "agentic-platform-engineering-git-ape" >}})。*

平台工程一直是那种在技术大会上听起来很棒的术语，但通常意味着"我们搭了一个内部门户和一个Terraform封装器。"真正的承诺 — 真正安全、受治理且快速的自助式基础设施 — 总是差那么几步。

Azure团队刚刚发布了[智能体平台工程系列的第二部分](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/)，这次全是关于动手实现。他们称之为**Git-APE**（是的，这个缩写是故意的），这是一个开源项目，使用GitHub Copilot智能体加Azure MCP服务器，将自然语言请求转化为经过验证和部署的基础设施。

## Git-APE究竟做什么

核心思路：开发者不再需要学习Terraform模块、浏览门户UI或向平台团队提交工单，而是直接和Copilot智能体对话。智能体理解意图、生成基础设施即代码、根据策略进行验证并部署 — 全部在VS Code内完成。

配置如下：

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

在VS Code中打开工作区，GitHub Copilot会自动发现智能体配置文件。你直接与智能体交互：

```
@git-ape deploy a function app with storage in West Europe
```

智能体在底层使用Azure MCP Server与Azure服务交互。VS Code设置中的MCP配置启用特定功能：

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## 为什么这很重要

对于我们在Azure上构建的人来说，这将平台工程的对话从"如何构建一个门户"转变为"如何将我们的护栏描述为API。"当你的平台接口是AI智能体时，你的约束和策略的质量就成了产品本身。

第一部分博客阐述了理论：描述良好的API、控制模式和明确的护栏使平台做好了智能体化的准备。第二部分通过交付实际工具证明它确实有效。智能体不会盲目生成资源 — 它会根据最佳实践进行验证、遵守命名约定并应用你组织的策略。

清理同样简单：

```
@git-ape destroy my-resource-group
```

## 我的看法

说实话 — 这里更多是关于模式而非具体工具。Git-APE本身是一个演示/参考架构。但底层的理念 — 智能体作为平台的接口、MCP作为协议、GitHub Copilot作为宿主 — 这就是企业开发者体验的前进方向。

如果你是一个正在寻找如何让内部工具对智能体友好的平台团队，没有比这更好的起点了。如果你是.NET开发者想知道这和你的世界如何关联：Azure MCP Server和GitHub Copilot智能体可以与任何Azure工作负载配合使用。你的ASP.NET Core API、你的.NET Aspire技术栈、你的容器化微服务 — 都可以成为智能体部署流程的目标。

## 总结

Git-APE是对智能体平台工程实践的一个早期但具体的展示。克隆[仓库](https://github.com/Azure/git-ape)，试试演示，开始思考你的平台的API和策略需要是什么样子，才能让智能体安全地使用它们。

阅读[完整文章](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/)获取详细教程和演示视频。
