---
title: "Laptop से Production तक: दो Commands में Microsoft Foundry पर AI Agents Deploy करना"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI में अब 'azd ai agent' commands हैं जो आपके AI agent को minutes में local dev से live Foundry endpoint तक ले जाती हैं। यहाँ है पूरा workflow।"
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

आप उस gap को जानते हैं जो "मेरी machine पर काम करता है" और "यह deploy हो गया है और traffic serve कर रहा है" के बीच है? AI agents के लिए, वह gap दर्दनाक रूप से चौड़ी रही है। आपको resources provision करने हैं, models deploy करने हैं, identity wire up करनी है, monitoring set up करनी है — और यह सब किसी के भी आपके agent को call करने से पहले।

Azure Developer CLI ने इसे [दो-command affair](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) बना दिया है।

## नया `azd ai agent` Workflow

आइए मैं बताता हूँ यह वास्तव में कैसा दिखता है। आपके पास एक AI agent project है — मान लीजिए एक hotel concierge agent। यह locally काम करता है। आप इसे Microsoft Foundry पर चलाना चाहते हैं।

```bash
azd ai agent init
azd up
```

बस। दो commands। `azd ai agent init` आपके repo में infrastructure-as-code scaffold करता है, और `azd up` Azure पर सब कुछ provision करता है और आपका agent publish करता है। आपको Foundry portal में अपने agent का direct link मिलता है।

## Under the Hood क्या होता है

`init` command आपके repo में real, inspectable Bicep templates generate करता है:

- एक **Foundry Resource** (top-level container)
- एक **Foundry Project** (जहाँ आपका agent रहता है)
- **Model deployment** configuration (GPT-4o, आदि)
- उचित RBAC role assignments के साथ **Managed identity**
- Service map के लिए `azure.yaml`
- Agent metadata और environment variables के साथ `agent.yaml`

यहाँ key part है: यह सब आपके पास है। यह आपके repo में versioned Bicep है। आप इसे inspect कर सकते हैं, customize कर सकते हैं, और अपने agent code के साथ commit कर सकते हैं। कोई magic black boxes नहीं।

## Dev Inner Loop

मुझे जो वास्तव में पसंद है वह local development story है। जब आप agent logic पर iterate कर रहे हों, तो आप हर बार prompt बदलने पर redeploy नहीं करना चाहते:

```bash
azd ai agent run
```

यह आपके agent को locally start करता है। इसे `azd ai agent invoke` के साथ pair करें test prompts भेजने के लिए, और आपके पास एक tight feedback loop है। Code edit करें, restart करें, invoke करें, दोहराएँ।

`invoke` command routing के बारे में भी smart है — जब एक local agent चल रहा होता है, तो यह automatically उसे target करता है। जब नहीं, तो यह remote endpoint को hit करता है।

## Real-Time Monitoring

यही वह feature है जिसने मुझे convince किया। एक बार आपका agent deploy हो जाने पर:

```bash
azd ai agent monitor --follow
```

आपके agent से गुज़रने वाला हर request और response real time में आपके terminal में stream होता है। Production issues debug करने के लिए, यह अमूल्य है। Log analytics खंगालने की ज़रूरत नहीं, metrics aggregate होने का इंतज़ार नहीं — आप देखते हैं कि अभी क्या हो रहा है।

## पूरा Command Set

यहाँ quick reference है:

| Command | क्या करता है |
|---------|-------------|
| `azd ai agent init` | IaC के साथ एक Foundry agent project scaffold करें |
| `azd up` | Azure resources provision करें और agent deploy करें |
| `azd ai agent invoke` | Remote या local agent को prompts भेजें |
| `azd ai agent run` | Development के लिए agent को locally चलाएँ |
| `azd ai agent monitor` | Published agent से real-time logs stream करें |
| `azd ai agent show` | Agent health और status check करें |
| `azd down` | सभी Azure resources cleanup करें |

## .NET Developers के लिए यह क्यों मायने रखता है

भले ही announcement का sample Python-based है, infrastructure story language-agnostic है। आपके .NET agent को वही Bicep scaffolding, वही managed identity setup, वही monitoring pipeline मिलती है। और अगर आप पहले से अपने .NET Aspire apps या Azure deployments के लिए `azd` उपयोग कर रहे हैं, तो यह आपके मौजूदा workflow में बिल्कुल fit होता है।

AI agents के लिए deployment gap ecosystem में सबसे बड़े friction points में से एक रही है। एक working prototype से proper identity, networking, और monitoring वाले production endpoint तक पहुँचने में DevOps का एक हफ्ता नहीं लगना चाहिए। अब इसमें दो commands और कुछ minutes लगते हैं।

## निष्कर्ष

`azd ai agent` अभी available है। अगर आप अपने AI agents deploy करना टाल रहे थे क्योंकि infrastructure setup बहुत मुश्किल लग रहा था, तो इसे एक chance दें। Frontend chat app integration सहित पूरे step-by-step के लिए [पूरा walkthrough](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) देखें।
