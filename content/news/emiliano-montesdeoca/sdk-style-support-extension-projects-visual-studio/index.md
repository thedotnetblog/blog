---
title: "SDK-Style Support for Extension Projects in Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 brings officially supported SDK-style project format to VSSDK-based extensions, cutting build times by up to 75% and reducing project files to ~20 lines."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

[SDK-Style support for VSSDK-based extension projects](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) is now officially in Visual Studio 18.5 — classic VSIX extension projects can ditch the old MPF-style `.csproj` format.

## What changes in the project file

The biggest visible change is how much smaller the project file gets. A typical VSSDK extension now looks like this:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net472</TargetFramework>
    <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup>
    <VsixDeployOnDebug>true</VsixDeployOnDebug>
    <GeneratePkgDefFile>true</GeneratePkgDefFile>
  </PropertyGroup>
  <ItemGroup><ProjectCapability Include="CreateVsixContainer" /></ItemGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.VisualStudio.SDK" Version="17.14.40265" ExcludeAssets="runtime" />
    <PackageReference Include="Microsoft.VSSDK.BuildTools" Version="18.5.38461" />
  </ItemGroup>
</Project>
```

`VSSDKBuildToolsAutoSetup=true` applies sensible defaults: `CreateVsixContainer=true` and legacy `DeployExtension=false`. That single property replaces a significant chunk of what previously had to be spelled out explicitly.

## Build time improvements

Fast Up-To-Date Check and incremental build support are included. For large solutions with small changes, this translates to **up to 75% build time reduction** — meaningful if you're iterating on an extension inside a large host solution.

## New projects vs existing

New extension projects created in 18.5 automatically use SDK-style. Existing MPF-style extensions keep working — migration is opt-in. One thing to watch during migration: add `<UseWpf>true</UseWpf>` if your extension uses XAML. You also need to mark the extension as deployable in your `.sln` or `.slnx` file.

The vsixmanifest designer is replaced by the XML editor as the default — right-click → Open With if you want the old designer back.

## Agentic migration path

The Modernize agent in [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) can automate the migration. Several real extensions have already been converted this way: Mads Kristensen's Smart Screen, Command Explorer, Postfix Templates, and Whitespace Visualizer.

## Worth noting

VisualStudio.Extensibility (the newer extensibility framework) already supported SDK-style. This update brings parity to the classic VSSDK path. The only requirement is the Visual Studio extension development workload.

Full details in the [official post](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
