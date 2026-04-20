---
title: "Azure पर अपने AI Agents को कहाँ Host करें? एक Practical Decision Guide"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure AI agents host करने के छह तरीके offer करता है — raw containers से लेकर fully managed Foundry Hosted Agents तक। यहाँ जानें कि अपने .NET workload के लिए सही कौन सा है।"
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-ai-agent-hosting-options-guide" >}}).*

अगर आप अभी .NET के साथ AI agents build कर रहे हैं, तो आपने शायद एक बात notice की होगी: Azure पर उन्हें host करने के *बहुत* तरीके हैं। Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — और ये सब तब तक reasonable लगते हैं जब तक आपको actually एक चुनना नहीं पड़ता। Microsoft ने हाल ही में [Azure AI agent hosting का एक comprehensive guide](https://devblogs.microsoft.com/all-things-azure/hostedagent/) publish किया है जो इसे clear करता है, और मैं इसे एक practical .NET developer perspective से break down करना चाहता हूँ।

## एक नज़र में छह options

यहाँ बताया गया है कि मैं इस landscape को कैसे summarize करूँगा:

| Option | सबसे अच्छा | आप manage करते हैं |
|--------|------------|---------------------|
| **Container Apps** | K8s complexity के बिना full container control | Observability, state, lifecycle |
| **AKS** | Enterprise compliance, multi-cluster, custom networking | सब कुछ (यही तो point है) |
| **Azure Functions** | Event-driven, short-running agent tasks | ज़्यादा नहीं — true serverless |
| **App Service** | Simple HTTP agents, predictable traffic | Deployment, scaling config |
| **Foundry Agents** | Code-optional agents via portal/SDK | लगभग कुछ नहीं |
| **Foundry Hosted Agents** | Custom framework agents with managed infra | केवल आपका agent code |

पहले चार general-purpose compute हैं — आप उन पर agents चला *सकते* हैं, लेकिन वे इसके लिए design नहीं किए गए। अंतिम दो agent-native हैं: वे conversations, tool calls, और agent lifecycles को first-class concepts के रूप में समझते हैं।

## Foundry Hosted Agents — .NET agent developers के लिए sweet spot

यहाँ जो मेरा ध्यान खींचा। Foundry Hosted Agents बीच में sit करते हैं: आपको अपना code चलाने की flexibility मिलती है (Semantic Kernel, Agent Framework, LangGraph — जो भी) लेकिन platform infrastructure, observability, और conversation management handle करता है।

मुख्य piece है **Hosting Adapter** — एक thin abstraction layer जो आपके agent framework को Foundry platform से bridge करता है। Microsoft Agent Framework के लिए, यह इस तरह दिखता है:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

यही आपकी पूरी hosting story है। Adapter protocol translation, server-sent events के ज़रिये streaming, conversation history, और OpenTelemetry tracing handle करता है — सब automatically। कोई custom middleware नहीं, कोई manual plumbing नहीं।

## Deploy करना genuinely simple है

मैंने पहले Container Apps पर agents deploy किए हैं और यह काम करता है, लेकिन आप state management और observability के लिए काफी glue code लिखते हैं। Hosted Agents और `azd` के साथ, deployment है:

```bash
# AI agent extension install करें
azd ext install azure.ai.agents

# Template से init करें
azd ai agent init

# Build, push, deploy — हो गया
azd up
```

वह single `azd up` आपका container build करता है, उसे ACR में push करता है, Foundry project provision करता है, model endpoints deploy करता है, और आपका agent start करता है। पाँच steps एक command में।

## Built-in conversation management

यही production में सबसे ज़्यादा समय बचाता है। अपना conversation state store बनाने की बजाय, Hosted Agents इसे natively handle करते हैं:

```python
# एक persistent conversation बनाएं
conversation = openai_client.conversations.create()

# पहला turn
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# दूसरा turn — context preserve होता है
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

कोई Redis नहीं। कोई Cosmos DB session store नहीं। Message serialization के लिए कोई custom middleware नहीं। Platform बस इसे handle कर लेता है।

## मेरा decision framework

सभी छह options को देखने के बाद, यह मेरा quick mental model है:

1. **क्या आपको zero infrastructure चाहिए?** → Foundry Agents (portal/SDK, no containers)
2. **क्या आपके पास custom agent code है लेकिन managed hosting चाहिए?** → Foundry Hosted Agents
3. **क्या आपको event-driven, short-lived agent tasks चाहिए?** → Azure Functions
4. **क्या आपको K8s के बिना maximum container control चाहिए?** → Container Apps
5. **क्या आपको strict compliance और multi-cluster चाहिए?** → AKS
6. **क्या आपके पास predictable traffic वाला simple HTTP agent है?** → App Service

Semantic Kernel या Microsoft Agent Framework के साथ build करने वाले ज़्यादातर .NET developers के लिए, Hosted Agents likely सही starting point है। आपको scale-to-zero, built-in OpenTelemetry, conversation management, और framework flexibility मिलती है — Kubernetes manage किए बिना या अपनी observability stack wire up किए बिना।

## निष्कर्ष

Azure पर agent hosting landscape तेज़ी से mature हो रहा है। अगर आप आज एक नया AI agent project शुरू कर रहे हैं, तो habit से Container Apps या AKS पर जाने से पहले Foundry Hosted Agents को seriously consider करें। Managed infrastructure real time बचाती है, और hosting adapter pattern आपको अपना framework choice रखने देता है।

[Microsoft का पूरा guide](https://devblogs.microsoft.com/all-things-azure/hostedagent/) और working examples के लिए [Foundry Samples repo](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) देखें।
