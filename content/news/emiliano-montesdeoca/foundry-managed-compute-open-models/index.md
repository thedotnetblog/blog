---
title: "Foundry Managed Compute Makes Open Models a Model Deployment Problem"
description: "Foundry Managed Compute serves open-source and custom models on dedicated GPU capacity with managed runtimes, unified endpoints, monitoring, and accelerator-based billing."
date: 2026-10-09
author: "Emiliano Montesdeoca"
tags: [microsoft-foundry, azure-ai, open-source-models, managed-compute, dotnet]
slug: foundry-managed-compute-open-models
---

Original source: [Announcing Foundry Managed Compute: Run open models in Microsoft Foundry](https://devblogs.microsoft.com/foundry/announcing-foundry-managed-compute/)

Running an open model in a notebook is a model problem. Running one for production traffic is usually a GPU infrastructure problem: choose a machine, fit the weights and KV cache, operate a runtime, patch the image, expose an endpoint, and figure out why the accelerator is idle.

Foundry Managed Compute is Microsoft Foundry's answer to that second problem. It is a managed platform for customizing and serving open-source AI models on elastic GPU capacity. The source describes it as a way to combine the model catalog, suitable runtimes, and GPU capacity in one experience, without asking each team to operate virtual machines, Kubernetes, or model-serving infrastructure.

The idea is not that open models have become effortless. It is that the deployment unit can become the model rather than the machine.

## Three deployment types, one platform

Foundry now presents three broad ways to serve models:

- **Pay-per-token** for first-party models, including Azure OpenAI, where billing follows input and output tokens.
- **Provisioned throughput units** for predictable, sustained workloads on first-party models.
- **Managed Compute** for open-source and community models from the Foundry catalog on dedicated GPU capacity, billed hourly by accelerator family.

That division gives a .NET team a more coherent choice when an application mixes model types. A frontier model can handle one route, an open model can handle another, and the application can use the same Foundry endpoint and SDK surface rather than building a separate hosting path for every model family. The right choice still depends on workload, latency, data requirements, and evaluation results; a unified control surface does not make those decisions disappear.

## Choose a model, template, and accelerator family

Managed Compute removes much of the raw VM sizing exercise. The deployment choices are:

1. **Model:** Select an open-weight model from the Foundry Model Catalog and its Hugging Face collection.
2. **Deployment template:** Choose a versioned, pre-tuned asset that pins the runtime, GPU count, context length, quantization, and model-specific serving settings.
3. **Accelerator family:** Select a family such as A100 or H100 rather than reasoning directly about a particular VM SKU.

The source's example shows Qwen3-32B templates for one A100 or H100 with a 40K context, and two A100s or H100s with a 128K context. The template is more than a deployment preset. It encodes the runtime and serving tradeoffs so the team can compare an option deliberately instead of starting with a blank GPU machine.

Quota is tracked per accelerator family in the Foundry resource, separately from Azure VM quota. That is a useful change in vocabulary, but it also means capacity planning needs to move from "which ND VM can I get?" to "how many accelerators does this model and template require?"

## Scaling without throwing away the KV cache

Adding model instances increases the token capacity of a deployment. Foundry routes requests across those instances with three behaviors that matter to interactive AI applications:

- concurrency-aware load balancing spreads traffic using the number of in-flight requests;
- prompt-prefix affinity routes shared prefixes, such as system prompts, tool definitions, or RAG context, to the same instance; and
- multi-turn session affinity keeps a user's turns on the same instance when a session identifier is supplied.

These are soft affinities with load bounds. If the preferred instance is too busy, the request can spill to another instance. That is a sensible compromise: preserve cache locality when it helps, but do not turn a hot instance into a queue just to maintain affinity.

For a .NET application, the practical benefit is that cache-aware routing does not need to become another service in your architecture. You still need to measure time to first token, decode time, throughput, and tail latency with your own prompts, but the first version of the routing policy is managed by the platform.

## Operations move into Foundry

Open-model runtimes change quickly, and the security work is continuous. Managed Compute applies supported container and runtime upgrades to live deployments in the background, including CVE fixes and runtime improvements. That can remove a substantial amount of maintenance from a team that would otherwise rebuild, retest, redeploy, and drain a GPU service for every patch.

It also brings administration and observability together. Managed Compute sits beside pay-per-token and provisioned throughput in the same Foundry resource. Azure RBAC, private networking, identity, cost management, and audit controls apply at the resource level, while Azure Monitor exposes request volume, availability, latency, time-to-first-token, inter-token decode time, and token usage. Those metrics can be consumed from the portal, Log Analytics, or Grafana.

The tradeoff is automatic change. A runtime upgrade is valuable only if it remains compatible with your workload. I would keep a staging deployment, run a fixed evaluation set after template or runtime changes, and watch both quality and latency before increasing production traffic.

## Agents and the endpoint story

The source says Managed Compute deployments use the same OpenAI SDK surface and endpoint model as the other Foundry deployment types. That is a meaningful integration point for .NET services: the model-hosting choice can change without forcing a new application protocol through every call site.

Foundry Agents support is available today by adding a chat-completions Managed Compute deployment as an admin-connected model, while native integration that removes that extra step is still coming. That distinction matters. The platform is usable for agent scenarios now, but teams should follow the current connection pattern rather than assume every deployment is automatically attached to an agent.

## Cost, scope, and preview boundaries

Managed Compute bills per accelerator used by each model instance. The source gives Global Managed Compute rates of $3.95 per hour for an A100 80GB and $7.91 per hour for an H100 80GB. MI300X is listed as coming soon at $7.91 per hour. A simple estimate is:

`accelerators per instance x model instances x hours running x hourly rate`

Global Managed Compute is the broad-capacity, lower-rate option available at launch. Data Zone Managed Compute is planned for residency and sovereignty requirements at a small premium. Both scopes are intended to share the same catalog, templates, SDKs, endpoint shape, and observability surface.

The current preview supports base models from the catalog on A100 or H100 accelerators in the Global scope. Data Zone scope, MI300X, broader Bring Your Own Weights support, and IP-protected marketplace models are on the roadmap described by the source. Verify regional availability, quota, and preview terms before committing an architecture to a specific accelerator.

## My recommendation

Managed Compute is most compelling when a team already has a real open-model workload but does not want to become a GPU platform team. Deploy one representative model, run production-shaped prompts through an evaluation set, and compare quality, time to first token, sustained throughput, and full hourly cost with the alternative of operating the infrastructure yourself.

For .NET teams already using Foundry, the unified endpoint and monitoring path are the strongest parts of the announcement. The winning design is not simply "use an open model." It is choosing the right model and template while letting Foundry carry the operational burden that used to distract from the application.

Resources:

- [Microsoft Foundry](https://learn.microsoft.com/azure/foundry)
- [Hugging Face open-source models in Foundry](https://ai.azure.com/nextgen)
- [Foundry Agents and AI gateway pattern](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/ai-gateway?tabs=api-management)
- [Microsoft Build session: Hugging Face open-source models to production](https://build.microsoft.com/en-US/sessions/DEM320)
