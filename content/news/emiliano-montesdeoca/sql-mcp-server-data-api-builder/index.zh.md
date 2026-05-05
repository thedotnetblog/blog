---
title: "SQL MCP Server — 给 AI 代理数据库访问的正确方式"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Data API builder 的 SQL MCP Server 为 AI 代理提供安全、确定性的数据库访问，无需暴露架构或依赖 NL2SQL。RBAC、缓存、多数据库支持 — 全部内置。"
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "sql-mcp-server-data-api-builder.md" >}})。*

说实话：今天市面上大多数数据库 MCP 服务器都很可怕。它们接受自然语言查询，即时生成 SQL，然后在你的生产数据上执行。有什么可能出错的？（一切。一切都可能出错。）

Azure SQL 团队刚刚[发布了 SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)，它采用了一种根本不同的方法。作为 Data API builder（DAB）2.0 的功能构建，它为 AI 代理提供结构化、确定性的数据库操作访问 — 没有 NL2SQL，不暴露你的架构，每一步都有完整的 RBAC。

## 为什么不用 NL2SQL？

这是最有趣的设计决策。模型不是确定性的，复杂查询最容易产生微妙的错误。用户希望 AI 能生成的那些查询，恰恰也是在非确定性生成时最需要审查的查询。

相反，SQL MCP Server 使用 **NL2DAB** 方法。代理使用 Data API builder 的实体抽象层和内置查询构建器来确定性地生成准确、格式良好的 T-SQL。对用户来说结果相同，但没有幻觉 JOIN 或意外数据泄露的风险。

## 七个工具，不是七百个

SQL MCP Server 精确暴露七个 DML 工具，与数据库大小无关：

- `describe_entities` — 发现可用实体和操作
- `create_record` — 插入行
- `read_records` — 查询表和视图
- `update_record` — 修改行
- `delete_record` — 删除行
- `execute_entity` — 运行存储过程
- `aggregate_records` — 聚合查询

这很聪明，因为上下文窗口是代理的思考空间。用数百个工具定义淹没它们会减少推理空间。七个固定工具让代理专注于*思考*而不是*导航*。

每个工具可以单独启用或禁用：

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## 三条命令开始

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

这就是一个运行中的 SQL MCP Server，暴露你的 Customers 表。实体抽象层意味着你可以为名称和列创建别名、按角色限制字段，并精确控制代理看到的内容 — 而不暴露内部架构细节。

## 安全故事很扎实

这是 Data API builder 成熟度发挥价值的地方：

- **每一层都有 RBAC** — 每个实体定义哪些角色可以读取、创建、更新或删除，以及哪些字段可见
- **Azure Key Vault 集成** — 安全管理连接字符串和密钥
- **Microsoft Entra + 自定义 OAuth** — 生产级认证
- **内容安全策略** — 代理通过受控契约交互，而不是原始 SQL

架构抽象特别重要。你的内部表名和列名永远不会暴露给代理。你定义对 AI 交互有意义的实体、别名和描述 — 而不是你的数据库 ERD 图。

## 多数据库和多协议

SQL MCP Server 支持 Microsoft SQL、PostgreSQL、Azure Cosmos DB 和 MySQL。由于它是 DAB 的功能，你可以从同一配置同时获取 REST、GraphQL 和 MCP 端点。相同的实体定义、相同的 RBAC 规则、相同的安全性 — 跨所有三种协议。

DAB 2.0 的自动配置甚至可以检查你的数据库并动态构建配置，如果你愿意为快速原型设计减少抽象的话。

## 我的看法

这就是 AI 代理的企业级数据库访问应该如何工作。不是"嘿 LLM，给我写点 SQL 然后对生产环境 YOLO"。而是：定义良好的实体层、确定性查询生成、每一步的 RBAC、缓存、监控和遥测。以最好的方式无聊着。

对于 .NET 开发者，集成故事很清晰 — DAB 是 .NET 工具，MCP Server 作为容器运行，与大多数人已经在用的 Azure SQL 配合工作。如果你正在构建需要数据访问的 AI 代理，从这里开始。

## 总结

SQL MCP Server 是免费、开源的，可在任何地方运行。这是微软为给 AI 代理提供安全数据库访问的规范性方法。查看[完整文章](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)和[文档](https://aka.ms/sql/mcp)开始使用。
