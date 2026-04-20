---
title: "Azure MCP Tools अब Visual Studio 2022 में बिल्ट-इन हैं — कोई Extension ज़रूरी नहीं"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP tools अब Visual Studio 2022 में Azure development workload के हिस्से के रूप में आते हैं। 230 से अधिक tools, 45 Azure services, और कोई extension इंस्टॉल नहीं करना।"
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-mcp-tools-built-into-visual-studio-2022" >}}).*

अगर आप Visual Studio में अलग extension के ज़रिए Azure MCP tools use करते रहे हैं, तो आप उस झंझट से परिचित हैं — VSIX install करो, restart करो, उम्मीद करो कि टूटे नहीं, version mismatches manage करो। वो friction अब खत्म हो गई।

Yun Jung Choi ने [घोषणा की](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) कि Azure MCP tools अब सीधे Visual Studio 2022 में Azure development workload के हिस्से के रूप में आते हैं। कोई extension नहीं। कोई VSIX नहीं। कोई restart dance नहीं।

## इसका वास्तव में क्या मतलब है

Visual Studio 2022 version 17.14.30 से शुरू होकर, Azure MCP Server Azure development workload के साथ bundled आता है। अगर आपके पास पहले से वो workload installed है, तो बस GitHub Copilot Chat में उसे toggle on करना है और आप तैयार हैं।

45 Azure services में 230 से अधिक tools — सीधे chat window से accessible। अपने storage accounts list करें, ASP.NET Core app deploy करें, App Service issues diagnose करें, Log Analytics query करें — बिना browser tab खोले।

## यह जितना लगता है उससे ज़्यादा मायने क्यों रखता है

Developer tooling की असली बात यह है: हर extra step friction है, और friction adoption को मार देती है। MCP को एक अलग extension के रूप में रखने का मतलब था version mismatches, installation failures, और एक और चीज़ जो update रखनी होगी। इसे workload में बेक करने का मतलब है:

- Visual Studio Installer के ज़रिए **एकल update path**
- Extension और IDE के बीच **कोई version drift नहीं**
- **हमेशा current** — MCP Server VS के regular releases के साथ update होता है

Azure पर standardize करने वाली teams के लिए यह बड़ी बात है। Workload एक बार install करें, tools enable करें, और वे हर session के लिए वहाँ मौजूद हैं।

## इससे आप क्या कर सकते हैं

Tools Copilot Chat के ज़रिए पूरे development lifecycle को cover करते हैं:

- **सीखें** — Azure services, best practices, architecture patterns के बारे में पूछें
- **Design और develop करें** — service recommendations पाएं, app code configure करें
- **Deploy करें** — resources provision करें और IDE से सीधे deploy करें
- **Troubleshoot करें** — logs query करें, resource health check करें, production issues diagnose करें

एक quick example — Copilot Chat में यह type करें:

```
List my storage accounts in my current subscription.
```

Copilot पर्दे के पीछे Azure MCP tools call करता है, आपके subscriptions query करता है, और names, locations, और SKUs के साथ एक formatted list return करता है। कोई portal ज़रूरी नहीं।

## इसे कैसे enable करें

1. Visual Studio 2022 **17.14.30** या उससे ऊपर update करें
2. सुनिश्चित करें कि **Azure development** workload installed है
3. GitHub Copilot Chat खोलें
4. **Select tools** button (दो wrenches icon) पर क्लिक करें
5. **Azure MCP Server** को toggle on करें

बस इतना। यह sessions के बीच enabled रहता है।

## एक ध्यान देने योग्य बात

Tools default रूप से disabled हैं — आपको opt in करना होगा। VS 2026-specific tools VS 2022 में उपलब्ध नहीं हैं। Tool availability आपके Azure subscription permissions पर भी निर्भर करती है, जैसे portal में होती है।

## बड़ी तस्वीर

यह एक स्पष्ट trend का हिस्सा है: MCP developer IDEs में cloud tools surface करने का मानक तरीका बनता जा रहा है। हम पहले ही [Azure MCP Server 2.0 stable release](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) और VS Code तथा अन्य editors में MCP integrations देख चुके हैं। इसे Visual Studio के workload system में built in होना स्वाभाविक प्रगति है।

हम .NET developers जो Visual Studio में काम करते हैं, उनके लिए यह Azure portal पर context-switch करने का एक और कारण हटाता है। और सच में, जितना कम tab-switching, उतना बेहतर।
