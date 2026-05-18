---
title: "Aspire 13.3: Kubernetes Support, Browser Logs, and the Aspireify Skill"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Five weeks after 13.2, Aspire 13.3 lands with 45 new features including first-class AKS deployment, an AI-assisted onboarding skill, browser log capture, and structured command results."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Five weeks is not a long time for a release, but Aspire 13.3 doesn't feel like it. The headline items are meaningful: first-class Kubernetes and AKS deployment with Helm, an agent-assisted onboarding skill called Aspireify, browser log capture directly in the dashboard, and structured command results. Plus 45 new features, 134 improvements, and 93 bug fixes.

Let's hit the highlights.

## Aspireify: Agent-Assisted Onboarding

Adding Aspire to an existing project sounds simple — drop an AppHost in, done. In practice it involves a lot of archaeology: which ports matter, which environment variables are real dependencies, which Docker Compose services should map to Aspire integrations.

The new **Aspireify skill** gives your coding agent a guided workflow for exactly this. When `aspire init` drops a skeleton AppHost, the Aspireify skill helps the agent inspect the repo, understand how it already runs, and wire the AppHost to fit the app — not the other way around.

The default stance is "minimize changes to your code." If your app already reads `DATABASE_URL`, the agent maps that with `WithEnvironment()` instead of asking you to rewrite your configuration. If a port is hardcoded, the skill tells the agent when to preserve it.

This is the kind of AI tooling that actually saves time rather than generating more work to review.

## First-Class Kubernetes and AKS Deployment

This one has been on the wishlist for a while. Aspire 13.3 ships **first-class Kubernetes and AKS deployment support with Helm**. You can now target AKS as a deployment target directly from the Aspire tooling.

For teams already running production workloads on AKS, this closes a significant gap. Your Aspire app model now has a clean path from local dev to Kubernetes without manual Helm chart authoring.

## Browser Logs in the Dashboard

This is one of those features that sounds small until you're debugging a frontend issue.

The new `WithBrowserLogs()` API attaches a tracked browser resource to any endpoint-capable resource. Aspire launches Chromium using a private CDP pipe and streams console logs, network requests, and errors directly into the resource log stream:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

TypeScript AppHost supports the same:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Console errors, failed network requests, client-side exceptions — all visible in the same dashboard where you're already watching traces and metrics. No more tab-switching to browser DevTools for the basic stuff.

## Structured Command Results

Resource commands got a meaningful upgrade. Until now, commands returned success/failure. Now they return structured results: text, JSON, or markdown that flows through the model, dashboard UI, CLI, and MCP tools.

The dashboard ties this together with a new notification center in the header. Command results show up as timestamped notifications with markdown rendering and a "View response" action.

This makes resource commands genuinely composable. An integration can now expose a command that returns meaningful output — like a tunnel URL — rather than just changing state somewhere.

## Wrapping Up

Aspire 13.3 is worth the upgrade even just for the Kubernetes support. The browser logs and structured command results feel like the kind of quality-of-life improvements that accumulate quickly in a day-to-day development workflow.

Full release notes: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
