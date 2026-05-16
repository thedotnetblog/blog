---
title: "SQL MCP Server 在 Azure App Service 上运行 — 无需容器"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server 现在可以在 Azure App Service 上运行，无需 Docker 或 Kubernetes。这对于构建与 SQL 数据库通信的 AI 代理的 .NET 开发者意味着什么。"
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*本文已自动翻译。要查看原始版本，请[点击此处]({{< ref "index.md" >}})。*

老实说：每次在教程中看到"需要容器"，我内心都会叹一口气。容器很棒——直到你的团队没有容器策略，一个看似简单的功能突然被意料之外的编排复杂性阻挡。

这就是为什么这个让我眼前一亮。SQL MCP Server 现在可以在 Azure App Service 上运行——无需 Docker，无需 Kubernetes，只需相同的 Data API Builder（DAB）配置文件，通过 MCP、REST 和 GraphQL 公开你的 SQL 数据库。

## 什么是 SQL MCP Server？

如果你还不了解，简单介绍一下。SQL MCP Server 位于你的 AI 代理和 SQL 数据库之间。它不是让代理直接访问数据库（这是个糟糕的想法），而是将你的表和视图作为带有定义权限的实体抽象层公开。

它构建在 [Data API Builder](https://learn.microsoft.com/zh-cn/azure/data-api-builder/) 之上，这意味着单个配置文件同时管理 MCP、REST 和 GraphQL。你的代理与 MCP 端点通信，传统应用与 REST 或 GraphQL 通信。相同的配置，相同的运行时，不同的接口。

这真的很有用——你不需要维护两个独立的 API 层。

## 容器问题（及解决方案）

SQL MCP Server 最初的部署模型是容器。这在很多团队中运行良好，但并非所有团队都适用。许多 .NET 团队标准化使用 Azure App Service 或虚拟机。仅仅为了公开 SQL 端点而需要容器运行时，增加了没有人要求的摩擦。

新的教程展示了如何完全跳过容器。一切都通过 `dab start` 命令运行，作为标准的 .NET 8 Web 进程托管在 App Service 上。

```bash
# 安装 Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# 初始化配置
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# 添加实体
dab add products --source dbo.products --permissions "authenticated:*"

# 配置 App Service 认证提供程序
dab configure --runtime.host.authentication.provider AppService

# 启动服务器
dab start
```

此时，你在 `/mcp` 有 MCP，同一进程提供 REST 和 GraphQL，没有任何东西运行在容器中。

## 无需共享 API 密钥的身份验证

这是我最欣赏的部分。部署到 App Service 时，你将 Microsoft Entra ID 配置为身份验证提供程序。配置文件中没有共享密钥，不需要轮换 API 密钥。

连接字符串保留在 App Service 环境变量中（不在 `dab-config.json` 中），MCP 端点通过平台身份验证保护。如果你的 Azure 工作负载已经与 Entra ID 对齐，这将自然融入。

本地开发时，切换到 `Simulator` 模式和 STDIO 传输。部署前切换回 `AppService` 模式。干净且明确。

## 部署到 App Service

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

然后使用你的团队已经使用的代码部署方法部署你的 DAB 项目。关键细节：这是**代码**部署，不是容器部署。

## 为什么这对 .NET 开发者很重要

如果你在 .NET 中构建 AI 代理，你的代理最终需要与数据库通信。SQL MCP Server 提供了一种结构化的方式来实现这一点，无需暴露原始连接字符串。

查看[原始博客文章](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/)和 [GitHub 示例仓库](https://github.com/Azure-Samples/SQL-MCP-NoContainer)的完整教程。

## 总结

App Service 上的 SQL MCP Server 是 .NET 团队的实用选择，无需容器策略即可为代理提供结构化的 SQL 数据访问。试试看——你的代理会很感激清晰的 API 接口。
