---
title: "تطبيقات MCP تحصل على Fluent API — بناء واجهات مستخدم أدوات AI غنية في .NET بثلاث خطوات"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "واجهة برمجة التطبيقات الجديدة للتهيئة السلسة لتطبيقات MCP على Azure Functions تتيح لك تحويل أي أداة MCP لـ .NET إلى تطبيق كامل مع views وصلاحيات وسياسات CSP."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

أدوات MCP رائعة لمنح وكلاء الذكاء الاصطناعي قدرات. لكن ماذا لو كانت أداتك تحتاج إلى إظهار شيء للمستخدم؟

قدّمت Lilian Kasem من فريق Azure SDK [واجهة برمجة التهيئة السلسة الجديدة](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).

## Fluent API في ثلاث خطوات

**الخطوة 1: عرّف دالتك:**

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**الخطوة 2: رقّها إلى تطبيق MCP:**

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

**الخطوة 3: أضف view HTML الخاص بك.**

أضف الحزمة:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

اقرأ [المنشور الكامل](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/).
