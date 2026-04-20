---
title: "VS Code 1.112: .NET डेवलपर्स के लिए वाकई जरूरी बातें"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 आ गया है और इसमें agent upgrades, integrated browser debugger, MCP sandboxing, और monorepo support भरपूर है। अगर आप .NET से build कर रहे हैं तो यहाँ जानिए क्या वाकई मायने रखता है।"
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "vscode-1-112-dotnet-developers" >}}).*

VS Code 1.112 आ गया है, और सच कहें तो? अगर आप अपने दिन .NET में बिता रहे हैं तो यह release अलग ही feel कराती है। [official release notes](https://code.visualstudio.com/updates/v1_112) में बहुत कुछ है, लेकिन मैं आपकी scrolling बचाता हूँ और focus करता हूँ उन चीज़ों पर जो हमारे लिए वाकई मायने रखती हैं।

## Copilot CLI और भी उपयोगी हो गया

इस release का बड़ा theme है **agent autonomy** — Copilot को हर कदम पर निगरानी किए बिना काम करने की ज्यादा जगह देना।

### Message steering और queueing

वह पल जब Copilot CLI किसी task के बीच में होता है और आपको याद आता है कि कुछ बताना भूल गए? पहले आपको इंतजार करना पड़ता था। अब आप request चलते हुए भी messages भेज सकते हैं — या तो current response को steer करने के लिए या follow-up instructions queue करने के लिए।

यह उन लंबे `dotnet` scaffolding tasks के लिए बहुत काम का है जहाँ आप Copilot को project setup करते देख रहे होते हैं और सोचते हैं "अरे रुको, मुझे MassTransit भी चाहिए था।"

### Permission levels

यह वाला मुझे सबसे ज्यादा excited करता है। Copilot CLI sessions अब तीन permission levels support करती हैं:

- **Default Permissions** — सामान्य flow जहाँ tools चलने से पहले confirmation माँगते हैं
- **Bypass Approvals** — सब कुछ auto-approve करता है और errors पर retry करता है
- **Autopilot** — पूरी तरह autonomous: tools approve करता है, अपने सवालों के खुद जवाब देता है, और task पूरा होने तक चलता रहता है

अगर आप एक नई ASP.NET Core API Entity Framework, migrations, और Docker setup के साथ scaffold कर रहे हैं — Autopilot mode का मतलब है कि आप बताएं क्या चाहिए और coffee लेने चले जाएं। यह खुद figure out कर लेगा।

Autopilot को `chat.autopilot.enabled` setting से enable कर सकते हैं।

### Delegation से पहले changes preview करें

जब आप Copilot CLI को कोई task delegate करते हैं, तो यह एक worktree बनाता है। पहले, अगर आपके uncommitted changes थे, तो आपको Source Control में देखना पड़ता था। अब Chat view में decision लेने से पहले ही pending changes दिखते हैं — copy, move, या ignore करने के लिए।

छोटी बात है, लेकिन "रुको, मेरे पास क्या staged था?" वाला पल बचाती है।

## VS Code से बाहर निकले बिना web apps debug करें

Integrated browser अब **full debugging** support करता है। आप breakpoints set कर सकते हैं, code step through कर सकते हैं, और variables inspect कर सकते हैं — सब VS Code के अंदर। Edge DevTools में switch करने की जरूरत नहीं।

एक नया `editor-browser` debug type है, और अगर आपके पास पहले से `msedge` या `chrome` launch configurations हैं, तो migrate करना उतना ही आसान है जितना `launch.json` में `type` field बदलना:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Blazor डेवलपर्स के लिए यह game changer है। आप terminal में `dotnet watch` पहले से चला रहे हैं — अब आपकी debugging भी उसी window में रहती है।

Browser को independent zoom levels भी मिले (आखिरकार), proper right-click context menus, और zoom हर website के लिए याद रखा जाता है।

## MCP server sandboxing

यह आप जितना सोच रहे हैं उससे ज्यादा मायने रखता है। अगर आप MCP servers use कर रहे हैं — शायद आपने Azure resources या database queries के लिए custom बनाया है — तो वे आपके VS Code process जितनी ही permissions के साथ चल रहे थे। यानी आपके filesystem, network, सब कुछ तक पूरी access।

अब आप उन्हें sandbox कर सकते हैं। अपने `mcp.json` में:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

जब किसी sandboxed server को कोई ऐसी चीज़ चाहिए जो उसके पास नहीं है, VS Code आपसे permission grant करने को कहता है। "उम्मीद है कोई कुछ अजीब नहीं करेगा" वाले तरीके से कहीं बेहतर।

> **नोट:** Sandboxing अभी macOS और Linux पर उपलब्ध है। Windows support आ रहा है — WSL जैसे remote scenarios काम करते हैं।

## Monorepo customizations discovery

अगर आप monorepo में काम कर रहे हैं (और सच कहें तो, कई enterprise .NET solutions आखिरकार एक बन जाते हैं), तो यह एक असली समस्या हल करता है।

पहले, अगर आप अपने repo का कोई subfolder खोलते थे, VS Code आपकी `copilot-instructions.md`, `AGENTS.md`, या custom skills जो repository root पर थीं, नहीं खोज पाता था। अब `chat.useCustomizationsInParentRepositories` setting के साथ, यह `.git` root तक जाकर सब कुछ खोजता है।

इसका मतलब है कि आपकी टीम monorepo के सभी projects में agent instructions, prompt files, और custom tools share कर सकती है, बिना सभी को root folder खोलने की जरूरत के।

## Agent debugging के लिए /troubleshoot

कभी custom instructions या skills set up किए और सोचा क्यों pick up नहीं हो रहीं? नई `/troubleshoot` skill agent debug logs पढ़ती है और बताती है क्या हुआ — कौन से tools use हुए या skip हुए, instructions क्यों load नहीं हुए, और slow responses का कारण क्या है।

इसे enable करें:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

फिर chat में बस `/troubleshoot why is my custom skill not loading?` type करें।

अब आप इन debug logs को export और import भी कर सकते हैं, जो तब बहुत काम आता है जब कुछ expected नहीं चल रहा हो और team के साथ share करना हो।

## Image और binary file support

Agents अब disk से image files और binary files natively पढ़ सकते हैं। Binary files hexdump format में present होती हैं, और image outputs (जैसे integrated browser के screenshots) carousel view में दिखती हैं।

.NET डेवलपर्स के लिए सोचें: UI bug का screenshot chat में paste करें और agent समझे क्या गलत है, या Blazor component rendering का output analyze करवाएं।

## Automatic symbol references

एक छोटा quality-of-life सुधार: जब आप किसी symbol का नाम (class, method, आदि) copy करके chat में paste करते हैं, VS Code अब automatically उसे `#sym:Name` reference में convert कर देता है। इससे agent को उस symbol का पूरा context मिल जाता है बिना आपको manually add किए।

अगर plain text चाहिए तो `Ctrl+Shift+V` use करें।

## Plugins अब enable/disable हो सकते हैं

पहले, MCP server या plugin disable करने का मतलब था उसे uninstall करना। अब आप उन्हें on और off toggle कर सकते हैं — globally और per-workspace दोनों तरह से। Extensions view या Customizations view में right-click करें और काम हो गया।

npm और pypi के plugins अब auto-update भी हो सकते हैं, हालाँकि वे पहले approval माँगेंगे क्योंकि updates का मतलब है आपकी machine पर नया code चलाना।

## अंतिम बात

VS Code 1.112 clearly agent experience पर जोर दे रहा है — अधिक autonomy, बेहतर debugging, tighter security। .NET डेवलपर्स के लिए, integrated browser debugging और Copilot CLI improvements standout features हैं।

अगर आपने अभी तक किसी .NET project के लिए Copilot CLI session Autopilot mode में नहीं चलाई है, तो यह release शुरू करने का अच्छा समय है। बस अपनी permissions set करें और इसे करने दें।

[VS Code 1.112 download करें](https://code.visualstudio.com/updates/v1_112) या VS Code के अंदर **Help > Check for Updates** से update करें।
