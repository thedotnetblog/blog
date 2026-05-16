---
title: "A2A v1 आ गया: Microsoft Agent Framework for .NET में Cross-Platform एजेंट संचार"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "A2A Protocol v1.0 जारी हो गया है और Microsoft Agent Framework के .NET पैकेज अपडेट हो गए हैं — AI एजेंट को कनेक्ट और एक्सपोज़ करने के लिए स्थिर इंटरऑपरेबिलिटी मानक।"
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[A2A v1 आ गया: Microsoft Agent Framework for .NET में Cross-Platform एजेंट संचार](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — A2A Protocol अभी v1.0 तक पहुंचा है, और .NET के लिए A2A Agent (क्लाइंट) और A2A Hosting (सर्वर) दोनों पैकेज अपडेट हो गए हैं।

## A2A v1 वास्तव में क्या है

A2A AI एजेंट के लिए एक ओपन इंटरऑपरेबिलिटी प्रोटोकॉल है जो AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP और ServiceNow के प्रतिनिधियों के साथ एक तकनीकी संचालन समिति द्वारा समर्थित है। v1 लेबल का मतलब है कि यह अब एक स्थिर, प्रोडक्शन-रेडी मानक है। इसे लागू करने वाले SDK और Agent Framework पैकेज अभी भी preview में हैं, लेकिन प्रोटोकॉल स्वयं स्थिर है।

v1 ने v0.3 में multi-tenancy support, cryptographic identity के लिए signed Agent Cards, बेहतर security flows, और web-aligned architecture जोड़कर सुधार किया है।

## Remote A2A एजेंट से कनेक्ट करना

Remote A2A एजेंट आपके कोड में बस एक `AIAgent` है — वही `RunAsync`, वही streaming, वही session handling:

```csharp
// Well-known URI के माध्यम से discovery
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Direct configuration
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Streaming उसी तरह काम करता है
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## अपने एजेंट को A2A endpoint के रूप में expose करना

कोई भी `AIAgent` जो आपने बनाया है — Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, या AWS Bedrock पर — ASP.NET Core में दो लाइन के साथ A2A endpoint के रूप में expose किया जा सकता है:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

एजेंट कार्ड `/.well-known/agent-card.json` पर स्वचालित रूप से serve होती है।

## व्यवहार में इसका क्या मतलब है

स्थिर v1 प्रोटोकॉल का मतलब है कि आप अपने .NET एजेंट को Python, Java या किसी अन्य भाषा में बने एजेंट से बिना breaking changes की चिंता किए जोड़ सकते हैं। Signed Agent Cards में cryptographic identity भी एजेंट के बीच trust verification के लिए एक आधार प्रदान करती है।

पूर्ण changelog और v0.3 से migration notes के लिए [पूरा post](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) देखें।
