content = """\
---
title: "Aspire का Isolated Mode Parallel Development के लिए Port Conflict के nightmare को ठीक करता है"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 --isolated mode लेकर आता है: random ports, अलग secrets, और एक ही AppHost के कई instances चलाने पर शून्य collisions। AI agents, worktrees, और parallel workflows के लिए perfect।"
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

अगर आपने कभी एक ही project के दो instances एक साथ चलाने की कोशिश की है, तो आप इस दर्द को जानते हैं। Port 8080 already in use है। Port 17370 लिया हुआ है। कुछ terminate करो, restart करो, environment variables juggle करो — यह productivity killer है।

यह समस्या बेहतर नहीं हो रही, बल्कि बदतर हो रही है। AI agents independently काम करने के लिए git worktrees बनाते हैं। Background agents अलग environments spin up करते हैं। Developers feature branches के लिए एक ही repo को दो बार checkout करते हैं। इन सभी scenarios में एक ही दीवार आती है: एक ही app के दो instances एक ही ports पर लड़ रहे हैं।

Aspire 13.2 इसे एक single flag से ठीक करता है। Aspire team के James Newton-King ने [पूरी जानकारी लिखी है](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), और यह उन features में से एक है जिसके बारे में आप सोचते हैं "यह पहले क्यों नहीं था"।

## Fix: `--isolated`

```bash
aspire run --isolated
```

बस इतना ही। हर run को मिलता है:

- **Random ports** — instances के बीच कोई collision नहीं
- **Isolated user secrets** — connection strings और API keys हर instance के लिए अलग रहते हैं

कोई manual port reassignment नहीं। कोई environment variable juggling नहीं। हर run को automatically एक fresh, collision-free environment मिलता है।

## Real scenarios जहाँ यह चमकता है

**Multiple checkouts।** एक directory में feature branch है और दूसरे में bugfix:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

दोनों बिना conflicts के चलते हैं। Dashboard दिखाता है कि क्या चल रहा है और कहाँ।

**VS Code में background agents।** जब Copilot Chat का background agent आपके code पर independently काम करने के लिए एक git worktree बनाता है, तो उसे आपका Aspire AppHost चलाना पड़ सकता है। `--isolated` के बिना, यह आपके primary worktree के साथ port collision है। इसके साथ, दोनों instances बस काम करते हैं।

`aspire agent init` के साथ ship होने वाली Aspire skill automatically agents को worktrees में काम करते समय `--isolated` use करने का निर्देश देती है। तो Copilot का background agent इसे out of the box handle करना चाहिए।

**Development के साथ-साथ integration tests।** Features build करते हुए एक live AppHost के against tests चलाने की ज़रूरत है? Isolated mode हर context को अपने ports और config देता है।

## यह under the hood कैसे काम करता है

जब आप `--isolated` pass करते हैं, तो CLI run के लिए एक unique instance ID generate करता है। यह दो behaviors drive करता है:

1. **Port randomization** — आपके AppHost config में defined predictable ports को bind करने की बजाय, isolated mode सब कुछ के लिए random available ports pick करता है — dashboard, service endpoints, सब कुछ। Service discovery automatically adjust होती है, इसलिए services एक-दूसरे को ढूंढ लेती हैं चाहे वे किसी भी port पर land करें।

2. **Secret isolation** — हर isolated run को अपना user secrets store मिलता है, instance ID से keyed। एक run के connection strings और API keys दूसरे में leak नहीं होते।

आपके code में कोई बदलाव नहीं चाहिए। Aspire की service discovery endpoints को runtime पर resolve करती है, इसलिए सब कुछ सही से connect होता है चाहे port assignment कुछ भी हो।

## इसे कब use करें

`--isolated` तब use करें जब एक ही AppHost के कई instances एक साथ चला रहे हों — चाहे वह parallel development हो, automated tests हों, AI agents हों, या git worktrees हों। Single-instance development के लिए जहाँ आप predictable ports पसंद करते हैं, regular `aspire run` अभी भी ठीक काम करता है।

## निष्कर्ष

Isolated mode एक छोटी feature है जो एक असली, तेज़ी से common होती समस्या को हल करती है। जैसे-जैसे AI-assisted development हमें अधिक parallel workflows की तरफ धकेलता है — multiple agents, multiple worktrees, multiple contexts — ports पर लड़ाई के बिना बस एक और instance spin up करने की क्षमता ज़रूरी है।

सभी technical details के लिए [पूरा पोस्ट](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) पढ़ें और 13.2 आज़माने के लिए `aspire update --self` से update करें।
"""

path = "/Users/emiliano/.copilot/copilot-worktrees/blog/emimontesdeoca-unwresting-colby/content/posts/emiliano-montesdeoca/aspire-isolated-mode-parallel-instances/index.hi.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Post 4 done")
