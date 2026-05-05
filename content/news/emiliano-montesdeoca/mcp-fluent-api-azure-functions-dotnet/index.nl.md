---
title: "MCP-apps Krijgen een Fluent API — Bouw Rijke AI Tool UI in .NET in Drie Stappen"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "De nieuwe fluent-configuratie-API voor MCP Apps op Azure Functions laat je elk .NET MCP-tool omzetten in een volledige app met views, machtigingen en CSP-beleid."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

MCP-tools zijn geweldig voor het geven van mogelijkheden aan AI-agents. Maar wat als je tool iets aan de gebruiker moet tonen?

Lilian Kasem van het Azure SDK-team [introduceerde de nieuwe fluent-configuratie-API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).

## De fluent API in drie stappen

**Stap 1: Definieer je functie:**

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Stap 2: Promoveer het naar een MCP App:**

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

**Stap 3: Voeg je HTML-view toe.**

Voeg het pakket toe:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Lees de [volledige post](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).
