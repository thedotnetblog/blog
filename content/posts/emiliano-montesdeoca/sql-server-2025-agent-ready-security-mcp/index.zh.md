---
title: "SQL Server 2025作为代理就绪数据库：一个引擎中的安全、备份和MCP"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Polyglot Tax系列的最终篇解决了生产环境中的难题：跨关系、JSON、图形和向量数据的统一行级安全，加上使SQL Server 2025真正代理就绪的MCP集成。"
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*本文已自动翻译。要查看原始版本，请[点击这里](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/)。*

我一直饶有兴趣地关注Aditya Badramraju的Polyglot Tax系列。第4部分用实际决定你是否会在生产环境中信任这种架构的部分来结束系列。

## 所有数据模型的单一安全模型

一个行级安全策略覆盖所有数据模型。对审计员来说，一个策略，一个证明。

## 统一备份 = 原子恢复

在多语言堆栈中，跨五个数据库的时间点恢复是一场一致性噩梦。只有一个数据库时，恢复在定义上就是原子的。

## MCP集成：无需手动编写中间件

SQL Server 2025直接支持SQL MCP服务器。代理调用工具，引擎自动强制租户隔离和列掩码。

原始文章（Aditya Badramraju著）：[The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/)。
