---
title: "How Copilot Studio Migrated to .NET 10 WebAssembly and Got 20% Faster"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10 WASM improvements aren't just for new projects. Here's what Copilot Studio measured after upgrading from .NET 8: automatic fingerprinting, WasmStripILAfterAOT by default, and real execution performance numbers."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

The Copilot Studio team did something every Blazor WASM developer has been curious about: they actually upgraded a production application from .NET 8 to .NET 10 and measured the results. The post shares specific numbers, which is rare and genuinely useful.

## The Upgrade Was Boring (That's a Good Thing)

Updating target framework, refreshing package references, fixing any breaking changes. That's it. The .NET 10 build is now running in production. The migration itself wasn't the interesting part — the changes in .NET 10 are.

## Automatic Asset Fingerprinting

Previously, shipping a WASM app meant writing custom scripts to rename published assets with SHA256 hashes for cache-busting. Copilot Studio had a PowerShell script doing exactly this — rename files, inject `integrity` attributes into the JavaScript loader, manage the whole thing manually.

In .NET 10, all of that is built in. Published assets are automatically fingerprinted, imported directly from `dotnet.js`, and integrity-validated without manual intervention. The team deleted the renaming script.

Small change in scope, significant reduction in complexity.

## WasmStripILAfterAOT Is Now On by Default

In .NET 8, stripping IL from AOT-compiled assemblies was opt-in. In .NET 10 it's the default. After AOT compilation, the original IL bytecode is removed from the output — it isn't needed at runtime, and keeping it was inflating package size for no reason.

Copilot Studio uses a specific optimization: it ships both a JIT engine (fast startup) and an AOT engine (maximum steady-state performance), loading both in parallel and handing off from JIT to AOT once it's ready. It also deduplicates files that are identical between the two engines.

The new IL stripping behavior means AOT assemblies no longer match their JIT counterparts bit-for-bit, so fewer files are deduplicated:
- .NET 8: 59 shared files
- .NET 10: 22 shared files

Net result: roughly 15% larger package size for the AOT engine. The AOT download is ~6% slower on fast LAN, ~17% slower on 4G. But it all happens in the background after the app is already interactive.

## The Performance Numbers

This is the part that matters:

- **~20% faster** on the first call (cold path)
- **~5% faster** on subsequent calls (warm path)

The improvements are most visible in "big bots" — large, complex agents where AOT-compiled code dominates. For simpler workflows the gain is smaller.

## If You're Still on .NET 8

The migration story is genuinely simple: update `<TargetFramework>`, refresh package references, remove any custom fingerprinting scripts, and you'll automatically benefit from `WasmStripILAfterAOT`. If you're AOT-compiling, expect similar performance gains.

One note from the post: if you load the .NET WASM runtime inside a `WebWorker`, set `dotnetSidecar = true` when initializing.

Original post: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
