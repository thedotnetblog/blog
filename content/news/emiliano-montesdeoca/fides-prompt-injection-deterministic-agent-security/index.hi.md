---
title: "FIDES वह तरह की नियतात्मक एजेंट-सुरक्षा कहानी है जिसे मैं और देखना चाहता हूँ"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Agent Framework में FIDES की नई क्षमताएँ इसलिए मायने रखती हैं क्योंकि वे prompt injection defense को heuristics से हटाकर labeled content और middleware checks पर आधारित लागू की जा सकने वाली नीति की ओर ले जाती हैं।"
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *यह लेख स्वचालित रूप से अनुवादित किया गया है। मूल संस्करण के लिए, [यहां क्लिक करें]({{< ref "index.md" >}}).*

prompt injection के खिलाफ रक्षा अक्सर अस्थिर जमीन पर खड़ी लगती है।

आप एक मजबूत system prompt जोड़ते हैं। आप एक फ़िल्टर जोड़ते हैं। आप कुछ allowlists जोड़ते हैं। और आशा करते हैं कि अगला अजीब input आपकी धारणाओं को नहीं तोड़ेगा।

इसी वजह से **FIDES** दिलचस्प है।

कहानी का मजबूत हिस्सा यह है कि यह सुरक्षा को अधिक deterministic चीज़ की ओर ले जाता है:

- content पर labels
- workflow के दौरान labels का propagation
- privileged tools के चलने से पहले middleware द्वारा enforcement
- untrusted context किस चीज़ को प्रभावित कर सकता है, इसके लिए स्पष्ट policy boundaries

## स्रोत लेख सही तरीके से सीधे बोलता है

यह इस पंक्ति से शुरू होता है कि prompt injection "**OWASP LLM Top 10 का नंबर 1 risk**" है।

अच्छा।

मुझे यहाँ इस तरह की स्पष्टता पसंद है, क्योंकि बहुत-सी टीमें अभी भी agent security को एक भविष्य की चिंता की तरह देखती हैं, न कि एक वर्तमान runtime design समस्या की तरह।

और लेख इसके बाद एक मजबूत practical contrast देता है: अधिकांश मौजूदा defenses heuristic हैं, जबकि FIDES सिस्टम को policy और enforcement की ओर ले जाने की कोशिश कर रहा है।

यही सही बदलाव है।

## यह किसी और security whitepaper से अधिक convincing क्यों है

AI security पर बहुत-सी writing abstract ही रहती है।

यह लेख कुछ बेहतर करता है। यह एक बहुत concrete example से गुजरता है: एक GitHub issue triage agent, एक malicious issue body, एक privileged file read, और public comment leak का प्रयास।

यह उपयोगी है क्योंकि यह पूरे discussion को एक actual workflow में anchor कर देता है।

और जब आप वह scenario देखते हैं, तो deterministic controls का मूल्य समझना बहुत आसान हो जाता है।

## मुख्य विचार "model को और smart बनाओ" नहीं है

सबसे महत्वपूर्ण बात यह है कि FIDES model से यह नहीं कह रहा कि वह जादुई रूप से attacks पहचानने में बेहतर हो जाए।

यह runtime contract बदल रहा है।

इसका मतलब:

- content को labels दिए जाते हैं
- labels आगे propagate होते हैं
- tools बताते हैं कि वे क्या accept करते हैं
- middleware execution से पहले unsafe paths को रोक देता है

यह कहीं बेहतर approach है।

क्योंकि जैसे ही agent वास्तविक परिणामों वाली tools call कर सकता है, सुरक्षा सिर्फ इस पर निर्भर नहीं रह सकती कि model का दिन अच्छा था या नहीं।

## मेरी राय

यही वह दिशा है जो मैं agent security में और अधिक देखना चाहता हूँ।

न कि "model पर भरोसा करो कि वह बुरी instructions ignore कर देगा", बल्कि "policy fence को runtime के अंदर बनाओ"।

यह कहीं अधिक स्वस्थ मॉडल है।

और अगर agent frameworks को production में गंभीरता से लिया जाना है, तो उन्हें ऐसी और कहानियों की ज़रूरत होगी।

मूल लेख: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)