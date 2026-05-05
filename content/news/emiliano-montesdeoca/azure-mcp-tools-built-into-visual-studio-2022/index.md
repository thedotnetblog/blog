---
title: "Azure MCP Tools Are Now Baked Into Visual Studio 2022 — No Extension Required"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP tools ship as part of the Azure development workload in Visual Studio 2022. Over 230 tools, 45 Azure services, zero extensions to install."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

If you've been using the Azure MCP tools in Visual Studio through the separate extension, you know the drill — install the VSIX, restart, hope it doesn't break, manage version mismatches. That friction is gone.

Yun Jung Choi [announced](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) that Azure MCP tools now ship directly as part of the Azure development workload in Visual Studio 2022. No extension. No VSIX. No restart dance.

## What this actually means

Starting with Visual Studio 2022 version 17.14.30, the Azure MCP Server is bundled with the Azure development workload. If you already have that workload installed, you just need to toggle it on in GitHub Copilot Chat and you're done.

Over 230 tools across 45 Azure services — accessible directly from the chat window. List your storage accounts, deploy an ASP.NET Core app, diagnose App Service issues, query Log Analytics — all without opening a browser tab.

## Why this matters more than it sounds

Here's the thing about developer tooling: every extra step is friction, and friction kills adoption. Having MCP as a separate extension meant version mismatches, installation failures, and one more thing to keep updated. Baking it into the workload means:

- **Single update path** through the Visual Studio Installer
- **No version drift** between the extension and the IDE
- **Always current** — the MCP Server updates with regular VS releases

For teams standardizing on Azure, this is a big deal. You install the workload once, enable the tools, and they're there for every session.

## What you can do with it

The tools cover the full development lifecycle through Copilot Chat:

- **Learn** — ask about Azure services, best practices, architecture patterns
- **Design & develop** — get service recommendations, configure app code
- **Deploy** — provision resources and deploy directly from the IDE
- **Troubleshoot** — query logs, check resource health, diagnose production issues

A quick example — type this in Copilot Chat:

```
List my storage accounts in my current subscription.
```

Copilot calls the Azure MCP tools behind the scenes, queries your subscriptions, and returns a formatted list with names, locations, and SKUs. No portal needed.

## How to enable it

1. Update to Visual Studio 2022 **17.14.30** or higher
2. Make sure the **Azure development** workload is installed
3. Open GitHub Copilot Chat
4. Click the **Select tools** button (the two wrenches icon)
5. Toggle **Azure MCP Server** on

That's it. It stays enabled across sessions.

## One caveat

The tools are disabled by default — you need to opt in. And VS 2026-specific tools aren't available in VS 2022. Tool availability also depends on your Azure subscription permissions, same as the portal.

## The bigger picture

This is part of a clear trend: MCP is becoming the standard way to surface cloud tools in developer IDEs. We've already seen the [Azure MCP Server 2.0 stable release](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) and MCP integrations across VS Code and other editors. Having it built into Visual Studio's workload system is the natural progression.

For us .NET developers who live in Visual Studio, this removes yet another reason to context-switch to the Azure portal. And honestly, the less tab-switching, the better.
