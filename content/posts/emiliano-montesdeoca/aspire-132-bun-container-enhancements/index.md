---
title: "Aspire 13.2 Gets Bun, Better Containers, and Less Debugging Friction"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 adds first-class Bun support for Vite apps, fixes Yarn reliability, and ships container improvements that make local dev behavior honest. Here's what actually changed and why it matters."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

If you've been building .NET backends with JavaScript frontends in Aspire, 13.2 is the kind of update that quietly makes your day better. No splashy new paradigms. Just solid improvements to things that were mildly annoying.

Let's walk through what actually landed.

## Bun is Now a First-Class Citizen

The headline feature: Bun support for Vite apps in Aspire. One fluent call, done.

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

If your team already uses Bun — which you might, given its dramatically faster install times and startup — Aspire no longer makes you fight against the grain. Previously, Aspire assumed npm and you had to work around it. Now `.withBun()` is a first-class option alongside `.withYarn()` and the default npm behavior.

Why does this matter? Because JavaScript tooling speed directly affects your inner dev loop. If your frontend takes 30 seconds to install dependencies every time you spin up a fresh environment, that adds up. Bun cuts that dramatically.

The C# AppHost equivalents are documented at [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun) if you prefer authoring in C# — all the same patterns apply.

## Yarn Got More Reliable

Bun gets the spotlight, but Yarn users get something arguably more impactful: fewer mysterious failures. Aspire 13.2 improves reliability for `withYarn()` with `addViteApp()`.

These kinds of fixes don't sound exciting until you've spent 20 minutes debugging why your Yarn-backed frontend resource wouldn't start. Consider it fixed.

## Container Publishing You Can Actually Reason About

Two container improvements worth knowing:

### Explicit Pull Policy

Docker Compose publishing now supports `PullPolicy`, including a `Never` option:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

This is the "please use the image I already built and leave the registry out of it" workflow. Super useful when iterating locally on images you're building and publishing manually, or when your CI produces an image and you want Compose to use exactly that one without sneaking in a remote pull.

### PostgreSQL 18+ Volumes Work Again

PostgreSQL 18 changed its internal data directory layout. This broke volume mapping in Aspire silently — your data volume would be set up but persistence wouldn't actually work correctly. 13.2 fixes this.

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

If you're running PostgreSQL 18 or later with a data volume, upgrade to Aspire 13.2 and don't think about it again.

## Debugging Quality-of-Life Improvements

A few things that make stepping through an AppHost session less frustrating:

- **DebuggerDisplayAttribute on core types** — `DistributedApplication`, resources, endpoint expressions now show useful values in the debugger instead of requiring you to drill into object trees
- **Better WaitFor failure messages** — when resources fail to start, the error context is actually helpful now
- **`BeforeResourceStartedEvent` fires at the right time** — only when a resource is actually starting, not on unrelated state transitions
- **`launchSettings.json` is more resilient** — less chance of a malformed setting corrupting your dev startup

None of these are individually earth-shattering, but collectively they remove friction from the debugging experience. If you've ever had to drill three levels deep into an Aspire resource object to figure out what endpoint it was using, the debugger display improvement alone is worth the update.

## Wrapping up

Aspire 13.2 is a focused quality release. Bun support is the headline, but the container and debugging improvements are what will make your day-to-day work smoother. Worth updating — especially if you're on PostgreSQL 18 with data volumes.

Full details in the [original post by David Pine](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) and the [Aspire 13.2 what's new docs](https://aspire.dev/whats-new/aspire-13-2/).
