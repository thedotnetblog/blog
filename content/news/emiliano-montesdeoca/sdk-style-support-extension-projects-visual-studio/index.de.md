---
title: "SDK-Stil-Unterstützung für Erweiterungsprojekte in Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 bringt offiziell unterstütztes SDK-Style-Projektformat für VSSDK-Erweiterungen, mit bis zu 75 % kürzerer Build-Zeit und ~20-Zeilen-Projektdateien."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Die SDK-Stil-Unterstützung für VSSDK-basierte Erweiterungsprojekte](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) ist jetzt offiziell in Visual Studio 18.5 verfügbar — klassische VSIX-Erweiterungsprojekte können das alte MPF-Style-`.csproj`-Format hinter sich lassen.

## Was sich in der Projektdatei ändert

Die größte sichtbare Änderung ist, wie viel kleiner die Projektdatei wird. Eine typische VSSDK-Erweiterung sieht jetzt so aus:

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

`VSSDKBuildToolsAutoSetup=true` setzt sinnvolle Standardwerte: `CreateVsixContainer=true` und das veraltete `DeployExtension=false`. Diese einzelne Eigenschaft ersetzt einen erheblichen Teil dessen, was bisher explizit angegeben werden musste.

## Build-Zeit-Verbesserungen

Fast Up-To-Date Check und Unterstützung für inkrementelle Builds sind enthalten. Bei großen Lösungen mit kleinen Änderungen ergibt sich eine **Build-Zeit-Reduzierung von bis zu 75 %** — bedeutsam, wenn Sie eine Erweiterung innerhalb einer großen Host-Lösung iterativ entwickeln.

## Neue vs. bestehende Projekte

Neue Erweiterungsprojekte in 18.5 verwenden automatisch den SDK-Stil. Bestehende MPF-Style-Erweiterungen funktionieren weiterhin — die Migration ist optional. Wichtig bei der Migration: `<UseWpf>true</UseWpf>` hinzufügen, falls die Erweiterung XAML verwendet. Außerdem muss die Erweiterung in der `.sln`- oder `.slnx`-Datei als deploybar markiert werden.

Der vsixmanifest-Designer wird standardmäßig durch den XML-Editor ersetzt — Rechtsklick → Öffnen mit, wenn Sie den alten Designer wünschen.

## Agentischer Migrationspfad

Der Modernize-Agent in [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) kann die Migration automatisieren. Mehrere echte Erweiterungen wurden bereits auf diesem Weg konvertiert: Mads Kristensens Smart Screen, Command Explorer, Postfix Templates und Whitespace Visualizer.

## Hinweis

VisualStudio.Extensibility (das neuere Erweiterbarkeits-Framework) unterstützte SDK-Style bereits. Dieses Update bringt Parität mit dem klassischen VSSDK-Pfad. Die einzige Voraussetzung ist die Visual Studio-Erweiterungsentwicklungs-Workload.

Vollständige Details im [offiziellen Beitrag](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
