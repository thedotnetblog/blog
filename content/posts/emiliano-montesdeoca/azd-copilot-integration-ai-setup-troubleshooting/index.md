---
title: "azd + GitHub Copilot: AI-Powered Project Setup and Smarter Error Fixes"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "The Azure Developer CLI now integrates with GitHub Copilot to scaffold your project and fix deployment errors — all without leaving the terminal."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

You know that moment when you want to deploy an existing app to Azure and suddenly find yourself staring at a blank `azure.yaml`, trying to remember whether your Express API should use Container Apps or App Service? Yeah, that moment. It just got a whole lot shorter.

The Azure Developer CLI (`azd`) now integrates with GitHub Copilot in two meaningful ways: AI-assisted project scaffolding during `azd init`, and intelligent error troubleshooting when deployments go sideways. Both features stay entirely in your terminal, which is exactly where I want them.

## Setting Up with Copilot During azd init

When you run `azd init`, there's now a "Set up with GitHub Copilot (Preview)" option. Select it and Copilot analyzes your codebase to generate the `azure.yaml`, infrastructure templates, and Bicep modules — based on your actual code, not a template guess.

```
azd init
# Select: "Set up with GitHub Copilot (Preview)"
```

For this to work you'll need:

- **azd 1.23.11 or later** — check with `azd version` or update with `azd update`
- **An active GitHub Copilot subscription** (Individual, Business, or Enterprise)
- **GitHub CLI (`gh`)** — `azd` will prompt for login if needed

What I find genuinely useful here is that it works both ways. Building from scratch? Copilot helps you set up the right Azure services from the start. Have an existing app you've been putting off deploying? Point Copilot at it and it generates the configuration without you having to restructure anything.

### What it actually does

Say you have a Node.js Express API with a PostgreSQL dependency. Instead of manually figuring out whether to target Container Apps or App Service, and then writing Bicep from scratch, Copilot detects your stack and generates:

- An `azure.yaml` with the right `language`, `host`, and `build` settings
- A Bicep module for Azure Container Apps
- A Bicep module for Azure Database for PostgreSQL

And it runs preflight checks before touching anything — verifies your git working directory is clean, asks for MCP server tool consent upfront. Nothing happens without you knowing exactly what's about to change.

## Copilot-Powered Error Troubleshooting

Deployment errors are a fact of life. Missing parameters, permission issues, SKU availability problems — and the error message rarely tells you the one thing you actually need to know: *how to fix it*.

Without Copilot, your loop looks like: copy the error → search docs → read through three unrelated Stack Overflow answers → run some `az` CLI commands → try again and hope. With Copilot integrated into `azd`, that loop collapses. When any `azd` command fails, it immediately offers four options:

- **Explain** — plain-language description of what went wrong
- **Guidance** — step-by-step fix instructions
- **Diagnose and Guide** — full analysis + Copilot applies the fix (with your approval) + optional retry
- **Skip** — handle it yourself

The key thing: Copilot already has context about your project, the command that failed, and the error output. Its suggestions are specific to *your situation*, not generic docs.

### Real examples where this shines

**Resource provider not registered:**
```
ERROR: deployment failed: MissingSubscriptionRegistration:
The subscription is not registered to use namespace 'Microsoft.App'.
```
This trips up anyone deploying to a fresh subscription. Copilot can register the provider and rerun the deployment automatically.

**SKU not available:**
```
ERROR: deployment failed: SkuNotAvailable:
The requested VM size 'Standard_D2s_v3' is not available in location 'westus'.
```
Copilot explains which VM size or region is blocked and suggests alternatives that are actually available in your subscription.

**Storage account name collision:**
```
ERROR: deployment failed: StorageAccountAlreadyTaken:
The storage account named 'myappstorage' is already taken.
```
Global uniqueness bites everyone at least once. Copilot suggests adding your environment name or a random suffix to your Bicep parameters.

### Set a default behavior

If you always want the same option, skip the interactive prompt:

```
azd config set copilot.errorHandling.category troubleshoot
```

Options: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. You can also enable auto-fix and retry:

```
azd config set copilot.errorHandling.fix allow
```

Reset to interactive at any time:

```
azd config unset copilot.errorHandling.category
```

## Why this matters for .NET developers

If you're building on Azure — whether it's a .NET Aspire app, a containerized API, or anything in between — `azd` has been the tool to know for a while now. This Copilot integration removes the last bit of friction that used to make it feel like you needed a cheat sheet just to get started.

The scaffolding piece is great for brownfield projects. You've got an ASP.NET Core app running locally, it works perfectly, but getting it *onto* Azure has always required a bit of infrastructure knowledge. Now Copilot bridges that gap. And the error troubleshooting feature is something I genuinely wish I'd had the last time I spent 45 minutes debugging a `SkuNotAvailable` error across three regions.

## Wrapping up

This is exactly the kind of Copilot integration that adds real value — not AI for AI's sake, but AI that understands your context and saves you actual time. Try it out by running `azd update` to get the latest version, then use `azd init` on your next project. The team is working on deeper features including Copilot-assisted infrastructure customization, so now's a good time to [sign up for user research](https://aka.ms/azd-user-research-signup) if you want to influence what comes next.

Read the [original announcement here](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
