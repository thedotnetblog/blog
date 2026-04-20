---
title: "Microsoft Foundry March 2026 — GPT-5.4, Agent Service GA, और वह SDK Refresh जो सब कुछ बदल देता है"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry का March 2026 update बहुत बड़ा है: Agent Service GA हुआ, GPT-5.4 reliable reasoning लाया, azure-ai-projects SDK सभी languages में stable हुआ, और Fireworks AI open models Azure पर लाया।"
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "microsoft-foundry-march-2026-whats-new" >}}).*

Monthly "What's New in Microsoft Foundry" posts आमतौर पर incremental improvements और कभी-कभी एक headline feature का mix होती हैं। [March 2026 edition](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? यह basically सब headline features हैं। Foundry Agent Service GA हो गया, GPT-5.4 production के लिए ship हुआ, SDK का एक major stable release आया, और Fireworks AI Azure पर open model inference लाया। आइए breakdown करें कि .NET developers के लिए क्या मायने रखता है।

## Foundry Agent Service production-ready है

यही सबसे बड़ी खबर है। Next-gen agent runtime generally available है — OpenAI Responses API पर बना, OpenAI agents के साथ wire-compatible, और multiple providers के models के लिए open। अगर आप आज Responses API के साथ build कर रहे हैं, तो Foundry पर migrate करने से आपकी existing agent logic के ऊपर enterprise security, private networking, Entra RBAC, full tracing, और evaluation मिलता है।

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Key additions: end-to-end private networking, MCP auth expansion (OAuth passthrough सहित), speech-to-speech agents के लिए Voice Live preview, और 6 नए regions में hosted agents।

## GPT-5.4 — raw intelligence से ज़्यादा reliability

GPT-5.4 स्मार्ट होने के बारे में नहीं है। यह ज़्यादा reliable होने के बारे में है। Long interactions पर stronger reasoning, बेहतर instruction adherence, कम mid-workflow failures, और integrated computer use capabilities। Production agents के लिए, वह reliability benchmark scores से कहीं ज़्यादा मायने रखती है।

| Model | Pricing (per M tokens) | Best For |
|-------|----------------------|----------|
| GPT-5.4 (≤272K) | $2.50 / $15 output | Production agents, coding, document workflows |
| GPT-5.4 Pro | $30 / $180 output | Deep analysis, scientific reasoning |
| GPT-5.4 Mini | Cost-effective | Classification, extraction, lightweight tool calls |

Smart approach एक routing strategy है: GPT-5.4 Mini high-volume, low-latency work handle करे जबकि GPT-5.4 reasoning-heavy requests लेता है।

## SDK आखिरकार stable है

`azure-ai-projects` SDK सभी languages में stable releases के साथ ship हुआ — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0, और .NET 2.0.0 (April 1)। `azure-ai-agents` dependency चली गई — सब कुछ `AIProjectClient` के अंदर रहता है। `pip install azure-ai-projects` से install करें और package `openai` और `azure-identity` को direct dependencies के रूप में bundle करता है।

.NET developers के लिए, इसका मतलब है full Foundry surface के लिए एक single NuGet package। अब अलग-अलग agent SDKs को juggle नहीं करना।

## Fireworks AI Azure पर open models लाता है

शायद सबसे architecturally interesting addition: Fireworks AI जो daily 13+ trillion tokens ~180K requests/second पर process करता है, अब Foundry के ज़रिए available है। Launch पर DeepSeek V3.2, gpt-oss-120b, Kimi K2.5, और MiniMax M2.5।

असली कहानी है **bring-your-own-weights** — serving stack बदले बिना कहीं से भी quantized या fine-tuned weights upload करें। Serverless pay-per-token या provisioned throughput के ज़रिए deploy करें।

## अन्य highlights

- **Phi-4 Reasoning Vision 15B** — charts, diagrams, और document layouts के लिए multimodal reasoning
- **Evaluations GA** — Azure Monitor में piped continuous production monitoring के साथ out-of-the-box evaluators
- **Priority Processing** (Preview) — latency-sensitive workloads के लिए dedicated compute lane
- **Voice Live** — speech-to-speech runtime जो directly Foundry agents से connect होता है
- **Tracing GA** — sort और filter के साथ end-to-end agent trace inspection
- **PromptFlow deprecation** — January 2027 तक Microsoft Framework Workflows पर migration

## निष्कर्ष

March 2026 Foundry के लिए एक turning point है। Agent Service GA, सभी languages में stable SDKs, reliable production agents के लिए GPT-5.4, और Fireworks AI के ज़रिए open model inference — platform serious workloads के लिए तैयार है।

[Full roundup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) पढ़ें और [अपना पहला agent build करें](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) शुरुआत के लिए।
