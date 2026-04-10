---
title: "VS Code 1.116 — Agents App Gets Keyboard Navigation and File Context Completions"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 focuses on Agents app polish — dedicated keybindings, accessibility improvements, file-context completions, and CSS @import link resolution."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

VS Code 1.116 is the April 2026 release, and while it's lighter than some recent updates, the changes are focused and meaningful — especially if you're using the Agents app daily.

Here's what landed, based on the [official release notes](https://code.visualstudio.com/updates/v1_116).

## Agents app improvements

The Agents app continues to mature with usability polish that makes a real difference in daily workflows:

**Dedicated keybindings** — you can now focus the Changes view, the files tree within Changes, and the Chat Customizations view with dedicated commands and keyboard shortcuts. If you've been clicking around the Agents app to navigate, this brings full keyboard-driven workflows.

**Accessibility help dialog** — pressing `Alt+F1` in the chat input box now opens an accessibility help dialog showing available commands and keybindings. Screen reader users can also control announcement verbosity. Good accessibility benefits everyone.

**File-context completions** — type `#` in the Agents app chat to trigger file-context completions scoped to your current workspace. This is one of those small quality-of-life improvements that speeds up every interaction — no more typing full file paths when referencing code.

## CSS `@import` link resolution

A nice one for frontend developers: VS Code now resolves CSS `@import` references that use node_modules paths. You can `Ctrl+click` through imports like `@import "some-module/style.css"` when using bundlers. Small but eliminates a friction point in CSS workflows.

## Wrapping up

VS Code 1.116 is about refinement — making the Agents app more navigable, more accessible, and more keyboard-friendly. If you're spending significant time in the Agents app (and I suspect many of us are), these changes add up.

Check the [full release notes](https://code.visualstudio.com/updates/v1_116) for the complete list.
