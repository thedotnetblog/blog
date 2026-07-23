---
title: 'Visual Studio Extension Teams Should Stop Releasing by Habit and Start Releasing by Pipeline'
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: 'A repeatable GitHub Actions flow for VSIX versioning and publishing is now simple enough that manual release steps are hard to justify.'
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Original source: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

If you maintain Visual Studio extensions and still run significant parts of release manually, this is your signal to modernize.

The workflow shown in this post is intentionally practical: stamp version, build, publish testing artifacts to a gallery, then publish stable bits to Marketplace. No heavy platform ceremony, just deterministic release behavior.

What I like most is that versioning gets treated as pipeline state, not a pre-release checklist item. That one decision eliminates a surprising number of mistakes: mismatched metadata, stale assembly versions, and inconsistent release notes.

The split between gallery publishing and Marketplace publishing is also operationally mature. Teams need a place for quick validation builds that do not carry official-release semantics. Pushing everything directly to Marketplace is high-friction and encourages risky shortcuts.

A strong release pattern for extension teams is:

On pull requests and main commits, produce CI VSIX artifacts and publish to gallery for testers.

On tagged releases, publish signed and validated packages to Marketplace.

Keep token handling minimal with dedicated secrets and least-privilege scopes.

My opinionated take: extension ecosystems lag behind app ecosystems in CI discipline because small teams assume manual workflows are manageable. They are manageable until they are not. One rushed patch, one broken package, one forgotten manifest update, and trust drops.

These reusable actions are useful because they encode repeated release logic once and let teams focus on extension quality instead of packaging mechanics.

There is still engineering judgment required. You should gate Marketplace publication behind quality checks, and you should treat publish manifests as audited release artifacts. But the baseline pipeline complexity is now low enough that manual-only releases are mostly technical debt.

If you lead extension development, standardize this now across repositories. You will get better traceability, easier onboarding, and fewer one-person release bottlenecks.

Suggested rollout:

Start with build plus gallery publish for one extension.

Introduce version stamping after validating your manifest-source conventions.

Add Marketplace publishing only after secret management and release gates are in place.

This is not about chasing DevOps fashion. It is about reliability for the people who install your tooling and expect updates to work.

Stable extension ecosystems are built the same way stable applications are built: with boring, repeatable automation that removes human guesswork.
