---
title: "Visual Studio 扩展项目的 SDK 风格支持"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 为 VSSDK 扩展项目添加了官方支持的 SDK 风格项目格式，将构建时间减少高达 75%，并将项目文件精简至约 20 行。"
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[VSSDK 扩展项目的 SDK 风格支持](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)现已在 Visual Studio 18.5 中正式推出——经典 VSIX 扩展项目可以从旧的 MPF 风格 `.csproj` 格式迁移出来。

## 项目文件的变化

最明显的变化是项目文件变得更加简洁。典型的 VSSDK 扩展现在看起来像这样：

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

`VSSDKBuildToolsAutoSetup=true` 应用合理的默认值：`CreateVsixContainer=true` 和旧版 `DeployExtension=false`。这一个属性替代了以前需要显式指定的大量内容。

## 构建时间改进

启用了快速最新检查和增量构建支持。对于只有少量更改的大型解决方案，这可以带来**高达 75% 的构建时间减少**——如果你在大型宿主解决方案中迭代扩展，这相当显著。

## 新项目与现有项目

在 18.5 中创建的新扩展项目自动使用 SDK 风格。现有的 MPF 风格扩展继续工作——迁移是可选的。迁移时的重要注意事项：如果扩展使用 XAML，请添加 `<UseWpf>true</UseWpf>`。还需要在 `.sln` 或 `.slnx` 文件中将扩展标记为可部署。

vsixmanifest 设计器默认替换为 XML 编辑器——如果需要旧设计器，右键单击 → 打开方式。

## 代理迁移路径

[vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) 中的 Modernize 代理可以自动化迁移。一些真实世界的扩展已经通过这种方式转换：包括 Mads Kristensen 的 Smart Screen、Command Explorer、Postfix Templates 和 Whitespace Visualizer。

## 值得注意的是

VisualStudio.Extensibility（更新的可扩展性框架）已经支持 SDK 风格。此更新与经典 VSSDK 路径实现了对等。唯一的要求是 Visual Studio 扩展开发工作负载。

完整详细信息请参阅[官方博文](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)。
