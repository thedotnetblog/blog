---
title: "Visual Studio's March Update Lets You Build Custom Copilot Agents — and the find_symbol Tool Is a Big Deal"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studio's March 2026 update ships custom Copilot agents, reusable agent skills, a language-aware find_symbol tool, and Copilot-powered profiling from Test Explorer. Here's what matters."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

Visual Studio just got its most significant Copilot update yet. Mark Downie [announced the March release](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), and the headline is custom agents — but honestly, the `find_symbol` tool buried further down might be the feature that changes your workflow the most.

Let me break down what's actually here.

## Custom Copilot agents in your repo

Want Copilot to follow your team's coding standards, run your build pipeline, or query your internal docs? Now you can build exactly that.

Custom agents are defined as `.agent.md` files that you drop into `.github/agents/` in your repository. Each agent gets full access to workspace awareness, code understanding, tools, your preferred model, and MCP connections to external services. They show up in the agent picker alongside the built-in agents.

This is the same pattern VS Code has been supporting — and it's great to see Visual Studio catch up. For teams that have already built agents for VS Code, your `.agent.md` files should work across both IDEs (though tool names can vary, so test them).

The [awesome-copilot](https://github.com/github/awesome-copilot) repo has community-contributed agent configurations you can use as starting points.

## Agent skills: reusable instruction packs

Skills are automatically picked up from `.github/skills/` in your repo or `~/.copilot/skills/` in your profile. Each skill is a `SKILL.md` file following the [Agent Skills specification](https://agentskills.io/specification).

Think of skills as modular expertise you can mix and match. You might have a skill for your API conventions, another for your testing patterns, and another for your deployment workflow. When a skill activates, it shows up in the chat so you know it's being applied.

If you've been using skills in VS Code, they work the same way in Visual Studio now.

## find_symbol: language-aware navigation for agents

This is where things get really interesting. The new `find_symbol` tool gives Copilot's agent mode actual language-service-powered symbol navigation. Instead of searching your code as text, the agent can:

- Find all references to a symbol across your project
- Access type information, declarations, and scope metadata
- Navigate call sites with full language awareness

What this means in practice: when you ask Copilot to refactor a method or update a parameter signature across call sites, it can actually see your code's structure. No more "the agent changed the method but missed three call sites" situations.

Supported languages include C#, C++, Razor, TypeScript, and anything with a supported LSP extension. For .NET developers, this is a massive improvement — C# codebases with deep type hierarchies and interfaces benefit enormously from symbol-aware navigation.

## Profile tests with Copilot

There's now a **Profile with Copilot** command in the Test Explorer context menu. Select a test, click profile, and the Profiling Agent automatically runs it and analyzes performance — combining CPU usage and instrumentation data to deliver actionable insights.

No more manually configuring profiler sessions, running the test, exporting results, and trying to read a flame graph. The agent does the analysis and tells you what's slow and why. Currently .NET only, which makes sense given Visual Studio's deep .NET diagnostics integration.

## Perf tips during live debugging

Performance optimization now happens while you debug, not after. As you step through code, Visual Studio shows execution time and performance signals inline. See a slow line? Click the Perf Tip and ask Copilot for optimization suggestions right there.

The Profiling Agent captures runtime data automatically — elapsed time, CPU usage, memory behavior — and Copilot uses it to pinpoint hot spots. This keeps performance work as part of your debugging flow instead of a separate task you keep postponing.

## Fix NuGet vulnerabilities from Solution Explorer

When a vulnerability is detected in a NuGet package, you now see a notification with a **Fix with GitHub Copilot** link directly in Solution Explorer. Click through and Copilot analyzes the vulnerability, recommends the right package updates, and implements them.

For teams that struggle to keep dependencies up to date (which is basically everyone), this removes the friction of "I know there's a vulnerability but figuring out the right update path is a project in itself."

## Wrapping up

Custom agents and skills are the headline, but `find_symbol` is the sleeper hit — it fundamentally changes how accurate Copilot can be when refactoring .NET code. Combined with live profiling integration and vulnerability fixes, this update makes Visual Studio's AI features feel genuinely practical rather than demo-ready.

Download [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) to try it all out.
