---
title: "Aspire in VS Code 13.4 Tightens the Developer Loop in All the Right Ways"
date: 2026-06-16
author: "Emiliano Montesdeoca"
description: "Aspire in VS Code 13.4 is not just a feature update. It is a real improvement to the daily development loop with better debugging, resource visibility, panel integration, and TypeScript AppHost support."
tags:
  - Aspire
  - VS Code
  - .NET
  - Developer Experience
  - TypeScript
---

The best tooling updates are the ones you feel after a few days, not the ones that only look good in release notes.

That is how **Aspire in VS Code 13.4** reads to me.

This update is all about tightening the inner loop: creating projects faster, debugging mixed-language resources more naturally, surfacing health and commands directly in the editor, and keeping the dashboard close without making it the only place you can work.

That is a very good direction.

## The big win is less context switching

If you use Aspire seriously, you are usually moving across several surfaces:

- AppHost code
- terminal
- dashboard
- logs
- debug sessions
- service endpoints

What 13.4 does well is reduce the friction between those surfaces.

The new VS Code experience makes more of the app state visible exactly where you are already working:

- resource health in the editor
- commands next to resource declarations
- easier dashboard access
- log access from the AppHost context
- a panel that remains useful even before full debugging starts

That sounds small until you do it every day.

## Debugging mixed stacks matters more than people think

One of the strongest parts of this update is the more natural story for debugging **C#, TypeScript, Python, Go, browser apps, and Azure Functions** in one Aspire-driven flow.

That reflects the real shape of modern apps much better than pretending everything lives in a single runtime.

For .NET developers especially, that is valuable because many of us are now building systems that mix API projects, frontends, workers, and AI-adjacent services in different languages.

The fact that Aspire is making this feel more unified inside VS Code is a very practical improvement.

## TypeScript AppHost support reaching GA is also meaningful

I would not ignore the TypeScript AppHost side of this release.

Aspire becoming more natural for both C# and TypeScript broadens who can work in the same system model without weird second-class workflows. That matters for teams where platform code, frontend code, and service orchestration all live close together.

## My take

Aspire 13.4 in VS Code is not about one killer feature. It is about smoothing the rough edges in the daily loop:

- start faster
- see more state where you code
- debug more naturally
- jump to logs and the dashboard only when needed

That is exactly how good tooling should evolve.

If you are already using Aspire, this update looks worth installing. If you are still wondering whether VS Code is a serious home for Aspire-based development, the answer is becoming more and more obvious.

Original post: [Aspire in VS Code: the 13.4 developer loop](https://devblogs.microsoft.com/aspire/aspire-vscode-extension-13-4/)