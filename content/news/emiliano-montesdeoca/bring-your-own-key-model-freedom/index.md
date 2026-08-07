---
title: "Bring Your Own Key: Model Freedom Without Leaving VS Code"
description: "VS Code's BYOK and Language Model Chat Provider API make local, hosted, and specialized models part of the same developer workflow. The hard part is choosing well."
date: 2026-08-16
author: Emiliano Montesdeoca
tags: [model-choice, BYOK, VS Code, OpenRouter, Ollama, extensibility]
slug: bring-your-own-key-model-freedom
---

Original source: [Expanding Model Choice in VS Code with Bring Your Own Key](https://code.visualstudio.com/blogs/2025/10/22/bring-your-own-key)

# Bring Your Own Key: Model Freedom Without Leaving VS Code

For a while, AI coding tools offered a simple bargain: use the vendor's model inside the vendor's editor.

VS Code keeps pushing in the opposite direction. Bring Your Own Key lets developers connect models from providers such as OpenRouter, Ollama, Google, or OpenAI. The Language Model Chat Provider API goes one step further by letting providers ship extensions that add their models directly to the editor.

That is meaningful for .NET teams because model choice is not only about benchmark scores. It is also about data boundaries, deployment location, latency, cost, and whether the model supports the tools your workflow needs.

## BYOK Changes the Editor's Boundary

The experience is straightforward: configure a provider, add its key or endpoint, and select the model in Chat: Manage Language Models. The editor does not need to own every integration.

The source describes the direction well: "This extensible ecosystem will allow us to scale out our model choice to meet developers' needs."

That is the right abstraction. VS Code provides the interaction surface while providers own the connection to their services. A local Ollama endpoint, an Azure AI Foundry deployment, and a hosted provider can all appear in one workflow without waiting for the editor team to add a bespoke integration for every model.

The benefit is flexibility. The cost is that the user now owns more of the decision.

## The Provider API Creates a Marketplace for Models

The Language Model Chat Provider API gives a provider extension a standard way to expose models in VS Code. The basic flow is:

1. A provider implements the API.
2. The provider ships a VS Code extension.
3. A developer installs the extension.
4. The provider's models appear in the model picker.

The source calls out providers including the AI Toolkit, Cerebras Inference, and Hugging Face. The long tail matters here. Smaller providers and internal platform teams can integrate without asking the editor vendor to become an integration bottleneck.

For an enterprise, this also opens a path to an internal provider extension. Your platform team can expose approved models and hide endpoints that do not meet your data or support requirements.

## Local Models Are Useful, Not Magical

An OpenAI-compatible endpoint makes it possible to point VS Code at a local service such as Ollama. A conceptual configuration might look like this:

```toml
[models]
provider = "openai-compatible"
endpoint = "http://localhost:11434/v1"
models = ["mistral", "deepseek-coder"]
```

Local inference can be useful for sensitive experiments, offline work, and predictable development costs. It also brings a different set of constraints: model download size, memory, GPU availability, startup time, and lower capability for complex tasks.

Do not turn "local" into a synonym for "secure" without checking the rest of the path. A local model can still read a broad workspace, emit sensitive logs, or be exposed through an incorrectly configured endpoint.

## The Caveat: Choice Creates Operational Work

A large model menu can become a team-wide source of inconsistency. Two developers ask the same coding question with different models and get different code. A provider changes pricing. A model loses tool-call support. An Ollama server runs out of memory halfway through an agent task.

I would define a small model policy:

- One default model for routine coding.
- One approved local or private model for sensitive code.
- One stronger model for architecture and difficult debugging.
- A documented reason to use anything else.

Also record model identity in important evaluations. A prompt without its model and configuration is not a reproducible experiment.

## The .NET Angle: Keep the Workflow, Change the Backend

.NET teams often have different environments across projects: a cloud-hosted application with Azure OpenAI, a regulated workload that needs a private endpoint, and a developer laptop running a local model. BYOK lets the editor experience remain familiar while the inference boundary changes.

That is especially useful when building AI features with `Microsoft.Extensions.AI`, Semantic Kernel, or the Microsoft Agent Framework. The same development habits—inspect context, call tools, run tests, review output—can be exercised against more than one model provider.

But the application still needs its own provider abstraction and tests. A model choice in VS Code does not guarantee the model your production application will use.

## What I Would Do Next

1. Configure one approved hosted provider and one local OpenAI-compatible endpoint.
2. Use both on a small .NET repository with no production credentials.
3. Compare tool calling, C# code quality, test behavior, latency, and cost.
4. Document the result as a team recommendation rather than a personal preference.

BYOK is not feature bloat. It is a recognition that the model market moves faster than any one editor vendor can curate. The editor becomes more valuable when it is a good home for many models, not only the model owned by its maker.

The freedom is real. So is the responsibility to use it deliberately.