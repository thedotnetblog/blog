---
title: "Intelligent Terminal 0.1 एआई-नेटिव shell अनुभव का एक गंभीर पहला प्रयास है"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Intelligent Terminal 0.1 एक native agent pane, error-aware सहायता, background tasks, और command palette से शुरू होने वाले agent flows जोड़ता है। यह अभी भी प्रयोगात्मक है, लेकिन दिशा बहुत आकर्षक है।"
tags:
  - Terminal
  - AI
  - GitHub Copilot
  - Developer Tools
  - Windows Terminal
---

> *इस लेख का स्वचालित रूप से अनुवाद किया गया है। मूल संस्करण के लिए, [यहां क्लिक करें]({{< ref "index.md" >}}).* 

मुझे अब भी लगता है कि terminal उन सबसे स्वाभाविक जगहों में से एक है जहाँ AI-सहायित विकास वास्तव में उपयोगी बन सकता है।

इसीलिए **Intelligent Terminal 0.1** एक साधारण point release से कहीं अधिक गंभीर घोषणा जैसा लगा।

दिलचस्प हिस्सा सिर्फ़ "terminal में chat" नहीं है। यह native integration है:

- एक agent pane
- error detection
- session management
- background tasks
- command palette से शुरू होने वाली agent actions

यह अब एक असली shell अनुभव जैसा लगने लगता है, न कि साइड में जोड़ा गया एक add-on।

## मूल लेख असली दर्द-बिंदु को समझता है

मूल पोस्ट के सबसे अच्छे हिस्सों में से एक यह है कि वह abstract AI ambition से शुरू नहीं होता।

यह एक बहुत सामान्य developer experience से शुरू होता है:

> "**क्या आपने कभी PowerShell command डाला, error मिला, उसे copy किया, browser खोला, paste किया, और फिर उसे ठीक करने के लिए कई forum posts के बीच भटके?**"

यह सवाल इसलिए काम करता है क्योंकि यह दर्दनाक रूप से परिचित है।

Terminal ऐसी छोटी-छोटी interruptions से भरा हुआ है।

तो अगर AI को कहीं होना चाहिए, तो वह इन interruptions के पास ही होना चाहिए।

## यह ज़्यादातर terminal AI demos से क्यों ज़्यादा मजबूत लगता है

इसे interesting बनाने वाली बात सिर्फ़ agent की मौजूदगी नहीं है।

बल्कि यह कि terminal experience को इस तरह से फिर से सोचा जा रहा है कि developers वास्तव में कैसे काम करते हैं:

- एक persistent agent surface
- shell output से context
- error आने पर तुरंत मदद
- background task spawning
- session resumption
- entry point के रूप में command palette

यह floating chatbot वाले shell window से कहीं ज़्यादा usable workflow जैसा है।

## Agent pane यहाँ असली product है

अगर मुझे design का सबसे महत्वपूर्ण हिस्सा चुनना हो, तो शायद वह agent pane होगा।

क्यों? क्योंकि यह दो awkward modes के बीच एक middle ground बनाता है:

- terminal को पूरी तरह छोड़ देना
- या सारी interaction को inline shell text में ठूंस देना

यह एक अच्छी design choice है।

यह terminal को working surface के रूप में सम्मान देती है, और साथ ही agent को autocomplete से ज़्यादा बनने के लिए पर्याप्त जगह भी देती है।

## Error detection वह जगह है जहाँ value साफ दिखने लगती है

Automatic error detection भी ठीक वही feature है जो यहाँ समझ में आता है।

Terminal के पास पहले से context है।
Error पहले ही हो चुका है।
और developer अभी भी flow में है।

इससे shell इन चीज़ों के लिए एक बेहतरीन जगह बन जाता है:

- तुरंत diagnosis
- fix suggestions
- तेज़ iteration
- current environment छोड़े बिना follow-up reasoning

यह magic नहीं है। यह बस workflow को सही जगह पर रखना है।

## मेरी राय

यह अभी शुरुआती दौर में है, लेकिन मैंने terminal AI के लिए जितनी भी directions देखी हैं, उनमें यह सबसे convincing में से एक है।

इसलिए नहीं कि यह जादू का वादा करता है।
बल्कि इसलिए कि यह उसी तरह के करीब रहता है जैसे developers पहले से shell के भीतर काम करते हैं।

और अगर यह इसी दिशा में आगे बढ़ता रहा, तो मुझे लगता है कि यह Microsoft toolchain portfolio में सबसे दिलचस्प AI-native developer experiences में से एक बन सकता है।

मूल पोस्ट: [Announcing Intelligent Terminal 0.1](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/)
