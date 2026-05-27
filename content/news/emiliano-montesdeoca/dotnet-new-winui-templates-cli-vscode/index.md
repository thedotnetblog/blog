---
title: "dotnet new WinUI: Create Windows Apps Without Touching Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI project templates now work from dotnet new — blank apps, NavigationView patterns, and more. VS Code support, no Visual Studio required, with Fluent Design defaults baked in."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI development used to require Visual Studio. That's changing: Microsoft has published open-source project and item templates for WinUI that work with `dotnet new`, bringing Windows app development into the standard CLI workflow.

## Getting Started in Three Commands

```shell
# Install the templates
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Create a NavigationView app
dotnet new winui-navview -n MyApp

# Run it
cd MyApp
dotnet run
```

No Visual Studio, no manual project setup. The app runs from `dotnet run`.

## What's Included

**Blank template** (`dotnet new winui`) — a modern starting point with a Fluent title bar already wired up, updated default app icon with `.ico` asset, proper light/dark mode defaults. Better than the old blank template that left you configuring the basics yourself.

**NavigationView template** (`dotnet new winui-navview`) — the master-detail navigation pattern, fully wired up with a NavigationView, modern title bar, and multi-page navigation structure. Follows the standard Windows app silhouette for navigation-based apps. If you're building anything with side navigation, start here.

Both templates follow the [Windows app silhouettes](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — modern Fluent Design patterns for layout, navigation, and visual structure — out of the box.

## Why This Matters for Non-Visual-Studio Developers

WinUI developers using VS Code, Rider, or command-line tooling have been underserved. The existing Visual Studio templates weren't usable outside of VS — you had to manually recreate project structure and wire up the basics.

These templates are open source (see [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), developed from [community feedback](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), and available now. Visual Studio support is in progress — these same templates will eventually work there too.

For teams that want to script their WinUI project setup, integrate it into CI, or just use an editor other than Visual Studio, this is a meaningful improvement.

Original post: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
