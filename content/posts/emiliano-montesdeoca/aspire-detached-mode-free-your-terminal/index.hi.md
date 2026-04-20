---
title: "Terminal की देखभाल बंद करें: Aspire का Detached Mode Workflow बदल देता है"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 आपको AppHost को background में चलाने और अपना terminal वापस लेने देता है। नए CLI commands और agent support के साथ मिलाकर, यह उतना बड़ा deal है जितना सुनने में लगता है।"
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

हर बार जब आप Aspire AppHost चलाते हैं, तो आपका terminal चला जाता है। बंद। कब्ज़ा हो जाता है जब तक आप Ctrl+C से बाहर नहीं निकलते। एक quick command चलानी है? दूसरा tab खोलिए। Logs चेक करने हैं? एक और tab। यह एक छोटी सी रुकावट है जो जल्दी बड़ी हो जाती है।

Aspire 13.2 इसे ठीक करता है। James Newton-King ने [पूरी जानकारी लिखी है](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), और सच कहूँ तो, यह उन features में से एक है जो तुरंत आपके काम करने का तरीका बदल देती है।

## Detached mode: एक command, terminal वापस

```bash
aspire start
```

यह `aspire run --detach` का shorthand है। आपका AppHost background में boot होता है और आपको तुरंत terminal वापस मिल जाता है। कोई extra tab नहीं। कोई terminal multiplexer नहीं। बस आपका prompt, काम के लिए तैयार।

## जो चल रहा है उसे manage करना

यहाँ बात यह है — background में चलाना तभी उपयोगी है जब आप वाकई manage कर सकें कि क्या चल रहा है। Aspire 13.2 इसके लिए CLI commands का पूरा सेट लेकर आता है:

```bash
# सभी running AppHosts की list
aspire ps

# किसी specific AppHost की state देखें
aspire describe

# किसी running AppHost के logs stream करें
aspire logs

# किसी specific AppHost को रोकें
aspire stop
```

इससे Aspire CLI एक proper process manager बन जाता है। आप कई AppHosts शुरू कर सकते हैं, उनकी status चेक कर सकते हैं, उनके logs tail कर सकते हैं, और उन्हें बंद कर सकते हैं — सब एक ही terminal session से।

## Isolated mode के साथ मिलाएं

Detached mode naturally isolated mode के साथ काम करता है। क्या आप बिना port conflicts के background में एक ही project के दो instances चलाना चाहते हैं?

```bash
aspire start --isolated
aspire start --isolated
```

हर एक को random ports, अलग secrets, और अपना lifecycle मिलता है। दोनों देखने के लिए `aspire ps` का उपयोग करें, जिसे बंद करना हो उसके लिए `aspire stop` का।

## Coding agents के लिए यह क्यों बड़ी बात है

यहीं चीज़ें वाकई दिलचस्प हो जाती हैं। आपके terminal में काम करने वाला एक coding agent अब यह कर सकता है:

1. `aspire start` से app शुरू करें
2. `aspire describe` से उसकी state query करें
3. समस्याएं diagnose करने के लिए `aspire logs` से logs चेक करें
4. काम हो जाने पर `aspire stop` से बंद करें

बिना terminal session खोए। Detached mode से पहले, एक agent जो आपका AppHost चलाता वह अपने ही terminal से lock out हो जाता। अब वह शुरू कर सकता है, observe कर सकता है, iterate कर सकता है, और cleanup कर सकता है — बिल्कुल वैसे जैसा आप एक autonomous agent से चाहते हैं।

Aspire team ने इसी पर ध्यान दिया। `aspire agent init` चलाने से एक Aspire skill file setup होती है जो agents को ये commands सिखाती है। तो Copilot का coding agent जैसे tools out of the box ही आपके Aspire workloads manage कर सकते हैं।

## निष्कर्ष

Detached mode एक simple flag के रूप में छुपा हुआ workflow upgrade है। आप terminals के बीच context-switch करना बंद कर देते हैं, agents खुद को block करना बंद कर देते हैं, और नए CLI commands आपको यह देखने की असली visibility देते हैं कि क्या चल रहा है। यह practical है, यह clean है, और यह daily development loop को ध्यान देने योग्य रूप से smooth बनाता है।

सभी details के लिए [पूरा पोस्ट](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) पढ़ें और `aspire update --self` से Aspire 13.2 प्राप्त करें।
