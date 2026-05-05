---
title: "VS Code 1.112: What .NET Developers Should Actually Care About"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 just dropped and it's packed with agent upgrades, an integrated browser debugger, MCP sandboxing, and monorepo support. Here's what actually matters if you're building with .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 just landed, and honestly? This one hits different if you're spending your days in .NET land. There's a lot in the [official release notes](https://code.visualstudio.com/updates/v1_112), but let me save you some scrolling and focus on what actually matters for us.

## Copilot CLI just got way more useful

The big theme this release is **agent autonomy** — giving Copilot more room to do its thing without you babysitting every step.

### Message steering and queueing

You know that moment when Copilot CLI is halfway through a task and you realize you forgot to mention something? Before, you had to wait. Now you can just send messages while a request is still running — either to steer the current response or queue up follow-up instructions.

This is huge for those longer `dotnet` scaffolding tasks where you're watching Copilot set up a project and think "oh wait, I also need MassTransit in there."

### Permission levels

This is the one I'm most excited about. Copilot CLI sessions now support three permission levels:

- **Default Permissions** — the usual flow where tools ask for confirmation before running
- **Bypass Approvals** — auto-approves everything and retries on errors
- **Autopilot** — goes fully autonomous: approves tools, answers its own questions, and keeps going until the task is done

If you're doing something like scaffolding a new ASP.NET Core API with Entity Framework, migrations, and a Docker setup — Autopilot mode means you describe what you want and go grab a coffee. It'll figure it out.

You can enable Autopilot with the `chat.autopilot.enabled` setting.

### Preview changes before delegation

When you delegate a task to Copilot CLI, it creates a worktree. Before, if you had uncommitted changes, you had to check Source Control to see what would be affected. Now the Chat view shows pending changes right there before you decide whether to copy, move, or ignore them.

Small thing, but it saves you from that "wait, what did I have staged?" moment.

## Debug web apps without leaving VS Code

The integrated browser now supports **full debugging**. You can set breakpoints, step through code, and inspect variables — all inside VS Code. No more switching to Edge DevTools.

There's a new `editor-browser` debug type, and if you already have existing `msedge` or `chrome` launch configurations, migrating is as simple as changing the `type` field in your `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

For Blazor developers, this is a game changer. You're already running `dotnet watch` in the terminal — now your debugging stays in the same window too.

The browser also got independent zoom levels (finally), proper right-click context menus, and the zoom is remembered per website.

## MCP server sandboxing

This one matters more than you might think. If you're using MCP servers — maybe you've set up a custom one for your Azure resources or database queries — they've been running with the same permissions as your VS Code process. That means full access to your filesystem, network, everything.

Now you can sandbox them. In your `mcp.json`:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

When a sandboxed server needs access to something it doesn't have, VS Code prompts you to grant permission. Much better than the "hope nobody does anything weird" approach.

> **Note:** Sandboxing is available on macOS and Linux for now. Windows support is coming — remote scenarios like WSL do work though.

## Monorepo customizations discovery

If you're working in a monorepo (and let's be honest, many enterprise .NET solutions end up as one), this solves a real pain point.

Previously, if you opened a subfolder of your repo, VS Code wouldn't find your `copilot-instructions.md`, `AGENTS.md`, or custom skills sitting at the repository root. Now with the `chat.useCustomizationsInParentRepositories` setting, it walks up to the `.git` root and discovers everything.

This means your team can share agent instructions, prompt files, and custom tools across all projects in a monorepo without everyone having to open the root folder.

## /troubleshoot for agent debugging

Ever set up custom instructions or skills and wonder why they're not being picked up? The new `/troubleshoot` skill reads agent debug logs and tells you what happened — which tools were used or skipped, why instructions didn't load, and what's causing slow responses.

Enable it with:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Then just type `/troubleshoot why is my custom skill not loading?` in chat.

You can also export and import these debug logs now, which is great for sharing with your team when something isn't working as expected.

## Image and binary file support

Agents can now read image files from disk and binary files natively. The binary files are presented in hexdump format, and image outputs (like screenshots from the integrated browser) show up in a carousel view.

For .NET developers, think: paste a screenshot of a UI bug into chat and have the agent understand what's wrong, or have it analyze the output of a Blazor component rendering.

## Automatic symbol references

Small quality-of-life improvement: when you copy a symbol name (a class, method, etc.) and paste it into chat, VS Code now automatically converts it to a `#sym:Name` reference. This gives the agent full context about that symbol without you having to manually add it.

If you want plain text instead, use `Ctrl+Shift+V`.

## Plugins can now be enabled/disabled

Previously, disabling an MCP server or plugin meant uninstalling it. Now you can toggle them on and off — both globally and per-workspace. Right-click in the Extensions view or the Customizations view and you're done.

Plugins from npm and pypi can also auto-update now, though they'll ask for approval first since updates mean running new code on your machine.

## Wrapping up

VS Code 1.112 is clearly pushing hard on the agent experience — more autonomy, better debugging, tighter security. For .NET developers, the integrated browser debugging and Copilot CLI improvements are the standout features.

If you haven't tried running a full Copilot CLI session in Autopilot mode for a .NET project yet, this release is a good time to start. Just remember to set your permissions and let it cook.

[Download VS Code 1.112](https://code.visualstudio.com/updates/v1_112) or update from within VS Code via **Help > Check for Updates**.
