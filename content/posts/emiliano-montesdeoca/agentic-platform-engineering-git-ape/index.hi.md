---
title: "Agentic Platform Engineering हकीकत बन रही है — Git-APE दिखाता है कैसे"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft का Git-APE प्रोजेक्ट agentic platform engineering को व्यवहार में लाता है — GitHub Copilot एजेंट्स और Azure MCP का उपयोग करके natural-language अनुरोधों को validated cloud infrastructure में बदलने के लिए।"
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform engineering उन शब्दों में से एक रहा है जो conference talks में शानदार लगता है लेकिन आमतौर पर "हमने एक internal portal और Terraform wrapper बनाया" का मतलब होता है। असली वादा — self-service infrastructure जो वास्तव में safe, governed और fast हो — हमेशा कुछ कदम दूर रहा है।

Azure टीम ने [agentic platform engineering series का Part 2](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) प्रकाशित किया है। वे इसे **Git-APE** कहते हैं — एक open-source प्रोजेक्ट जो GitHub Copilot एजेंट्स और Azure MCP सर्वर का उपयोग करके natural-language अनुरोधों को validated, deployed infrastructure में बदलता है।

## Git-APE वास्तव में क्या करता है

मूल विचार: developers Terraform modules सीखने के बजाय, एक Copilot एजेंट से बात करते हैं। एजेंट intent interpret करता है, Infrastructure-as-Code generate करता है, policies के खिलाफ validate करता है, और deploy करता है — सब VS Code में।

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

VS Code में workspace खोलें, और agent configuration files GitHub Copilot द्वारा auto-discovered हो जाती हैं:

```
@git-ape deploy a function app with storage in West Europe
```

Clean-up भी उतना ही आसान है:

```
@git-ape destroy my-resource-group
```

## यह क्यों मायने रखता है

Azure पर build करने वालों के लिए, यह platform engineering conversation को "हम portal कैसे बनाएं" से "हम अपने guardrails को APIs के रूप में कैसे describe करें" में shift करता है।

.NET डेवलपर के रूप में: Azure MCP Server और GitHub Copilot एजेंट्स किसी भी Azure workload के साथ काम करते हैं। आपकी ASP.NET Core API, .NET Aspire stack — सब कुछ agentic deployment flow का target हो सकता है।

## समापन

Git-APE agentic platform engineering का एक शुरुआती लेकिन concrete नज़रिया है। [रेपो](https://github.com/Azure/git-ape) clone करें और [पूरी पोस्ट](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) पढ़ें।
