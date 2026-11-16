---
title: "NTLM 即将从 Git/libcurl 中移除：Azure DevOps Server 团队需要真正的迁移计划"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "2026 年 9 月的 NTLM 移除不是一个小兼容问题；它是对本地 Azure DevOps Server 环境的身份架构截止日期。"
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

即将到来的 libcurl 中 NTLM 的移除，是那种看起来是技术问题但实际上是组织问题的变化。如果你通过 HTTPS 到 Azure DevOps Server 的 Git 路径仍然依赖 NTLM，你的问题不是工具，而是身份债务。

原文来源：https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

微软在这方面强硬推动是正确的。NTLM 存在已知的加密弱点，不应成为现代企业的默认选项。危险之处在于，许多环境自以为在使用 Kerberos，实际上却靠无声的 SPNEGO 回退到 NTLM 在维持。这个假象将在 2026 年 9 月消失。

我的观点：**不要把这当作一个"客户端版本"问题**。重新启用 NTLM 标志、锁定旧版 Git 版本，或希望回退仍然可用，是个短期解决方案且伴随长期风险。如果你的修复策略是降级和延迟，你是在主动增加运维脆弱性。

一个实用的迁移序列应该直白且可衡量。

- **立即验证当前的身份验证行为。** 在真实的开发者和构建代理上下文中运行基于跟踪的检查和票据缓存验证，包括脱离域和远程网络路径。
- **端到端修复 Kerberos：** SPN、DNS 别名、负载均衡器设置、委派和域控制器可达性。
- **尽早识别非域加入或工作组场景**，并在 Kerberos 无法可靠运行的地方设计 SSH 通道。

你还需要明确所有权。安全团队应定义策略基线，但平台工程必须负责实施就绪性。这不能是单个仓库管理员的副线任务，它需要跨 IIS、AD、网络边缘、CI 代理和开发者工作站指导的协调变更。

一个微妙的风险是自动化。构建代理和服务账户经常在没有 Kerberos 票据或票据无效的上下文中运行，即使人类用户一切正常。如果你只测试交互式开发者工作流，你会错过最关键的故障点。

好处是实实在在的。干净地迁移到 Kerberos 或 SSH 不仅避免了故障，还**减少了攻击面并将身份控制与现代化合规期望对齐**。现在开始这个过渡的团队会把 9 月当作无事发生。等待的团队将在发布压力下调试身份验证故障。

这不是一个存档警告。**这是一个需要执行的截止日期。**