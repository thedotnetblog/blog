---
title: "How VS Code Builds with AI: Lessons from Weekly Releases"
description: "The VS Code team's AI-assisted development workflow offers practical lessons in parallel work, issue triage, automated validation, and human judgment."
date: 2026-08-27
author: "Emiliano Montesdeoca"
tags: [vscode, ai-workflow, team-practices, developer-velocity]
slug: vscode-builds-with-ai
---

# How VS Code Builds with AI: Lessons from Weekly Releases

Original source: [How VS Code Builds with AI](https://code.visualstudio.com/blogs/2026/03/13/how-VS-Code-Builds-with-AI)

The VS Code team moved from monthly to weekly releases, and the interesting lesson is not simply that agents write code quickly. The team uses them across triage, review, release notes, validation, and task management, while keeping human judgment at the points where product and architecture matter.

That is a useful pattern for .NET teams because it puts the focus on the system around the model. Faster generation without better validation only produces faster regressions.

## Parallelize the Work Around Interruptions

A developer who is about to enter a meeting can start several bounded agent sessions: investigate a failing test, inspect a deprecated API, draft a pull request description, or prototype a small change. Those tasks can run in separate sessions, worktrees, or cloud environments while the developer is unavailable.

The key is to prepare the tasks before starting them. Each session needs a target, an expected output, and a boundary on what it may change. When the developer returns, the results are ready for review rather than still waiting for a first command.

For a .NET team, this could mean delegating an inventory of obsolete package references, a scan of missing API tests, and a review of a build failure in parallel. The agents do not need to agree; the human can compare evidence once the work is collected.

## Automate the Overhead That Follows Speed

More commits and issues create more administrative work. The VS Code workflow uses agents to summarize commits, triage issues, detect likely duplicates, suggest ownership, and draft release information.

The lesson is to automate work where the input is plentiful and the decision can remain reviewable. A triage suggestion is useful when it includes its confidence and evidence. A generated release note is useful when a maintainer can edit it before publishing.

.NET teams can apply the same pattern to areas such as ASP.NET, Entity Framework, MAUI, or Azure Functions. Let an agent collect signals and prepare a first pass. Keep final ownership, labels, and release wording under human control.

## Replace Some Documents with Working Prototypes

The source describes a workflow where an issue or product idea can become a working pull request prototype. That shortens the loop between feedback and something concrete that engineers can run.

A prototype is not automatically an accepted design. It is a more informative conversation starter than a document that has never been tested. Engineers still need to challenge the architecture, inspect the diff, and reject a change that does not fit the product.

This is also a test of whether a repository is agent-ready. Can the agent find the relevant components? Can it run the right checks? Can another developer understand the generated pull request? If not, the missing structure or documentation is useful feedback for the team.

## Validation Is the Harness

The team's workflow emphasizes automated validation, browser-based checks, golden scenarios, and code review. That is the part worth copying first.

For a .NET application, golden scenarios can describe the behavior that must remain stable: creating a database context, authenticating an API request, scaffolding a MAUI screen, or deploying a function with the expected settings. Agents can run those scenarios after changes, while human reviewers decide whether the change fits the product and long-term architecture.

Automated review should be treated as an additional signal. It can catch a missed null check or a suspicious dependency change, but it does not replace a reviewer who understands why the system exists.

## What Makes a Codebase Ready

Good structure, clear documentation, ownership information, and tests give agents something reliable to work with. Without those foundations, an agent may still produce code, but the team spends its time correcting context and assumptions.

Start by making the repository easier for humans. Add a short contribution guide, make build and test commands reproducible, document service boundaries, and record architectural decisions. Those improvements help agents because they help every developer.

Then introduce parallel sessions and automate one administrative task. Measure recovery time, review effort, and regression rate. The goal is not to maximize agent activity. It is to ship useful changes sooner while keeping the quality bar intact.

The VS Code team's weekly cadence is a reminder that AI-assisted development is a workflow design problem. Agents can accelerate the loop, but tests, ownership, and human taste determine whether the loop is worth running.