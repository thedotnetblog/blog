---
title: "MCP Uygulamaları Fluent API Alıyor — .NET'te Üç Adımda Zengin AI Araç UI'ları Oluşturun"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Azure Functions'taki MCP Uygulamaları için yeni fluent yapılandırma API'si, herhangi bir .NET MCP aracını görünümler, izinler ve CSP politikalarıyla tam uygulamaya dönüştürmenizi sağlar."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

MCP araçları, AI agentlarına yetenekler vermek için harika. Peki ya aracınızın kullanıcıya bir şey göstermesi gerekiyorsa?

Azure SDK ekibinden Lilian Kasem, [yeni fluent yapılandırma API'sini tanıttı](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).

## Üç adımda fluent API

**Adım 1: Fonksiyonunuzu tanımlayın:**

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Adım 2: MCP Uygulamasına yükseltin:**

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

**Adım 3: HTML görünümünüzü ekleyin.**

Paketi ekleyin:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

[Tam yazıyı](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) okuyun.
