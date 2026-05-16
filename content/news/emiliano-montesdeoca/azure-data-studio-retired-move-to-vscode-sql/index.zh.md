---
title: "Azure Data Studio 已停用：将您的 Azure SQL 工作流迁移到 VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio 于 2025 年 2 月 6 日停用，支持将于 2026 年 2 月 28 日结束。以下是使用 MSSQL 扩展迁移到 VS Code 的完整路径。"
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[Azure Data Studio 于 2025 年 2 月 6 日停用](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)，支持将于 2026 年 2 月 28 日结束——推荐的替代方案是带有 MSSQL 扩展的 VS Code。

## 需要安装的内容

开始所需的三样东西：

- **MSSQL 扩展** — 在 VS Code Marketplace 中搜索"SQL Server (mssql)"
- **SQL Database Projects 扩展** — 模式即代码、构建验证、引导式发布
- **.NET 8 SDK** — 构建系统所需；SDK 缺失是首次运行时最常见的问题

## 迁移 ADS 连接和设置

MSSQL 扩展附带 **ADS Migration Toolkit**，在引导式流程中处理一次性迁移：已保存的连接、连接组、设置和键绑定均自动导入。

## 恢复 F5 肌肉记忆

ADS 用户依靠 F5 运行查询。安装 **MSSQL Database Management Keymap** 扩展，即可恢复 ADS 风格的键绑定，包括 F5。

## SQL Database Projects：模式即代码

右键单击项目 → **发布** → 配置目标 → 审查生成的 T-SQL 脚本 → 部署。部署前的脚本预览是关键安全功能。项目模板为表、存储过程和视图生成存根——与 SSDT 相同的工作流。

常见问题：如果项目是针对不同的 SQL Server 版本创建的，`.sqlproj` 文件中的**目标平台不匹配**将导致构建错误。

## Schema Compare 和 Schema Designer

该扩展还包括 **Schema Compare**（对比项目与已部署数据库的差异）和 **Schema Designer**（无需手动编写 DDL 即可进行可视化架构编辑）。

## Microsoft Fabric 开发者

设置相同，但请先从 **Fabric 门户**开始，先将数据库连接到 Git，再在 VS Code 中打开。Microsoft 有专门的指南：*Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*。

## 总结

迁移是一次性的引导式流程，而非手动重建。安装三个工具，运行 ADS Migration Toolkit，恢复键绑定，即可在 10 分钟内恢复正常。

请参阅[完整文章](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)，获取逐步截图和 Fabric 专属演练。
