---
title: "Where Should You Host Your AI Agents on Azure? A Practical Decision Guide"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure offers six ways to host AI agents — from raw containers to fully managed Foundry Hosted Agents. Here's how to pick the right one for your .NET workload."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

If you're building AI agents with .NET right now, you've probably noticed something: there are a *lot* of ways to host them on Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — and they all sound reasonable until you actually need to pick one. Microsoft just published a [comprehensive guide to Azure AI agent hosting](https://devblogs.microsoft.com/all-things-azure/hostedagent/) that clears this up, and I want to break it down from a practical .NET developer perspective.

## The six options at a glance

Here's how I'd summarize the landscape:

| Option | Best for | You manage |
|--------|----------|------------|
| **Container Apps** | Full container control without K8s complexity | Observability, state, lifecycle |
| **AKS** | Enterprise compliance, multi-cluster, custom networking | Everything (that's the point) |
| **Azure Functions** | Event-driven, short-running agent tasks | Not much — true serverless |
| **App Service** | Simple HTTP agents, predictable traffic | Deployment, scaling config |
| **Foundry Agents** | Code-optional agents via portal/SDK | Almost nothing |
| **Foundry Hosted Agents** | Custom framework agents with managed infra | Your agent code only |

The first four are general-purpose compute — you *can* run agents on them, but they weren't designed for it. The last two are agent-native: they understand conversations, tool calls, and agent lifecycles as first-class concepts.

## Foundry Hosted Agents — the sweet spot for .NET agent developers

Here's what caught my attention. Foundry Hosted Agents sit right in the middle: you get the flexibility of running your own code (Semantic Kernel, Agent Framework, LangGraph — whatever) but the platform handles infrastructure, observability, and conversation management.

The key piece is the **Hosting Adapter** — a thin abstraction layer that bridges your agent framework to the Foundry platform. For Microsoft Agent Framework, it looks like this:

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

That's your entire hosting story. The adapter handles protocol translation, streaming via server-sent events, conversation history, and OpenTelemetry tracing — all automatically. No custom middleware, no manual plumbing.

## Deploying is genuinely simple

I've deployed agents to Container Apps before and it works, but you end up writing a lot of glue code for state management and observability. With Hosted Agents and `azd`, the deployment is:

```bash
# Install the AI agent extension
azd ext install azure.ai.agents

# Init from a template
azd ai agent init

# Build, push, deploy — done
azd up
```

That single `azd up` builds your container, pushes it to ACR, provisions the Foundry project, deploys model endpoints, and starts your agent. Five steps collapsed into one command.

## Built-in conversation management

This is the part that saves the most time in production. Instead of building your own conversation state store, Hosted Agents handle it natively:

```python
# Create a persistent conversation
conversation = openai_client.conversations.create()

# First turn
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Second turn — context is preserved
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

No Redis. No Cosmos DB session store. No custom middleware for message serialization. The platform just handles it.

## My decision framework

After going through all six options, here's my quick mental model:

1. **Do you need zero infrastructure?** → Foundry Agents (portal/SDK, no containers)
2. **Do you have custom agent code but want managed hosting?** → Foundry Hosted Agents
3. **Do you need event-driven, short-lived agent tasks?** → Azure Functions
4. **Do you need maximum container control without K8s?** → Container Apps
5. **Do you need strict compliance and multi-cluster?** → AKS
6. **Do you have a simple HTTP agent with predictable traffic?** → App Service

For most .NET developers building with Semantic Kernel or Microsoft Agent Framework, Hosted Agents is likely the right starting point. You get scale-to-zero, built-in OpenTelemetry, conversation management, and framework flexibility — without managing Kubernetes or wiring up your own observability stack.

## Wrapping up

The agent hosting landscape on Azure is maturing fast. If you're starting a new AI agent project today, I'd seriously consider Foundry Hosted Agents before reaching for Container Apps or AKS out of habit. The managed infrastructure saves real time, and the hosting adapter pattern lets you keep your framework choice.

Check out the [full guide from Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) and the [Foundry Samples repo](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) for working examples.
