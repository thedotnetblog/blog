---
title: "NuGet Package Pruning in .NET 10 Is the Kind of Improvement You Feel Everywhere"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "NuGet package pruning in .NET 10 reduces false-positive vulnerability reports, simplifies the restore graph, and improves restore performance. It is one of those platform changes that quietly makes daily work better."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

Some platform improvements are exciting because they unlock new scenarios.

Others are exciting because they make existing workflows less noisy, less fragile, and less annoying.

**NuGet package pruning in .NET 10** is very much in the second category, and I mean that as a compliment.

## Why this matters

If you have dealt with transitive vulnerability noise, unnecessarily large restore graphs, or packages that are technically present but not actually relevant to the runtime your app uses, this change hits a real pain point.

Pruning helps by removing platform-provided packages from the effective dependency graph when the runtime already supplies them.

That means:

- fewer false-positive vulnerability reports
- cleaner transitive dependency graphs
- less restore overhead
- more actionable audit results

## My take

This is exactly the sort of .NET improvement I love.

It makes the defaults better, reduces mental overhead, and improves both security signal quality and day-to-day tooling behavior.

That is a win even if it never gets a keynote slide.

Original post: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)