---
title: "VS Code 1.116 — Agents App में Keyboard Navigation और File Context Completions"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 का ध्यान Agents app की polish पर है — dedicated keybindings, accessibility improvements, file-context completions, और CSS @import link resolution।"
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "vscode-1-116-agents-app-updates" >}}).*

VS Code 1.116 April 2026 release है, और हालाँकि यह कुछ recent updates से हल्की है, बदलाव focused और meaningful हैं — खासकर अगर आप रोज़ाना Agents app use कर रहे हैं।

[official release notes](https://code.visualstudio.com/updates/v1_116) के आधार पर, यहाँ क्या मिला है।

## Agents app में सुधार

Agents app उपयोगिता polish के साथ mature होता जा रहा है जो रोज़मर्रा के workflows में वास्तविक फर्क डालती है:

**Dedicated keybindings** — अब आप dedicated commands और keyboard shortcuts से Changes view, Changes के अंदर files tree, और Chat Customizations view focus कर सकते हैं। अगर आप Agents app में navigate करने के लिए click करते रहे हैं, तो यह पूरी keyboard-driven workflows लाता है।

**Accessibility help dialog** — chat input box में `Alt+F1` दबाने पर अब एक accessibility help dialog खुलता है जो available commands और keybindings दिखाता है। Screen reader users announcement verbosity भी control कर सकते हैं। अच्छी accessibility सभी को फायदा पहुँचाती है।

**File-context completions** — Agents app chat में `#` type करें और आपके current workspace तक scoped file-context completions trigger होती हैं। यह उन छोटे quality-of-life improvements में से एक है जो हर interaction को तेज़ बनाती है — code reference करते समय अब पूरे file paths type नहीं करने होंगे।

## CSS `@import` link resolution

Frontend developers के लिए एक अच्छी addition: VS Code अब CSS `@import` references resolve करता है जो node_modules paths use करते हैं। आप bundlers use करते समय `@import "some-module/style.css"` जैसे imports को `Ctrl+click` से follow कर सकते हैं। छोटा है लेकिन CSS workflows में एक friction point खत्म करता है।

## अंतिम बात

VS Code 1.116 refinement के बारे में है — Agents app को अधिक navigable, अधिक accessible, और अधिक keyboard-friendly बनाना। अगर आप Agents app में काफी समय बिता रहे हैं (और मुझे लगता है हम में से कई बिता रहे हैं), तो ये बदलाव जुड़ते जाते हैं।

पूरी list के लिए [full release notes](https://code.visualstudio.com/updates/v1_116) देखें।
