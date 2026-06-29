---
title: "Single-File Apps in .NET 10"
date: 2026-01-15
author: "Emiliano Montesdeoca"
description: "How to build, publish, and optimize single-file executables with .NET 10 — from a basic console app to a trimmed, AOT-compiled binary."
tags:
  - dotnet
  - dotnet-10
  - deployment
  - aot
---

Single-file publishing is one of the simplest ways to make a .NET app easy to move around. Instead of asking someone to install a runtime, copy a folder of files, or understand your deployment layout, you can hand them one executable and let the runtime bundle do the rest.

.NET has supported this for several versions, but .NET 10 is where the story feels especially complete. The tooling around single-file, trimming, and ahead-of-time compilation is mature enough that you can make sensible trade-offs instead of treating packaging as an afterthought.

This tutorial shows the path from a basic console app to a compact, production-friendly binary. The goal is not just to make the output smaller. The real goal is to understand which publish switches solve which problem so you can choose the right combination for your app.

## What single-file actually means

Single-file publishing is about packaging, not magic. It does not automatically make your app self-contained, it does not automatically trim unused code, and it does not automatically turn your app into native code. Those are separate choices.

In practice, the terms are easy to mix up. Single-file means the app is delivered as one executable. Self-contained means the target machine does not need a separate .NET installation. Trimming removes unused IL. Native AOT compiles the app ahead of time into native machine code. They are related, but they solve different problems.

That distinction matters because it helps you avoid over-optimizing too early. Some apps only need a self-contained single file. Others need trimming as well. A smaller subset benefit from Native AOT. The right answer depends on startup time, deployment friction, reflection usage, and how much compatibility risk you can tolerate.

## Prerequisites

- .NET 10 SDK installed, which you can confirm with `dotnet --version`
- A console or ASP.NET Core app to experiment with
- A target runtime identifier in mind, such as `win-x64`, `linux-x64`, or `osx-arm64`

## Step 1: Create a new console app

Start with the smallest possible app so you can see the effect of each publish switch clearly.

```bash
dotnet new console -n SingleFileDemo
cd SingleFileDemo
```

Once the baseline app works, publish settings become much easier to reason about. If you begin with a complex web app, you often cannot tell whether a warning comes from your code, your dependencies, or the publish mode itself.

## Step 2: Publish as a single file

The minimal command for a self-contained single-file app looks like this:

```bash
dotnet publish -c Release -r linux-x64 \
  --self-contained true \
  -p:PublishSingleFile=true \
  -o ./output
```

Replace `linux-x64` with the runtime identifier that matches your target machine. The `--self-contained true` flag bundles the runtime, and `PublishSingleFile=true` tells the SDK to package the app into a single executable artifact.

After publishing, you should see one main executable in `./output/`. Depending on the platform and the libraries your app uses, the runtime may still extract some native components at runtime, but the deployment artifact itself is still a single file you can copy and run.

## Step 3: Understand the publish flags

These switches are easy to memorize, but it helps to understand what each one contributes.

- `-r` selects the target runtime and operating system combination.
- `--self-contained true` bundles the .NET runtime so the destination machine does not need it installed separately.
- `PublishSingleFile=true` packages the app into one executable rather than a folder full of assemblies.
- `-o ./output` gives you a predictable output folder you can inspect or ship.

That combination is a very good default for distribution scenarios where you want to reduce setup friction. It is not always the smallest or fastest option, but it is usually the easiest way to make a .NET app feel like a normal native application from the user's point of view.

## Step 4: Add trimming

Trimming removes code the linker believes your app does not use. On a simple app, the size reduction can be dramatic. On a complicated app, it can surface warnings that need real attention, especially if your code relies on reflection, dynamically loaded assemblies, or conventions that are hard for the linker to analyze.

Add these properties to your project file:

```xml
<PropertyGroup>
  <PublishSingleFile>true</PublishSingleFile>
  <SelfContained>true</SelfContained>
  <PublishTrimmed>true</PublishTrimmed>
  <TrimMode>full</TrimMode>
</PropertyGroup>
```

Then publish again:

```bash
dotnet publish -c Release -r linux-x64 -o ./output
```

The first thing to look for is not just file size, but whether the app still behaves correctly. Trimming is a powerful optimization, but it changes the relationship between your code and the runtime in ways that can expose hidden assumptions. If your app uses reflection heavily, start carefully, review the warnings, and make sure the critical code paths are tested.

## Step 5: Native AOT when startup and size really matter

If your app needs fast startup, very low memory usage, or a tiny deployment footprint, Native AOT may be worth the extra effort.

```xml
<PropertyGroup>
  <PublishAot>true</PublishAot>
</PropertyGroup>
```

Native AOT compiles the app into native machine code at publish time. There is no JIT at runtime, which usually means faster startup and less runtime overhead. The trade-off is compatibility: not every API pattern works cleanly with AOT, especially when the app relies on runtime code generation or deep reflection.

> **Note:** Native AOT is best treated as a deliberate choice, not a default. Run `dotnet publish` once, read the warnings, and confirm that the specific parts of your app you care about still work before you commit to the model.

## Checking binary size

You can inspect the output directly to see the effect of each optimization:

```bash
ls -lh ./output/
# -rwxr-xr-x 1 user staff  12M SingleFileDemo
```

On a small console app, a trimmed and AOT-compiled build may land somewhere in the 5-15 MB range depending on dependencies and platform. The exact number matters less than the trend: if the app ships more quickly and starts faster without breaking behavior, the optimization is doing its job.

## Common trade-offs

- Reflection-heavy code may need extra care during trimming.
- Native dependencies can still matter even when the app is packaged as a single file.
- Environment-specific configuration is still configuration; packaging does not remove the need to handle secrets, app settings, or file paths correctly.
- Web applications and plugin-based systems often need more testing than simple console apps before you turn on aggressive publish settings.

Those trade-offs are normal. The point is not to avoid optimization. The point is to choose the level of optimization that matches the app you are actually shipping.

## Wrapping up

Single-file publishing in .NET 10 is production-ready for most straightforward workloads. Start with `PublishSingleFile=true`, add trimming once the app is stable enough to validate the warnings, and move to Native AOT only when startup time, binary size, or runtime simplicity are strong enough reasons to justify the extra compatibility work.

If you remember one rule from this tutorial, make it this: single-file is the packaging choice, trimming is the size choice, and AOT is the runtime choice. Use them together only when you know why each one is helping.
