---
title: "Improving token efficiency for GitHub Copilot in VS Code"
description: "VS Code documents agent-harness efficiency improvements for GitHub Copilot, including longer OpenAI prompt caching, deferred tool loading, WebSockets, and embedding-guided local tool search."
date: 2026-11-06
author: "Emiliano Montesdeoca"
tags: ["GitHub Copilot", "Visual Studio Code", "AI", "Token Efficiency", "Cost Optimization"]
slug: vscode-copilot-token-efficiency
---

Original source: [Improving token efficiency for GitHub Copilot in VS Code](https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot)

With usage-based billing for GitHub Copilot, every token in an agentic session affects credits, latency, and the context available for the task. The Visual Studio Code team describes a series of harness-level improvements that reduce repeated work while preserving task success through production A/B experiments and offline evaluations.

The common problem is repetition. System instructions, tool definitions, repository context, and conversation history can appear again and again across turns. The recent work focuses on keeping reusable prompt state warm and avoiding the cost of loading every possible tool into every request.

## Two recurring costs in an agentic request

The first cost is the **prompt prefix**. When requests share the same prefix, an inference provider can reuse the model state computed for that prefix instead of processing it from scratch. Cached tokens can be up to 10 times cheaper, so keeping the prefix stable and the cache hit rate high affects both cost and latency.

The second cost is **tool-definition overhead**. MCP servers, built-in tools, and extensions can expose a large catalog. Each tool historically arrived with a name, description, and complete JSON parameter schema on every request. Tool search changes that pattern: the model sees lightweight metadata first and loads the heavier definition only when it searches for that tool.

Deferred tools are added outside the cached prompt prefix. That preserves the reusable portion of the request while leaving more context and budget for the actual coding task.

## OpenAI model improvements

The VS Code team describes three changes for OpenAI models.

### Extended prompt caching

OpenAI prompt caching normally keeps model state in fast GPU memory for roughly 5 to 10 minutes of inactivity, with some cases lasting longer. VS Code enabled the `prompt_cache_retention` body parameter with a value of `24h` for supported models, moving the cache to roomier GPU-local storage for longer retention.

The measured benefit depends on the gap between requests. In the reported table, relative cache hit-rate increases range from about 10% to 32% after a 10 to 20 minute gap, and from 279% to 919% after a 40 to 60 minute gap across GPT-5.2, GPT-5.3-Codex, and GPT-5.4. These are relative changes, not percentage-point increases. A 919% increase means the hit rate was 10.19 times its previous value.

### Tool search

OpenAI’s native tool search is available for GPT-5.4 and newer and uses deferred loading. In a four-day VS Code experiment with GPT-5.4 and GPT-5.5, median total tokens per turn fell by 9.81% and 8.61%, respectively. Median time to first token fell by 6.88% and 7.34%, while time to complete fell by 5.31% and 5.42%.

Across an entire session, total token usage for the median Copilot user decreased by 8.97% with GPT-5.4 and 10.92% with GPT-5.5 in that experiment.

### WebSockets

Agentic turns often involve several sequential requests while the model calls tools. Responses API WebSocket mode keeps a persistent connection and lets OpenAI reuse connection-local response state. During the initial VS Code Stable rollout, the source reports relative TTFT reductions of roughly 12% to 19% and time-to-complete reductions of roughly 6% to 14%, depending on model and percentile.

The improvements led WebSockets to become the default transport for OpenAI models GPT-5.2 and newer across Copilot products, including VS Code.

## Anthropic model improvements

Anthropic prompt caching uses explicit `cache_control` breakpoints. The VS Code team reworked the placement of up to four breakpoints around the end of tool definitions, the end of the system prompt, and two rolling anchors for recent messages. For agentic workloads, the resulting cache hit rate sits around 94%.

Anthropic tool search first deferred tool definitions through server-side search, then moved the search client-side. The local search uses an internal Copilot embedding model to compare the request with vector representations of available tools. That means a request such as “find all references to this symbol” can surface the right tool even when the tool name does not share literal words with the request.

In a seven-day experiment, server-side tool search reduced median per-turn prompt tokens by 11.30% and median per-user prompt tokens by 18.32%. Median total tokens fell by 11.09% per turn and 18.03% per user. In a two-week VS Code Stable rollout, client-side search added latency improvements of about 1.3% to 3.35% for the reported Claude percentiles and reduced the Claude Sonnet 4.6 user error rate by 4.01%.

Client-side search also responds locally against cached embeddings, reflects MCP tools added or removed during a session, and improves the chance that the relevant tool is found. Once discovered, a tool remains available for the rest of the conversation.

## What this means for .NET teams

1. **Long pauses are less expensive for supported OpenAI models.** Extended retention can preserve reusable prompt state after a break, subject to model and cache availability.
2. **Large tool catalogs are less disruptive.** Deferred loading keeps unused schemas out of the active context until they are needed.
3. **Measurements show meaningful reductions.** The reported experiments show roughly 8% to 18% token reductions in several OpenAI and Anthropic scopes, not a universal guarantee for every task.
4. **Transport affects long tool chains.** WebSockets reduce repeated continuation overhead for supported OpenAI models.
5. **The work is continuing.** The team is exploring specialized subagents for narrow tasks such as workspace search, command execution, and summarization, using smaller models where appropriate.

Token efficiency is infrastructure for agent-assisted development. The improvements in this release are not one dramatic feature; they are a collection of changes that leave more of the context window and usage budget available for the .NET work that the developer actually asked Copilot to do.