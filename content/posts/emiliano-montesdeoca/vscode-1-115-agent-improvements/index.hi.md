---
title: "VS Code 1.115 — Background Terminal Notifications, SSH Agent Mode, और भी बहुत कुछ"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 में agents के लिए background terminal notifications, SSH remote agent hosting, terminal में file paste, और session-aware edit tracking आई है। .NET डेवलपर्स के लिए क्या मायने रखता है।"
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "vscode-1-115-agent-improvements" >}}).*

VS Code 1.115 अभी [आया है](https://code.visualstudio.com/updates/v1_115), और हालाँकि headline features के मामले में यह थोड़ी हल्की release है, agent-related सुधार genuinely useful हैं अगर आप रोज़ाना AI coding assistants के साथ काम करते हैं।

आइए वो बातें highlight करें जो वाकई जानने लायक हैं।

## Background terminals agents को जवाब देते हैं

यह standout feature है। Background terminals अब automatically agents को notify करते हैं जब commands पूरी होती हैं, जिसमें exit code और terminal output शामिल होता है। Background terminals में input prompts भी detect होते हैं और user को दिखाए जाते हैं।

यह क्यों मायने रखता है? अगर आपने background में build commands या test suites चलाने के लिए Copilot के agent mode का उपयोग किया है, तो आप जानते हैं "क्या वो खत्म हुई?" वाली परेशानी — background terminals essentially fire-and-forget थे। अब agent notify होता है जब आपका `dotnet build` या `dotnet test` पूरा होता है, output देखता है, और उसी के अनुसार react करता है। यह एक छोटा बदलाव है जो agent-driven workflows को काफी ज्यादा reliable बनाता है।

एक नया `send_to_terminal` tool भी है जो agents को user confirmation के साथ background terminals में commands भेजने देता है, उस समस्या को fix करते हुए जहाँ timeout के साथ `run_in_terminal` terminals को background में move कर देता था और उन्हें read-only बना देता था।

## SSH remote agent hosting

VS Code अब SSH के ज़रिए remote machines से connect करने, CLI automatically install करने, और उसे agent host mode में start करने को support करता है। इसका मतलब है आपके AI agent sessions सीधे remote environments को target कर सकते हैं — .NET डेवलपर्स के लिए useful जो Linux servers या cloud VMs पर build और test करते हैं।

## Agent sessions में edit tracking

Agent sessions के दौरान किए गए file edits अब track और restore होते हैं, diffs, undo/redo, और state restoration के साथ। अगर कोई agent आपके code में changes करता है और कुछ गलत हो जाता है, तो आप देख सकते हैं क्या बदला और उसे वापस ला सकते हैं। Agents को आपका codebase modify करने देने में मन की शांति।

## Browser tab awareness और अन्य सुधार

कुछ और quality-of-life additions:

- **Browser tab tracking** — chat अब session के दौरान खोले गए browser tabs को track और link कर सकती है, ताकि agents आपके देख रहे web pages reference कर सकें
- **Terminal में file paste** — files (images सहित) Ctrl+V, drag-and-drop, या right-click से terminal में paste करें
- **Minimap में test coverage** — quick visual overview के लिए test coverage indicators अब minimap में दिखते हैं
- **Mac पर pinch-to-zoom** — integrated browser pinch-to-zoom gestures support करता है
- **Sessions में Copilot entitlements** — status bar Sessions view में usage info दिखाता है
- **Go to File में Favicon** — quick pick list में open web pages favicons दिखाते हैं

## अंतिम बात

VS Code 1.115 एक incremental release है, लेकिन agent improvements — background terminal notifications, SSH agent hosting, और edit tracking — AI-assisted development के लिए noticeably smoother experience बनाते हैं। अगर आप .NET projects के लिए Copilot के agent mode का उपयोग कर रहे हैं, तो ये वो quality-of-life fixes हैं जो रोज़ाना friction कम करते हैं।

हर detail के लिए [full release notes](https://code.visualstudio.com/updates/v1_115) देखें।
