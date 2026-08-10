---
title: "Visual Studio Code 1.124"
description: "Visual Studio Code 1.124 adds scoped Agents window history, multi-chat local sessions, background send, session keyboard navigation, bulk close, and regex flags for folding markers."
date: 2026-10-29
author: "Emiliano Montesdeoca"
tags: ["Visual Studio Code", "Release", "Productivity", "Development Tools", "Agent Window"]
slug: vscode-1-124-release
---

Original source: [Visual Studio Code 1.124](https://code.visualstudio.com/updates/v1_124)

Visual Studio Code 1.124 is a focused release for developers who spend substantial time in the Agents window. The changes are small enough to miss in a broad feature list, but they address the friction that appears when several agent sessions, prompts, and tool-assisted tasks are active at once.

## Chat history finally follows the session

In the Agents window, pressing `Up` or `Down` in the chat input now navigates prompts submitted in the current session only. Previous behavior included prompts from other sessions, which made history less useful as the number of conversations grew.

Scoped history is a simple distinction with a practical payoff. A developer can stay inside a debugging conversation and recall an earlier prompt from that conversation without stepping through unrelated architecture questions, documentation work, or repository investigations from other sessions.

The change does not make a session a durable project record. Important decisions still belong in issues, pull requests, or repository documentation. Session-local history is best treated as working context that helps continue the task in front of you.

## More control over local agent sessions

The release adds multi-chat support for local sessions in the Agents window. It also adds background send: press `Alt+Enter` or `Alt`-click Send to start a session without navigating into it. That lets you submit work and immediately compose the next message while keeping your current view.

For a .NET developer, this makes it easier to separate work by intent. One local session can inspect a failing test, another can reason about a refactoring, and a third can review a deployment change. The sessions remain separate, so the context for one investigation does not need to be carried into another by accident.

Background send is especially useful for longer tasks. It does not make the model complete faster, and it does not remove the need to review tool activity. It simply lets the developer keep arranging the next piece of work while a session starts in the background.

## Keyboard navigation for a busy grid

The Agents window sessions grid now supports direct keyboard navigation and bulk close:

- **`Ctrl+1` through `Ctrl+9`** on Windows and Linux, or **`Cmd+1` through `Cmd+9`** on macOS, focuses a session by position.
- **`Ctrl+K Ctrl+W`** on Windows and Linux, or **`Cmd+K Cmd+W`** on macOS, closes all sessions at once.

These shortcuts are useful when the session grid becomes part of the normal development workspace rather than a place visited occasionally. Direct positioning reduces repetitive clicking, while bulk close gives the end of an investigation a clear cleanup action.

Keep the grid organized enough that position-based shortcuts remain predictable. A shortcut that jumps to “session five” is most useful when old sessions are closed or renamed as work changes.

## Regex flags for folding markers

VS Code 1.124 also updates folding marker patterns in `language-configuration.json`. Folding markers can now use an object form with a `pattern` and `flags`, enabling options such as case-insensitive matching.

For extension authors and teams maintaining custom language configurations, this provides more control over how regions are recognized. A configuration can express a pattern and its regular-expression flags together rather than relying on a pattern that handles every case manually.

```json
"folding": {
  "markers": {
    "start": {
      "pattern": "^\\s*#region",
      "flags": "i"
    }
  }
}
```

The exact configuration belongs in the language extension’s existing schema and conventions, so test a customized marker with the files and casing used by the language. The release note documents the new `{ pattern, flags }` form; it does not change the meaning of every existing folding configuration.

## What .NET teams should try

1. Keep related agent work in separate local sessions and use scoped history when revisiting a prompt.
2. Use background send for tasks that can start while you prepare the next investigation.
3. Give the sessions grid a simple cleanup habit so keyboard positions remain useful.
4. Try the direct navigation and bulk-close shortcuts in the Agents window.
5. If you maintain custom language support, test folding marker flags in `language-configuration.json`.

VS Code 1.124 is an incremental release, but incremental improvements matter when an editor is also the control surface for several agent workflows. Better session boundaries, less navigation overhead, and more expressive folding configuration make the daily loop easier to supervise.