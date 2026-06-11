---
title: "Agent Harness, Hosted Agents और CodeAct: Agent Framework का यही अपडेट है जिस पर मैं ध्यान दूँगा"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Build 2026 में Agent Framework की घोषणा बहुत भरी हुई है, लेकिन सबसे अहम बातें हैं harness मॉडल, Foundry hosted agents, और orchestration overhead कम करने वाला CodeAct."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Agent Framework की Build घोषणा बहुत कुछ कवर करती है, लेकिन तीन थीम तुरंत अलग दिखती हैं:

- **harness का runtime कहानी में एक अधिक first-class हिस्सा बनना**
- **Foundry hosted agents का production path देना**
- **CodeAct का multi-step orchestration overhead कम करना**

यही वे हिस्से हैं जिन पर मैं नज़र रखूँगा।

## harness असल में केंद्र में आ रहा है

स्रोत पोस्ट harness को उस परत के रूप में वर्णित करती है जहाँ मॉडल की reasoning और वास्तविक execution मिलती है।

यह सही वर्णन है, और यही कारण है कि मुझे लगता है यह हिस्सा कई अलग-अलग फीचर बुलेट्स से ज़्यादा महत्वपूर्ण है।

जिस क्षण किसी agent को चाहिए:

- file access
- shell execution
- planning modes
- to-dos
- session memory
- approval workflows

आप अब केवल prompt और model की बात नहीं कर रहे होते।

आप runtime व्यवहार की बात कर रहे होते हैं।

यही वह जगह है जहाँ frameworks या तो सच में उपयोगी बनते हैं या खिलौने बनकर रह जाते हैं।

और Microsoft Agent Framework साफ तौर पर उसी layer में ज़्यादा उपयोगी बनने की कोशिश कर रहा है।

## Hosted agents वही जगह हैं जहाँ local-to-production कहानी सच में महत्वपूर्ण बनती है

मुझे यह भी लगता है कि hosted agents वाला हिस्सा इस घोषणा का सबसे रणनीतिक रूप से महत्वपूर्ण भागों में से एक है।

स्रोत पोस्ट साफ़ तौर पर कहती है कि यह उस agent को production home देने का सबसे आसान तरीका है।

यह वाक्य महत्वपूर्ण है क्योंकि ज़्यादातर agent frameworks अभी भी local experimentation में deployment से कहीं मजबूत हैं।

अगर Foundry hosted agents local development से आगे इन चीज़ों तक जाना बहुत आसान बना दें:

- scaling
- observability
- managed identity
- session handling
- versioning

तो यह current agent ecosystem की सबसे बड़ी खाइयों में से एक को भर देता है।

यह एक सार्थक सुधार होगा।

## CodeAct इस अपडेट का सबसे रोमांचक तकनीकी विचार है

अगर मुझे पोस्ट में सबसे दिलचस्प technical concept चुनना हो, तो मैं शायद CodeAct चुनूँगा।

यह जिस समस्या को हल करना चाहता है, वह बहुत वास्तविक है: बहुत सारे multi-step agent workflows महंगे हो जाते हैं, क्योंकि orchestration loop खुद ही बहुत सारे model turns खा जाता है।

इसलिए जब source post में ऐसा परिणाम दिखता है:

- 52.4% faster
- 63.9% fewer tokens

तो मेरा ध्यान तुरंत खिंच जाता है।

बेशक, ये representative workload पर आधारित benchmark numbers हैं, कोई सार्वभौमिक नियम नहीं। लेकिन बड़ा विचार फिर भी काफ़ी compelling है।

अगर model tool-calling chain को ज़्यादा efficient execution shape में समेट सके, तो agent systems की economics काफ़ी बदल सकती है।

## इस अपडेट से developers को असल में क्या सीखना चाहिए

महत्वपूर्ण सबक यह नहीं है कि कितनी features ship हुईं।

सबक यह है कि framework उन जगहों पर मज़बूत हो रहा है जहाँ real applications को सबसे ज़्यादा ज़रूरत है:

- runtime shell
- deployment path
- execution efficiency
- built-in operational patterns

यह उस तरह की maturity signal है जिस पर मैं दूसरी superficial AI feature checklist से कहीं ज़्यादा ध्यान देता हूँ।

## मेरा निष्कर्ष

यह अपडेट इसलिए मायने रखता है क्योंकि यह सिर्फ surface area नहीं बढ़ा रहा।

यह agents के आसपास runtime और deployment की कहानी को उन तरीकों से मजबूत कर रहा है जो real applications के लिए मायने रखते हैं, खासकर उन teams के लिए जो local experiments से ऐसे systems तक जाना चाहती हैं जिन्हें वे सच में run और maintain कर सकें।

यही वह जगह है जहाँ framework ज़्यादा compelling बनता है।

और अगर मैं इस release को closely follow कर रहा होता, तो harness, hosted agents, और CodeAct वही तीन चीज़ें होतीं जिन पर मैं सबसे ज़्यादा ध्यान देता।

मूल पोस्ट: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
