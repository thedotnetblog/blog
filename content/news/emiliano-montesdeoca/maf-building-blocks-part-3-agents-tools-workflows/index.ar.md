---
title: "Microsoft Agent Framework الجزء الثالث: من الأدوات إلى سير العمل — تتشابك قطع البناء في مكانها"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "يغطي الجزء الثالث من سلسلة Building Blocks for AI في .NET إطار عمل Microsoft Agent Framework — من الوكلاء المفردين بالأدوات إلى سير عمل متعدد الوكلاء مع الذاكرة. إليك ما يهم حقاً."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
dir: rtl
---

*تمت ترجمة هذه المقالة تلقائياً. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

إذا كنت تتابع سلسلة Building Blocks for AI في .NET، فأنت تعلم: الجزء الأول أعطانا `IChatClient` (الواجهة العالمية للنماذج)، والجزء الثاني أعطانا `Microsoft.Extensions.VectorData` (البحث الدلالي وRAG). كلاهما أساسي ومفيد بمفرده. لكن هنا يبدأ كل شيء في الاتصال ببعضه.

الجزء الثالث عن [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — وبصراحة، هذه القطعة التي كنت أنتظر رؤيتها في .NET. الإصدار 1.0 شُحن في أبريل. الواجهة البرمجية مستقرة. حان وقت بناء وكلاء حقيقيين.

## ما هو الوكيل فعلاً (مقابل روبوت المحادثة)

قبل الخوض في الكود، لنوضح هذا التمييز. روبوت المحادثة يستقبل المدخلات، يستدعي النموذج، يُعيد المخرجات. حلقة بسيطة.

الوكيل لديه *استقلالية*. يمكنه التفكير في مهمة، وتحديد الأدوات التي سيستخدمها، واستدعائها، وتقييم النتائج، والتقرير بما يفعله بعد ذلك — كل هذا دون كتابة منطق خطوة بخطوة لكل سيناريو. تعطيه الأدوات والتعليمات، ويتولى التنسيق بنفسه.

فكر في الأمر هكذا: `IChatClient` كإجراء محادثة. الوكيل كتفويض قائمة مهام لشخص ما.

## وكيلك الأول في 10 أسطر

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

أسلوب التمديد `.AsAIAgent()` هو الجسر. نفس النمط مثل `.AsIChatClient()` من MEAI — يلف SDK الموفر في تجريد مستقر. يعمل مع Azure OpenAI وOpenAI وGitHub Models وMicrosoft Foundry أو النماذج المحلية.

البث يعمل أيضاً:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## إعطاء الأدوات للوكيل

هنا يتوقف الوكلاء عن كونهم روبوتات محادثة متطورة. الأدوات هي وظائف يمكن للنموذج أن يقرر استدعاءها بناءً على طلب المستخدم. لا حاجة لمنطق توجيه من جانبك — النموذج يكتشف ذلك بنفسه.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

شيئان يستحقان الملاحظة. أولاً، `AIFunctionFactory` من MEAI — نفس مصنع الأدوات الذي ستستخدمه مع `IChatClient` العادي. إذا عرّفت أدوات لسيناريوهات الدردشة بالفعل، فهي تعمل هنا أيضاً.

ثانياً، سمات `Description` مهمة جداً. هذه هي الطريقة التي يفهم بها النموذج ما تفعله الأداة ومتى يستخدمها. تعامل معها كتوثيق لذكاءك الاصطناعي، لا للبشر.

## الجلسات: محادثات تتذكر فعلاً

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

بدون جلسة، كل استدعاء `RunAsync` عديم الحالة. مع الجلسة، الوكيل يعرف النكتة التي تشير إليها. `AgentSession` يحافظ على تاريخ المحادثة بين الأدوار.

للخدمات عديمة الحالة في الإنتاج، الجلسات تُسلسَل بشكل نظيف:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... خزّنه في مكان ما ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

هذا أمر بالغ الأهمية إذا كان وكيلك يعمل في بيئة serverless أو مُوسَّعة أفقياً.

## AIContextProvider: ذاكرة دائمة عبر الجلسات

الجلسات تحافظ على تاريخ المحادثة *داخل* جلسة. ولكن ماذا عن معرفة أشياء عن مستخدم عبر الجلسات؟ `AIContextProvider` يتعامل مع ذلك.

له خطافان:
- **`ProvideAIContextAsync`** — يعمل *قبل* كل تفاعل، يحقن سياقاً في الوكيل
- **`StoreAIContextAsync`** — يعمل *بعد* كل تفاعل، يتيح التعلم والاستمرارية

النمط أنيق: يمكنك تكديس موفرين متعددين — واحد لتفضيلات المستخدم، وآخر للتفاعلات الأخيرة، وآخر يستعلم من مخزن VectorData الخاص بك عن المستندات ذات الصلة. هذا الأخير هو بالضبط نمط RAG من الجزء الثاني، يعمل الآن تلقائياً كجزء من كل استدعاء للوكيل.

## سير عمل متعدد الوكلاء

هنا يستحق الإطار اسمه. يتضمن نظام سير عمل قائم على الرسم البياني حيث يتصل المنفذون (الوكلاء، الوظائف، أياً كان) عبر الحواف.

بعض الأنماط المدعومة أصلاً:

- **تسلسلي**: مخرجات الوكيل A تغذي الوكيل B
- **متزامن (توزيع/تجميع)**: الإرسال إلى وكلاء متعددين بالتوازي وتجميع النتائج
- **توجيه مشروط**: توجيه العمل إلى وكلاء مختلفين بناءً على المخرجات
- **حلقات الكاتب-الناقد**: وكيل يكتب، آخر يقيّم، حلقة حتى الموافقة
- **سير عمل فرعية**: تأليف سير العمل بشكل هرمي

مثال الكاتب-الناقد:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

نظيف، مقروء، والتوجيه القائم على الشروط يعني أنك لا تكتب منطق الحلقة بنفسك.

## الإنسان في الحلقة

لا ينبغي أن يعمل كل شيء باستقلالية كاملة. للعمليات الحساسة — الكتابة في قواعد البيانات، المعاملات المالية، إرسال الاتصالات — تريد أن يوافق إنسان قبل أن ينفذ الوكيل.

يحتوي الإطار على دعم مدمج لهذا عبر `FunctionApprovalRequestContent` و`FunctionApprovalResponseContent`. الوكيل يقترح استدعاء الأداة، كود تطبيقك يعرضه للمستخدم، والاستجابة تحدد ما إذا كان التنفيذ يستمر.

هذه هي الطريقة الصحيحة للتفكير في الوكلاء في البيئات المؤسسية: ليس مستقلاً بالكامل، بل *استقلالية بضوابط*.

## الصورة الكاملة

إذا تراجعت خطوة للخلف:

- **MEAI** يمنحك واجهة عالمية لأي نموذج
- **VectorData** يمنح وكلاءك الوصول إلى معرفة مؤسستك عبر البحث الدلالي
- **Agent Framework** ينسق كل شيء — يستخدم `IChatClient` داخلياً، يتكامل مع موفري السياق، وينسق عبر سير العمل

كل قطعة صُممت لتتكامل مع الأخريات. راجع [المنشور الأصلي لـ Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) و[مستودع GitHub لـ Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) للحصول على الأمثلة الكاملة.

## الخلاصة

منشور الجزء الثالث من Microsoft Agent Framework يُغلق حلقة سلسلة Building Blocks. لمطوري .NET الذين يريدون بناء وكلاء الذكاء الاصطناعي — ليس فقط روبوتات المحادثة، بل وكلاء حقيقيين يستخدمون الأدوات ويتذكرون الأشياء وينسقون — هذا هو طريقك للأمام.

الإصدار المستقر 1.0 يعني أنه يمكنك البناء بهذا في الإنتاج. إذا كنت تنتظر للقفز في تطوير الوكلاء في .NET، فالوقت الآن مناسب.
