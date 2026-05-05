---
title: "每天花68分钟重新解释代码？这里有个解决方案"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "上下文腐烂是真实存在的——你的AI代理在30轮之后就会迷失，你每小时都在支付压缩税。auto-memory给GitHub Copilot CLI提供了外科式的记忆，而不需要消耗数千个token。"
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*本文已自动翻译。要查看原始版本，请[点击这里](https://thedotnetblog.com/posts/emiliano-montesdeoca/auto-memory-stop-re-explaining-code-to-copilot/)。*

你知道那个时刻——当你的Copilot会话触发`/compact`，代理完全忘记你在做什么？你花接下来五分钟重新解释文件结构、失败的测试、你已经尝试过的三种方法。然后又发生了。

Desi Villanueva测量了一下：**每天68分钟** — 仅用于重新定向。不是写代码，不是审查PR，只是让AI了解它已经知道的事情。

## 上下文窗口的谎言

实际计算：200K总上下文，减去MCP工具65K，减去指令文件10K，实际上**在你输入任何内容之前只剩125K**。LLM在60%容量时会撞墙，有效限制是**45K token**。

## 压缩税

残忍的部分：**记忆已经存在。** Copilot CLI将每个会话写入`~/.copilot/session-store.db`中的本地SQLite数据库。代理只是无法读取它。

## auto-memory：召回层，而非记忆系统

```bash
pip install auto-memory
```

~1,900行Python。零依赖。30秒安装完成。

不是用grep结果淹没上下文，而是给代理外科式访问真正重要的内容——**50个token而不是10,000个**。

## 总结

上下文腐烂是真实的架构约束。auto-memory通过给你的代理提供廉价、精确的召回机制来绕过它。

查看：[GitHub上的auto-memory](https://github.com/dezgit2025/auto-memory)。Desi Villanueva的原始文章：[I Wasted 68 Minutes a Day](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/)。
