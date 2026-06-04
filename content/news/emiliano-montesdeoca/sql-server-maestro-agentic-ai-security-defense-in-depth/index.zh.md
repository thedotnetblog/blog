---
title: "MAESTRO, 深度防御，以及为什么 SQL Server 现在是 AI 的安全边界"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "智能体 AI 引入了传统 STRIDE 模型未设计应对的威胁。以下是 Microsoft SQL 如何映射到 MAESTRO 框架以提供受治理的执行边界。"
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

安全威胁模型建立在关于谁或什么在发出请求的假设之上。STRIDE 假设人类参与者通过定义的接口与系统交互。AI 智能体不是这样工作的。

## STRIDE 不是为 AI 智能体设计的

智能体系统自主运行，通过 API 调用将工具串联成链，决定检索哪些数据和执行哪些操作，并可从多个来源（用户提示、工具结果、检索数据）接收指令。STRIDE 威胁模型（欺骗、篡改、否认、信息泄露、拒绝服务、权限提升）无法充分捕获提示词注入、上下文污染或工具滥用等智能体特有的攻击向量。

云安全联盟（Cloud Security Alliance）专门针对 AI 智能体风险发布了 MAESTRO 框架。

## MAESTRO 框架

MAESTRO 将智能体 AI 风险组织为七个层次：

1. **Foundation Models** — 底层 LLM 及其训练漏洞
2. **Data Operations** — 数据检索、存储和操纵
3. **Agent Frameworks** — 智能体编排和协调中间件
4. **Deployment & Infrastructure** — 智能体运行的位置和配置方式
5. **Evaluation & Observability** — 随时间监控智能体行为
6. **Security & Compliance** — 访问控制、审计和监管合规
7. **Agent Ecosystem** — 智能体如何相互之间以及与外部工具交互

每个层次都有传统安全控制未直接解决的特定攻击向量。

## Microsoft SQL 作为受治理的执行边界

SQL Server 2025 以具体方式映射到 MAESTRO 各层：

**Data Operations 层**：内置于 T-SQL 的 `AI_GENERATE_EMBEDDINGS` 将向量操作保持在数据库受治理的边界内。数据无需离开到模型服务进行嵌入处理。

**Security & Compliance 层**：行级安全（RLS）和动态数据掩码（DDM）无论请求如何到达都会应用——无论来自人类用户还是 AI 智能体。智能体无法绕过由数据库本身强制执行的控制。

**Agent Frameworks 层**：存储过程充当工具边界。不给智能体任意 SQL 访问，而是将允许的操作定义为过程并作为智能体工具暴露。参数化查询在执行级别防止注入。

**Evaluation & Observability 层**：审计日志和 Query Store 捕获每个智能体实际执行的内容——不仅是被要求做的事情。在归因复杂的智能体系统中，这种可追溯性对于事件调查至关重要。

## 智能体 AI 的深度防御

原则与传统安全相同：没有单一控制就足够了。变化的是哪些控制对智能体最重要：

**减少爆炸半径**：通过存储过程的工具边界意味着受损的智能体只能执行预定义的操作。它无法转向任意查询。

**可观测性**：事件发生后你必须能够回答"这个智能体究竟做了什么？"。没有数据库级别可追溯性的智能体 AI 系统存在应用程序日志无法覆盖的盲点。

**受约束的执行**：参数化、RLS 和 DDM 无论调用者是否为人类都是安全资产。不要为了适应智能体而削弱它们。

**问责制**：SQL Server 审计日志创建了谁（哪个智能体，使用什么凭据）在什么时间执行了什么的记录。当智能体系统采取在现实世界中产生实际后果的行动时，这一点很重要。

SQL Server 2025 不是为抽象地解决智能体风险而构建的——它是作为关系数据库构建的。但使企业数据库可信的治理恰恰是使智能体执行边界安全的东西。

原文链接：[Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
