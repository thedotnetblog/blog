---
title: "Microsoft Agent Framework में स्थायी वर्कफ़्लो: In-Memory से Azure Functions तक"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAF का वर्कफ़्लो प्रोग्रामिंग मॉडल अब Durable Task द्वारा समर्थित स्थायी निष्पादन का समर्थन करता है — यहाँ बताया गया है कि कैसे ऐसे कम्पोज़ेबल एजेंट वर्कफ़्लो बनाएं जो प्रोसेस रिस्टार्ट से बचते हैं और Azure Functions पर स्केल होते हैं।"
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

शुरुआती AI एजेंट वर्कफ़्लो की समस्याओं में से एक: वे नाजुक होते हैं। एक प्रोसेस से बंधे लंबे समय तक चलने वाले मल्टी-स्टेप वर्कफ़्लो का मतलब है कि प्रोसेस रिस्टार्ट = राज्य खोना। सरल डेमो के लिए यह ठीक है। प्रोडक्शन वर्कलोड के लिए नहीं।

Microsoft Agent Framework का वर्कफ़्लो प्रोग्रामिंग मॉडल अब Azure Functions होस्टिंग के साथ Durable Task फ्रेमवर्क द्वारा समर्थित **स्थायी निष्पादन** का समर्थन करता है। यहाँ प्रोग्रामिंग मॉडल कैसे काम करता है और स्थायित्व क्यों महत्वपूर्ण है।

## मूल निर्माण खंड

**Executor** काम की मूल इकाई हैं। प्रत्येक टाइप्ड है — एक विशिष्ट इनपुट लेता है और एक विशिष्ट आउटपुट उत्पन्न करता है:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // ऑर्डर खोजें, वापस करें
        return new Order(Id: message.OrderId, ...);
    }
}
```

**वर्कफ़्लो** fluent builder का उपयोग करके executor को directed graphs में जोड़ते हैं। फ्रेमवर्क निष्पादन, चरणों के बीच डेटा प्रवाह और त्रुटि प्रसार संभालता है।

आप मॉडल कर सकते हैं:
- अनुक्रमिक श्रृंखलाएं (चरण A → चरण B → चरण C)
- समानांतर Fan-out/Fan-in (एजेंट A, B, C को समानांतर में चलाएं, परिणाम एकत्र करें)
- सशर्त शाखाएं
- Human-in-the-loop अनुमोदन (वर्कफ़्लो रोकें, बाहरी सिग्नल की प्रतीक्षा करें)

## स्थानीय विकास के लिए In-Memory Runner

शुरू करना त्वरित है:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

कोर पैकेज में एक हल्का in-process runner शामिल है। कोई बाहरी निर्भरता नहीं, कोई डेटाबेस नहीं, कोई Azure संसाधन नहीं। स्थानीय विकास और unit testing के लिए बेहतरीन।

## Durable Task के साथ स्थायित्व जोड़ना

जब एक वर्कफ़्लो को प्रोसेस रिस्टार्ट से बचना हो — क्योंकि यह लंबे समय तक चलता है, क्योंकि इसमें human-in-the-loop चरण हैं, क्योंकि यह कई समानांतर एजेंट कॉल पर वितरित है — in-memory runner पर्याप्त नहीं है।

MAF का Durable Task एकीकरण Azure Storage में वर्कफ़्लो स्थिति संग्रहीत करता है। अगर प्रोसेस रिस्टार्ट होती है, तो वर्कफ़्लो वहीं से फिर शुरू होता है जहाँ रुका था। प्रोग्रामिंग मॉडल वही रहता है; आप केवल runner बदलते हैं।

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

वही executor, वही वर्कफ़्लो ग्राफ — स्थायी स्थिति द्वारा समर्थित।

## Azure Functions होस्टिंग

तीसरी परत Azure Functions होस्टिंग है। आपका वर्कफ़्लो Function app बन जाता है: HTTP endpoint के माध्यम से वर्कफ़्लो ट्रिगर करें, और स्थायी runtime स्केलिंग, स्थिति और विश्वसनीयता संभालता है।

इसका मतलब है कि समानांतर कॉल, सशर्त शाखाओं और मानव अनुमोदन वाला multi-agent वर्कफ़्लो कस्टम स्थिति प्रबंधन के बिना serverless Functions वातावरण में स्केल कर सकता है।

## यह क्यों महत्वपूर्ण है

यह संयोजन वास्तविक AI सिस्टम के लिए महत्वपूर्ण है:

- **समानांतर एजेंट कॉल** — बिना ब्लॉकिंग के एक साथ कई विशेष एजेंटों में वितरित करें, सभी पूर्ण होने पर परिणाम एकत्र करें
- **लंबे समय तक चलने वाली प्रक्रियाएं** — मानव अनुमोदन या बाहरी घटनाओं वाले वर्कफ़्लो घंटों या दिनों में रुक और फिर शुरू हो सकते हैं
- **स्केलिंग** — Azure Functions क्षैतिज रूप से निष्पादन स्केल करता है; Durable Task फ्रेमवर्क समानांतर स्थिति समन्वय प्रबंधित करता है

अगर आप सरल स्थानीय डेमो से परे MAF वर्कफ़्लो बना रहे हैं, तो यही प्रोडक्शन-गुणवत्ता निष्पादन का रास्ता है।

मूल पोस्ट: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
