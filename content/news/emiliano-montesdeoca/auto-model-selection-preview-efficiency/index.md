---
title: "Auto Model Selection in VS Code: Smart Cost Optimization for Coding Agents"
description: "Auto-selects the best model based on capacity and performance. Capacity-aware routing, fallback, and transparent request costs change how teams operate coding agents."
date: 2026-08-15
author: Emiliano Montesdeoca
tags: [GitHub Copilot, cost-optimization, capacity, preview, model-selection]
slug: auto-model-selection-preview-efficiency
---

Original source: [Introducing auto model selection (preview)](https://code.visualstudio.com/blogs/2025/09/15/autoModelSelection)

# Auto Model Selection in VS Code: Smart Cost Optimization for Coding Agents

When you have access to multiple language models, which one do you choose for each request?

Most users pick a favorite and stick with it. That is understandable, but it is rarely optimal. Some requests need deep reasoning. Others need a quick edit. Capacity changes during the day, and model costs are not identical.

GitHub Copilot's auto model selection is designed to make that decision for you. It chooses a model based on capacity, performance, and cost, while showing which model handled the request and what multiplier applied.

That is less glamorous than announcing another model, but it may have a larger effect on daily developer experience.

## Capacity Is Part of the Developer Experience

The feature watches which models are available and avoids sending every request to a single overloaded endpoint. If one model is near capacity, another can handle the request instead.

The source describes the goal clearly: "Auto selects the best model to ensure that you get the optimal performance and reduce the likelihood of rate limits."

That matters for coding agents because a request is often part of a longer loop. A failed or delayed model call can leave an agent waiting while a developer tries to understand whether the problem is the prompt, the tool, or service capacity. Capacity-aware routing removes one source of noise.

The trade-off is that model choice becomes a system decision instead of a personal habit. For routine work, that is probably a good trade.

## Cost Transparency Makes Automation Trustworthy

Auto selection is much easier to accept when the cost is visible. The experience shows which model powered the response and the multiplier applied to it. That lets a developer or team understand what happened instead of guessing.

The source describes paid users receiving a discount when auto selects a model, while zero-cost models can provide a fallback path when premium requests are exhausted. The exact economics depend on the subscription and model, so teams should treat the UI and Copilot usage reports as the source of truth rather than hard-coding assumptions.

The important design principle is broader: automated routing must be observable. If the system picks a model on your behalf, it should tell you what it picked.

For an organization, I would track at least:

- Which models are selected most often.
- How often requests fall back to a lower-cost model.
- Whether latency or rework changes by model.
- Whether premium usage falls without reducing developer confidence.

## Fallback Keeps Agents Moving

A coding agent is sensitive to interruptions. If a model is unavailable or a user reaches a premium request limit, the task can stall at exactly the wrong moment.

Auto selection provides a fallback path. A request can continue with a model in a different cost tier instead of failing immediately. That does not mean every model is interchangeable. A small model may be perfectly adequate for a rename and a poor choice for a cross-project refactor.

This is where good agent design still matters. Make tasks small enough that a fallback model can make progress, and keep architectural decisions behind explicit review.

## The Caveat: Predictability Versus Optimization

The obvious downside is loss of predictability. If a task depends on a specific model's behavior, auto selection may not be the right default. Model capabilities, tool support, and response style vary.

Keep manual selection for work where you have a reason to control the model: a difficult design review, a benchmark, or a reproducibility investigation. Use auto for the broad middle of daily development and compare the results.

A sensible team policy is not "always use auto". It is "use auto by default, and make exceptions explicit."

## What I Would Try in a .NET Team

I would run a small experiment across three task types:

```text
1. Rename and test a small API behavior.
2. Implement a bounded ASP.NET Core endpoint.
3. Review a cross-project architecture change.
```

Use auto for the first two. Keep a selected model for the third. Record latency, number of revisions, test results, and developer confidence. That produces a better decision than arguing about model names in the abstract.

## My Take

Auto model selection is infrastructure disguised as a convenience feature. Global inference capacity is finite, and routing requests intelligently helps both the service and the developer.

The feature earns trust when it stays visible: show the chosen model, expose the cost multiplier, and let developers override the decision when the task warrants it.

For most .NET teams, I would enable auto for everyday coding assistance and reserve manual selection for deliberate experiments and high-context design work. Let the system optimize the routine, but keep engineering judgment in charge of the important decisions.