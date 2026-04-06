---
title: "VS Code 1.115 — Background Terminal Notifications, SSH Agent Mode, and More"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 brings background terminal notifications for agents, SSH remote agent hosting, file paste in terminals, and session-aware edit tracking. Here's what matters for .NET developers."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

VS Code 1.115 just [dropped](https://code.visualstudio.com/updates/v1_115), and while it's a lighter release in terms of headline features, the agent-related improvements are genuinely useful if you're working with AI coding assistants daily.

Let me highlight what's actually worth knowing.

## Background terminals talk back to agents

This is the standout feature. Background terminals now automatically notify agents when commands complete, including the exit code and terminal output. Input prompts in background terminals are also detected and surfaced to the user.

Why does this matter? If you've used Copilot's agent mode to run build commands or test suites in the background, you know the pain of "did that finish yet?" — background terminals were essentially fire-and-forget. Now the agent gets notified when your `dotnet build` or `dotnet test` completes, sees the output, and can react accordingly. It's a small change that makes agent-driven workflows significantly more reliable.

There's also a new `send_to_terminal` tool that lets agents send commands to background terminals with user confirmation, fixing the issue where `run_in_terminal` with a timeout would move terminals to the background and make them read-only.

## SSH remote agent hosting

VS Code now supports connecting to remote machines over SSH, automatically installing the CLI and starting it in agent host mode. This means your AI agent sessions can target remote environments directly — useful for .NET developers who build and test on Linux servers or cloud VMs.

## Edit tracking in agent sessions

File edits made during agent sessions are now tracked and restored, with diffs, undo/redo, and state restoration. If an agent makes changes to your code and something goes wrong, you can see exactly what changed and roll it back. Peace of mind for letting agents modify your codebase.

## Browser tab awareness and other improvements

A few more quality-of-life additions:

- **Browser tab tracking** — chat can now track and link to browser tabs opened during a session, so agents can reference web pages you're looking at
- **File paste in terminal** — paste files (including images) into the terminal with Ctrl+V, drag-and-drop, or right-click
- **Test coverage in minimap** — test coverage indicators now show in the minimap for a quick visual overview
- **Pinch-to-zoom on Mac** — integrated browser supports pinch-to-zoom gestures
- **Copilot entitlements in Sessions** — status bar shows usage info in the Sessions view
- **Favicon in Go to File** — open web pages show favicons in the quick pick list

## Wrapping up

VS Code 1.115 is an incremental release, but the agent improvements — background terminal notifications, SSH agent hosting, and edit tracking — add up to a noticeably smoother experience for AI-assisted development. If you're using Copilot's agent mode for .NET projects, these are the kinds of quality-of-life fixes that reduce friction daily.

Check out the [full release notes](https://code.visualstudio.com/updates/v1_115) for every detail.
