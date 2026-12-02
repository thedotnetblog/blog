---
title: "智能体 SQL 的真正前沿：SQL MCP Server 中带 OBO 的可审计性"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "Data API builder 加 SQL MCP Server 中的 OBO 身份验证是一个重要的治理里程碑，因为 Azure SQL 终于可以审计智能体操作背后的人类用户了。"
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

企业 AI 项目中有一个痛苦的真相：很多团队痴迷于模型质量而忽视了问责性。当一个智能体写入或读取生产数据时，事件审查的第一个问题不是"答案好吗？"而是"这到底是谁干的？"

原文来源：https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

这就是为什么 Data API builder 2.0 与 SQL MCP Server 中的 OBO 支持比它初看起来重要得多。用户名/密码和托管身份方法在操作上仍然有效，但两者都将身份折叠到服务边界中。日志显示的是应用或中间件，而不是人类请求的源头。这对简单的自动化来说是可以接受的，但对受监管的智能体工作流来说是不可接受的。

使用 OBO，SQL 验证的是**委派的用户上下文**，而不是工具宿主身份。这给了你一个根本更好的审计模型：用户主体、操作、语句上下文和中间层应用标识符一起出现。你在获得可追溯性的同时，没有失去 MCP 工具和 DAB 实体权限的控制面。

我的观点很坚定：如果你的智能体可以接触敏感的 SQL 数据，OBO 应该是你的默认架构，而不是一个可选的加固任务。设置更复杂，但身份债务总是会晚些时候偿还——通常是在安全事件、合规审计或高管升级期间。

### 实用实施指导

- **从一个最小的 WhoAmI 视图和集成测试中的自动化检查开始验证身份流**。如果 SQL 主体与登录用户不匹配，在交付前停下来修复。
- **将针对 SQLSecurityAuditEvents 的 Log Analytics 查询接入你的 SOC 仪表盘**，并对通过 OBO 路径发起的风险操作进行告警。
- **对齐 RBAC 和 DAB 权限**，确保用户级身份和操作级授权端到端保持一致。

公告中一个微妙但重要的设计点是缓存行为。DAB 在启用用户委派身份验证时显式阻止响应缓存。这个权衡是正确的。在多租户或受监管环境中，可能泄漏用户范围结果的性能技巧不值得冒险。

**SQL MCP Server 加 OBO** 是一种成熟模式的开始：智能体作为受控操作者，用户作为可问责主体，数据平面作为可审计系统。如果你的架构不能自信地回答"这是谁做的"，无论演示多么精美，它都不是生产就绪的 AI。