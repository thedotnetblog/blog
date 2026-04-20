---
title: "Laptop से Production तक: दो Commands से Microsoft Foundry पर AI Agents Deploy करना"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI में अब 'azd ai agent' commands हैं जो आपके AI agent को local dev से live Foundry endpoint तक minutes में ले जाते हैं।"
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

आप उस gap को जानते हैं "यह मेरी machine पर काम करता है" और "यह deployed है और traffic serve कर रहा है" के बीच? AI agents के लिए, वह gap painfully wide थी।

Azure Developer CLI ने यह एक [two-command affair](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) बना दिया।

## नया `azd ai agent` workflow

```bash
azd ai agent init
azd up
```

बस इतना। `azd ai agent init` आपके repo में infrastructure-as-code scaffold करता है, और `azd up` Azure पर सब कुछ provision करता है और आपका agent publish करता है।

## Under the hood क्या होता है

`init` command आपके repo में real, inspectable Bicep templates generate करता है — Foundry Resource, Foundry Project, model deployment configuration, managed identity with RBAC।

## Dev inner loop

```bash
azd ai agent run    # local agent start करें
azd ai agent invoke # test prompts भेजें
azd ai agent monitor --follow  # real-time logs stream करें
```

## पूरा command set

| Command | क्या करता है |
|---------|-------------|
| `azd ai agent init` | IaC के साथ Foundry agent project scaffold करें |
| `azd up` | Resources provision करें और agent deploy करें |
| `azd ai agent invoke` | Remote या local agent को prompts भेजें |
| `azd ai agent run` | Development के लिए agent locally run करें |
| `azd ai agent monitor` | Published agent से real-time logs stream करें |
| `azd down` | सभी Azure resources clean up करें |

[Full walkthrough](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) देखें।
