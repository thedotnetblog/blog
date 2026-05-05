---
title: "VS Code 1.118: Copilot CLI Gets Session Names, Model Badges, and TypeScript 7.0 Nightly Opt-In"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Visual Studio Code 1.118 is a focused release centered on Copilot CLI improvements — session naming, model badges, auto model selection, and a new option to opt into TypeScript 7.0 nightlies."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
  - TypeScript
---

[Visual Studio Code 1.118](https://code.visualstudio.com/updates/v1_118) is a smaller focused release — mostly Copilot CLI refinements — but there are a few things worth noting if you use the Agents app or TypeScript heavily.

## Copilot CLI: sessions get real names

The Copilot CLI SDK session-title APIs are now used as the source of truth for session names. Previously you'd get auto-generated labels; now sessions surface the actual name from the SDK. Small quality-of-life improvement but it makes navigating multiple agent sessions a lot less confusing.

## Switch sessions faster with keyboard shortcuts

The Agents app now has `Ctrl+1`, `Ctrl+2`, etc. bound to quickly switch between sessions. If you're running multiple Copilot CLI sessions in parallel (which, if you're doing agent-heavy work, you probably are), this removes a lot of mouse clicking.

## Model badges in chat

Copilot CLI responses in the chat panel now show a model badge — you can see at a glance which model handled each request. Useful when you're experimenting with different models in the same session.

## Auto model selection lands in Copilot CLI

The auto model selection feature — previously available in other parts of Copilot — now works in the Copilot CLI agent too. Let the system pick the best model for the task rather than manually switching.

## TypeScript 7.0 nightly opt-in

This one's interesting if you're on the TypeScript cutting edge: you can now opt in to testing TypeScript 7.0 nightlies directly from VS Code settings. TypeScript 7.0 is a major release with significant changes (the [beta dropped a few days ago](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)), and the opt-in path makes it easy to test without changing your global TypeScript install.

## Under the hood: `node-pty` cleanup

The Copilot CLI SDK now resolves `node-pty` from VS Code via `hostRequire` instead of copying binaries into the SDK's prebuilds folder at build time. This is an internal change but it simplifies distribution and means fewer things that can go wrong at runtime.

## Wrapping up

Not a splashy release, but the Copilot CLI improvements add up — especially session management for anyone doing agent-heavy development. The TypeScript 7.0 nightly opt-in is a nice touch for those who like living on the edge.

See the [full release notes](https://code.visualstudio.com/updates/v1_118) for the complete change list.
