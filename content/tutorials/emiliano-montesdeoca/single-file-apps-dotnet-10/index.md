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

Single-file publishing has been part of .NET since version 5, but .NET 10 takes it to a new level with improved ahead-of-time (AOT) compilation, better trimming analysis, and smaller default output sizes. This tutorial walks you through publishing a real app as a single binary — no install required on the target machine.

## Prerequisites

- .NET 10 SDK installed (`dotnet --version` should show `10.x.x`)
- A console or ASP.NET Core app to work with

## Step 1: Create a new console app

```bash
dotnet new console -n SingleFileDemo
cd SingleFileDemo
```

## Step 2: Publish as a single file

The minimal publish command for a self-contained single-file app:

```bash
dotnet publish -c Release -r linux-x64 \
  --self-contained true \
  -p:PublishSingleFile=true \
  -o ./output
```

Replace `linux-x64` with your target runtime identifier (`win-x64`, `osx-arm64`, etc.). The `--self-contained true` flag bundles the .NET runtime into the output binary.

After publishing, `./output/` contains a single executable file.

## Step 3: Add trimming

Trimming removes unreachable code from the final binary, often cutting size by 60–80%:

```xml
<!-- Add to your .csproj -->
<PropertyGroup>
  <PublishSingleFile>true</PublishSingleFile>
  <SelfContained>true</SelfContained>
  <PublishTrimmed>true</PublishTrimmed>
  <TrimMode>full</TrimMode>
</PropertyGroup>
```

Then just run:

```bash
dotnet publish -c Release -r linux-x64 -o ./output
```

## Step 4: Native AOT (optional but powerful)

For the smallest and fastest binaries, use Native AOT instead of single-file:

```xml
<PropertyGroup>
  <PublishAot>true</PublishAot>
</PropertyGroup>
```

Native AOT compiles your app to native machine code at publish time. There's no JIT at runtime, which means near-instant startup and a much smaller memory footprint.

> **Note:** Native AOT doesn't support all reflection patterns. Run `dotnet publish` once and review any AOT compatibility warnings before committing to this approach.

## Checking binary size

```bash
ls -lh ./output/
# -rwxr-xr-x 1 user staff  12M SingleFileDemo
```

With trimming + AOT on a simple console app, expect 5–15 MB depending on dependencies.

## Wrapping up

Single-file publishing in .NET 10 is production-ready for most workloads. Start with `PublishSingleFile=true`, add trimming once your app is stable, and consider Native AOT if startup time or binary size are hard constraints.
