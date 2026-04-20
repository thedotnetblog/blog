---
title: "Visual Studio के March अपडेट में Custom Copilot Agents बनाने की सुविधा — और find_symbol टूल एक बड़ी बात है"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studio के March 2026 अपडेट में custom Copilot agents, reusable agent skills, language-aware find_symbol टूल, और Test Explorer से Copilot-powered profiling आई है। यहाँ जानिए क्या मायने रखता है।"
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "visual-studio-march-2026-custom-copilot-agents" >}}).*

Visual Studio को अब तक का सबसे महत्वपूर्ण Copilot अपडेट मिला है। Mark Downie ने [March release की घोषणा की](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), और headline custom agents की है — लेकिन सच कहें तो थोड़ा आगे छुपा `find_symbol` टूल वह feature हो सकता है जो आपके workflow को सबसे ज्यादा बदलेगा।

आइए देखें यहाँ वास्तव में क्या है।

## आपके repo में Custom Copilot agents

चाहते हैं कि Copilot आपकी टीम के coding standards का पालन करे, आपका build pipeline चलाए, या आपके internal docs query करे? अब आप ठीक वैसा ही बना सकते हैं।

Custom agents को `.agent.md` files के रूप में परिभाषित किया जाता है जिन्हें आप अपने repository में `.github/agents/` में रखते हैं। प्रत्येक agent को workspace awareness, code understanding, tools, आपका preferred model, और external services से MCP connections तक पूरी access मिलती है। वे built-in agents के साथ agent picker में दिखते हैं।

यह वही pattern है जो VS Code support करता रहा है — और यह देखकर अच्छा लगता है कि Visual Studio भी catch up कर रहा है। जिन टीमों ने VS Code के लिए agents बनाए हैं, उनकी `.agent.md` files दोनों IDEs में काम करनी चाहिए (हालाँकि tool names भिन्न हो सकते हैं, इसलिए test करें)।

[awesome-copilot](https://github.com/github/awesome-copilot) repo में community-contributed agent configurations हैं जिन्हें आप starting points के रूप में use कर सकते हैं।

## Agent skills: reusable instruction packs

Skills आपके repo में `.github/skills/` या आपके profile में `~/.copilot/skills/` से automatically pick up होती हैं। प्रत्येक skill एक `SKILL.md` file है जो [Agent Skills specification](https://agentskills.io/specification) का पालन करती है।

Skills को modular expertise के रूप में सोचें जिन्हें आप mix और match कर सकते हैं। आपके पास आपके API conventions के लिए एक skill हो सकती है, testing patterns के लिए एक और, और deployment workflow के लिए एक अलग। जब कोई skill activate होती है, तो वह chat में दिखती है ताकि आप जान सकें कि वह apply हो रही है।

अगर आप VS Code में skills use कर रहे थे, तो अब वे Visual Studio में भी उसी तरह काम करती हैं।

## find_symbol: agents के लिए language-aware navigation

यहाँ चीजें वाकई दिलचस्प हो जाती हैं। नया `find_symbol` टूल Copilot के agent mode को actual language-service-powered symbol navigation देता है। आपके code को text के रूप में search करने की बजाय, एजेंट अब कर सकता है:

- पूरे project में किसी symbol के सभी references खोजना
- type information, declarations, और scope metadata access करना
- पूरी language awareness के साथ call sites पर navigate करना

व्यावहारिक रूप से इसका मतलब है: जब आप Copilot से कोई method refactor करने या call sites में parameter signature update करने को कहते हैं, तो वह वास्तव में आपके code की structure देख सकता है। अब "एजेंट ने method बदल दिया लेकिन तीन call sites miss कर दिए" जैसी स्थितियाँ नहीं होंगी।

Supported languages में C#, C++, Razor, TypeScript, और supported LSP extension वाली कोई भी language शामिल है। .NET डेवलपर्स के लिए यह एक बड़ा सुधार है — deep type hierarchies और interfaces वाले C# codebases symbol-aware navigation से बहुत फायदा उठाते हैं।

## Copilot से tests profile करें

Test Explorer context menu में अब **Profile with Copilot** command है। कोई test select करें, profile पर click करें, और Profiling Agent automatically उसे run करके performance analyze करता है — actionable insights देने के लिए CPU usage और instrumentation data को मिलाकर।

अब manually profiler sessions configure नहीं करने, test run नहीं करने, results export नहीं करने, और flame graph पढ़ने की कोशिश नहीं करनी होगी। एजेंट analysis करता है और बताता है क्या slow है और क्यों। अभी केवल .NET के लिए, जो Visual Studio के deep .NET diagnostics integration को देखते हुए समझ में आता है।

## Live debugging के दौरान performance tips

Performance optimization अब debug करने के बाद नहीं, debug करते समय होती है। जब आप code में step through करते हैं, Visual Studio execution time और performance signals inline दिखाता है। कोई slow line दिखे? Perf Tip पर click करें और Copilot से वहीं optimization suggestions माँगें।

Profiling Agent automatically runtime data capture करता है — elapsed time, CPU usage, memory behavior — और Copilot उसका उपयोग hot spots पहचानने के लिए करता है। यह performance work को आपके debugging flow का हिस्सा बनाए रखता है, न कि एक अलग काम जिसे आप टालते रहते हैं।

## Solution Explorer से NuGet vulnerabilities fix करें

जब किसी NuGet package में vulnerability detect होती है, तो अब Solution Explorer में सीधे **Fix with GitHub Copilot** link के साथ notification दिखता है। Click करें और Copilot vulnerability analyze करता है, सही package updates recommend करता है, और उन्हें implement करता है।

उन टीमों के लिए जो dependencies up to date रखने में संघर्ष करती हैं (यानी लगभग सभी), यह "मुझे पता है vulnerability है लेकिन सही update path निकालना अपने आप में एक project है" वाली परेशानी दूर करता है।

## अंतिम बात

Custom agents और skills headline हैं, लेकिन `find_symbol` sleeper hit है — यह मौलिक रूप से बदलता है कि Copilot .NET code refactor करते समय कितना accurate हो सकता है। Live profiling integration और vulnerability fixes के साथ मिलकर, यह अपडेट Visual Studio के AI features को demo-ready की बजाय genuinely practical बनाता है।

इसे आज़माने के लिए [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) download करें।
