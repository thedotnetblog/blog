---
title: "Cosmos DB Shell 现已推出公共预览版 — 并且内置了 MCP 服务器"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell 是一款新的开源 CLI，将数据库命令作为 MCP 工具公开。您的 AI 代理可以使用与您相同的界面导航容器、运行查询和管理数据。"
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

如果您曾经为了回答一个关于 Cosmos DB 的问题，不得不在门户标签页、SDK 示例和半成品脚本之间来回切换，那么您已经了解这个项目旨在消除的摩擦。

Azure Cosmos DB Shell 刚刚进入公共预览版。这是一个具有类 bash 语法的开源 CLI，还有——让它变得有趣的部分——一个内置的 MCP 服务器。

## 与其他数据库 CLI 的不同之处

CLI 本身很有用：熟悉的命令、脚本支持、CI/CD 集成。这部分是面向开发者的数据库工具的最低要求。

有趣的部分是 MCP 服务器集成。CLI 公开的每个命令都可以作为 AI 代理可以调用的 MCP 工具。没有自定义 API 层，没有需要编写的集成代码。您的代理可以：

- 使用 `cd`、`ls`、`pwd` 导航数据库层次结构
- 使用 `query` 执行 SQL 查询并获取结构化结果
- 使用 `create item`、`update`、`rm` 创建和修改项目
- 使用 `mkdb`、`mkcon`、`rmdb`、`rmcon` 管理数据库和容器
- 使用 `endpoint`、`pwd` 检查当前上下文

关键变化：您的代理不是在与 Cosmos DB API 交互——而是在与您使用的相同 shell 界面交互。命令是确定性的、可审计的，并且是开源的，因此您可以检查确切发生了什么。

## 开源基础很重要

这不是一个黑箱托管服务。Shell 是开源的，这意味着：

- 安全团队可以审计实现
- 平台团队可以 fork 并根据其特定标准进行扩展
- 开发者可以贡献对所有人有益的改进

对于采用 AI 工具的企业团队来说，"我们能确切看到它是如何工作的吗"越来越不是可选要求。这里的开源是一个重要的差异化因素。

## 三个变得更容易的场景

**智能数据分析** — 将代理连接到 shell，用自然语言提问，获取结构化查询结果。代理处理查询构建；shell 处理执行。

**自主数据管理** — 需要在 Cosmos DB 中创建、更新或删除数据的工作流可以通过 MCP 工具完成，无需自定义集成。

**实时监控和警报** — 代理可以定期查询容器，比较结果，并通过任何有意义的通知渠道报告异常。

MCP 接口使这些场景可以与任何支持 MCP 的 AI 平台组合——不仅仅是微软的工具。

## 入门

Shell 处于公共预览阶段。安装它，配置您的 Cosmos DB 连接，并启用 MCP 服务器。从那里，任何 MCP 兼容的代理宿主都可以发现并使用这些工具。

原始文章：[Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
