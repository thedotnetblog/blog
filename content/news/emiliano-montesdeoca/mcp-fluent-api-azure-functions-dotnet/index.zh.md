---
title: "MCP Apps 迎来 Fluent API — 三步在 .NET 中构建丰富的 AI 工具界面"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Azure Functions 上 MCP Apps 的全新 Fluent 配置 API 让你只需几行代码就能将任何 .NET MCP 工具转变为带有视图、权限和 CSP 策略的完整应用。"
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}})。*

MCP 工具非常适合赋予 AI 代理各种能力。但如果你的工具需要向用户展示某些东西呢？比如仪表板、表单或交互式可视化？这就是 MCP Apps 的用武之地，而且现在构建它们变得简单多了。

Azure SDK 团队的 Lilian Kasem [发布了全新的 Fluent 配置 API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)，用于 .NET Azure Functions 上的 MCP Apps。这种开发者体验的改进会让你想，为什么以前不一直这么简单呢。

## 什么是 MCP Apps？

MCP Apps 扩展了 Model Context Protocol，让工具可以携带自己的 UI 视图、静态资源和安全控制。你的 MCP 工具不再只是返回文本，而是可以渲染完整的 HTML 体验 — 交互式仪表板、数据可视化、配置表单 — 全部可由 AI 代理调用，并通过 MCP 客户端呈现给用户。

问题在于，手动连接这一切需要深入了解 MCP 规范：`ui://` URI、特殊 MIME 类型、工具和资源之间的元数据协调。不难，但很繁琐。

## Fluent API 三步走

**第一步：定义你的函数。** 标准的 Azure Functions MCP 工具：

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**第二步：将其提升为 MCP App。** 在程序启动中：

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**第三步：添加你的 HTML 视图。** 创建 `assets/hello-app.html`，放入你需要的界面。

就这样。Fluent API 处理了所有 MCP 协议的管道工作 — 生成合成资源函数、设置正确的 MIME 类型、注入将工具与其视图连接起来的元数据。

## API 设计精良

几个我特别喜欢的地方：

**视图源灵活。** 你可以从磁盘文件提供 HTML，也可以将资源直接嵌入程序集中以实现自包含部署：

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP 可组合。** 你明确允许应用所需的来源，遵循最小权限原则。多次调用 `WithCsp`，来源会累积：

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**可见性控制。** 你可以让工具仅对 LLM 可见、仅对宿主 UI 可见，或两者兼具。想要一个只渲染 UI 而不应被模型调用的工具？简单：

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## 开始使用

添加预览包：

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

如果你已经在用 Azure Functions 构建 MCP 工具，这只是一个包更新。如果你是新手，[MCP Apps 快速入门](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp)是最好的起点。

## 总结

MCP Apps 是 AI 工具领域最令人兴奋的发展之一 — 不仅能*做事*，还能向用户*展示事物*的工具。Fluent API 消除了协议复杂性，让你专注于真正重要的事：工具的逻辑和界面。

阅读[完整文章](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)获取完整的 API 参考和示例。
