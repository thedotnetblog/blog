---
title: "Terminal को बंधक बनाना बंद करें: Aspire का Detached Mode Workflow बदल देता है"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 आपको AppHost को background में चलाने और terminal वापस लेने देता है। नए CLI commands और agent support के साथ मिलाकर, यह उससे कहीं ज़्यादा बड़ी बात है जितनी लगती है।"
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

हर बार जब आप Aspire AppHost चलाते हैं, तो आपका terminal चला जाता है। Lock हो जाता है। Ctrl+C तक occupied रहता है। Quick command चलाना है? नया tab खोलें। Logs check करनी हैं? और एक tab। यह छोटा सा friction जल्दी ही बड़ा बन जाता है।

Aspire 13.2 इसे fix करता है। James Newton-King ने [पूरी details लिखी हैं](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), और honestly, यह उन features में से एक है जो immediately आपके काम करने का तरीका बदल देता है।

## Detached mode: एक command, terminal वापस

```bash
aspire start
```

यह `aspire run --detach` का shorthand है। आपका AppHost background में boot होता है और आपको terminal immediately वापस मिल जाता है।

## Running चीज़ों को manage करना

Background में चलाना तभी useful है जब आप actually manage कर सकें। Aspire 13.2 इसके लिए CLI commands का पूरा set लाता है:

```bash
# सभी running AppHosts list करें
aspire ps

# किसी specific AppHost की state inspect करें
aspire describe

# Running AppHost से logs stream करें
aspire logs

# किसी specific AppHost को stop करें
aspire stop
```

## Isolated mode के साथ combine करें

Detached mode naturally isolated mode के साथ pair करता है:

```bash
aspire start --isolated
aspire start --isolated
```

हर instance को random ports, separate secrets, और अपना lifecycle मिलता है।

## Coding agents के लिए यह क्यों बड़ा है

Terminal में काम करने वाला coding agent अब:

1. `aspire start` से app शुरू करें
2. `aspire describe` से state query करें
3. `aspire logs` से issues diagnose करें
4. `aspire stop` से काम होने पर बंद करें

`aspire agent init` चलाना agents को ये commands सिखाने के लिए Aspire skill file setup करता है।

## समापन

Detached mode एक simple flag के रूप में disguised workflow upgrade है। [पूरी post](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) पढ़ें और `aspire update --self` से Aspire 13.2 लें।
