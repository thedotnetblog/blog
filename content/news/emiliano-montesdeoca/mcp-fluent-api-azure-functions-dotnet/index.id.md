---
title: "Aplikasi MCP Mendapatkan Fluent API — Buat UI Alat AI Kaya di .NET dalam Tiga Langkah"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "API konfigurasi fluent baru untuk Aplikasi MCP di Azure Functions memungkinkan Anda mengubah alat MCP .NET mana pun menjadi aplikasi lengkap dengan tampilan, izin, dan kebijakan CSP."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

Alat MCP sangat bagus untuk memberikan kemampuan kepada agen AI. Tapi bagaimana jika alat Anda perlu menampilkan sesuatu kepada pengguna?

Lilian Kasem dari tim Azure SDK [memperkenalkan API konfigurasi fluent baru](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).

## Fluent API dalam tiga langkah

**Langkah 1: Definisikan fungsi Anda:**

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Langkah 2: Promosikan ke Aplikasi MCP:**

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

**Langkah 3: Tambahkan tampilan HTML Anda.**

Tambahkan paket:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Baca [posting lengkap](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).
