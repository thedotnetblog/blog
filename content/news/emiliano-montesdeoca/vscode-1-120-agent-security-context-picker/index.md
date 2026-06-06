---
title: "VS Code 1.120: Password Prompts, Context Size Picker, GitHub Metadata in Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 is a focused release for Copilot users: secure password prompt handling, model context size picker, GitHub PR metadata in agent sessions, and session archive management."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 shipped with a set of Copilot agent improvements that are small individually but noticeably better in day-to-day use.

## Secure Password Prompt Detection in Agent Terminals

When a Copilot agent runs a terminal command that triggers a password or passphrase prompt, VS Code now detects this and shows a confirmation dialog. The dialog focuses the terminal so you can type the secret directly — and critically, secrets are never routed through the model.

This is a meaningful security improvement. Previously, agents running commands that triggered authentication prompts could create situations where users might inadvertently expose credentials. The screen reader announcement means accessibility users also get the notification.

## Context Size Picker in the Model Picker

A new context size picker lets you select how much context the model uses for a session. Different models have different context window sizes, and some workflows benefit from constraining it (lower latency, lower cost) or maximizing it (complex codebases, long-running sessions).

## GitHub PR Metadata in Agent Host Sessions

For sessions backed by a GitHub repository, VS Code now surfaces GitHub metadata — including a pull request button — in the agent host UI. Less context switching to the browser or GitHub extension when you're working on a PR.

## Chat Session Archive Management

Two improvements for the sessions Quick Pick:
- Archived sessions are hidden by default (less visual clutter)
- Searching still matches archived sessions, so you can revive one by title

Sessions are also grouped by recency by default, making recent work easier to find.

## Copilot CLI Plugin Discovery

VS Code now automatically discovers Copilot CLI user-installed plugins from `~/.copilot/installed-plugins/`. If you've set up WinUI or other domain-specific agent skills, they're picked up without manual configuration.

## Custom Diff Editor API (Preview)

For extension authors: a new `customDiffEditorProvider` proposed API lets extensions render a unified diff in a single webview with access to both original and modified documents, instead of two side-by-side custom editor views.

Original post: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
