---
title: 'PostgreSQL 性能工作应该在你写代码的地方进行'
date: 2026-07-20
author: 'Emiliano Montesdeoca'
description: '最好的 PostgreSQL 调优工作流不是更多的仪表盘，而是编辑器内更紧密的反馈循环。'
tags:
  - postgresql
  - azure
  - visual-studio-code
  - database-performance
  - devops
---

原文来源：[The performance dividend: Optimizing PostgreSQL on Azure directly in Visual Studio Code](https://azure.microsoft.com/en-us/blog/the-performance-dividend-optimizing-postgresql-on-azure-directly-in-visual-studio-code/)

我同意这个 Azure 更新的核心论点：性能工作失败更少是因为缺少工具，更多是因为上下文碎片化。大多数团队已经有监控、查询编辑器和运维仪表盘。他们缺乏的是从信号到行动的连续性。

VS Code 中的 PostgreSQL 扩展方向之所以重要，是因为它缩短了那条路径。当服务器指标、查询计划和顾问建议出现在开发者已经编辑 SQL 的同一个地方时，团队从诊断到修复的速度就会加快。这听起来很明显，但在真实组织中这是一个结构性转变。上下文切换正是所有权丢失的地方。

以下是对工程负责人的实用部分。如果你想要可衡量的提升，不要把这几项功能作为可选的锦上添花来引入。让它们成为你审查工作流的一部分：

- **要求每个非平凡的查询变更附带查询计划截图或摘要**。
- **每周跟踪最大的顾问建议**并分配负责人，而不仅仅是告警。
- **将架构感知的 IntelliSense 和 search_path 正确性视为预防性工具**，而非便利功能。

文章还将 Azure HorizonDB 定位为前瞻选择，同时让 Azure Database for PostgreSQL 保持为当前的生产默认。这正是正确的框架。团队在过早将预览期技术兴奋转化为运维承诺时会遇到麻烦。先稳定，再有选择地实验。

我强烈的观点：**性能文化在成为云问题之前首先是编辑器问题**。如果调优只在火线和作战室中进行，你做的不是性能工程，而是性能事件响应。VS Code 集成故事帮助团队左移，在那里修复成本更低。

有一个注意事项。集成的建议可能会导致过度自信，如果团队停止基于工作负载行为验证假设。AI 辅助调优和顾问提示是加速器，而非基准纪律的替代品。你仍然需要基线、可重复的负载测试和回归门控。

如果你的组织在 Azure 上大规模运行 PostgreSQL，现在正确的做法是标准化这个集成工作流，然后检测从问题检测到缓解的周期时间。性能红利是真实的，但前提是你把它运维化。否则，它只是另一个功能演示。

**核心观点：** 不要购买更多的可观测性。**缩短从洞察到变更的距离。**