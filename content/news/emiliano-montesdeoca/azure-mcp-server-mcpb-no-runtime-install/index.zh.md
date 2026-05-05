---
title: "Azure MCP Server 现在是 .mcpb — 无需任何运行时即可安装"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 现已作为 MCP Bundle (.mcpb) 提供 — 下载、拖入 Claude Desktop，完成。无需 Node.js、Python 或 .NET 运行时。"
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*本文已自动翻译。如需查看原文，请[点击此处]({{< ref "index.md" >}})。*

你知道配置 MCP 服务器有什么烦人的地方吗？需要运行时。npm 版需要 Node.js，pip/uvx 需要 Python，dotnet 版需要 .NET SDK。

[Azure MCP Server 刚刚改变了这一切](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)。它现在作为 `.mcpb` — MCP Bundle — 提供，配置方式是拖放。

## 什么是 MCP Bundle？

把它想象成 VS Code 扩展（`.vsix`）或浏览器扩展（`.crx`），但用于 MCP 服务器。`.mcpb` 文件是一个独立的 ZIP 存档，包含服务器二进制文件及其所有依赖项。

## 如何安装

**1. 为你的平台下载 Bundle**

前往 [GitHub Releases 页面](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server)，下载适合你 OS 和架构的 `.mcpb` 文件。

**2. 在 Claude Desktop 中安装**

最简单的方式：在扩展设置页面（`☰ → 文件 → 设置 → 扩展`）打开时，将 `.mcpb` 文件拖放到 Claude Desktop 窗口中。查看服务器详情，点击安装，确认。完成。

**3. 向 Azure 进行身份验证**

```bash
az login
```

就这样。Azure MCP Server 使用你现有的 Azure 凭据。

## 能做什么

直接从 AI 客户端访问 100 多个 Azure 服务工具：
- 查询和管理 Cosmos DB、Storage、Key Vault、App Service、Foundry
- 为任何任务生成 `az` CLI 命令
- 创建 Bicep 和 Terraform 模板

## 开始使用

- **下载**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **仓库**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **文档**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

查看[完整文章](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)。
