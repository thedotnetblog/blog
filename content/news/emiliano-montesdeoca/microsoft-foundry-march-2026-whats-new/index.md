---
title: "Microsoft Foundry March 2026 — GPT-5.4, Agent Service GA, and the SDK Refresh That Changes Everything"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry's March 2026 update is massive: Agent Service hits GA, GPT-5.4 brings reliable reasoning, the azure-ai-projects SDK goes stable across all languages, and Fireworks AI brings open models to Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

The monthly "What's New in Microsoft Foundry" posts are usually a mix of incremental improvements and the occasional headline feature. The [March 2026 edition](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? It's basically all headline features. Foundry Agent Service goes GA, GPT-5.4 ships for production, the SDK gets a major stable release, and Fireworks AI brings open model inference to Azure. Let me break down what matters for .NET developers.

## Foundry Agent Service is production-ready

This is the big one. The next-gen agent runtime is generally available — built on the OpenAI Responses API, wire-compatible with OpenAI agents, and open to models from multiple providers. If you're building with the Responses API today, migrating to Foundry adds enterprise security, private networking, Entra RBAC, full tracing, and evaluation on top of your existing agent logic.

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

Key additions: end-to-end private networking, MCP auth expansion (including OAuth passthrough), Voice Live preview for speech-to-speech agents, and hosted agents in 6 new regions.

## GPT-5.4 — reliability over raw intelligence

GPT-5.4 isn't about being smarter. It's about being more reliable. Stronger reasoning over long interactions, better instruction adherence, fewer mid-workflow failures, and integrated computer use capabilities. For production agents, that reliability matters way more than benchmark scores.

| Model | Pricing (per M tokens) | Best For |
|-------|----------------------|----------|
| GPT-5.4 (≤272K) | $2.50 / $15 output | Production agents, coding, document workflows |
| GPT-5.4 Pro | $30 / $180 output | Deep analysis, scientific reasoning |
| GPT-5.4 Mini | Cost-effective | Classification, extraction, lightweight tool calls |

The smart play is a routing strategy: GPT-5.4 Mini handles high-volume, low-latency work while GPT-5.4 takes the reasoning-heavy requests.

## The SDK is finally stable

`azure-ai-projects` SDK shipped stable releases across all languages — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0, and .NET 2.0.0 (April 1). The `azure-ai-agents` dependency is gone — everything lives under `AIProjectClient`. Install with `pip install azure-ai-projects` and the package bundles `openai` and `azure-identity` as direct dependencies.

For .NET developers, this means a single NuGet package for the full Foundry surface. No more juggling separate agent SDKs.

## Fireworks AI brings open models to Azure

Perhaps the most architecturally interesting addition: Fireworks AI processing 13+ trillion tokens daily at ~180K requests/second, now available through Foundry. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5, and MiniMax M2.5 at launch.

The real story is **bring-your-own-weights** — upload quantized or fine-tuned weights from anywhere without changing the serving stack. Deploy via serverless pay-per-token or provisioned throughput.

## Other highlights

- **Phi-4 Reasoning Vision 15B** — multimodal reasoning for charts, diagrams, and document layouts
- **Evaluations GA** — out-of-the-box evaluators with continuous production monitoring piped into Azure Monitor
- **Priority Processing** (Preview) — dedicated compute lane for latency-sensitive workloads
- **Voice Live** — speech-to-speech runtime that connects directly to Foundry agents
- **Tracing GA** — end-to-end agent trace inspection with sort and filter
- **PromptFlow deprecation** — migration to Microsoft Framework Workflows by January 2027

## Wrapping up

March 2026 is a turning point for Foundry. The Agent Service GA, stable SDKs across all languages, GPT-5.4 for reliable production agents, and open model inference via Fireworks AI — the platform is ready for serious workloads.

Read the [full roundup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) and [build your first agent](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) to get started.
