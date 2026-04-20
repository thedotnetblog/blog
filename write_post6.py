content = """\
---
title: "azd update — आपके सभी Package Managers को एक Command से संभालें"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI में अब एक universal update command है जो काम करती है चाहे आपने इसे कैसे भी install किया हो — winget, Homebrew, Chocolatey, या install script।"
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azd-update-universal-upgrade-command" >}}).*

आपने वो "azd का नया version उपलब्ध है" message ज़रूर देखा होगा जो हर कुछ हफ्तों में pop up होता है? वो जिसे आप dismiss कर देते हैं क्योंकि आपको याद नहीं कि आपने `azd` winget से install किया था, Homebrew से, या उस curl script से जो आपने छह महीने पहले चलाई थी? हाँ, यह finally ठीक हो गया।

Microsoft ने [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) ship किया है — एक single command जो Azure Developer CLI को latest version में update करती है चाहे आपने इसे originally कैसे भी install किया हो। Windows, macOS, Linux — कोई फर्क नहीं। एक command।

## यह कैसे काम करता है

```bash
azd update
```

बस इतना ही। अगर आप नए features का early access चाहते हैं, तो आप daily insiders build पर switch कर सकते हैं:

```bash
azd update --channel daily
azd update --channel stable
```

Command आपकी current installation method detect करती है और under the hood appropriate update mechanism use करती है। अब "रुको, इस machine पर मैंने winget use किया था या choco?" नहीं।

## छोटी सी catch

`azd update` version 1.23.x से शुरू होकर ship होती है। अगर आप पुराने version पर हैं, तो आपको अपनी original installation method से एक आखिरी manual update करनी होगी। उसके बाद, `azd update` सब कुछ forward में handle करेगा।

`azd version` से अपना current version check करें। अगर आपको fresh install की ज़रूरत है, [install docs](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) में सब है।

## यह क्यों मायने रखता है

यह एक छोटा quality-of-life improvement है, लेकिन उन लोगों के लिए जो daily basis पर Azure पर AI agents और Aspire apps deploy करने के लिए `azd` use करते हैं, current रहने का मतलब है कम "यह bug तो latest version में already fix हो गया था" moments। एक कम चीज़ जिसके बारे में सोचना पड़े।

अधिक context के लिए [पूरी announcement](https://devblogs.microsoft.com/azure-sdk/azd-update/) और Jon Gallant का [deeper dive](https://blog.jongallant.com/2026/04/azd-update) पढ़ें।
"""

path = "/Users/emiliano/.copilot/copilot-worktrees/blog/emimontesdeoca-unwresting-colby/content/posts/emiliano-montesdeoca/azd-update-universal-upgrade-command/index.hi.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Post 6 done")
