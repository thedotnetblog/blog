---
title: "Aspire 13.2：Bun支持、更好的容器和更少的调试摩擦"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2为Vite应用添加了一流的Bun支持，修复了Yarn可靠性问题，并带来了使本地开发行为更可预测的容器改进。"
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*本文已自动翻译。要查看原始版本，请[点击这里](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/)。*

如果你在Aspire中构建.NET后端和JavaScript前端，13.2是那种悄悄让你一天变得更好的更新。

## Bun现在是一等公民

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

如果你的团队已经使用Bun，Aspire不再让你逆流而上。

## Yarn更可靠了

Yarn用户在`withYarn()`和`addViteApp()`中会遇到更少的神秘失败。

## 容器改进

`ImagePullPolicy.Never`用于使用本地镜像而不访问注册表。PostgreSQL 18+数据卷现在可以正确工作。

## 调试改进

核心类型上的`DebuggerDisplayAttribute`，`WaitFor`的更好错误消息，`BeforeResourceStartedEvent`在正确时机触发。

David Pine的原始文章：[Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/)。
