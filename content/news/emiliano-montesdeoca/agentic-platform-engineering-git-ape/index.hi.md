---
title: "Agentic Platform Engineering हकीकत बन रही है — Git-APE दिखाता है कैसे"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft का Git-APE project agentic platform engineering को व्यवहार में लाता है — GitHub Copilot agents और Azure MCP का उपयोग करके natural-language requests को validated cloud infrastructure में बदलता है।"
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform engineering उन terms में से एक रही है जो conference talks में बहुत अच्छी लगती है, लेकिन आमतौर पर इसका मतलब होता है "हमने एक internal portal और एक Terraform wrapper बनाया।" असली वादा — self-service infrastructure जो वास्तव में safe, governed और fast हो — हमेशा कुछ कदम दूर रही है।

Azure team ने अभी [अपनी agentic platform engineering series का Part 2 प्रकाशित किया](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/), और यह पूरी तरह hands-on implementation के बारे में है। वे इसे **Git-APE** कहते हैं (हाँ, acronym जानबूझकर है), और यह एक open-source project है जो GitHub Copilot agents plus Azure MCP servers का उपयोग करके natural-language requests को validated, deployed infrastructure में बदलता है।

## Git-APE वास्तव में क्या करता है

मूल विचार: developers को Terraform modules सीखने, portal UIs navigate करने, या platform team को tickets file करने की बजाय, वे एक Copilot agent से बात करते हैं। Agent intent को समझता है, Infrastructure-as-Code generate करता है, उसे policies के खिलाफ validate करता है, और deploy करता है — सब VS Code के अंदर।

यहाँ setup है:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

VS Code में workspace खोलें, और agent configuration files GitHub Copilot द्वारा auto-discovered हो जाती हैं। आप agent के साथ directly interact करते हैं:

```
@git-ape deploy a function app with storage in West Europe
```

Agent Azure services के साथ interact करने के लिए Azure MCP Server का उपयोग करता है। VS Code settings में MCP configuration specific capabilities enable करता है:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## यह क्यों मायने रखता है

जो लोग Azure पर build कर रहे हैं, उनके लिए यह platform engineering की conversation को "हम एक portal कैसे बनाएं" से "हम अपने guardrails को APIs के रूप में कैसे describe करें" की ओर shift करता है। जब आपके platform का interface एक AI agent हो, तो आपके constraints और policies की गुणवत्ता ही product बन जाती है।

Part 1 blog ने theory रखी: well-described APIs, control schemas, और explicit guardrails platforms को agent-ready बनाते हैं। Part 2 actual tooling ship करके साबित करता है कि यह काम करता है। Agent अंधाधुंध resources generate नहीं करता — यह best practices के खिलाफ validate करता है, naming conventions का सम्मान करता है, और आपके organization की policies लागू करता है।

Clean-up भी उतनी ही आसान है:

```
@git-ape destroy my-resource-group
```

## मेरी राय

सच कहूँ तो — यह specific tool से ज़्यादा pattern के बारे में है। Git-APE खुद एक demo/reference architecture है। लेकिन underlying idea — agents आपके platform का interface, MCP protocol, GitHub Copilot host — यही वह जगह है जहाँ enterprise developer experience जा रही है।

अगर आप एक platform team हैं जो देख रहे हैं कि अपने internal tooling को agent-friendly कैसे बनाएं, तो इससे बेहतर कोई starting point नहीं है। और अगर आप एक .NET developer हैं जो सोच रहे हैं कि यह आपकी दुनिया से कैसे जुड़ता है: Azure MCP Server और GitHub Copilot agents किसी भी Azure workload के साथ काम करते हैं। आपकी ASP.NET Core API, आपका .NET Aspire stack, आपके containerized microservices — यह सब एक agentic deployment flow का target हो सकता है।

## अंत में

Git-APE agentic platform engineering का एक प्रारंभिक लेकिन ठोस रूप है। [repo](https://github.com/Azure/git-ape) clone करें, demo आज़माएं, और सोचना शुरू करें कि आपके platform की APIs और policies को एक agent द्वारा safely उपयोग किए जाने के लिए कैसा दिखना होगा।

walkthrough और video demos के लिए [पूरा post](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) पढ़ें।
