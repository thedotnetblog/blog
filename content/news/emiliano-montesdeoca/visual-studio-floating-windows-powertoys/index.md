---
title: "That Visual Studio Floating Windows Setting You Didn't Know About (But Should)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "A hidden Visual Studio setting gives you full control over floating windows — independent taskbar entries, proper multi-monitor behavior, and perfect FancyZones integration. One dropdown changes everything."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

If you use multiple monitors with Visual Studio (and honestly, who doesn't these days), you've probably experienced the annoyance: floating tool windows disappear when you minimize the main IDE, they always stay on top of everything else, and they don't show up as separate taskbar buttons. It works for some workflows, but for multi-monitor setups it's frustrating.

Mads Kristensen from the Visual Studio team [shared a little-known setting](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) that completely changes how floating windows behave. One dropdown. That's it.

## The setting

**Tools > Options > Environment > Windows > Floating Windows**

The dropdown "These floating windows are owned by the main window" has three options:

- **None** — full independence. Every floating window gets its own taskbar entry and behaves like a normal Windows window.
- **Tool Windows** (default) — documents float freely, tool windows stay tied to the IDE.
- **Documents and Tool Windows** — classic Visual Studio behavior, everything tied to the main window.

## Why "None" is the move for multi-monitor setups

Set it to **None** and suddenly all your floating tool windows and documents behave like real Windows applications. They appear in the taskbar, stay visible when you minimize the main Visual Studio window, and stop forcing themselves to the front of everything.

Combine this with **PowerToys FancyZones** and it's a game changer. Create custom layouts across your monitors, snap your Solution Explorer to one zone, debugger to another, and code files wherever you want. Everything stays put, everything is independently accessible, and your workspace feels organized instead of chaotic.

## Quick recommendations

- **Multi-monitor power users**: Set to **None**, pair with FancyZones
- **Occasional floaters**: **Tool Windows** (default) is a solid middle ground
- **Traditional workflow**: **Documents and Tool Windows** keeps everything classic

Pro tip: **Ctrl + double-click** on any tool window title bar to instantly float or dock it. No restart needed after changing the setting.

## Wrapping up

It's one of those "I can't believe I didn't know about this" settings. If floating windows in Visual Studio have ever annoyed you, go change this right now.

Read the [full post](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) for the details and screenshots.
