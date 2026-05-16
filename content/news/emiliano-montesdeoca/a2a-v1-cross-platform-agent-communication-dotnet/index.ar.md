---
title: "A2A v1 هنا: التواصل بين الوكلاء عبر المنصات في Microsoft Agent Framework لـ .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "تم إصدار بروتوكول A2A v1.0 وتحديث حزم Microsoft Agent Framework لـ .NET — تشغيل بيني مستقر لربط وكلاء الذكاء الاصطناعي وعرضهم عبر الموفرين."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[A2A v1 هنا: التواصل بين الوكلاء عبر المنصات في Microsoft Agent Framework لـ .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — وصل بروتوكول A2A إلى الإصدار v1.0، وتم تحديث حزمتي A2A Agent (العميل) و A2A Hosting (الخادم) لـ .NET لتتطابق معه.

## ما هو A2A v1 في الواقع

A2A هو بروتوكول تشغيل بيني مفتوح لوكلاء الذكاء الاصطناعي مدعوم من لجنة توجيهية تقنية تضم ممثلين من AWS وCisco وGoogle وIBM Research وMicrosoft وSalesforce وSAP وServiceNow. يعني تسمية v1 أنه أصبح معيارًا مستقرًا وجاهزًا للإنتاج. حزم SDK وAgent Framework التي تنفذه لا تزال في مرحلة المعاينة، لكن البروتوكول نفسه مثبّت.

يُحسّن v1 على v0.3 بدعم تعدد المستأجرين، وبطاقات Agent Cards الموقّعة للهوية التشفيرية، وتدفقات أمان محسّنة، وبنية متوافقة مع الويب بشكل عام.

## الاتصال بوكيل A2A بعيد

الوكيل البعيد A2A هو مجرد `AIAgent` في كودك — نفس `RunAsync`، ونفس البث، ونفس إدارة الجلسات:

```csharp
// الاكتشاف عبر URI المعروف
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// التكوين المباشر
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// البث يعمل بنفس الطريقة
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## عرض وكيلك كنقطة نهاية A2A

أي `AIAgent` بنيته — على Microsoft Foundry أو Azure OpenAI أو OpenAI أو Anthropic أو AWS Bedrock — يمكن عرضه كنقطة نهاية A2A بسطرين في ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

تُقدَّم بطاقة الوكيل تلقائيًا على `/.well-known/agent-card.json`، حتى يتمكن أي عميل متوافق مع A2A من اكتشاف وكيلك واستدعائه.

## ما يعنيه هذا عمليًا

البروتوكول المستقر v1 يعني أنك تستطيع ربط وكلائك .NET بوكلاء مبنية بـ Python أو Java أو أي لغة أخرى دون القلق من تغييرات مكسِرة. الهوية التشفيرية في بطاقات الوكيل الموقّعة تمنحك أيضًا أساسًا للتحقق من الثقة بين الوكلاء.

راجع [المنشور الكامل](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) للاطلاع على سجل التغييرات الكامل وملاحظات الترحيل من v0.3.
