---
title: ".NET के Composable Stack के साथ AI-Powered Conference App बनाना"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft ने ConferencePulse बनाया — एक लाइव कॉन्फ्रेंस Blazor ऐप — Microsoft.Extensions.AI, DataIngestion, VectorData, MCP और Agent Framework को मिलाकर। यहाँ बताया गया है कि टुकड़े कैसे फिट होते हैं।"
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[.NET के Composable Stack के साथ AI-Powered Conference App बनाना](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft ने ConferencePulse बनाया, एक Blazor Server ऐप लाइव कॉन्फ्रेंस सत्रों के लिए, पाँच .NET एक्सटेंशन लाइब्रेरी को मिलाकर। इसे MVP Summit में उपयोग किया गया।

## ConferencePulse क्या करता है

ConferencePulse लाइव सत्रों के दौरान चलता है और प्रदान करता है: सत्र सामग्री से AI-जनित पोल, एक लाइव नॉलेज बेस से RAG पाइपलाइन के साथ दर्शक Q&A, ऑटो-जनित अंतर्दृष्टि, और कई समवर्ती AI एजेंटों द्वारा उत्पादित सत्र सारांश। स्टैक .NET 10, Blazor Server, Aspire है, जो पाँच प्रोजेक्ट्स में विभाजित है: Web, Core, Ingestion, Agents, Mcp और AppHost।

## Microsoft.Extensions.AI: सब कुछ के लिए एक abstraction

`IChatClient` एकीकृत abstraction है — इसे एक बार सेट करें और वही इंटरफ़ेस Azure OpenAI, OpenAI, Anthropic या किसी भी अन्य प्रोवाइडर के लिए काम करता है। फ़ंक्शन invocation, OpenTelemetry ट्रेसिंग और लॉगिंग मिडलवेयर के साथ पूरी तरह से कॉन्फ़िगर किए गए क्लाइंट के लिए छह लाइनें:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

वही `IChatClient` बाद में डेटा इंजेस्शन enrichment चरण के लिए पुन: उपयोग किया जाता है — इसके लिए कोई अलग क्लाइंट नहीं।

## DataIngestion पाइपलाइन

सत्र सामग्री एक पाइपलाइन से बहती है: `MarkdownReader` → `HeaderChunker` (500 टोकन, 50 टोकन ओवरलैप) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant)। एनरिचर्स इंडेक्सिंग से पहले सारांश उत्पन्न करने और कीवर्ड निकालने के लिए उसी `IChatClient` का उपयोग करते हैं। दर्शकों के प्रश्न, Q&A जोड़े और पोल परिणाम वास्तविक समय में सत्र के आगे बढ़ने पर इंजेस्ट किए जाते हैं — नॉलेज बेस बात के दौरान बढ़ता है।

## VectorData: प्रोवाइडर-अज्ञेयवादी खोज

`VectorStoreCollection.SearchAsync()` उसी तरह काम करता है चाहे बैकिंग स्टोर Qdrant हो या Azure AI Search। हाइब्रिड खोज (वेक्टर + फुल-टेक्स्ट) समर्थित है। दर्शक Q&A के लिए RAG पाइपलाइन इस कलेक्शन को क्वेरी करती है और चैट क्लाइंट को संदर्भ के रूप में पास करने के लिए प्रासंगिक चंक्स वापस प्राप्त करती है।

## MCP: टूल्स के रूप में सत्र सामग्री

सत्र सामग्री MCP के माध्यम से उजागर की जाती है ताकि कोई भी MCP-संगत क्लाइंट इसे एक्सेस कर सके। सर्वर और क्लाइंट दोनों लागू हैं — सर्वर सत्र ज्ञान को MCP टूल्स के रूप में उजागर करता है, और क्लाइंट एजेंट पाइपलाइन के भीतर उन टूल्स को कॉल करने की अनुमति देता है।

## Agent Framework: समानांतर मल्टी-एजेंट सारांश

सत्र सारांश तीन एजेंटों द्वारा समवर्ती रूप से उत्पन्न किया जाता है — `PollSummaryAgent`, `QuestionSummaryAgent` और `InsightSummaryAgent` — फिर मर्ज किया जाता है। यह Microsoft Agent Framework से ग्रुप चैट या समानांतर निष्पादन पैटर्न का उपयोग करता है। प्रत्येक एजेंट एक चिंता संभालता है; ऑर्केस्ट्रेटर आउटपुट को मर्ज करता है।

## डिज़ाइन सिद्धांत

पोस्ट एक बात कहती है जो याद रखने योग्य है: सबसे सरल टूल का उपयोग करें जो फिट हो। सरल जनरेशन कार्यों के लिए प्रत्यक्ष `IChatClient` कॉल। संरचित डेटा निष्कर्षण के लिए टूल/फ़ंक्शन कॉलिंग। पूर्ण एजेंट केवल तब जब आपको स्वायत्त मल्टी-स्टेप रीजनिंग की आवश्यकता हो। लाइब्रेरी लेयरिंग इसे enforce करती है — आप पूर्ण Agent Framework को शामिल किए बिना `Microsoft.Extensions.AI` उठा सकते हैं।

पूर्ण प्रोजेक्ट संरचना और स्रोत लिंक के लिए [पूर्ण पोस्ट](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) देखें।
