---
title: "VS Code 1.117: Agents को अपनी Git Branch मिल रही है — और मैं इसके साथ हूँ"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 में agent sessions के लिए worktree isolation, persistent Autopilot mode, और subagent support आई है। Agentic coding workflow अब और भी वास्तविक हो गई है।"
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

"AI assistant" और "AI teammate" के बीच की रेखा लगातार पतली होती जा रही है। VS Code 1.117 अभी आया है और [full release notes](https://code.visualstudio.com/updates/v1_117) भरे पड़े हैं, लेकिन यहाँ की कहानी साफ है: agents आपके dev workflow में first-class citizens बनते जा रहे हैं।

यहाँ वो है जो वाकई मायने रखता है।

## Autopilot mode आखिरकार आपकी preference याद रखता है

पहले, हर नई session शुरू करने पर Autopilot को फिर से enable करना पड़ता था। परेशान करने वाला। अब आपका permission mode sessions के पार persist होता है, और आप default configure कर सकते हैं।

Agent Host तीन session configs support करता है:

- **Default** — tools चलने से पहले confirmation माँगते हैं
- **Bypass** — सब कुछ auto-approve करता है
- **Autopilot** — पूरी तरह autonomous, अपने सवालों के खुद जवाब देता है और चलता रहता है

अगर आप migrations, Docker, और CI के साथ एक नया .NET project scaffold कर रहे हैं — एक बार Autopilot set करें और भूल जाएं। वह preference बनी रहती है।

## Agent sessions के लिए Worktree और git isolation

यह बड़ी बात है। Agent sessions अब पूरी worktree और git isolation support करती हैं। इसका मतलब है जब कोई agent किसी task पर काम करता है, उसे अपनी branch और working directory मिलती है। आपकी main branch untouched रहती है।

इससे भी बेहतर — Copilot CLI इन worktree sessions के लिए meaningful branch names generate करता है। अब `agent-session-abc123` नहीं। आपको कुछ ऐसा मिलता है जो वास्तव में बताता है agent क्या कर रहा है।

Multiple feature branches चलाने वाले या एक लंबे scaffolding task के दौरान bugs fix करने वाले .NET डेवलपर्स के लिए, यह game changer है। आपका एक agent एक worktree में API controllers बना सकता है जबकि आप दूसरे में service layer issue debug कर रहे हैं। कोई conflicts नहीं। कोई stashing नहीं। कोई mess नहीं।

## Subagents और agent teams

Agent Host Protocol अब subagents support करता है। एक agent किसी task के हिस्सों को handle करने के लिए दूसरे agents spin up कर सकता है। इसे delegation की तरह सोचें — आपका main agent coordinate करता है, और specialized agents टुकड़े handle करते हैं।

यह early है, लेकिन .NET workflows के लिए potential स्पष्ट है। कल्पना करें एक agent आपके EF Core migrations handle करे जबकि दूसरा integration tests setup करे। हम पूरी तरह वहाँ नहीं हैं, लेकिन अभी protocol support land होने का मतलब है tooling जल्दी आएगी।

## Agents input भेजने पर terminal output automatically include होता है

छोटा लेकिन meaningful। जब कोई agent terminal को input भेजता है, terminal output अब automatically context में include हो जाता है। पहले, agent को बस यह देखने के लिए एक extra turn लेना पड़ता था कि क्या हुआ।

अगर आपने कभी किसी agent को `dotnet build` चलाते, fail होते, और फिर error देखने के लिए सिर्फ एक और round-trip लेते देखा है — वह friction खत्म हो गया। यह output तुरंत देखता है और react करता है।

## macOS पर self-updating Agents app

macOS पर standalone Agents app अब self-update करती है। अब manually नए versions download नहीं करने होंगे। यह बस current रहती है।

## जानने लायक छोटी बातें

- **package.json hovers** अब installed version और latest available दोनों दिखाते हैं। Useful है अगर आप .NET projects के साथ npm tooling manage करते हैं।
- **JSDoc** comments में **Images** hovers और completions में सही render होती हैं।
- **Copilot CLI sessions** अब indicate करती हैं कि वे VS Code द्वारा बनाई गईं या externally — handy जब आप terminals के बीच jump कर रहे हों।
- **Copilot CLI, Claude Code, और Gemini CLI** shell types के रूप में recognize होते हैं। Editor जानता है आप क्या चला रहे हैं।

## निष्कर्ष

VS Code 1.117 कोई flashy feature dump नहीं है। यह infrastructure है। Worktree isolation, persistent permissions, subagent protocols — ये उस workflow के building blocks हैं जहाँ agents बिना आपके code पर कदम रखे real, parallel tasks handle करते हैं।

अगर आप .NET से build कर रहे हैं और अभी तक agentic workflow में नहीं उतरे हैं, तो honestly, अब शुरू करने का समय है।
