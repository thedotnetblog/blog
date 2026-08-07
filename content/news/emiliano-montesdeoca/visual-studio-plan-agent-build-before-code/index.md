---
title: "The New Plan Agent in Visual Studio Fixes a Very Real AI Workflow Problem"
date: 2026-09-08
author: "Emiliano Montesdeoca"
description: "The new Plan agent in Visual Studio matters because it creates a structured planning stage before implementation, which is exactly what bigger features and refactors often need."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

One of the more frustrating AI coding workflows is when the implementation starts too fast.

The code may even be technically fine, but it is solving the wrong version of the problem you had in mind.

You wanted a refactor. It started a rewrite.
You wanted a scoped improvement. It touched half the project.
You wanted to talk through options. It jumped straight into file changes.

That is why the new **Plan agent** in Visual Studio is such a useful addition.

## This fixes a real workflow problem, not a cosmetic one

The source post describes a very familiar situation: “**The code isn’t wrong… it just isn’t what you were going for.**”

That line is perfect.

Because the weak point in a lot of AI-assisted development is not whether the model can produce code. It is whether the workflow creates enough space to agree on the intended shape of the work before implementation begins.

That matters most for:

- larger features
- unfamiliar codebases
- non-trivial refactors
- architecture-sensitive changes
- work that needs team review before edits start

In those situations, jumping straight into implementation is often the wrong move.

## Planning is not overhead when the task is real

I think teams sometimes underestimate how much time they lose by starting implementation too early.

If the agent:

- touches the wrong files
- chooses the wrong approach
- misses a key constraint
- ignores a required edge case

then the “fast” start becomes a slower overall workflow.

That is why I like this feature.

It makes room for:

- clarifying questions
- plan drafting
- editing the plan directly
- sharing the plan before code changes happen

That is not bureaucracy. That is often just good engineering.

## The markdown plan file is a smart choice

One detail I especially like is that every plan is saved to `.copilot/plans/plan-{title}.md`.

That makes the planning step tangible.

It means the plan is not trapped inside a chat transcript. It becomes something you can:

- review
- edit
- version mentally
- discuss with teammates
- hand off into implementation more deliberately

That makes the feature feel much more serious than a temporary preamble before code generation.

## This is where AI workflows start respecting team process

I think this is one of the stronger signs that these tools are maturing.

The best AI developer workflows are not the ones that remove all intermediate steps. They are the ones that improve the right intermediate steps.

Planning is one of those steps.

If the plan is strong, implementation gets easier.
If the plan is weak, implementation gets noisy.

This feature acknowledges that directly.

## My take

This is not just an AI nicety.

It is a workflow improvement.

And for real features and refactors, it is exactly the kind of improvement that can save a lot of unnecessary churn, review noise, and “this is not what I meant” rework.

I think more agent experiences will eventually need something like this.

Visual Studio just got there sooner in a way that feels useful.

Original post: [Plan Before You Build: Introducing the Plan agent in Visual Studio](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)