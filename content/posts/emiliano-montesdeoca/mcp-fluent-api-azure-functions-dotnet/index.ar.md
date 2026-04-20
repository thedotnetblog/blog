---
title: "تطبيقات MCP تحصل على واجهة برمجة سلسة — أنشئ واجهات أدوات AI غنية في .NET بثلاث خطوات"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "واجهة التهيئة السلسة الجديدة لتطبيقات MCP على Azure Functions تتيح لك تحويل أي أداة .NET MCP إلى تطبيق كامل بمشاهدات وصلاحيات وسياسات CSP في بضعة أسطر من الكود."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

أدوات MCP رائعة لمنح وكلاء الذكاء الاصطناعي قدرات. لكن ماذا لو احتاجت أداتك إلى عرض شيء للمستخدم — لوحة معلومات، أو نموذج، أو مرئيات تفاعلية؟ هنا يأتي دور تطبيقات MCP، وقد أصبح بناؤها أسهل بكثير للتوّ.

Lilian Kasem من فريق Azure SDK [قدّمت واجهة التهيئة السلسة الجديدة](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) لتطبيقات MCP على .NET Azure Functions، وهو نوع تحسين تجربة المطوّر الذي يجعلك تتساءل لماذا لم يكن الأمر بهذه البساطة دائماً.

## ما هي تطبيقات MCP؟

تطبيقات MCP تُوسّع Model Context Protocol بالسماح للأدوات بحمل مشاهداتها UI الخاصة، والأصول الثابتة، وعناصر التحكم الأمني. بدلاً من إعادة نص فحسب، يمكن لأداة MCP الخاصة بك عرض تجارب HTML كاملة — لوحات معلومات تفاعلية، ومرئيات بيانات، ونماذج تهيئة — كلها قابلة للاستدعاء من وكلاء الذكاء الاصطناعي ومُقدَّمة للمستخدمين من قِبل عملاء MCP.

كان الإشكال أن توصيل كل هذا يدوياً استلزم معرفة عميقة بمواصفات MCP: عناوين URI بصيغة `ui://`، وأنواع MIME خاصة، وتنسيق البيانات الوصفية بين الأدوات والموارد. ليس صعباً، لكنه مُضجِر.

## واجهة البرمجة السلسة في ثلاث خطوات

**الخطوة 1: عرّف دالتك.** مجرد أداة Azure Functions MCP قياسية:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**الخطوة 2: ارقِها إلى تطبيق MCP.** في بدء تشغيل برنامجك:

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

**الخطوة 3: أضف مشهد HTML الخاص بك.** أنشئ `assets/hello-app.html` بأي واجهة مستخدم تحتاجها.

هذا كل شيء. واجهة البرمجة السلسة تتولى جميع التجهيزات الخاصة بمواصفات MCP — توليد دالة الموارد الاصطناعية، وضبط نوع MIME الصحيح، وحقن البيانات الوصفية التي تربط أداتك بمشهدها.

## سطح واجهة البرمجة مصمَّم جيداً

بعض الأشياء التي أعجبتني حقاً:

**مصادر المشهد مرنة.** يمكنك تقديم HTML من ملفات على القرص، أو تضمين الموارد مباشرةً في التجميع للنشر الكامل المستقل:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP قابل للتركيب.** تُدرج صراحةً المصادر الأصلية التي يحتاجها تطبيقك، متبعاً مبادئ الامتياز الأدنى. استدعِ `WithCsp` عدة مرات وتتراكم المصادر:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**التحكم في الرؤية.** يمكنك جعل الأداة مرئية لـ LLM فقط، أو لواجهة المضيف فقط، أو لكليهما. تريد أداة تعرض واجهة المستخدم فقط ولا ينبغي للنموذج استدعاؤها؟ سهل:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## البدء

أضف حزمة المعاينة:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

إذا كنت تبني أدوات MCP مع Azure Functions بالفعل، فهذا مجرد تحديث حزمة. [دليل البدء السريع لتطبيقات MCP](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) هو أفضل نقطة انطلاق إذا كنت جديداً على المفهوم.

## خلاصة

تطبيقات MCP من أكثر التطورات إثارةً في مساحة أدوات الذكاء الاصطناعي — أدوات لا تكتفي بـ *فعل الأشياء* بل تستطيع *عرض الأشياء* للمستخدمين. واجهة البرمجة السلسة تُزيل تعقيد البروتوكول وتتيح لك التركيز على ما يهمّ: منطق أداتك وواجهة مستخدمها.

اقرأ [المنشور الكامل](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) للمرجع الكامل لواجهة البرمجة والأمثلة.
