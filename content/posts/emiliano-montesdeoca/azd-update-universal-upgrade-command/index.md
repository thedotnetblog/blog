---
title: "azd update — One Command to Rule All Your Package Managers"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "The Azure Developer CLI now has a universal update command that works regardless of how you installed it — winget, Homebrew, Chocolatey, or install script."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

You know that "A new version of azd is available" message that pops up every few weeks? The one you dismiss because you can't remember whether you installed `azd` via winget, Homebrew, or that curl script you ran six months ago? Yeah, that's finally fixed.

Microsoft just shipped [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — a single command that updates the Azure Developer CLI to the latest version regardless of how you originally installed it. Windows, macOS, Linux — doesn't matter. One command.

## How it works

```bash
azd update
```

That's it. If you want early access to new features, you can switch to the daily insiders build:

```bash
azd update --channel daily
azd update --channel stable
```

The command detects your current installation method and uses the appropriate update mechanism under the hood. No more "wait, did I use winget or choco on this machine?"

## The small catch

`azd update` ships starting with version 1.23.x. If you're on an older version, you'll need to do one last manual update using your original installation method. After that, `azd update` handles everything going forward.

Check your current version with `azd version`. If you need a fresh install, the [install docs](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) have you covered.

## Why it matters

This is a small quality-of-life improvement, but for those of us who use `azd` daily for deploying AI agents and Aspire apps to Azure, staying current means fewer "this bug was already fixed in the latest version" moments. One less thing to think about.

Read the [full announcement](https://devblogs.microsoft.com/azure-sdk/azd-update/) and Jon Gallant's [deeper dive](https://blog.jongallant.com/2026/04/azd-update) for more context.
