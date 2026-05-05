---
title: "Microsoft Agent Framework 中的后台响应：告别超时焦虑"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 现在允许通过延续令牌卸载长时间运行的 AI 任务。了解后台响应如何工作以及为什么它们对你的 .NET 代理很重要。"
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

如果你用 o3 或 GPT-5.2 等推理模型构建过任何东西，你就知道那种痛苦。你的代理开始思考一个复杂的任务，客户端在那里等待，在"没问题"和"它是不是崩了？"之间的某个时刻，你的连接超时了。那些工作？全没了。

Microsoft Agent Framework 刚刚推出了[后台响应](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — 说实话，这是那种从第一天就应该存在的功能。

## 阻塞调用的问题

在传统的请求-响应模式中，你的客户端会阻塞直到代理完成。对于快速任务来说没问题。但当你让推理模型做深度研究、多步分析或生成 20 页报告时？你面对的是几分钟的实际等待时间。在这个窗口期：

- HTTP 连接可能超时
- 网络抖动会杀死整个操作
- 你的用户盯着一个加载动画想知道是否有事情在发生

后台响应彻底翻转了这个局面。

## 延续令牌如何工作

你不再阻塞等待，而是启动代理任务并获得一个**延续令牌**。把它想象成修理店的取件单 — 你不需要站在柜台前等着，准备好了再回来取就行。

流程很简单：

1. 使用 `AllowBackgroundResponses = true` 发送请求
2. 如果代理支持后台处理，你会收到一个延续令牌
3. 按你的节奏轮询，直到令牌返回 `null` — 这意味着结果准备好了

这是 .NET 版本：

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// 轮询直到完成
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

如果代理立即完成（简单任务、不需要后台处理的模型），不会返回延续令牌。你的代码正常工作 — 无需特殊处理。

## 带恢复的流式传输：真正的魔法

轮询对于即发即忘的场景没问题，但当你想要实时进度呢？后台响应也支持带内置恢复功能的流式传输。

每个流式更新都携带自己的延续令牌。如果你的连接在流传输中断了，你可以从中断的确切位置恢复：

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // 模拟网络中断
}

// 从中断的确切位置恢复
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

无论客户端发生什么，代理都会继续在服务器端处理。这是内置的容错能力，无需你编写重试逻辑或断路器。

## 什么时候该真正使用这个

不是每个代理调用都需要后台响应。对于快速完成，你只是在无故增加复杂性。但以下场景是它们大放异彩的地方：

- **复杂推理任务** — 多步分析、深度研究、任何让推理模型真正思考的内容
- **长内容生成** — 详细报告、多部分文档、广泛分析
- **不可靠的网络** — 移动客户端、边缘部署、不稳定的企业 VPN
- **异步 UX 模式** — 提交任务，去做别的事，回来取结果

对于构建企业应用的 .NET 开发者来说，最后一点特别有趣。想想一个 Blazor 应用，用户请求一个复杂的报告 — 你启动代理任务，显示进度指示器，让他们继续工作。不需要 WebSocket 体操，不需要自定义队列基础设施，只需一个令牌和一个轮询循环。

## 总结

后台响应现在通过 Microsoft Agent Framework 在 .NET 和 Python 中都可用。如果你构建的代理做的事情比简单的问答更复杂，这值得加入你的工具包。延续令牌模式保持简单的同时解决了一个非常真实的生产问题。

查看[完整文档](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/)获取完整的 API 参考和更多示例。
