---
title: "GitHub Copilot's Modernization Assessment Is the Best Migration Tool You're Not Using Yet"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "GitHub Copilot's modernization extension doesn't just suggest code changes — it produces a full migration assessment with actionable issues, Azure target comparisons, and a collaborative workflow. Here's why the assessment document is the key to everything."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

Migrating a legacy .NET Framework app to modern .NET is one of those tasks everyone knows they should do but nobody wants to start. It's never just "change the target framework." It's APIs that disappeared, packages that don't exist anymore, hosting models that work completely differently, and a million small decisions about what to containerize, what to rewrite, and what to leave alone.

Jeffrey Fritz just published a [deep dive into GitHub Copilot's modernization assessment](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/), and honestly? This is the best migration tooling I've seen for .NET. Not because of the code generation — that's table stakes now. Because of the assessment document it produces.

## It's not just a code suggestion engine

The VS Code extension follows an **Assess → Plan → Execute** model. The assessment phase analyzes your entire codebase and produces a structured document that captures everything: what needs to change, what Azure resources to provision, what deployment model to use. Everything downstream — infrastructure-as-code, containerization, deployment manifests — flows from what the assessment finds.

The assessment is stored under `.github/modernize/assessment/` in your project. Each run produces an independent report, so you build up a history and can track how your migration posture evolves as you fix issues.

## Two ways to start

**Recommended Assessment** — the fast path. Pick from curated domains (Java/.NET Upgrade, Cloud Readiness, Security) and get meaningful results without touching configuration. Great for a first look at where your app stands.

**Custom Assessment** — the targeted path. Configure exactly what to analyze: target compute (App Service, AKS, Container Apps), target OS, containerization analysis. Pick multiple Azure targets to compare migration approaches side-by-side.

That comparison view is genuinely useful. An app with 3 mandatory issues for App Service might have 7 for AKS. Seeing both helps drive the hosting decision before you commit to a migration path.

## The issue breakdown is actionable

Each issue comes with a criticality level:

- **Mandatory** — must fix or migration fails
- **Potential** — might impact migration, needs human judgment
- **Optional** — recommended improvements, won't block migration

And each issue links to affected files and line numbers, provides a detailed description of what's wrong and why it matters for your target platform, gives concrete remediation steps (not just "fix this"), and includes links to official documentation.

You can hand individual issues to developers and they have everything they need to act. That's the difference between a tool that tells you "there's a problem" and one that tells you how to solve it.

## The upgrade paths covered

For .NET specifically:
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Each upgrade path has detection rules that know which APIs were removed, which patterns have no direct equivalent, and what security issues need attention.

For teams managing multiple apps, there's also a CLI that supports multi-repo batch assessments — clone all repos, assess them all, get per-app reports plus an aggregated portfolio view.

## My take

If you're sitting on legacy .NET Framework apps (and let's be real, most enterprise teams are), this is *the* tool to start with. The assessment document alone is worth the time — it turns a vague "we should modernize" into a concrete, prioritized list of work items with clear paths forward.

The collaborative workflow is smart too: export assessments, share with your team, import them without re-running. Architecture reviews where the decision-makers aren't the ones running the tools? Covered.

## Wrapping up

GitHub Copilot's modernization assessment transforms .NET migration from a scary, undefined project into a structured, trackable process. Start with a recommended assessment to see where you stand, then use custom assessments to compare Azure targets and build your migration plan.

Read the [full walkthrough](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) and grab the [VS Code extension](https://aka.ms/ghcp-appmod/vscode-ext) to try it on your own codebase.
