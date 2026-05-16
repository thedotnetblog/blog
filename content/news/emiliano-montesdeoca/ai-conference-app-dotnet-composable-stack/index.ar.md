---
title: "بناء تطبيق مؤتمر مدعوم بالذكاء الاصطناعي باستخدام Stack القابل للتركيب في .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "قامت Microsoft ببناء ConferencePulse — تطبيق Blazor للمؤتمرات المباشرة — من خلال تركيب Microsoft.Extensions.AI وDataIngestion وVectorData وMCP وAgent Framework معًا. إليك كيف تتلاءم القطع."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[بناء تطبيق مؤتمر مدعوم بالذكاء الاصطناعي باستخدام Stack القابل للتركيب في .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — قامت Microsoft ببناء ConferencePulse، وهو تطبيق Blazor Server للجلسات المباشرة في المؤتمرات، من خلال تركيب خمسة مكتبات امتداد .NET معًا. استخدمته في قمة MVP.

## ما الذي يفعله ConferencePulse

يعمل ConferencePulse خلال الجلسات المباشرة ويوفر: استطلاعات مولدة بالذكاء الاصطناعي من محتوى الجلسة، وأسئلة وأجوبة الجمهور عبر خط أنابيب RAG يسحب من قاعدة معرفة مباشرة، ورؤى مولدة تلقائيًا، وملخصات الجلسات المنتجة بواسطة وكلاء ذكاء اصطناعي متزامنين متعددين. المكدس هو .NET 10 وBlazor Server وAspire، مقسم عبر خمسة مشاريع: Web وCore وIngestion وAgents وMcp وAppHost.

## Microsoft.Extensions.AI: تجريد واحد لكل شيء

`IChatClient` هو التجريد الموحد — تقوم بإعداده مرة واحدة ويعمل نفس الواجهة مع Azure OpenAI وOpenAI وAnthropic أو أي موفر آخر. ست أسطر للحصول على عميل مكوّن بالكامل مع استدعاء الوظائف وتتبع OpenTelemetry ووسيطة التسجيل:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

يُعاد استخدام نفس `IChatClient` لاحقًا في خطوة إثراء استيعاب البيانات — لا يوجد عميل منفصل لذلك.

## خط أنابيب DataIngestion

يتدفق محتوى الجلسة عبر خط أنابيب: `MarkdownReader` ← `HeaderChunker` (500 رمز، تداخل 50 رمزًا) ← `SummaryEnricher` + `KeywordEnricher` ← `VectorStoreWriter` (Qdrant). تستخدم أدوات الإثراء نفس `IChatClient` لتوليد الملخصات واستخراج الكلمات المفتاحية قبل الفهرسة. يتم استيعاب أسئلة الجمهور وأزواج الأسئلة والأجوبة ونتائج الاستطلاعات في الوقت الفعلي مع تقدم الجلسة — تنمو قاعدة المعرفة خلال المحادثة.

## VectorData: بحث مستقل عن الموفر

`VectorStoreCollection.SearchAsync()` يعمل بنفس الطريقة سواء كان المخزن الداعم هو Qdrant أو Azure AI Search. البحث الهجين (متجه + نص كامل) مدعوم. يستعلم خط أنابيب RAG لأسئلة وأجوبة الجمهور هذه المجموعة ويحصل على أجزاء ذات صلة لتمريرها كسياق إلى عميل الدردشة.

## MCP: محتوى الجلسة كأدوات

يتم الكشف عن محتوى الجلسة عبر MCP بحيث يمكن لأي عميل متوافق مع MCP الوصول إليه. يتم تنفيذ كل من الخادم والعميل — يكشف الخادم عن معرفة الجلسة كأدوات MCP، ويتيح العميل استدعاء تلك الأدوات من داخل خط أنابيب الوكيل.

## Agent Framework: ملخص متعدد الوكلاء المتوازي

يتم توليد ملخص الجلسة بواسطة ثلاثة وكلاء يعملون في وقت واحد — `PollSummaryAgent` و`QuestionSummaryAgent` و`InsightSummaryAgent` — ثم يتم دمجها. يستخدم هذا نمط الدردشة الجماعية أو التنفيذ المتوازي من Microsoft Agent Framework. يتعامل كل وكيل مع مصلحة واحدة؛ يدمج المنسق المخرجات.

## مبدأ التصميم

يُقدم المنشور نقطة تستحق الاحتفاظ بها: استخدم أبسط أداة تناسب الغرض. استدعاءات `IChatClient` المباشرة لمهام التوليد البسيطة. استدعاء الأداة/الوظيفة لاستخراج البيانات المنظمة. الوكلاء الكاملون فقط عندما تحتاج إلى استدلال متعدد الخطوات المستقل. يفرض تطبق المكتبات ذلك — يمكنك اختيار `Microsoft.Extensions.AI` دون سحب Agent Framework الكامل.

راجع [المنشور الكامل](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) للاطلاع على هيكل المشروع الكامل وروابط المصدر.
