---
title: "Model Router Evals Are the Step Too Many Teams Skip"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "The new Foundry model router evaluation repo matters because routing decisions need to be measured against quality, latency, and cost before teams treat automatic model selection as magic."
tags:
  - Microsoft Foundry
  - AI
  - Evaluations
  - Model Router
  - Cost Optimization
---

Automatic model routing sounds great right up until you realize you still have to prove it is the right choice for your workload.

That is why the new **model router evaluation repo** is useful.

It gives teams a more concrete way to answer the questions that actually matter:

- does routing preserve quality?
- does it improve cost?
- what does it do to latency?
- what changes if I restrict the model subset?

## The source article asks the right questions

One thing I really like about the original post is that it does not treat the model router as self-evidently good.

Instead, it asks the uncomfortable but correct questions:

- “**On my prompts, does the model router’s auto-selected model match or beat the single model I’d otherwise pick?**”
- “**Am I actually saving money end-to-end, or just shifting spend around?**”

That is exactly the right attitude.

Because automatic routing is attractive, but it is still a systems decision. And systems decisions should be measured, not admired.

## Why this repo matters more than it first sounds

At one level, this is just an evaluation repo.

At another level, it is a sign of maturity.

It says: if you want to adopt automatic routing, here is a more disciplined way to test:

- quality
- cost
- latency
- subset trade-offs
- model distribution behavior

That is much better than treating routing as a black box with good branding.

## My take

This is a good example of the kind of tooling AI platforms need more of: not more magic, but more ways to validate the magic before you trust it.

That is how teams avoid building expensive confidence on top of untested assumptions.

Original post: [How to run evals for the model router](https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/)