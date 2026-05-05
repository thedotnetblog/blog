---
title: "MCP Apps को Fluent API मिला — .NET में तीन Steps में Rich AI Tool UIs बनाएं"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Azure Functions पर MCP Apps के लिए नया fluent configuration API आपको किसी भी .NET MCP tool को कुछ ही lines of code में views, permissions, और CSP policies के साथ एक full app में बदलने देता है।"
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

MCP tools AI agents को capabilities देने के लिए बेहतरीन हैं। लेकिन क्या होगा अगर आपके tool को user को कुछ दिखाना हो — एक dashboard, एक form, एक interactive visualization? यहीं MCP Apps काम आते हैं, और उन्हें build करना अब बहुत आसान हो गया है।

Azure SDK team की Lilian Kasem ने [.NET Azure Functions पर MCP Apps के लिए नया fluent configuration API introduce किया](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/), और यह उस तरह का developer experience improvement है जो आपको सोचने पर मजबूर करता है कि यह हमेशा से इतना simple क्यों नहीं था।

## MCP Apps क्या हैं?

MCP Apps Model Context Protocol को extend करते हैं जिससे tools अपने खुद के UI views, static assets, और security controls carry कर सकें। सिर्फ text return करने की बजाय, आपका MCP tool full HTML experiences render कर सकता है — interactive dashboards, data visualizations, configuration forms — सब AI agents द्वारा invokable और MCP clients द्वारा users को present किए जाने योग्य।

पहले की दिक्कत यह थी कि यह सब manually wire करने के लिए MCP spec को गहराई से जानना ज़रूरी था: `ui://` URIs, special mime types, tools और resources के बीच metadata coordination। मुश्किल नहीं, लेकिन झंझटी।

## Fluent API तीन steps में

**Step 1: अपना function define करें।** बस एक standard Azure Functions MCP tool:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Step 2: इसे MCP App में promote करें।** अपने program startup में:

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

**Step 3: अपना HTML view जोड़ें।** `assets/hello-app.html` बनाएं जिसमें आपको जो भी UI चाहिए।

बस। Fluent API सारी MCP spec plumbing handle करता है — synthetic resource function generate करना, सही mime type set करना, वह metadata inject करना जो आपके tool को उसके view से connect करता है।

## API surface अच्छी तरह design किया गया है

कुछ चीज़ें जो मुझे वाकई पसंद हैं:

**View sources flexible हैं।** आप disk पर files से HTML serve कर सकते हैं, या self-contained deployments के लिए resources directly अपनी assembly में embed कर सकते हैं:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP composable है।** आप explicitly उन origins को allowlist करते हैं जिनकी आपके app को ज़रूरत है, least-privilege principles follow करते हुए। `WithCsp` को कई बार call करें और origins accumulate होते हैं:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Visibility control।** आप किसी tool को केवल LLM को, केवल host UI को, या दोनों को visible बना सकते हैं। एक ऐसा tool चाहते हैं जो सिर्फ UI render करे और model द्वारा call नहीं होना चाहिए? आसान:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, model से छुपा हुआ
```

## शुरुआत करें

Preview package जोड़ें:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

अगर आप पहले से Azure Functions के साथ MCP tools build कर रहे हैं, तो यह बस एक package update है। [MCP Apps quickstart](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) शुरुआत के लिए सबसे अच्छी जगह है।

## निष्कर्ष

MCP Apps AI tooling space में सबसे exciting developments में से एक हैं — ऐसे tools जो सिर्फ *काम नहीं करते* बल्कि users को *कुछ दिखा भी सकते हैं*। Fluent API protocol की complexity हटाता है और आपको उस पर focus करने देता है जो मायने रखता है: आपके tool की logic और उसका UI।

Complete API reference और examples के लिए [पूरी post](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) पढ़ें।
