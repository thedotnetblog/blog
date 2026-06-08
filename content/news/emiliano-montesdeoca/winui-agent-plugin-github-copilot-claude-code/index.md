---
title: "A WinUI Agent Plugin for GitHub Copilot and Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft released agent skills for WinUI development — scaffold, build, run, test, iterate, all with GitHub Copilot CLI or Claude Code. The key innovation: purpose-built tools that ground the agent in WinUI-specific facts."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Getting AI agents to write WinUI apps has been hit-or-miss. Generic agents pull from too much context — mixing WinUI 3 with older UWP patterns, getting MSIX packaging wrong, or generating apps that don't actually run. The new WinUI agent plugin takes a different approach.

## What It Is

A set of [open-source agent skills](https://aka.ms/winui-skills) designed specifically for WinUI and Windows App SDK development, compatible with both GitHub Copilot CLI and Claude Code.

Install and run:

```shell
# Add the WinUI plugin to GitHub Copilot CLI
/plugin install winui@awesome-copilot

# Run the setup skill to install prerequisites
/winui:winui-setup
```

Then describe the app you want. The agent handles the rest.

## The End-to-End Loop

The skills are built around a complete development loop: scaffold → build → run → test → iterate. What makes this different from just asking a generic agent:

**Scaffold correctly** — the agent picks the right `dotnet new` WinUI template, not an older UWP pattern.

**Build through the right pipeline** — WinUI apps need packaged execution. Generic agents often don't know this and generate apps that compile but don't run. The skills handle the packaged execution model correctly.

**Interact and validate** — if you ask, the agent can interact with the running app to validate functionality, not just check that the build succeeded.

**Fix compilation errors automatically** — rather than stopping at the first error, the agent recognizes common WinUI failure modes and steers toward working solutions.

Beyond the basics, the skills also handle higher-level polish: accessibility audits, code reviews, MSIX packaging.

## The Token Efficiency Design

Building in rich WinUI context up front would make every turn expensive. Instead, the skills are paired with purpose-built tools that give the agent ground-truth answers on demand — only pulling in specific reference data when the agent needs it, not loading entire documentation pages preemptively.

The result: agents that know WinUI deeply without the token overhead of loading everything every turn.

## Supported Features

The skills handle: XAML and Fluent Design, MVVM, MSIX packaging, code signing, Store submission, accessibility, theming, UI automation. That covers most of the surface area where agents typically get stuck.

Original post: [Introducing WinUI agent plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/build-native-windows-apps-with-ai-agents-for-winui-and-windows-app-sdk/)
