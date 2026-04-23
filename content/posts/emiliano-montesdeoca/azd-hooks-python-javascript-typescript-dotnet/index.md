---
title: "azd Hooks in Python, TypeScript, and .NET: Stop Fighting Shell Scripts"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "The Azure Developer CLI now lets you write hooks in Python, JavaScript, TypeScript, or .NET. No more context-switching to Bash just to run a migration script."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

If you've ever had a fully .NET project and still found yourself writing Bash scripts just to run azd hooks, you know the pain. Why switch to shell syntax just for a pre-provision step when everything else in your project is C#?

That frustration is now officially solved. The Azure Developer CLI [just shipped multi-language hook support](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), and it's exactly as good as it sounds.

## Hooks, quickly, if you're not familiar

Hooks are scripts that run at key points in the `azd` lifecycle — before provisioning, after deployment, and more. They're defined in `azure.yaml` and let you inject custom logic without forking the CLI itself.

Previously you were limited to Bash and PowerShell. Now you can use **Python, JavaScript, TypeScript, or .NET** — and `azd` handles the rest automatically.

## How the detection works

You just point the hook at a file and `azd` infers the language from the extension:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

That's it. No extra config. If the extension is ambiguous, you can add an explicit `kind: python` (or whatever) to override.

## Language-specific details worth knowing

### Python

Drop a `requirements.txt` or `pyproject.toml` next to your script (or anywhere up the directory tree) and `azd` creates a virtual environment, installs deps, and runs your script:

```
hooks/
├── setup.py
└── requirements.txt
```

No virtualenv management on your end. `azd` walks up from the script location to find the nearest project file.

### JavaScript and TypeScript

Same pattern — put a `package.json` near your script and `azd` runs `npm install` first. For TypeScript, it uses `npx tsx` so there's no compile step and no `tsconfig.json` required:

```
hooks/
├── seed.ts
└── package.json
```

Want to use pnpm or yarn? There's a `config.packageManager` option for that.

### .NET

Two modes here, which is nice:

- **Project mode**: If there's a `.csproj` next to the script, `azd` runs `dotnet restore` and `dotnet build` automatically.
- **Single-file mode**: On .NET 10+, you can drop a standalone `.cs` file and it runs directly via `dotnet run script.cs`. No project file needed.

```yaml
hooks:
  postprovision:
    run: ./hooks/migrate.cs
```

If you're already on .NET 10, single-file mode is honestly the cleanest option for simple migration or seeding scripts. No project scaffolding, no `.csproj` to maintain.

## Executor-specific config

Each language supports an optional `config` block when you need to tweak the defaults:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postdeploy:
    run: ./hooks/seed.py
    config:
      virtualEnvName: .venv
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

You can also mix formats in the same `hooks:` block — different languages for different lifecycle events, platform-specific overrides for Windows vs. Linux, whatever you need.

## Why this matters for .NET developers

The boring answer is "consistency." But honestly it goes deeper than that. Hooks are often the last place in an azd-based project that forces you into a different language context. Now your entire deployment pipeline — from app code to infrastructure scripts to lifecycle hooks — can live in one language.

More practically: you can now reuse your existing .NET utilities in hooks. Have a shared class library for database schema management? Just reference it in your hook project. Have a Python data-seeding script you already wrote? Drop it straight into `azure.yaml`.

## Wrapping up

This is one of those changes that sounds small but quietly removes a lot of friction from daily azd workflows. Multi-language hook support is available now — check the [official post](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) for the full docs, and head to [the azd GitHub repo](https://github.com/Azure/azure-dev) to try it out on your next project.
