---
title: "OpenEnv और Foundry बातचीत को स्थिर agents से आगे ले जा रहे हैं"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "OpenEnv और Foundry की नई कहानी reinforcement learning के buzzwords से कहीं आगे जाती है। असल में यह ऐसे agent systems की ओर धक्का है जिन्हें वास्तविक business outcomes के खिलाफ समय के साथ evaluate, optimize और improve किया जा सकता है."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल लेख के लिए [यहाँ क्लिक करें]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}}).* 

ज़्यादातर agent conversations अभी भी inference पर ही रुक जाती हैं।

क्या model prompt का जवाब दे सकता है? क्या वह tool call कर सकता है? क्या वह task एक बार पूरा कर सकता है?

नई **OpenEnv + Foundry** चर्चा दिलचस्प है क्योंकि यह बातचीत को एक अधिक महत्वाकांक्षी जगह ले जाने की कोशिश कर रही है: **आप ऐसा agent system कैसे बनाते हैं जो समय के साथ सचमुच बेहतर होता जाए?**

यह कहीं बेहतर सवाल है।

## मुख्य बदलाव responses से learning loops की ओर है

Foundry post समस्या को environments, evals, rubrics, optimization, और post-training के आसपास रखता है।

इसे एक ही वाक्य में समेटा जा सकता है:

**लक्ष्य अब सिर्फ agent को चलाना नहीं है, बल्कि ऐसा loop रखना है जो आपके वास्तविक outcomes के मुकाबले agent को मापे और बेहतर करे.**

यही वह हिस्सा है जिस पर मुझे लगता है कि developers को ध्यान देना चाहिए।

क्योंकि जब आप इसे इस तरह देखते हैं, तो स्थायी asset सिर्फ model या prompt नहीं रह जाता। उसके आसपास का system भी उतना ही महत्वपूर्ण हो जाता है:

- वह environment जहाँ वह काम करता है
- वह rubric जो उसे score करती है
- वे traces जो बताते हैं कि क्या हुआ
- वह optimizer जो configuration को बेहतर बनाता है

यह सोचने का कहीं अधिक enterprise-ready तरीका है।

## यह तब भी क्यों मायने रखता है जब आप RL research नहीं करते

सच कहें: OpenEnv, post-training, और world-modeling जैसे शब्द बहुत से developers को तुरंत disconnect कर सकते हैं।

लेकिन practical takeaway terminology से सरल है।

भले ही आप सीधे कभी training loop न छुएँ, यह work future agent development के लिए platform story को shape करता है:

- evaluations first-class बनती हैं
- optimization occasional के बजाय continuous बनती है
- environments reusable assets बनते हैं
- बेहतर agent behavior कुछ मापा जा सकने वाला बन जाता है, सिर्फ "demo में बेहतर लगता है" नहीं

यह आगे की ओर बड़ा कदम है।

## मेरी राय

इस announcement की सबसे समझदारी वाली बात कोई एक research detail नहीं है।

यह framing है।

Microsoft साफ़ तौर पर ecosystem को static prompt engineering से **outcome-driven agent systems** की ओर ले जाने की कोशिश कर रहा है। ऐसे systems जिन्हें evaluate, tune, govern, और धीरे-धीरे improve किया जा सकता है।

यही serious platform value है।

और अगर आप आज agents बना रहे हैं, application layer पर भी, तो यह देखना worth it है कि यह दिशा कहाँ जा रही है।

मूल लेख: [परिणाम-चालित learning systems: OpenEnv और Foundry के साथ Enterprise RL](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)