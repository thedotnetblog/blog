---
title: "停止锤打一个挣扎中的依赖：Azure Functions + Service Bus 的重试模式"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "指数退避和熔断器模式现在为 Service Bus 触发的 Azure Functions 提供原生支持 — 以下是它们的工作原理以及为什么你需要两者。"
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

以下是可恢复故障在 Functions 应用中变成服务中断的过程：依赖项开始超时，每个 Functions 实例立即无限重试，依赖项被数百个并发失败的请求轰炸，原本只是短暂故障的问题变成了全系统的反压事件。

你可能对这个故事很熟悉。Azure Functions 快速扩展 — 这就是整个意义所在。但"快速扩展"和"立即重试"结合在一起可能会使故障急剧恶化。

两种模式有所帮助。指数退避和熔断器。两者现在都为 Service Bus 触发的 Azure Functions 提供原生支持。

## 两种模式，不同角色

这些模式是互补的，而非替代：

**指数退避**回答：*我应该什么时候重试？*
它增加重试之间的延迟，让依赖项有时间恢复。在消息级别，调整重试时机。

**熔断器**回答：*我现在是否应该调用这个依赖项？*
在达到失败阈值后停止对不健康依赖项的重复调用，然后在冷却期后谨慎地探测。在系统级别，防止重试风暴。

你需要两者。退避处理每条消息的重试节奏。熔断器处理聚合的健康决策。

## 为什么这对 Service Bus 特别重要

队列吸收突发流量，这很好。但没有控制的话，队列可能增长，而工作者继续在会失败的调用上浪费计算资源。有毒消息保持活跃的时间比应该的更长。热分区或有限的下游容量会造成级联问题。

更安全的设计：

1. 检测瞬时故障
2. 使用指数退避延迟下一次尝试
3. 当达到失败阈值时停止调用依赖项（电路打开）
4. 冷却期后谨慎恢复（电路探测）
5. 将不可恢复的工作移到 dead-letter 或隔离路径

## 原生支持的外观

新支持与现有的 Azure Functions 主机模型集成 — 无需额外库，无需自定义实现。配置进入你的 `host.json`：

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

熔断器配置设置失败阈值和重置间隔，这样不健康的依赖项在恢复期间不会被轰炸。

## 涵盖的语言

这不仅仅是 .NET。该功能涵盖 dotnet、JavaScript、TypeScript 和 Python — Azure Functions 中 Service Bus 触发器支持的完整语言集。

## 总结

重试模式在配置时并不令人兴奋，直到第一次下游中断导致你的 Functions 加剧问题而不是优雅降级。主动配置这些是廉价的。在事故中进行改造则不然。

原始文章：[Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
