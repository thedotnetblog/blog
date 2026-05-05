---
title: "azd Now Lets You Run and Debug AI Agents Locally — Here's What Changed in March 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "The Azure Developer CLI shipped seven releases in March 2026. The highlights: a local run-and-debug loop for AI agents, GitHub Copilot integration in project setup, and Container App Jobs support."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

Seven releases in one month. That's what the Azure Developer CLI (`azd`) team pushed in March 2026, and the headline feature is the one I've been waiting for: **a local run-and-debug loop for AI agents**.

PC Chan [published the full roundup](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), and while there's a lot in there, let me filter it down to what actually matters for .NET developers building AI-powered apps.

## Run and debug AI agents without deploying

This is the big one. The new `azure.ai.agents` extension adds a set of commands that give you a proper inner-loop experience for AI agents:

- `azd ai agent run` — starts your agent locally
- `azd ai agent invoke` — sends messages to it (local or deployed)
- `azd ai agent show` — displays container status and health
- `azd ai agent monitor` — streams container logs in real time

Before this, testing an AI agent meant deploying to Microsoft Foundry every time you made a change. Now you can iterate locally, test your agent's behavior, and only deploy when you're ready. If you've been building agents with the Microsoft Agent Framework or Semantic Kernel, this changes your daily workflow.

The invoke command works against both local and deployed agents, which means you can use the same testing workflow regardless of where the agent is running. That's the kind of detail that saves you from maintaining two sets of test scripts.

## GitHub Copilot scaffolds your azd project

`azd init` now offers a "Set up with GitHub Copilot (Preview)" option. Instead of manually answering prompts about your project structure, a Copilot agent scaffolds the configuration for you. It checks for a dirty working directory before modifying anything and asks for MCP server tool consent upfront.

When a command fails, `azd` now offers AI-assisted troubleshooting: pick a category (explain, guidance, troubleshoot, or skip), let the agent suggest a fix, and retry — all without leaving the terminal. For complex infrastructure setups, that's a real time saver.

## Container App Jobs and deployment improvements

A few deployment features worth noting:

- **Container App Jobs**: `azd` now deploys `Microsoft.App/jobs` through the existing `host: containerapp` config. Your Bicep template determines whether the target is a Container App or a Job — no extra setup.
- **Configurable deployment timeouts**: New `--timeout` flag on `azd deploy` and a `deployTimeout` field in `azure.yaml`. No more guessing the default 1200-second limit.
- **Remote build fallback**: When remote ACR build fails, `azd` falls back to local Docker/Podman build automatically.
- **Local preflight validation**: Bicep parameters get validated locally before deploying, catching missing params without a round-trip to Azure.

## Developer experience polish

Some smaller improvements that add up:

- **Automatic pnpm/yarn detection** for JS/TS projects
- **pyproject.toml support** for Python packaging
- **Local template directories** — `azd init --template` now accepts filesystem paths for offline iteration
- **Better error messages** in `--no-prompt` mode — all missing values reported at once with resolution commands
- **Build environment variables** injected into all framework build subprocesses (.NET, Node.js, Java, Python)

That last one is subtle but important: your .NET build now has access to `azd` environment variables, which means you can do build-time configuration injection without extra scripting.

## Wrapping up

The local AI agent debugging loop is the star of this release, but the accumulation of deployment improvements and DX polish makes `azd` feel more mature than ever. If you're deploying .NET apps to Azure — especially AI agents — this update is worth the install.

Check the [full release notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) for every detail, or get started with [azd install](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd).
