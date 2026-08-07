---
title: ".NET 11 Preview 5: What I Would Actually Try First"
date: 2026-10-26
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 ships improvements across the SDK, runtime, C#, ASP.NET Core, and EF Core. Here are the updates I think are most worth testing early if you build real .NET apps."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

.NET preview posts are always packed.

That is good news for the platform, but it also means the practical question gets buried: **what should you actually test first?**

.NET 11 Preview 5 brings a lot across the SDK, runtime, libraries, ASP.NET Core, C#, MAUI, and EF Core. Instead of turning this into a giant changelog recap, I want to focus on the parts that I think deserve real developer attention right now.

## The MCP server template being in `dotnet new` is a signal

This is probably the most strategic item in the SDK section.

When a project template lands directly in the SDK, it means the platform is no longer treating the scenario as niche. Having an **MCP Server template** built into `dotnet new` lowers the cost of trying the pattern and sends a clear message about where the ecosystem is going.

If you are building agent tooling, internal assistants, or AI-integrated developer utilities in .NET, this is one of the first things I would test.

## Build-time vulnerability and end-of-life checks are exactly the kind of defaults I like

Security and lifecycle awareness are much better when the platform helps you *during the build*, not after the fact in a separate report nobody reads.

The new SDK checks for vulnerabilities and end-of-life packages during build are the kind of feature I love because they make better behavior the default.

These are not flashy, but they are the kind of improvements that age really well.

## C# continues to get more expressive in the right places

The Preview 5 C# items are interesting, especially:

- closed class hierarchies
- union declarations and union patterns
- continued unsafe evolution work

I would not blindly adopt all of this in production code yet, because preview language features always deserve a sober test cycle. But the direction is good. C# keeps moving toward richer modeling without losing its identity.

## ASP.NET Core and EF Core have practical updates worth testing early

Two areas I would definitely put through a spike:

### Blazor improvements

Client-side validation for Blazor SSR and QuickGrid improvements without interactivity are both the kind of quality-of-life features that can simplify real apps.

### EF Core defaults and warnings

EF Core moving SQL Server 2022 compatibility to the default and adding warnings for async EF queries running synchronously are exactly the kind of changes that can surface hidden issues in real codebases.

That means it is worth testing sooner rather than later.

## My short list for a first pass

If I had half a day to explore Preview 5, I would do this:

1. try the MCP server template
2. run builds and inspect the new vulnerability/EOL checks
3. test any codebase that might benefit from the new C# modeling features
4. validate Blazor SSR scenarios if you are on that stack
5. run EF Core-heavy paths and watch for warning changes or SQL differences

That is where I think the early value is.

## My take

.NET 11 Preview 5 feels like one of those releases where the platform keeps pushing in two directions at once:

- more ambitious developer capabilities
- better defaults for production-minded teams

That combination is what I want from a preview cycle.

Try it, but try it with purpose.

Original post: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)