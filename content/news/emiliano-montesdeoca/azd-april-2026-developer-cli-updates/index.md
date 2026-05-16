---
title: "Azure Developer CLI (azd) April 2026 Updates"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd shipped five releases in April 2026, headlined by multi-language hook support for Python, JavaScript, TypeScript, and .NET — plus azd update public preview, AI quota preflight checks, and more."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

[Azure Developer CLI (azd) shipped five releases in April 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14 through 1.24.2), with the big story being hooks that now run in Python, JavaScript, TypeScript, and .NET — not just Bash and PowerShell.

## Multi-language hooks in azure.yaml

Hooks can now point to `.py`, `.js`, `.ts`, or `.cs` files in addition to shell scripts. Each language gets automatic dependency resolution:

- **Python** — detects `requirements.txt` or `pyproject.toml`, creates a virtualenv, and installs deps before running. Configure the env name with `virtualEnvName`.
- **JavaScript / TypeScript** — detects `package.json` and runs `npm install` automatically. TypeScript executes via `npx tsx` with no compile step needed. Choose your package manager with the `packageManager` config block.
- **.NET** — runs `.cs` files with `dotnet run`. Single-file scripts are supported on .NET 10+. Configure the target framework via the `configuration/framework` block.

This means teams that already live in one of these languages no longer need to maintain a separate Bash or PowerShell hook just to wire up provisioning lifecycle events.

## azd update graduates to public preview

`azd update` is now in public preview across all platforms. A single command handles the update regardless of how azd was originally installed — no more tracking down Homebrew, WinGet, or MSI paths separately.

## Non-interactive mode via AZD_NON_INTERACTIVE

Setting `AZD_NON_INTERACTIVE=true` (or using `--non-interactive` / `--no-prompt`) now produces consistent, deterministic failures in CI/CD pipelines when a required input cannot be resolved automatically. Previously the behavior was inconsistent across commands.

## AI model quota preflight check

`azd provision` validates Azure Cognitive Services quota before attempting to provision AI model resources. Deployments that would fail due to quota limits now surface the error early in the process rather than partway through provisioning.

## "Fix this error" in Copilot troubleshooting

The azd Copilot troubleshooting integration gains the ability to directly apply a suggested fix — not just describe it. When the agent identifies a fixable issue, it can make the change in-place.

## Custom provisioning providers and Key Vault secret resolver

Extension authors can now register alternative infrastructure backends with `WithProvisioningProvider()`. Separately, azd automatically resolves `@Microsoft.KeyVault(...)` references before passing configuration to extensions, removing the need for manual secret resolution in custom providers.

## Template and watch-mode exclusions

Two new ignore files give finer control over file handling:
- **`.azdignore`** — excludes contributor-only files (docs, CI configs) from template copies so end users get a clean project scaffold.
- **`.azdxignore`** — excludes directories from triggering rebuilds during `azd x watch`, reducing noise during iterative development.

## Reserved-name preflight and docker.network option

azd now warns when predicted resource names would contain Azure reserved words (`MICROSOFT`, `WINDOWS`, or the `LOGIN` prefix) before provisioning begins. A new `docker.network` option passes `--network` to `docker build`, which is useful in corporate proxy environments that require a specific Docker network.

## Security fixes

The Windows MSI package now includes code-signing verification. A separate fix closes an environment variable leak that could expose values across extension command boundaries.

---

A packed month — the multi-language hook support in particular removes a real friction point for teams not working primarily in Bash. See the [full release notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) for the complete changelog across all five releases.
