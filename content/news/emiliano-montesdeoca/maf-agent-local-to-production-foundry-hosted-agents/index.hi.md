---
title: "आपके लोकल MAF एजेंट को प्रोडक्शन में घर मिल गया"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents आपके Microsoft Agent Framework एजेंट को पहचान, स्केलिंग, सत्र स्थायित्व और बिना अतिरिक्त सेटअप के ऑब्जर्वेबिलिटी देता है। यहाँ देखें यह व्यवहार में कैसा दिखता है।"
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

एजेंट को लोकल में काम करवाना मज़ेदार हिस्सा है। मुश्किल हिस्सा उसके बाद का सब कुछ है: बिना दिमाग खोए उसे डिप्लॉय करना, सेशन मैनेज करना, आइडेंटिटी सेटअप करना, ऑब्जर्वेबिलिटी जोड़ना। आमतौर पर इसका मतलब होता है बहुत सारा कस्टम इंफ्रास्ट्रक्चर।

Foundry Hosted Agents ने Microsoft Agent Framework (MAF) यूज़र्स के लिए उस अधिकांश इंफ्रास्ट्रक्चर को हटा दिया है।

## Foundry Hosted Agents वास्तव में क्या करता है

जब आप एक MAF एजेंट को Foundry Hosted Agents में डिप्लॉय करते हैं, तो प्लेटफ़ॉर्म उन चीजों की एक आश्चर्यजनक लंबी सूची संभालता है जो आपको अन्यथा खुद बनानी होतीं:

- **शून्य तक स्केल** — आपका एजेंट आइडल होने पर कुछ भी खर्च नहीं करता और अपने आप वापस चालू हो जाता है
- **प्रति-सेशन VM-आइसोलेटेड सैंडबॉक्स** — हर यूज़र सेशन को अपना सैंडबॉक्स मिलता है जिसमें फाइलसिस्टम पर्सिस्टेंस है जो स्केल-डाउन इवेंट्स से बचती है
- **बिल्ट-इन Entra ID** — हर एजेंट को अपनी आइडेंटिटी मिलती है ताकि वह इमेज में सीक्रेट डाले बिना Foundry मॉडल्स, Toolbox और Azure सर्विसेज को कॉल कर सके
- **वर्शन्ड डिप्लॉयमेंट** — हर डिप्लॉयमेंट एक अपरिवर्तनीय स्नैपशॉट है, जिसमें blue/green और कैनरी रोलआउट सपोर्ट है
- **ज़ीरो-कॉन्फिग ऑब्जर्वेबिलिटी** — `APPLICATIONINSIGHTS_CONNECTION_STRING` रनटाइम पर इंजेक्ट होती है ताकि MAF के OpenTelemetry ट्रेस App Insights में अपने आप आ जाएं

आखिरी वाला वाकई अच्छा है। कोई अतिरिक्त वायरिंग नहीं, कोई अतिरिक्त कॉन्फिग नहीं। ट्रेस बस दिखने लगते हैं।

## कोड का अंतर बहुत कम है

इस इंटीग्रेशन में मुझे यही सबसे ज़्यादा पसंद है। आपको अपना एजेंट फिर से नहीं लिखना। बस उसे रैप करना है:

**.NET में:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Python में:**

```python
server = ResponsesHostServer(agent)
server.run()
```

बस इतना। वही लॉजिक जो आपने लोकल में टेस्ट किया वही प्रोडक्शन में चलता है। प्लेटफ़ॉर्म इसे सेशन मैनेजमेंट, आइडेंटिटी और स्केलिंग इंफ्रास्ट्रक्चर में रैप करता है।

## दो प्रोटोकॉल, एक एजेंट

Hosted Agents दो एंडपॉइंट स्टाइल सपोर्ट करता है:

- **Responses** (`/responses`) — OpenAI-कम्पेटिबल, कनवर्सेशन हिस्ट्री और स्ट्रीमिंग मैनेज करता है। चैट-शेप्ड एजेंट्स के लिए अच्छा डिफ़ॉल्ट।
- **Invocations** (`/invocations`) — आप रिक्वेस्ट/रिस्पांस स्कीमा डिफाइन करते हैं। नॉन-कनवर्सेशनल वर्कफ्लो के लिए अच्छा।

अगर आप कुछ ऐसा बना रहे हैं जो बातचीत जैसा लगे, Responses से शुरू करें। अगर आप API-शेप्ड एजेंट बना रहे हैं जो स्ट्रक्चर्ड इनपुट लेता है और स्ट्रक्चर्ड आउटपुट देता है, तो Invocations लचीलापन देता है।

## `azd` के साथ डिप्लॉयमेंट फ्लो

जब आप MAF एजेंट के साथ `azd up` चलाते हैं:

1. ऑप्शनल रूप से Foundry प्रोजेक्ट बनाता है और मॉडल डिप्लॉय करता है
2. आपके कोड को पैकेज करता है और Azure Container Registry में इमेज पुश करता है
3. ACR इमेज से कंप्यूट प्रोविज़न करता है
4. एजेंट को एक डेडिकेटेड Entra ID असाइन करता है
5. एक स्टेबल एंडपॉइंट एक्सपोज़ करता है (`https://{project_endpoint}/agents/{agent_name}`)
6. उस पॉइंट से आगे सब कुछ हैंडल करता है

सेशन 30 दिनों तक बनी रहती हैं। आइडल कंप्यूट 15 मिनट बाद डिप्रोविज़न हो जाता है और अगले रिक्वेस्ट पर पारदर्शी रूप से रिस्टोर हो जाता है। एजेंट के नज़रिए से, कुछ भी नहीं बदला।

## निष्कर्ष

AI एजेंट्स के लिए "लोकल में काम कर रहा है" और "प्रोडक्शन में चल रहा है" के बीच की दूरी ऐतिहासिक रूप से लंबी और तकलीफदेह रही है। Foundry Hosted Agents + MAF उस खाई को काफी हद तक पाटता है। अगर आपके पास Agent Framework से बना लोकल एजेंट है, तो आज इसे आज़माने लायक है।

टीम का कहना है कि GA जल्द आने वाला है — यह अभी प्रीव्यू में है। शुरुआत के लिए [MAF Hosted Agent इंटीग्रेशन डॉक्स](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) और [.NET सैम्पल्स](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) देखें।

ओरिजिनल आर्टिकल: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
