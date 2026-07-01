---
title: "Visual Studio में नया Plan agent एक बहुत वास्तविक AI workflow समस्या को हल करता है"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "Visual Studio का नया Plan agent इसलिए महत्वपूर्ण है क्योंकि यह implementation से पहले एक structured planning stage बनाता है, और यही अक्सर बड़े features और refactors को चाहिए होता है।"
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल लेख के लिए [यहाँ क्लिक करें]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

AI coding workflow में सबसे frustrating चीज़ों में से एक तब होती है जब implementation बहुत जल्दी शुरू हो जाती है।

कई बार code तकनीकी रूप से ठीक भी होता है, लेकिन वह समस्या के उस version को हल कर रहा होता है जो आपके मन में था ही नहीं।

आप refactor चाहते थे। उसने rewrite शुरू कर दी।
आप scoped improvement चाहते थे। उसने project का आधा हिस्सा छू लिया।
आप options पर बात करना चाहते थे। वह सीधे file changes पर चला गया।

इसीलिए Visual Studio में नया **Plan agent** एक बहुत उपयोगी addition है।

## यह एक असली workflow problem हल करता है, सिर्फ cosmetic problem नहीं

मूल पोस्ट एक बहुत familiar situation का वर्णन करती है: "**Code गलत नहीं है... बस वह नहीं है जो आप चाहते थे.**"

यह line बहुत बढ़िया है।

क्योंकि AI-assisted development की कमजोरी यह नहीं है कि model code बना सकता है या नहीं। असली सवाल यह है कि क्या workflow implementation शुरू होने से पहले काम के intended shape पर सहमत होने के लिए पर्याप्त space देता है।

यह खास तौर पर इन मामलों में मायने रखता है:

- बड़े features
- unfamiliar codebases
- non-trivial refactors
- architecture-sensitive changes
- ऐसा काम जिसे editing शुरू करने से पहले team review चाहिए

ऐसी स्थितियों में सीधे implementation में कूदना अक्सर गलत कदम होता है।

## जब task real हो, तब planning overhead नहीं होती

मुझे लगता है teams कभी-कभी यह कम आँकती हैं कि बहुत जल्दी implementation शुरू करने से वे कितना समय खो देती हैं।

अगर agent:

- गलत files छू ले
- गलत approach चुन ले
- कोई key constraint मिस कर दे
- कोई जरूरी edge case ignore कर दे

तो "fast" start अंततः धीमा workflow बन जाता है।

इसलिए मुझे यह feature पसंद है।

यह जगह बनाता है:

- स्पष्ट करने वाले सवालों के लिए
- प्लान का मसौदा तैयार करने के लिए
- प्लान को सीधे संपादित करने के लिए
- कोड में बदलाव शुरू होने से पहले प्लान साझा करने के लिए

यह bureaucracy नहीं है। अक्सर यह बस good engineering होती है।

## Markdown plan file एक smart choice है

एक detail जो मुझे खास तौर पर पसंद है, वह यह है कि हर plan `.copilot/plans/plan-{title}.md` में save होता है।

इससे planning step tangible बन जाता है।

यानी plan chat transcript के अंदर बंद नहीं रहता। वह ऐसी चीज़ बन जाता है जिसे आप:

- review कर सकते हैं
- edit कर सकते हैं
- mentally version कर सकते हैं
- teammates के साथ discuss कर सकते हैं
- implementation में अधिक deliberate तरीके से hand off कर सकते हैं

इससे feature temporary preamble से कहीं ज़्यादा serious लगता है।

## यहीं से AI workflows team process का सम्मान करना शुरू करते हैं

मुझे लगता है यह इस बात के सबसे strong संकेतों में से एक है कि ये tools mature हो रहे हैं।

सबसे अच्छे AI developer workflows वे नहीं होते जो हर intermediate step हटा दें। वे होते हैं जो सही intermediate steps को बेहतर करें।

और planning उन्हीं steps में से एक है।

अगर plan मजबूत है, तो implementation आसान हो जाती है।
अगर plan कमजोर है, तो implementation noisy हो जाती है।

यह feature इसे सीधे स्वीकार करता है।

## मेरी राय

यह सिर्फ AI nicety नहीं है।

यह workflow improvement है।

और real features और refactors के लिए, यह ठीक वही सुधार है जो unnecessary churn, review noise, और "यह मेरा मतलब नहीं था" वाले rework को बहुत कम कर सकता है।

मुझे लगता है आगे चलकर और भी agent experiences को ऐसी किसी चीज़ की ज़रूरत होगी।

Visual Studio वहाँ जल्दी पहुँच गया, और वह भी उपयोगी तरीके से।

मूल लेख: [बिल्ड करने से पहले plan करें: Visual Studio में Plan agent का परिचय](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)