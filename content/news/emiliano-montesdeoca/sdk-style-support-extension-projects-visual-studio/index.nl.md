---
title: "SDK-stijl ondersteuning voor extensieprojecten in Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 brengt officieel ondersteunde SDK-stijl projectindeling voor VSSDK-extensies, met tot 75% kortere buildtijden en ~20 regels projectbestanden."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[SDK-stijl ondersteuning voor VSSDK-gebaseerde extensieprojecten](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) is nu officieel in Visual Studio 18.5 — klassieke VSIX-extensieprojecten kunnen het oude MPF-stijl `.csproj`-formaat achter zich laten.

## Wat verandert er in het projectbestand

De grootste zichtbare verandering is hoe veel kleiner het projectbestand wordt. Een typische VSSDK-extensie ziet er nu zo uit:

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

`VSSDKBuildToolsAutoSetup=true` past verstandige standaardwaarden toe: `CreateVsixContainer=true` en het verouderde `DeployExtension=false`. Deze enkele eigenschap vervangt een aanzienlijk deel van wat eerder expliciet moest worden opgegeven.

## Verbeteringen in buildtijd

Fast Up-To-Date Check en ondersteuning voor incrementele builds zijn inbegrepen. Voor grote oplossingen met kleine wijzigingen leidt dit tot een **verlaging van de buildtijd van tot 75%** — significant als u aan een extensie werkt binnen een grote hostoplossing.

## Nieuwe vs. bestaande projecten

Nieuwe extensieprojecten die in 18.5 worden aangemaakt, gebruiken automatisch de SDK-stijl. Bestaande MPF-stijl extensies blijven werken — migratie is optioneel. Iets om op te letten bij migratie: voeg `<UseWpf>true</UseWpf>` toe als uw extensie XAML gebruikt. U moet de extensie ook als implementeerbaar markeren in uw `.sln`- of `.slnx`-bestand.

De vsixmanifest-ontwerper wordt vervangen door de XML-editor als standaard — rechtsklik → Openen met als u de oude ontwerper wilt.

## Agentisch migratiepad

De Modernize-agent in [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) kan de migratie automatiseren. Verschillende echte extensies zijn al op deze manier geconverteerd: Smart Screen, Command Explorer, Postfix Templates en Whitespace Visualizer van Mads Kristensen.

## Let op

VisualStudio.Extensibility (het nieuwere extensibiliteitsframework) ondersteunde SDK-stijl al. Deze update brengt pariteit met het klassieke VSSDK-pad. De enige vereiste is de werkbelasting voor Visual Studio-extensieontwikkeling.

Volledige details in de [officiële post](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
