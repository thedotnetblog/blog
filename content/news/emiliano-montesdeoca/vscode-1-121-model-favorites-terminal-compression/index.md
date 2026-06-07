---
title: "VS Code 1.121: Pin Favorite Models, Terminal Output Compression, Agent SSH"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 adds model favorites, expanded terminal tool output compression for test runners and build tools, idle-silence timer for background terminals, and keyboard-interactive SSH in agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 continues the Copilot agent quality improvements from 1.120, with a focus on model management and terminal behavior.

## Pin Favorite Models

The model picker now supports pinning. If you always reach for the same model or two, pin them to the top of the list. Reduces the scrolling when you have access to many models across multiple providers.

## Expanded Terminal Output Compression

The agent terminal tool already compressed output for common commands. 1.121 expands this to cover test runners and build tools:

- **Test runners:** `pytest`, `jest`, `cargo test`
- **Build tools:** `tsc`, `cargo build`, `make`
- **Linters, Docker, package managers**

Long build output and test failure reports are compressed into relevant excerpts before being passed to the model. This keeps context usage manageable when the agent runs build cycles or test suites, which can produce thousands of lines of output.

## Idle-Silence Timer for Background Terminals

A new idle-silence timer for the `run_in_terminal` tool: if a sync command produces no output for a configurable period, it's automatically promoted to background execution. This prevents long-running commands from blocking the agent when they're silently processing. You get a terminal ID to check on later.

## VSCODE_AGENT Environment Variable

When Copilot Chat runs commands in the terminal, a `VSCODE_AGENT` environment variable is now set. Useful if you have scripts or tools that behave differently when called from an agent session versus interactively.

## Add to Chat from Browser

Right-clicking in the integrated browser now shows an "Add to Chat" option. Select content from a web page and add it directly to your Copilot Chat context without copy-pasting.

## Fixed: Multi-Line Shell Commands in Agent Host

A bug fix that's overdue: multi-line shell commands in the Agent Host terminal tool now work correctly. Previously these could fail or produce incorrect behavior.

## Keyboard-Interactive SSH Authentication

Agent Host SSH connections now support keyboard-interactive authentication — the fallback auth method used by some SSH servers (including some older corporate configurations). Agents working on remote SSH hosts are less likely to hit auth failures.

Original post: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
