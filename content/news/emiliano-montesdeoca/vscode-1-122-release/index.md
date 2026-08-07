---
title: "VS Code 1.122: Remote Agent Tasks, Model Management, and Better Issue Reporting"
description: "The May 2026 release adds remote task triggers for agents, granular language-model management, changed-file search, and a richer issue reporter."
date: 2026-09-15
author: "Emiliano Montesdeoca"
tags: [visual-studio-code, release, ai-agents, developer-tools]
slug: vscode-1-122-release
---

Original source: [Visual Studio Code 1.122](https://code.visualstudio.com/updates/v1_122)

VS Code 1.122 is a compact release, but several changes improve the agent loop around a real .NET repository. Agents can trigger tasks on remote machines, source control state refreshes after Git operations, model configuration is easier to manage, and issue reports can include richer evidence.

The release is less about one dramatic feature than about removing the handoffs that make agent-assisted development feel unfinished.

## Remote Tasks Put the Build Where the Work Is

Agents can now trigger tasks on remote machines. That matters for developers working through remote development environments or against a machine with the CPU, network, or service access that a local laptop does not have.

For a .NET solution, the useful task might be a full `dotnet build`, a targeted `dotnet test`, an integration test that needs a private network, or a custom analyzer. Define the task explicitly in the repository and make its output understandable to the agent. Remote execution does not remove the need to inspect what the task is allowed to access.

This is a good place to separate fast feedback from expensive validation. Let an agent run a focused test while iterating, then use a broader remote task when the change is ready for review. Make the environment and data boundary clear so a task intended for a test machine cannot accidentally target production resources.

The Agents window also refreshes source control state after an agent commits, syncs, or performs other Git operations. That small change closes a common feedback gap: the editor should show the repository state that the agent just created.

## Better Model Management

The Language Models editor now exposes granular actions for provider groups, including Update API Key, Add Model, Go to config file, Rename, and Delete. These actions are useful when a team works with multiple providers, Azure-hosted models, local models, or different configurations for different tasks.

Use names that communicate purpose rather than vendor defaults. A model configuration used for a fast test-writing pass should be distinguishable from one used for a long architectural review. Keep API-key rotation separate from model selection, and review the configuration file when a model behaves differently than expected.

The `/models` command opens the model picker directly from chat. That makes comparison easier, but comparison still needs a stable task and a review criterion. A model that produces a plausible answer quickly is not necessarily the model that makes the smallest correct change in a multi-project .NET solution.

## Issue Reports With Better Evidence

The new issue reporter wizard can create issues directly from VS Code and include screenshots or video recordings. Enable it with:

```json
"issueReporter.wizard.enabled": true
```

For an extension issue such as a C# Dev Kit or REST Client problem, a recording can communicate a race condition or a UI state that is difficult to describe in prose. The best report still includes a minimal reproduction, expected behavior, actual behavior, and the relevant logs. Evidence is most useful when it helps another developer reproduce the same failure.

Treat recordings as potentially sensitive. Review what is visible in the editor, terminal, and browser before submitting an issue, especially when the workspace contains customer names, endpoints, or credentials.

## Small Changes With Practical Payoff

Mermaid C4 diagrams with inline data-URI images now render correctly in chat and Markdown preview. Mermaid diagrams also use a theme derived from the current VS Code color theme, and diagrams opened in a new editor show their full content. For .NET teams documenting services and dependencies in Markdown, these changes make architecture notes easier to read without changing the source format.

The search panel adds a toggle to search only in changed files. During a large refactor, that narrows attention to the files a developer has actually modified. It is a useful review aid, not proof that unchanged files are unaffected.

Terminal commands running in chat show dot or ASCII loading animations, which gives a clearer signal that a command is still active. BYOK models can work in air-gapped scenarios without GitHub authentication, and local agent hosting is enabled by default in Insiders builds. The release also avoids showing import actions that tsgo handles differently and fixes remote-agent changed-file labels that previously displayed internal URIs.

## What .NET Developers Should Do

1. Define remote tasks for repeatable builds and tests, with explicit environment boundaries.
2. Keep model configurations named, reviewable, and easy to rotate.
3. Use `/models` to compare stable tasks rather than vague impressions.
4. Add reproduction steps and scrub sensitive content before submitting recordings.
5. Use changed-file search as a focused review aid during refactors.

VS Code 1.122 improves the infrastructure around agent work. The result is a smoother loop: run the right task where the resources are, see Git state update, choose a model deliberately, and report failures with evidence another engineer can use.