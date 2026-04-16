---
title: "Azure MCP 工具现已内置于 Visual Studio 2022 — 无需安装扩展"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP 工具作为 Visual Studio 2022 Azure 开发工作负载的一部分随附发布。超过 230 个工具、45 项 Azure 服务，零扩展安装。"
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *本文为自动翻译。如需查看原文，请[点击此处]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}})。*

如果你一直通过单独的扩展在 Visual Studio 中使用 Azure MCP 工具，那你一定很熟悉这套流程——安装 VSIX、重启、祈祷别出问题、处理版本不匹配。这种摩擦现在消失了。

Yun Jung Choi [宣布](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/)，Azure MCP 工具现在直接作为 Visual Studio 2022 中 Azure 开发工作负载的一部分发布。无需扩展，无需 VSIX，无需重启。

## 这实际意味着什么

从 Visual Studio 2022 版本 17.14.30 开始，Azure MCP Server 捆绑在 Azure 开发工作负载中。如果你已经安装了该工作负载，只需在 GitHub Copilot Chat 中启用它即可。

超过 230 个工具，覆盖 45 项 Azure 服务——直接从聊天窗口即可访问。列出你的存储账户、部署 ASP.NET Core 应用、诊断 App Service 问题、查询 Log Analytics——全程无需打开浏览器标签页。

## 为什么这比听起来更重要

开发工具有个道理：每多一个步骤就是摩擦，摩擦会扼杀采用率。MCP 作为单独的扩展意味着版本不匹配、安装失败，以及又多了一个需要保持更新的东西。将它内置到工作负载中意味着：

- **单一的更新路径**——通过 Visual Studio Installer
- **无版本偏差**——扩展和 IDE 之间不会出现版本不一致
- **始终保持最新**——MCP Server 随 VS 常规发布一起更新

对于标准化使用 Azure 的团队来说，这意义重大。安装一次工作负载，启用工具，每次会话都能使用。

## 你能用它做什么

这些工具通过 Copilot Chat 覆盖完整的开发生命周期：

- **学习**——询问 Azure 服务、最佳实践、架构模式
- **设计与开发**——获取服务推荐，配置应用代码
- **部署**——预配资源并直接从 IDE 进行部署
- **排查问题**——查询日志、检查资源健康状况、诊断生产环境问题

一个简单的例子——在 Copilot Chat 中输入：

```
List my storage accounts in my current subscription.
```

Copilot 在后台调用 Azure MCP 工具，查询你的订阅，返回一个包含名称、位置和 SKU 的格式化列表。无需打开门户。

## 如何启用

1. 更新到 Visual Studio 2022 **17.14.30** 或更高版本
2. 确保已安装 **Azure development** 工作负载
3. 打开 GitHub Copilot Chat
4. 点击 **Select tools** 按钮（双扳手图标）
5. 开启 **Azure MCP Server**

就这样。跨会话保持启用状态。

## 一个注意事项

这些工具默认是禁用的——你需要手动启用。而且 VS 2026 特有的工具在 VS 2022 中不可用。工具的可用性还取决于你的 Azure 订阅权限，与门户中一样。

## 更大的图景

这是一个清晰趋势的一部分：MCP 正在成为在开发者 IDE 中呈现云工具的标准方式。我们已经看到了 [Azure MCP Server 2.0 稳定版发布](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)以及在 VS Code 和其他编辑器中的 MCP 集成。将其内置到 Visual Studio 的工作负载系统中是自然而然的演进。

对于我们这些常年在 Visual Studio 中工作的 .NET 开发者来说，这又少了一个需要切换到 Azure 门户的理由。说实话，标签页切换越少越好。
