---
title: "Microsoft Agent Framework भाग 3: टूल्स से वर्कफ्लो तक — बिल्डिंग ब्लॉक्स अपनी जगह पर क्लिक हो जाते हैं"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: ".NET AI बिल्डिंग ब्लॉक्स सीरीज के भाग 3 में Microsoft Agent Framework को कवर किया गया है — टूल्स वाले सिंगल एजेंट से लेकर मेमोरी वाले मल्टी-एजेंट वर्कफ्लो तक। जानें क्या वाकई मायने रखता है।"
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

अगर आप .NET में Building Blocks for AI सीरीज को फॉलो कर रहे हैं, तो आप जानते हैं: भाग 1 ने हमें `IChatClient` (यूनिवर्सल मॉडल इंटरफेस) दिया और भाग 2 ने `Microsoft.Extensions.VectorData` (सिमेंटिक सर्च और RAG)। दोनों फंडामेंटल हैं, दोनों अपने आप में उपयोगी हैं। लेकिन यहाँ से सब कुछ कनेक्ट होना शुरू होता है।

भाग 3 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) के बारे में है — और ईमानदारी से, यह वही पीस है जिसे मैं .NET में देखने का इंतजार कर रहा था। 1.0 अप्रैल में शिप हुआ। API स्थिर है। असली एजेंट बनाने का समय आ गया है।

## एजेंट वास्तव में क्या है (vs. चैटबॉट)

कोड में जाने से पहले, इस अंतर को समझ लेते हैं। एक चैटबॉट इनपुट रिसीव करता है, मॉडल कॉल करता है, आउटपुट रिटर्न करता है। सिंपल लूप।

एक एजेंट के पास *ऑटोनॉमी* होती है। वह किसी टास्क के बारे में रिजन कर सकता है, तय कर सकता है कि कौन से टूल्स इस्तेमाल करने हैं, उन्हें कॉल कर सकता है, रिजल्ट्स इवैल्युएट कर सकता है और तय कर सकता है कि आगे क्या करना है — यह सब बिना आपके हर सिनेरियो के लिए स्टेप-बाय-स्टेप लॉजिक लिखे। आप उसे टूल्स और इंस्ट्रक्शन देते हैं, और वह ऑर्केस्ट्रेशन खुद संभाल लेता है।

इस तरह सोचें: `IChatClient` एक बातचीत करने जैसा है। एक एजेंट किसी को टास्क लिस्ट सौंपने जैसा है।

## 10 लाइनों में आपका पहला एजेंट

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

`.AsAIAgent()` एक्सटेंशन मेथड ब्रिज है। MEAI के `.AsIChatClient()` जैसा ही पैटर्न — प्रोवाइडर के SDK को एक स्थिर एब्स्ट्रैक्शन में रैप करता है। Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry या लोकल मॉडल्स के साथ काम करता है।

स्ट्रीमिंग भी काम करती है:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## एजेंट को टूल्स देना

यहीं पर एजेंट फैंसी चैटबॉट्स नहीं रहते। टूल्स वो फंक्शन्स हैं जिन्हें मॉडल यूजर के रिक्वेस्ट के आधार पर कॉल करने का फैसला कर सकता है। आपकी तरफ से कोई रूटिंग लॉजिक नहीं चाहिए — मॉडल खुद समझ लेता है।

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

दो बातें ध्यान देने लायक। पहली, `AIFunctionFactory` MEAI से है — वही टूल फैक्ट्री जो आप एक नॉर्मल `IChatClient` के साथ इस्तेमाल करते। अगर आपने चैट सिनेरियोज़ के लिए टूल्स पहले से डिफाइन किए हैं, वो यहाँ भी काम करते हैं।

दूसरी, `Description` एट्रिब्यूट्स बहुत मायने रखते हैं। इसी तरह मॉडल समझता है कि कोई टूल क्या करता है और कब इस्तेमाल करना है। इन्हें इंसानों के लिए नहीं, अपनी AI के लिए डॉक्युमेंटेशन मानें।

## सेशन: वाकई याद रखने वाली बातचीत

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

बिना सेशन के, हर `RunAsync` कॉल स्टेटलेस होती है। सेशन के साथ, एजेंट जानता है आप किस जोक की बात कर रहे हैं। `AgentSession` टर्न्स के बीच कन्वर्सेशन हिस्ट्री प्रिजर्व करता है।

प्रोडक्शन स्टेटलेस सर्विसेज के लिए, सेशन्स क्लीनली सीरियलाइज होते हैं:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... कहीं स्टोर करें ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

यह क्रिटिकल है अगर आपका एजेंट सर्वरलेस या होरिजोंटली-स्केल्ड एनवायरनमेंट में रन करता है।

## AIContextProvider: सेशन्स के पार परसिस्टेंट मेमोरी

सेशन्स एक सेशन *के भीतर* कन्वर्सेशन हिस्ट्री प्रिजर्व करते हैं। लेकिन सेशन्स के पार किसी यूजर के बारे में जानकारी? `AIContextProvider` यह हैंडल करता है।

इसके दो हुक्स हैं:
- **`ProvideAIContextAsync`** — हर इंटरैक्शन से *पहले* रन होता है, एजेंट में कॉन्टेक्स्ट इंजेक्ट करता है
- **`StoreAIContextAsync`** — हर इंटरैक्शन के *बाद* रन होता है, सीखने और परसिस्ट करने की सुविधा देता है

पैटर्न एलीगेंट है: आप मल्टीपल प्रोवाइडर्स स्टैक कर सकते हैं — एक यूजर प्रेफरेंसेज के लिए, एक हालिया इंटरैक्शन्स के लिए, एक जो रिलेवेंट डॉक्यूमेंट्स के लिए VectorData स्टोर क्वेरी करे। आखिरी वाला भाग 2 का RAG पैटर्न है, जो अब हर एजेंट कॉल के पार्ट के रूप में ऑटोमैटिकली रन होता है।

## मल्टी-एजेंट वर्कफ्लो

यहाँ फ्रेमवर्क अपना नाम सार्थक करता है। इसमें एक ग्राफ-बेस्ड वर्कफ्लो सिस्टम है जहाँ एग्जीक्यूटर्स (एजेंट, फंक्शन्स, जो भी) एजेस के जरिए कनेक्ट होते हैं।

नेटिवली सपोर्टेड कुछ पैटर्न:

- **सीक्वेंशियल**: एजेंट A का आउटपुट एजेंट B में जाता है
- **कंकरेंट (फैन-आउट/फैन-इन)**: मल्टीपल एजेंट्स को पैरेलल में डिस्पैच, रिजल्ट्स कलेक्ट
- **कंडीशनल रूटिंग**: आउटपुट के आधार पर अलग-अलग एजेंट्स को वर्क रूट करें
- **राइटर-क्रिटिक लूप्स**: एक एजेंट लिखता है, दूसरा इवैल्युएट करता है, अप्रूव होने तक लूप
- **सब-वर्कफ्लो**: वर्कफ्लो को हायरार्किकली कम्पोज करें

राइटर-क्रिटिक एग्जाम्पल:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

क्लीन, रीडेबल, और कंडीशन-बेस्ड रूटिंग का मतलब है कि आपको खुद लूप लॉजिक नहीं लिखनी।

## ह्यूमन-इन-द-लूप

हर चीज पूरी तरह ऑटोनॉमस तरीके से नहीं चलनी चाहिए। सेंसिटिव ऑपरेशन्स के लिए — डेटाबेस राइट्स, फाइनेंशियल ट्रांजेक्शन्स, कम्युनिकेशन भेजना — आप चाहते हैं कि एजेंट एग्जीक्यूट करने से पहले कोई इंसान अप्रूव करे।

फ्रेमवर्क में इसके लिए `FunctionApprovalRequestContent` और `FunctionApprovalResponseContent` के जरिए बिल्ट-इन सपोर्ट है। एजेंट टूल कॉल प्रोपोज करता है, आपका एप्लिकेशन कोड इसे यूजर को प्रेजेंट करता है, और रिस्पॉन्स तय करता है कि एग्जीक्यूशन आगे बढ़ेगा या नहीं।

एंटरप्राइज सेटिंग्स में एजेंट्स के बारे में सोचने का यही सही तरीका है: पूरी तरह ऑटोनॉमस नहीं, बल्कि *गार्डरेल्स के साथ ऑटोनॉमी*।

## पूरी तस्वीर

एक कदम पीछे जाकर देखें:

- **MEAI** किसी भी मॉडल का यूनिवर्सल इंटरफेस देता है
- **VectorData** सिमेंटिक सर्च के जरिए एजेंट्स को आपके ऑर्गेनाइजेशन की नॉलेज तक पहुंचने देता है
- **Agent Framework** सब कुछ ऑर्केस्ट्रेट करता है — इंटर्नली `IChatClient` इस्तेमाल करता है, कॉन्टेक्स्ट प्रोवाइडर्स के साथ कम्पोज होता है, वर्कफ्लो के जरिए कोऑर्डिनेट करता है

हर पीस को दूसरों के साथ कम्पोज होने के लिए डिजाइन किया गया है। [Jeremy Likness के ओरिजिनल पोस्ट](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) और [Agent Framework GitHub रेपो](https://github.com/microsoft/agent-framework/tree/main/dotnet) में पूरे सैंपल देखें।

## निष्कर्ष

Microsoft Agent Framework भाग 3 का पोस्ट बिल्डिंग ब्लॉक्स सीरीज का लूप बंद करता है। .NET डेवलपर्स के लिए जो AI एजेंट बनाना चाहते हैं — सिर्फ चैटबॉट नहीं, असली एजेंट जो टूल्स इस्तेमाल करें, चीजें याद रखें और कोऑर्डिनेट करें — यही आगे बढ़ने का रास्ता है।

स्टेबल 1.0 रिलीज का मतलब है कि आप प्रोडक्शन में इस पर बिल्ड कर सकते हैं। अगर आप .NET में एजेंट डेवलपमेंट में कूदने का इंतजार कर रहे थे, तो अभी सही समय है।
