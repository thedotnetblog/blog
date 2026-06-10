---
title: "FIDES Is the Kind of Deterministic Agent Security Story I Want to See More Of"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "The new FIDES capabilities in Agent Framework matter because they move prompt injection defense away from heuristics and toward enforceable policy based on labeled content and middleware checks."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

Prompt injection defenses often feel like they live on shaky ground.

You add a stronger system prompt. You add a filter. You add some allowlists. You hope the next weird input does not break the assumptions.

That is why **FIDES** is interesting.

The strong part of the story is that it moves security toward something more deterministic:

- labels on content
- propagation through the workflow
- middleware enforcement before privileged tools run
- clear policy boundaries around what untrusted context can influence

## The source article is blunt in the right way

It opens by saying prompt injection is “**the #1 risk on the OWASP LLM Top 10**.”

Good.

I actually like that kind of blunt framing here, because too many teams still treat agent security as if it were a future concern instead of a present runtime design problem.

And the article follows that with a strong practical contrast: most current defenses are heuristic, while FIDES is trying to move the system toward policy and enforcement.

That is exactly the right shift.

## What makes this more compelling than another security whitepaper

A lot of AI security writing stays abstract.

This post does something better. It walks through a very concrete example: a GitHub issue triage agent, a malicious issue body, a privileged file read, and an attempted public comment leak.

That is useful because it grounds the whole discussion in an actual workflow.

And once you see that scenario, the value of deterministic controls becomes much easier to understand.

## The key idea is not “make the model smarter”

The most important thing here is that FIDES is not asking the model to magically become better at spotting attacks.

It is changing the runtime contract.

That means:

- content gets labeled
- labels propagate
- tools declare what they accept
- middleware blocks unsafe paths before execution

That is a much healthier approach.

Because once the agent can call tools with real consequences, security cannot depend purely on whether the model had a good day.

## My take

This is exactly the kind of agent security direction I want to see more often.

Not “trust the model to ignore bad instructions,” but “build the policy fence into the runtime.”

That is a much healthier model.

And if agent frameworks want to be taken seriously for production use, more of them will need stories like this.

Original post: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)