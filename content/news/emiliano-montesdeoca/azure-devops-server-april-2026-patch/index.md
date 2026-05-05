---
title: "Azure DevOps Server April 2026 Patch — PR Completion Fix and Security Updates"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server gets Patch 3 with a fix for PR completion failures, improved sign-out validation, and restored GitHub Enterprise Server PAT connections."
tags:
  - azure-devops
  - devops
  - patches
---

Quick heads-up for teams running self-hosted Azure DevOps Server: Microsoft released [Patch 3 for April 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) with three targeted fixes.

## What's fixed

- **Pull request completion failures** — a null reference exception during work item auto-completion could cause PR merges to fail. If you've hit random PR completion errors, this is likely the cause
- **Sign-out redirect validation** — improved validation during sign-out to prevent potential malicious redirects. This is a security fix worth applying promptly
- **GitHub Enterprise Server PAT connections** — creating Personal Access Token connections to GitHub Enterprise Server was broken, now it's restored

## How to update

Download [Patch 3](https://aka.ms/devopsserverpatch3) and run the installer. To verify the patch is applied:

```bash
<patch-installer>.exe CheckInstall
```

If you're running Azure DevOps Server on-premises, Microsoft strongly recommends staying on the latest patch for both security and reliability. Check the [release notes](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) for full details.
