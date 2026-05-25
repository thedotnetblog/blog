---
title: ".NET 11 Preview 4: MCP Server Template, Runtime-Async Libraries, Process API"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 is out. Here are the highlights that caught my eye: the MCP Server template shipping in the SDK, runtime libraries compiled with runtime-async, dotnet watch for mobile, and a major Process API expansion."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 is available. Every release of a major .NET preview adds a long list of items across the runtime, SDK, libraries, ASP.NET Core, MAUI, C#, and Entity Framework. Rather than repeat the full list, here are the things that stand out to me.

## MCP Server Template Ships in the .NET SDK

The single most interesting item: an MCP Server project template is now included in the SDK. That means `dotnet new mcp-server` (or whatever the command ends up being) works out of the box. For anyone building MCP tooling in .NET, this removes the bootstrapping friction considerably. MCP integration in the platform toolchain signals the direction the ecosystem is heading.

## Runtime Libraries Compiled with Runtime-Async

The runtime itself now compiles its standard libraries using the runtime-async feature. This is an internal change that affects performance — async state machines in the runtime become more efficient. The significance here isn't user-visible API changes; it's that runtime-async is mature enough to be used for the BCL itself, which is a meaningful signal about the feature's readiness.

## JIT Optimizations and Hardware Intrinsics

Preview 4 continues the JIT work. Hardware intrinsics and code generation improvements ship here — details are in the runtime release notes. These are typically the kind of changes that improve throughput on tight computation loops without any code changes on your part.

## Process API Expansion

A major update to `System.Diagnostics.Process` ships in Preview 4:

- `Process.RunAndCaptureTextAsync` — start a process, capture stdout/stderr, wait for exit, all in one call without deadlock risk
- `KillOnParentExit` — lightweight lifetime coupling between parent and child processes
- `SafeProcessHandle`-based APIs that are more trimmer-friendly

If you've ever written boilerplate to capture process output without hitting deadlocks (async read from stdout *and* stderr simultaneously), `RunAndCaptureTextAsync` is the API you were missing.

## dotnet watch for Android and iOS

`dotnet watch` now supports device selection for .NET MAUI Android and iOS projects. Faster iteration on mobile without manually managing device connections in the build loop.

## Span-based Compression APIs

New span-based Deflate, ZLib, and GZip encoder/decoder APIs ship in the libraries. Less allocation when dealing with compressed data — relevant if you're doing high-throughput data processing.

## Try It

[Download .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — it's a preview, not production-ready, but worth running against your projects to catch any issues early before the RC cycle.

Original post: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
