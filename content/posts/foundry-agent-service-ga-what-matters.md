---
title: "Foundry Agent Service is GA: What Actually Matters for .NET Agent Builders"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft's Foundry Agent Service just hit GA with private networking, Voice Live, production evaluations, and an open multi-model runtime. Here's what you need to know."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Let's be honest — building an AI agent prototype is the easy part. The hard part is everything after: getting it into production with proper network isolation, running evaluations that actually mean something, handling compliance requirements, and not breaking things at 2 AM.

The [Foundry Agent Service just went GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), and this release is laser-focused on that "everything after" gap.

## Built on the Responses API

Here's the headline: the next-gen Foundry Agent Service is built on the OpenAI Responses API. If you're already building with that wire protocol, migrating to Foundry is minimal code changes. What you gain: enterprise security, private networking, Entra RBAC, full tracing, and evaluation — on top of your existing agent logic.

The architecture is intentionally open. You're not locked to one model provider or one orchestration framework. Use DeepSeek for planning, OpenAI for generation, LangGraph for orchestration — the runtime handles the consistency layer.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> If you're coming from the `azure-ai-agents` package, agents are now first-class operations on `AIProjectClient` in `azure-ai-projects`. Drop the standalone pin and use `get_openai_client()` to drive responses.

## Private networking: the enterprise blocker removed

This is the feature that unblocks enterprise adoption. Foundry now supports full end-to-end private networking with BYO VNet:

- **No public egress** — agent traffic never touches the public internet
- **Container/subnet injection** into your network for local communication
- **Tool connectivity included** — MCP servers, Azure AI Search, Fabric data agents all operate over private paths

That last point is critical. It's not just inference calls that stay private — every tool invocation and retrieval call stays inside your network boundary too. For teams operating under data classification policies that prohibit external routing, this is what was missing.

## MCP authentication done right

MCP server connections now support the full spectrum of auth patterns:

| Auth method | When to use |
|-------------|-------------|
| Key-based | Simple shared access for org-wide internal tools |
| Entra Agent Identity | Service-to-service; the agent authenticates as itself |
| Entra Managed Identity | Per-project isolation; no credential management |
| OAuth Identity Passthrough | User-delegated access; agent acts on behalf of users |

OAuth Identity Passthrough is the interesting one. When users need to grant an agent access to their personal data — their OneDrive, their Salesforce org, a SaaS API scoped by user — the agent acts on their behalf with standard OAuth flows. No shared system identity pretending to be everyone.

## Voice Live: speech-to-speech without the plumbing

Adding voice to an agent used to mean stitching together STT, LLM, and TTS — three services, three latency hops, three billing surfaces, all synchronized by hand. **Voice Live** collapses that into a single managed API with:

- Semantic voice activity and end-of-turn detection (understands meaning, not just silence)
- Server-side noise suppression and echo cancellation
- Barge-in support (users can interrupt mid-response)

Voice interactions go through the same agent runtime as text. Same evaluators, same traces, same cost visibility. For customer support, field service, or accessibility scenarios, this replaces what previously required a custom audio pipeline.

## Evaluations: from checkbox to continuous monitoring

This is where Foundry gets serious about production quality. The evaluation system now has three layers:

1. **Out-of-the-box evaluators** — coherence, relevance, groundedness, retrieval quality, safety. Connect to a dataset or live traffic and get scores back.

2. **Custom evaluators** — encode your own business logic, tone standards, and domain-specific compliance rules.

3. **Continuous evaluation** — Foundry samples live production traffic, runs your evaluator suite, and surfaces results through dashboards. Set Azure Monitor alerts for when groundedness drops or safety thresholds breach.

Everything publishes to Azure Monitor Application Insights. Agent quality, infrastructure health, cost, and app telemetry — all in one place.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Six new regions for hosted agents

Hosted agents are now available in East US, North Central US, Sweden Central, Southeast Asia, Japan East, and more. This matters for data residency requirements and for compressing latency when your agent runs close to its data sources.

## Why this matters for .NET developers

Even though the code samples in the GA announcement are Python-first, the underlying infrastructure is language-agnostic — and the .NET SDK for `azure-ai-projects` follows the same patterns. The Responses API, the evaluation framework, the private networking, the MCP auth — all of this is available from .NET.

If you've been waiting for AI agents to go from "cool demo" to "I can actually ship this at work," this GA release is the signal. Private networking, proper auth, continuous evaluation, and production monitoring are the pieces that were missing.

## Wrapping up

Foundry Agent Service is available now. Install the SDK, open [the portal](https://ai.azure.com), and start building. The [quickstart guide](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) takes you from zero to a running agent in minutes.

For the full technical deep-dive with all code samples, check the [GA announcement](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
