---
title: "Visual Studio की वो Floating Windows सेटिंग जो आप नहीं जानते थे (लेकिन जाननी चाहिए)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Visual Studio की एक छुपी सेटिंग आपको floating windows पर पूरा नियंत्रण देती है — independent taskbar entries, सही multi-monitor behavior, और FancyZones के साथ बेहतरीन integration। एक dropdown सब कुछ बदल देता है।"
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "visual-studio-floating-windows-powertoys" >}}).*

अगर आप Visual Studio के साथ multiple monitors इस्तेमाल करते हैं (और सच कहें तो आजकल कौन नहीं करता), तो आपने यह परेशानी जरूर झेली होगी: floating tool windows मुख्य IDE minimize करते ही गायब हो जाती हैं, वे हमेशा बाकी सब चीज़ों के ऊपर रहती हैं, और taskbar में अलग बटन के रूप में नहीं दिखतीं। कुछ workflows के लिए यह ठीक है, लेकिन multi-monitor setups के लिए यह बहुत frustrating है।

Visual Studio टीम के Mads Kristensen ने [एक कम-जानी-मानी सेटिंग share की](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) जो floating windows के व्यवहार को पूरी तरह बदल देती है। बस एक dropdown। बस।

## सेटिंग कहाँ है

**Tools > Options > Environment > Windows > Floating Windows**

"These floating windows are owned by the main window" dropdown में तीन विकल्प हैं:

- **None** — पूरी स्वतंत्रता। हर floating window को अपना taskbar entry मिलता है और यह एक सामान्य Windows window की तरह व्यवहार करती है।
- **Tool Windows** (default) — documents स्वतंत्र रूप से float होते हैं, tool windows IDE से जुड़ी रहती हैं।
- **Documents and Tool Windows** — Visual Studio का classic व्यवहार, सब कुछ main window से बंधा रहता है।

## Multi-monitor setups के लिए "None" ही सही विकल्प है

इसे **None** पर सेट करें और अचानक आपकी सभी floating tool windows और documents असली Windows applications की तरह व्यवहार करने लगती हैं। वे taskbar में दिखती हैं, main Visual Studio window minimize करने पर भी visible रहती हैं, और खुद को बाकी सब चीज़ों के आगे नहीं रखतीं।

इसे **PowerToys FancyZones** के साथ combine करें और यह game changer साबित होता है। अपने monitors पर custom layouts बनाएं, Solution Explorer को एक zone में snap करें, debugger को दूसरे में, और code files जहाँ चाहें। सब कुछ अपनी जगह रहता है, सब कुछ independently accessible है, और आपका workspace अव्यवस्थित की बजाय organised लगता है।

## त्वरित सुझाव

- **Multi-monitor power users**: **None** सेट करें, FancyZones के साथ जोड़ें
- **कभी-कभार float करने वाले**: **Tool Windows** (default) एक अच्छा middle ground है
- **पारंपरिक workflow**: **Documents and Tool Windows** सब कुछ classic रखता है

Pro tip: किसी भी tool window title bar पर **Ctrl + double-click** करके तुरंत float या dock करें। सेटिंग बदलने के बाद restart की जरूरत नहीं।

## अंतिम बात

यह उन सेटिंग्स में से एक है जिनके बारे में सोचकर आप कहते हैं "मुझे यह पहले क्यों नहीं पता था"। अगर Visual Studio में floating windows ने कभी आपको परेशान किया है, तो अभी जाकर यह बदलें।

विवरण और screenshots के लिए [पूरी पोस्ट](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) पढ़ें।
