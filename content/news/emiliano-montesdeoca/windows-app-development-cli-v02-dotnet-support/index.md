---
title: "Windows App Development CLI v0.2 Gives .NET Projects a First-Class Packaging Path"
description: "The Windows App Development CLI v0.2 adds direct .csproj support, manifest placeholders, and Store tooling for .NET Windows app workflows."
date: 2026-08-23
author: "Emiliano Montesdeoca"
tags: [windows, dotnet, msix]
slug: windows-app-development-cli-v02-dotnet-support
---

Original source: [Windows App Development CLI v0.2: .NET support, manifest placeholders, “winapp store” and more!](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-2-net-support-manifest-placeholders-winapp-store-and-more/)

## Packaging Should Understand the Project It Packages

The Windows App Development CLI v0.2 moves .NET projects toward a more natural packaging workflow. Instead of treating a .NET application as a generic folder that needs a separate configuration file, the CLI can work directly with the project file and its existing build conventions.

That is a meaningful change for WinUI, WPF, WinForms, and other Windows applications built with .NET. The project file already describes the target framework and dependencies. Keeping packaging-related configuration close to that source of truth reduces the chance that a project and its package definition drift apart.

The release is still preview software, but the direction is clear: Windows packaging tools should fit the .NET build rather than ask .NET developers to maintain a parallel description of the application.

## Direct .csproj Support

When `winapp init` finds a .csproj, the new flow can configure the project directly. The source describes updates to the Windows target framework, Windows App SDK and related NuGet references, plus generated manifest and asset files.

That makes the packaging setup visible in normal project review. A package dependency can be examined alongside the rest of the NuGet graph, and changes can move through the same pull request and CI process as application code.

There is a migration consequence. Existing scripts that expect a generated `winapp.yaml` for every project need to distinguish .NET projects from other supported stacks. Do not assume that a file disappearing means packaging has been lost; in the new .NET flow, the project file is the intended configuration boundary.

The practical check is simple: inspect the generated project diff, confirm the target framework and package versions, and build the app before relying on the new packaging path in CI.

## Manifest Placeholders Help CI

Executable names can vary between configurations and project setups. Hardcoding them in an appx manifest makes Debug, Release, and matrix builds more fragile.

Version 0.2 adds Visual Studio-style placeholders such as `$targetnametoken$` and `$targetentrypoint$`. The CLI can resolve those values during packaging, and the source describes an explicit executable option for cases where more than one executable is present.

This is useful for teams building Windows apps in GitHub Actions or Azure Pipelines. One manifest can travel through the pipeline without a script rewriting the executable name for every configuration. It also keeps the package definition closer to the information MSBuild already knows.

Placeholders do not remove the need to verify the package. Add a CI step that inspects the generated manifest and package contents, especially when a solution produces multiple executables or uses custom build output paths.

## Store Publishing Has One Entry Point

The CLI also adds a `winapp store` command that proxies the Microsoft Store Developer CLI. The tool can manage the required binary on first use, which means developers do not need a separate installation and PATH setup just to reach Store operations.

The benefit is operational rather than glamorous. A team can keep the local workflow centered on the Windows App Development CLI for packaging and Store-related steps. That reduces setup differences between developer machines and build agents.

Do keep publishing credentials and release approvals outside the project file. A unified command is not a reason to blur the boundary between building a package and authorizing a production Store release.

## Preview Caveats and Migration Work

The release changes a few assumptions. Certificate generation is now explicit rather than an automatic side effect of initialization. The CLI also uses the global NuGet cache instead of a local `.winapp/packages` directory, and .NET projects no longer receive a separate `winapp.yaml` from initialization.

Review scripts for all three behaviors. Add certificate generation deliberately where local identity setup is required, remove hardcoded paths to the old package cache, and update any pipeline logic that reads the YAML file for .NET projects.

Because this is preview software, avoid making it the only path for a locked-down production release until your build and signing process is stable on the version you intend to use. Preview tooling can change its configuration shape, and packaging is too close to the release boundary for an untested migration.

## What .NET Developers Should Do

For a new Windows App SDK project, try v0.2 in a disposable branch and inspect everything it adds to the .csproj and manifest. For an existing project, make a migration checklist around certificates, package-cache paths, and CI scripts before changing the default workflow.

The CLI is heading in the right direction. Direct project integration, portable manifest placeholders, and a bundled Store entry point reduce friction without replacing the .NET build system. Adopt it experimentally now, keep the preview boundary visible, and promote it into production only after the generated package and signing pipeline are repeatable.