---
title: "Windows App Dev CLI v0.3: F5 from the Terminal and UI Automation for Agents"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 ships winapp run for terminal-based debug launches, winapp ui for UI automation, and a new NuGet package that makes dotnet run work with packaged apps."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

Visual Studio's F5 experience is great. But having to open VS just to launch and debug a packaged Windows app is a bit much when you're deep in a CI pipeline, running an automated workflow, or — increasingly — when an AI agent is doing the testing.

Windows App Development CLI v0.3 just [shipped](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/), and it addresses this directly with two headline features: `winapp run` and `winapp ui`.

## winapp run: F5 from anywhere

`winapp run` takes an unpackaged app folder and a manifest, and does everything VS does for a debug launch: registers a loose package, launches the app, and preserves your `LocalState` across re-deploys.

```bash
# Build your app, then run it as a packaged app
winapp run ./bin/Debug
```

Works for WinUI, WPF, WinForms, Console, Avalonia, and more. The modes are designed for both developers and automated workflows:

- **`--detach`**: Launch and return control to the terminal immediately. Good for CI/automation where you need the app running but don't want to block.
- **`--unregister-on-exit`**: Cleans up the registered package when the app closes. Clean test runs, no leftover state.
- **`--debug-output`**: Captures `OutputDebugString` messages and exceptions in real time. When a crash happens, a minidump is captured and analyzed in-process — managed (.NET) crashes via ClrMD, native (C++/WinRT) crashes via DbgEng. Add `--symbols` to pull PDBs from the Microsoft Symbol Server.

This is the kind of setup that makes headless test runs and agent-driven validation actually work. An agent can now launch your app, interact with it, verify behavior, and clean up — all without Visual Studio.

## New NuGet package: dotnet run for packaged apps

For .NET developers specifically, there's a new NuGet package: `Microsoft.Windows.SDK.BuildTools.WinApp`.

Add it to your project (or let `winapp init` do it), and `dotnet run` handles the entire inner loop: build, prepare a loose-layout package, register with Windows, and launch — all in one step.

```bash
# Let winapp init set it up
winapp init

# Or install directly
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

Works with WinUI, WPF, WinForms, Console, Avalonia. No manual registration, no extra commands. Just `dotnet run`.

This is a big quality-of-life win. If you've been maintaining a Makefile or PowerShell script just to wire together the build-and-register-and-launch cycle, that's now a solved problem.

## winapp ui: UI Automation from the command line

This is the one that opens up agentic scenarios. `winapp ui` gives you full UI Automation access to any running Windows app — WPF, WinForms, Win32, Electron, WinUI3 — all from the terminal.

What you can do:

- List all top-level windows
- Walk the full UI Automation tree of any window
- Find elements by name, type, or automation ID
- Click, invoke, and set values
- Take screenshots (per-window or multi-window composites)
- Wait for elements to appear — useful for test synchronization

Combine `winapp ui` with `winapp run` and you have a complete build → launch → verify workflow from the terminal. An agent can run your app, inspect the UI state, interact with it programmatically, and validate the result. No Visual Studio, no test framework bootstrapping, no manual steps.

For those building CI pipelines that do actual UI validation on Windows desktop apps, this is genuinely useful.

## Other bits worth noting

- **`winapp unregister`**: The cleanup counterpart to `winapp run`. Removes a sideloaded dev package when you're done.
- **`winapp manifest add-alias`**: Adds a `uap5:AppExecutionAlias` so a packaged app can be launched by name from the terminal.
- **Tab completion**: One command to set up completions for PowerShell, then every `winapp` command and option is tab-completable.
- **`Package.appxmanifest` by default**: `winapp init` now creates `Package.appxmanifest` (VS convention) instead of `appxmanifest.xml`.

## Get it

```bash
winget install Microsoft.WinAppCli
# or
npm install -g @microsoft/winappcli
```

The CLI is in public preview. Check the [GitHub repo](https://github.com/microsoft/WinAppCli) for full docs, guides for .NET, C++, Electron, Rust, Flutter, and more — and to file issues. The [original announcement](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) has all the details.
