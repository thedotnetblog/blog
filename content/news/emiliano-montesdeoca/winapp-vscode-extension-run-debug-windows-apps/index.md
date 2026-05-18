---
title: "WinApp VS Code Extension: Run, Debug, and Package Windows Apps Without Leaving the Editor"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "The WinApp VS Code extension brings the full Windows App Development CLI into VS Code — run, debug with package identity, package, and sign Windows apps (WPF, WinUI, .NET, C++) without touching Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

If you've ever tried to build a Windows app in VS Code, you know the moment it happens. You're flowing along, editing code in your editor of choice, and then you need package identity for a Windows API. Or you need to create an MSIX. Or you need to sign a package. And suddenly you're reaching for Visual Studio, or digging through SDK command-line tools, or Googling "msix packaging without visual studio" at 11pm.

That friction is gone now. The [WinApp VS Code extension](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) is in public preview — and it's the full [Windows App Development CLI](https://github.com/microsoft/WinAppCli) wrapped directly into VS Code. No separate installation, no Visual Studio required.

## Package Identity From F5

Here's the thing about Windows APIs — notifications, background tasks, on-device AI features, share targets — many of them require your app to have **package identity**. Without it, those APIs just won't work.

Getting package identity traditionally meant building a full MSIX installer or running from Visual Studio. The WinApp extension changes this completely with a custom `winapp` debug type.

Add this to your `launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

Hit F5. The extension locates your build output and manifest, gives your app package identity via `winapp run`, and attaches the debugger. For .NET apps that's `coreclr` (needs C# Dev Kit). C/C++ uses `cppvsdbg`. Node/Electron uses the built-in debugger.

You can wire up a `preLaunchTask` so the project builds automatically before each F5 press — same as Visual Studio's build-and-launch flow, just in VS Code.

## Everything in the Command Palette

Open `Ctrl+Shift+P`, type `WinApp`, and you get the full toolkit:

- **Initialize Project** — configure your project with Windows SDK and/or Windows App SDK
- **Run Application** — launch as a loose-layout packaged app with package identity
- **Create MSIX Package** — package your app with certificate and runtime options
- **Update Manifest Assets** — auto-generate all required app icons from a single source image
- **Generate / Install Certificate** — development certificate management
- **Sign Package** — sign an MSIX or executable
- **Run SDK Tool** — run `makeappx`, `signtool`, `mt`, or `makepri` directly

No WinApp CLI installation needed either. It's bundled with the extension.

## Works Across Frameworks

This isn't just a .NET WPF/WinUI tool. The extension works with:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

That breadth is deliberate. VS Code is where web and cross-platform developers live. If you're building a Tauri or Electron app that needs Windows packaging and notarization, this extension covers you without requiring you to adopt Visual Studio.

## Why This Matters for .NET Developers

I work a lot in VS Code — it's where I write Markdown, manage configs, edit small projects, and run terminals. But for .NET Windows desktop work, Visual Studio has been the only real option the moment you need anything packaging-related.

This extension closes that gap. You can now have a complete Windows .NET desktop development cycle — edit, build, run with package identity, debug, package, sign — without leaving VS Code. That's a genuine quality-of-life improvement.

It also matters for agentic and automation scenarios. The Windows App Development CLI v0.3 (which this extension wraps) unlocked `run`, `debug`, and `ui` commands that agents and scripts can use. The extension brings all of that into a VS Code context, which means AI coding agents working in VS Code can now interact with Windows apps too.

## Getting Started

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Or search for **WinApp** in the Extensions view (`Ctrl+Shift+X`).

Requirements:
- Windows 10 or later
- VS Code 1.109.0 or later
- The debugger extension for your app's language (C# Dev Kit for .NET, C/C++ extension for C++)

Full docs are at the [WinApp VS Code extension README](https://github.com/microsoft/winappCli/blob/main/src/winapp-VSC/README.md).

It's a public preview, and the team is actively collecting feedback. If you hit a rough edge, [file a bug](https://github.com/microsoft/winappCli/issues/new?template=bug-report.yml). If something's missing, [open a feature request](https://github.com/microsoft/winappCli/issues/new?template=feature_request.yml).

Read the [full announcement from Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) for more details.

## Wrapping Up

The WinApp VS Code extension is a welcome addition for .NET Windows desktop developers who live in VS Code but have had to bounce to Visual Studio for packaging work. Package identity from F5, MSIX packaging from the command palette, certificate management built in — it's the right set of things to bring together.

Give it a try on your next WPF or WinUI project. The friction you've been working around just got a lot smaller.
