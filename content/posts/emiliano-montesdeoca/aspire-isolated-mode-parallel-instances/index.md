---
title: "Aspire's Isolated Mode Fixes the Port Conflict Nightmare for Parallel Development"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introduces --isolated mode: random ports, separate secrets, and zero collisions when running multiple instances of the same AppHost. Perfect for AI agents, worktrees, and parallel workflows."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

If you've ever tried running two instances of the same project at the same time, you know the pain. Port 8080 is already in use. Port 17370 is taken. Kill something, restart, juggle environment variables — it's a productivity killer.

This problem is getting worse, not better. AI agents create git worktrees to work independently. Background agents spin up separate environments. Developers checkout the same repo twice for feature branches. Every one of these scenarios hits the same wall: two instances of the same app fighting over the same ports.

Aspire 13.2 fixes this with a single flag. James Newton-King from the Aspire team [wrote up the full details](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), and it's one of those "why didn't we have this sooner" features.

## The fix: `--isolated`

```bash
aspire run --isolated
```

That's it. Each run gets:

- **Random ports** — no more collisions between instances
- **Isolated user secrets** — connection strings and API keys stay separate per instance

No manual port reassignment. No environment variable juggling. Each run gets a fresh, collision-free environment automatically.

## Real scenarios where this shines

**Multiple checkouts.** You've got a feature branch in one directory and a bugfix in another:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Both run without conflicts. The dashboard shows what's running and where.

**Background agents in VS Code.** When Copilot Chat's background agent creates a git worktree to work on your code independently, it may need to run your Aspire AppHost. Without `--isolated`, that's a port collision with your primary worktree. With it, both instances just work.

The Aspire skill that ships with `aspire agent init` automatically instructs agents to use `--isolated` when working in worktrees. So Copilot's background agent should handle this out of the box.

**Integration tests alongside development.** Need to run tests against a live AppHost while continuing to build features? Isolated mode gives each context its own ports and config.

## How it works under the hood

When you pass `--isolated`, the CLI generates a unique instance ID for the run. This drives two behaviors:

1. **Port randomization** — instead of binding to predictable ports defined in your AppHost config, isolated mode picks random available ports for everything — the dashboard, service endpoints, all of it. Service discovery adjusts automatically, so services find each other regardless of which ports they land on.

2. **Secret isolation** — each isolated run gets its own user secrets store, keyed by the instance ID. Connection strings and API keys from one run don't leak into another.

Your code doesn't need any changes. Aspire's service discovery resolves endpoints at runtime, so everything connects correctly regardless of port assignment.

## When to use it

Use `--isolated` when running multiple instances of the same AppHost simultaneously — whether that's parallel development, automated tests, AI agents, or git worktrees. For single-instance development where you prefer predictable ports, regular `aspire run` still works fine.

## Wrapping up

Isolated mode is a small feature that solves a real, increasingly common problem. As AI-assisted development pushes us toward more parallel workflows — multiple agents, multiple worktrees, multiple contexts — the ability to just spin up another instance without fighting over ports is essential.

Read the [full post](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) for all the technical details and try it out with `aspire update --self` to get 13.2.
