---
title: "Aplikacje MCP Dostają Fluent API — Buduj Bogate UI Narzędzi AI w .NET w Trzech Krokach"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Nowe płynne API konfiguracji dla aplikacji MCP na Azure Functions pozwala zamienić dowolne narzędzie MCP .NET w pełną aplikację z widokami, uprawnieniami i politykami CSP."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

Narzędzia MCP świetnie nadają się do dawania agentom AI możliwości. Ale co jeśli Twoje narzędzie musi coś pokazać użytkownikowi?

Lilian Kasem z zespołu Azure SDK [przedstawiła nowe płynne API konfiguracji](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).

## Płynne API w trzech krokach

**Krok 1: Zdefiniuj swoją funkcję:**

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Krok 2: Promuj ją do aplikacji MCP:**

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

**Krok 3: Dodaj swój widok HTML.**

Dodaj pakiet:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Przeczytaj [pełny post](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).
