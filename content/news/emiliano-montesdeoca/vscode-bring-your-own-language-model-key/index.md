---
title: "Bring your own language model key to VS Code"
description: "VS Code BYOK lets developers add provider-backed or local language models to the Chat model picker, with direct provider billing and no GitHub sign-in required for BYOK chat workflows."
date: 2026-11-08
author: "Emiliano Montesdeoca"
tags: ["Visual Studio Code", "AI", "Language Models", "Developer Tools", "Copilot"]
slug: vscode-bring-your-own-language-model-key
---

Original source: [Use your own language model key in VS Code](https://code.visualstudio.com/blogs/2026/06/18/byok-vscode)

The model picker in VS Code does not have to be limited to the models bundled with a Copilot plan. Bring your own language model key, or **BYOK**, lets developers add models from supported providers and use local models directly from VS Code Chat.

That flexibility is useful for different reasons. A team may already have provider billing and governance, a developer may need a model that is not built into VS Code, or a project may require an offline local model. BYOK puts those choices in the same Chat model picker while keeping the boundaries between Copilot features and provider-backed chat explicit.

## What BYOK adds

VS Code supports models from providers such as Azure, Anthropic, Hugging Face, Gemini, OpenAI, and OpenRouter. It also supports local options including Ollama and Foundry Local, among others. A provider can contribute support through an extension, so the list can grow without every provider being hard-coded into the editor.

After you configure a provider, its models appear in the Chat model picker. That makes it possible to choose different models for different jobs: a fast model for a short question, a reasoning model for planning or debugging, or a local model for an offline experiment.

The selected model must support the capabilities required by the workflow. BYOK models are available for VS Code Chat, including agent workflows when the model supports those capabilities. They are not a universal replacement for every AI feature in the editor.

## Important boundaries

BYOK models can work without signing into a GitHub account and without a Copilot plan. Local models can support fully offline scenarios. Usage for provider-backed models is billed directly by that provider and does not count against GitHub Copilot request quotas.

There are limits to that independence:

- BYOK applies to Chat and utility tasks, not standard code completions.
- Semantic search, inline suggestions, and features that rely on embeddings may still require a GitHub account or Copilot support.
- For Copilot Business and Enterprise, administrators can control BYOK availability through Copilot policy settings.

This distinction is important for teams that want to change model billing without accidentally assuming that every editor feature follows the same route. A local model can handle a chat task while inline suggestions or embedding-backed features continue to depend on their existing services.

## Configure a provider

The easiest entry point is the **Language Models** editor. Open the Chat model picker, select the **Manage Language Models** gear icon, or run **Chat: Manage Language Models** from the Command Palette.

For a built-in provider, the flow is straightforward:

1. Open **Chat: Manage Language Models**.
2. Select **Add Models**.
3. Choose a provider.
4. Enter the group name shown in the model picker.
5. Provide the required API key, endpoint, deployment name, or other provider details.
6. Select the configured model from the Chat model picker.

Depending on the provider, VS Code may open `chatLanguageModels.json` for the remaining configuration. The source gives a Mistral example with an endpoint, API type, model capabilities, and a placeholder API key. Store real credentials through the configuration mechanism and secret-management practices appropriate for the development environment; do not commit keys to a repository.

Provider extensions use a similar flow. Search the Extensions view for `@tag:language-models`, install the provider extension, follow its setup instructions, and then select its model from the picker.

## Utility models matter too

VS Code uses lightweight models for background tasks such as chat titles, commit messages, and rename suggestions. These utility tasks default to built-in Copilot models. When using BYOK without a GitHub account, those defaults are unavailable, and Chat prompts you to configure replacements.

The relevant settings are `chat.utilityModel` and `chat.utilitySmallModel`. Point them to BYOK models to keep those features working. A fast, inexpensive model is usually a better fit for a title or rename suggestion than a large reasoning model.

## A useful model strategy for .NET work

1. Use a fast model for short API questions, summaries, and small edits.
2. Choose a reasoning-capable model for planning, debugging, and complex refactors.
3. Use a local model for experiments that must stay offline.
4. Keep utility tasks on a small model so background work does not consume an unnecessarily expensive provider.
5. Check provider billing and organization policy before standardizing the setup across a team.

BYOK makes model choice a practical part of the VS Code workflow, but choice works best with clear boundaries. The Chat picker can become one place for Copilot, provider-backed, extension-contributed, and local models without pretending that their billing, authentication, and editor capabilities are identical.