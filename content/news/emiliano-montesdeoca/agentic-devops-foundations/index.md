---
title: "Agentic DevOps Foundations: Four Agent Types and When to Use Them"
description: "A practical introduction to local, CLI, cloud, and third-party agents, with guidance for .NET teams choosing execution models and building reusable agent workflows."
date: 2026-09-02
author: "Emiliano Montesdeoca"
tags: [devops, agents, foundations, architecture]
slug: agentic-devops-foundations
---

Original source: [Getting Started with Agentic DevOps - Part 1: Foundations](https://devblogs.microsoft.com/all-things-azure/getting-started-with-agentic-devops-part-1-foundations/)

Agentic DevOps is a way to use AI-powered agents across the software development lifecycle. The important distinction is between asking for assistance and delegating work. Chat is usually synchronous and guided turn by turn. An agent can take on a task end to end, collaborate across tools, and return a durable result within the boundaries a team defines.

For .NET developers starting out, the first practical decision is not which model to pick. It is where the agent should run and how much supervision the task needs.

## Four Agent Types

The source introduces local, CLI, cloud, and third-party agents.

Local agents operate inside VS Code and are suited to synchronous, interactive work. Use them for a refactoring, test generation, code review, or exploratory change where you want to see progress and redirect the work immediately. This is the natural starting point for a .NET developer who wants to learn how an agent reads a solution, runs `dotnet` commands, and applies edits.

CLI agents run in terminal environments such as Copilot CLI. They fit scripts, automation, and CI/CD because they do not require an open editor. A team can use a CLI agent in a pipeline for a bounded review or local build workflow, provided the pipeline controls its permissions and records the result.

Cloud agents run asynchronously in hosted environments. They are a better fit for long-running work, scheduled analysis, or batch changes that do not need a developer watching every step. A nightly dependency review or a large mechanical migration may benefit from this model, especially when the work can be isolated and verified when it returns.

Third-party agents are hosted by external providers or platforms. They can be useful when a specialized workflow lives outside the editor, but the team needs to understand the provider's data, identity, tool, and audit boundaries before connecting it to a repository.

## Synchronous and Asynchronous Work

The execution model should follow the shape of the task. Synchronous local work is valuable when a developer needs to steer the agent, inspect an intermediate assumption, or decide between alternatives. Asynchronous cloud work is useful when a task takes a long time and has a clear completion condition.

Do not force a thirty-minute batch operation into an interactive session simply because the local agent is convenient. Conversely, do not send an uncertain architectural question to a background agent when the cost of a wrong direction is high and the developer needs to collaborate in real time.

Before delegating, write down the expected output and the checks that establish completion. "Review the API" is broad. "Inspect the authentication endpoints, list findings with file references, and do not edit files" is a bounded assignment.

## Customization Makes Patterns Transferable

Instructions, MCP servers, and skills give agents the context needed to work with a repository's conventions. A `.instructions.md` file or `.github/copilot-instructions.md` can document the same rules a senior engineer would explain during onboarding.

For a .NET team, start with patterns that affect every change: approved NuGet packages, async and cancellation conventions, dependency injection setup, test framework and naming, error handling, logging, and project organization. Keep the rules concrete enough to verify. "Write good tests" is less useful than naming the required integration test or command.

The repository should be the durable source of truth. Chat memory can help an individual session, but instructions and tests are what make behavior consistent across local, CLI, and cloud agents.

## Subagents Add Specialization

A general-purpose agent can handle many tasks, but focused subagents can provide better results for a specific domain. A .NET workflow might use a migration subagent for framework compatibility, a security subagent for dependency and input validation review, a performance subagent for async behavior, and a test subagent for a difficult business rule.

Composition only helps when each role has a clear contract. Define the input, output, permission boundary, and handoff between subagents. A security reviewer should return evidence and severity rather than silently rewriting production code. A migration agent should state which files it changed and which compatibility assumptions remain.

Start with one specialized subagent and a human review step. Add orchestration only after the single-agent workflow is predictable.

## A Three-Part Learning Path

The source is the first post in a three-part series. The next part covers context engineering, MCP servers, and multi-agent orchestration. The final part covers application modernization for Java, .NET, PHP, and microservices.

That sequence is sensible. First choose the execution model and make repository patterns explicit. Then add the context and tool interfaces that make an agent effective. Only after that should a team automate a chain of specialized agents.

## What .NET Teams Should Do Now

1. Classify current work as interactive, scripted, scheduled, or externally hosted.
2. Start with a local agent on a small, reversible task.
3. Document package, testing, DI, async, logging, and error-handling conventions.
4. Pick one bounded CI or review task for a CLI agent experiment.
5. Define a completion signal and validation command for every delegated task.

Agentic DevOps foundations are mostly about choosing the right execution boundary and making expectations explicit. Once those are in place, agents become easier to evaluate, compare, and use without turning every workflow into an experiment.