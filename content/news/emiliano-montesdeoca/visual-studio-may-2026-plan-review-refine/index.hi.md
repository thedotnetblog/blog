---
title: "Visual Studio का मई अपडेट असल में idea और change के बीच बेहतर control के बारे में है"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "Visual Studio का मई अपडेट Plan agent, बेहतर skill management, context window visibility, और मज़बूत multi-file diff अनुभव जोड़ता है। साझा थीम AI-assisted inner loop पर बेहतर control है।"
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल लेख के लिए [यहाँ क्लिक करें]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}}).* 

Visual Studio के मई अपडेट में सबसे दिलचस्प बात कोई एक isolated feature नहीं है।

यह shared direction है।

यह release लगातार उस space को बेहतर कर रहा है जो बीच में है:

- एक idea
- एक plan
- एक generated change
- एक review
- एक refined result

यही AI-assisted development का वह हिस्सा है जो तय करता है कि workflow भरोसेमंद लगेगा या chaotic।

## Feature list अलग-अलग है, लेकिन intent एक जैसा है

कागज़ पर, इस release में कई चीज़ें हैं:

- नया Plan agent
- skill management सुधार
- context window visibility
- multi-file summary diff
- Copilot-related workflow cleanup
- C++ side पर MSVC updates

यह एक mixed bag जैसा लग सकता है।

मुझे नहीं लगता कि यह ऐसा है।

मुख्य धारा काफ़ी साफ़ है: **Visual Studio developers को AI-assisted work पर ज़्यादा control देना चाहता है, बिना उन्हें धीमा किए।**

यही सही tradeoff है जिसे pursue करना चाहिए।

## Plan agent इस release का philosophical center है

दूसरी features महत्वपूर्ण हों तब भी, मुझे अब भी लगता है कि Plan agent इस update का सबसे revealing हिस्सा है।

यह कुछ ऐसा साफ़ करता है जो coding agents इस्तेमाल करते समय हम में से बहुतों ने महसूस किया है:

जल्दी शुरू करना हमेशा प्रभावी ढंग से आगे बढ़ना नहीं होता।

यह release planning, review, और controlled implementation को एक ज़्यादा natural sequence बनाकर इस बात को और मज़बूत करता है।

यह healthy है।

## multi-file diff का काम quietly बड़ा improvement है

मुझे यह भी लगता है कि multi-file summary diff को शायद जितना credit मिलेगा, उससे ज़्यादा मिलना चाहिए।

जब agents एक साथ कई files बदलते हैं, तो review experience ही product बन जाता है।

अगर changes का review messy लगे, तो developers workflow पर कम भरोसा करते हैं।

अगर changes का review coherent लगे, तो developers tool का इस्तेमाल जारी रखने की ज़्यादा संभावना रखते हैं।

इसीलिए एक unified summary view बहुत मायने रखती है। यह generated work को हाँ या नहीं कहने की cognitive cost कम करती है।

## context window indicator जितना सुनाई देता है उससे स्मार्ट है

मुझे context usage indicator भी पसंद है।

यह छोटा detail लग सकता है, लेकिन यह एक असली AI workflow problem हल करता है: यह न जानना कि tool कब बातचीत के पहले हिस्से को भूलना शुरू करने वाला है।

इसे visible बनाना अच्छा design choice है।

यह model context को magically बढ़ा नहीं देता, लेकिन limit को observable बना देता है, और अक्सर यही अगला सबसे अच्छा विकल्प होता है।

## मेरी राय

यह update असल में developers को AI-assisted loop पर बेहतर visibility और control देने के बारे में है।

और novelty नहीं।
और chaos नहीं।
ज़्यादा control।

अगर लक्ष्य AI tooling को एक serious IDE workflow के अंदर ज़्यादा भरोसेमंद बनाना है, तो invest करने की सही जगह यही है।

मूल लेख: [Visual Studio का मई अपडेट — Plan, Review, Refine](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)