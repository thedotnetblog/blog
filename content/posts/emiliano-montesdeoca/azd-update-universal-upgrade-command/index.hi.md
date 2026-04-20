---
title: "azd update — सभी Package Managers को Manage करने के लिए एक Command"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI में अब एक universal update command है जो इस बात की परवाह किए बिना काम करता है कि आपने इसे कैसे install किया — winget, Homebrew, Chocolatey, या install script।"
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azd-update-universal-upgrade-command" >}}).*

वह "azd का नया version available है" message जो हर कुछ हफ्तों में आती है? वह जिसे आप dismiss कर देते हैं क्योंकि आपको याद नहीं कि आपने `azd` winget, Homebrew, या उस curl script से install किया था जो आपने छह महीने पहले चलाई थी? यह finally fix हो गया।

Microsoft ने [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) ship किया — एक single command जो Azure Developer CLI को latest version में update करता है, चाहे आपने इसे originally कैसे भी install किया हो।

## यह कैसे काम करता है

```bash
azd update
```

बस इतना। Early access के लिए:

```bash
azd update --channel daily
azd update --channel stable
```

Command आपका current installation method detect करता है और under the hood appropriate update mechanism use करता है।

## छोटी सी बात

`azd update` version 1.23.x से शुरू होकर ship होता है। अगर आप पुराने version पर हैं, तो आपको एक आखिरी manual update करनी होगी। इसके बाद, `azd update` सब कुछ संभाल लेता है।

## यह क्यों मायने रखता है

यह एक small quality-of-life improvement है, लेकिन जो लोग daily `azd` use करते हैं AI agents और Aspire apps deploy करने के लिए, current रहना मायने रखता है।

[पूरा announcement](https://devblogs.microsoft.com/azure-sdk/azd-update/) पढ़ें।
