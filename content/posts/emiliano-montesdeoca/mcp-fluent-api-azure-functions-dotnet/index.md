---
title: "MCP Apps Get a Fluent API — Build Rich AI Tool UIs in .NET with Three Steps"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "The new fluent configuration API for MCP Apps on Azure Functions lets you turn any .NET MCP tool into a full app with views, permissions, and CSP policies in just a few lines of code."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

MCP tools are great for giving AI agents capabilities. But what if your tool needs to show something to the user — a dashboard, a form, an interactive visualization? That's where MCP Apps come in, and they just got a lot easier to build.

Lilian Kasem from the Azure SDK team [introduced the new fluent configuration API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) for MCP Apps on .NET Azure Functions, and it's the kind of developer experience improvement that makes you wonder why it wasn't always this simple.

## What are MCP Apps?

MCP Apps extend the Model Context Protocol by letting tools carry their own UI views, static assets, and security controls. Instead of just returning text, your MCP tool can render full HTML experiences — interactive dashboards, data visualizations, configuration forms — all invocable by AI agents and presented to users by MCP clients.

The catch was that wiring all this up manually required knowing the MCP spec intimately: `ui://` URIs, special mime types, metadata coordination between tools and resources. Not hard, but fiddly.

## The fluent API in three steps

**Step 1: Define your function.** Just a standard Azure Functions MCP tool:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Step 2: Promote it to an MCP App.** In your program startup:

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

**Step 3: Add your HTML view.** Create `assets/hello-app.html` with whatever UI you need.

That's it. The fluent API handles all the MCP spec plumbing — generating the synthetic resource function, setting the correct mime type, injecting the metadata that connects your tool to its view.

## The API surface is well-designed

A few things I really like:

**View sources are flexible.** You can serve HTML from files on disk, or embed resources directly in your assembly for self-contained deployments:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP is composable.** You explicitly allowlist origins your app needs, following least-privilege principles. Call `WithCsp` multiple times and origins accumulate:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Visibility control.** You can make a tool visible to the LLM only, the host UI only, or both. Want a tool that only renders UI and shouldn't be called by the model? Easy:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Getting started

Add the preview package:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

If you're already building MCP tools with Azure Functions, this is just a package update. The [MCP Apps quickstart](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) is the best place to start if you're new to the concept.

## Wrapping up

MCP Apps are one of the more exciting developments in the AI tooling space — tools that don't just *do things* but can *show things* to users. The fluent API removes the protocol complexity and lets you focus on what matters: your tool's logic and its UI.

Read the [full post](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) for the complete API reference and examples.
