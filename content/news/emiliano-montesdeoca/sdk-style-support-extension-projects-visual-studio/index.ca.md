---
title: "Suport d'estil SDK per a projectes d'extensió a Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 afegeix suport oficial del format de projecte SDK-style per a extensions VSSDK, reduint el temps de compilació fins a un 75% i simplificant els fitxers de projecte a ~20 línies."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[El suport d'estil SDK per a projectes d'extensió de Visual Studio](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) és ara oficial a Visual Studio 18.5 — els projectes d'extensió VSIX clàssics poden abandonar el vell format `.csproj` estil MPF.

## Què canvia en el fitxer de projecte

El canvi més visible és com de petit es torna el fitxer de projecte. Una extensió VSSDK típica ara té aquest aspecte:

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

`VSSDKBuildToolsAutoSetup=true` aplica valors predeterminats sensats: `CreateVsixContainer=true` i el llegat `DeployExtension=false`. Aquesta única propietat substitueix una part significativa del que abans s'havia d'especificar explícitament.

## Millores del temps de compilació

S'inclouen Fast Up-To-Date Check i suport de compilació incremental. Per a solucions grans amb canvis petits, això es tradueix en una **reducció del temps de compilació de fins al 75%** — significativa si esteu iterant en una extensió dins d'una solució gran.

## Projectes nous vs. existents

Els nous projectes d'extensió creats a la versió 18.5 utilitzen automàticament l'estil SDK. Les extensions d'estil MPF existents continuen funcionant — la migració és opcional. Una cosa a tenir en compte durant la migració: afegiu `<UseWpf>true</UseWpf>` si la vostra extensió utilitza XAML. També cal marcar l'extensió com a desplegable al fitxer `.sln` o `.slnx`.

El dissenyador vsixmanifest és substituït per l'editor XML com a predeterminat — clic dret → Open With si voleu el dissenyador antic.

## Ruta de migració agèntica

L'agent Modernize de [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) pot automatitzar la migració. Diverses extensions reals ja han estat convertides d'aquesta manera: Smart Screen, Command Explorer, Postfix Templates i Whitespace Visualizer de Mads Kristensen.

## A tenir en compte

VisualStudio.Extensibility (el marc d'extensibilitat més nou) ja admetia l'estil SDK. Aquesta actualització porta la paritat a la ruta VSSDK clàssica. L'únic requisit és la càrrega de treball de desenvolupament d'extensions de Visual Studio.

Detalls complets al [post oficial](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
