---
title: "Azure MCP Server Is Now a .mcpb — Install It Without Any Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "The Azure MCP Server is now available as an MCP Bundle (.mcpb) — download it, drag it into Claude Desktop, and you're done. No Node.js, Python, or .NET runtime required."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

You know what was annoying about setting up MCP servers? You needed a runtime. Node.js for the npm version, Python for pip/uvx, .NET SDK for the dotnet flavor, Docker if you wanted containers. Just to get a tool connected to your AI client.

The [Azure MCP Server just changed that](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). It's now available as an `.mcpb` — an MCP Bundle — and the setup is drag-and-drop.

## What's an MCP Bundle?

Think of it like a VS Code extension (`.vsix`) or a browser extension (`.crx`), but for MCP servers. A `.mcpb` file is a self-contained ZIP archive that includes the server binary and all its dependencies. Everything needed to run on your platform, packaged together.

The end result: you download one file, open it in a supported client, and the server runs. No runtime to install, no `package.json` to manage, no version conflicts.

## How to install it

Three steps:

**1. Download the bundle for your platform**

Go to the [GitHub Releases page](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) and grab the `.mcpb` file for your OS and architecture. Make sure you pick the right one — `osx-arm64` for Apple Silicon, `osx-x64` for Intel Mac, etc.

**2. Install in Claude Desktop**

The easiest way: drag and drop the `.mcpb` file into the Claude Desktop window while you're on the Extensions settings page (`☰ → File → Settings → Extensions`). Review the server details, click Install, confirm. Done.

> Tip: You can also set Claude Desktop as the default app for `.mcpb` files and double-click to install.

**3. Authenticate to Azure**

```bash
az login
```

That's it. The Azure MCP Server uses your existing Azure credentials.

## What you can do with it

Once installed, you have access to 100+ Azure service tools directly from your AI client:

- Query and manage Cosmos DB, Storage, Key Vault, App Service, Foundry
- Generate `az` CLI commands for any task
- Create Bicep and Terraform templates
- Get architecture recommendations and diagnostics

Try prompts like:
- "List all resource groups in my subscription"
- "Generate a Bicep template for a web app with a SQL database"
- "What Cosmos DB databases do I have?"
- "Show me the secrets in my Key Vault named my-vault"

## Which install method should you use?

| Method | Best for |
|--------|----------|
| `.mcpb` | Claude Desktop users who want zero-config |
| VS Code Extension | Developers working in VS Code + GitHub Copilot |
| npm/npx | Developers who already have Node.js |
| pip/uvx | Python developers |
| Docker | CI/CD pipelines and containers |

All methods give you the same tools. The `.mcpb` is just the most frictionless path for Claude Desktop users.

## Why this matters

MCP servers are genuinely useful — they let AI clients interact with external systems in a structured way. But the setup friction has been a real barrier, especially for users who aren't developers or who just don't want to manage runtimes for every tool they install.

The `.mcpb` format feels like the right direction. It's the same principle as VS Code extensions or browser extensions: one file, platform-native binary, install and go.

If the MCP ecosystem keeps moving this direction, connecting AI clients to services will get a lot simpler.

## Get started

- **Download**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repo**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Check the [full post](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/) for troubleshooting tips and a comparison of all install methods.
