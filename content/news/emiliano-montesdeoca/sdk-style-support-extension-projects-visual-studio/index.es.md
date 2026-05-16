---
title: "Soporte de estilo SDK para proyectos de extensión en Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 añade soporte oficial del formato de proyecto SDK-style para extensiones VSSDK, reduciendo los tiempos de compilación hasta un 75% y simplificando los archivos de proyecto a ~20 líneas."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[El soporte de estilo SDK para proyectos de extensión VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) es ahora oficial en Visual Studio 18.5 — los proyectos de extensión VSIX clásicos pueden abandonar el viejo formato `.csproj` estilo MPF.

## Qué cambia en el archivo de proyecto

El cambio más visible es cuánto más pequeño se vuelve el archivo de proyecto. Una extensión VSSDK típica ahora tiene este aspecto:

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

`VSSDKBuildToolsAutoSetup=true` aplica valores predeterminados sensatos: `CreateVsixContainer=true` y el heredado `DeployExtension=false`. Esta única propiedad reemplaza una parte significativa de lo que antes había que especificar explícitamente.

## Mejoras en el tiempo de compilación

Se incluyen Fast Up-To-Date Check y soporte para compilación incremental. En soluciones grandes con cambios pequeños, esto se traduce en una **reducción del tiempo de compilación de hasta el 75%** — significativa si estás iterando en una extensión dentro de una solución grande.

## Proyectos nuevos vs. existentes

Los nuevos proyectos de extensión en la versión 18.5 usan automáticamente el estilo SDK. Las extensiones de estilo MPF existentes continúan funcionando — la migración es opcional. Algo a tener en cuenta durante la migración: añade `<UseWpf>true</UseWpf>` si tu extensión usa XAML. También necesitas marcar la extensión como desplegable en tu archivo `.sln` o `.slnx`.

El diseñador vsixmanifest es reemplazado por el editor XML como predeterminado — clic derecho → Abrir con si quieres el diseñador antiguo.

## Ruta de migración agéntica

El agente Modernize de [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) puede automatizar la migración. Varias extensiones reales ya han sido convertidas de esta manera: Smart Screen, Command Explorer, Postfix Templates y Whitespace Visualizer de Mads Kristensen.

## A tener en cuenta

VisualStudio.Extensibility (el framework de extensibilidad más nuevo) ya soportaba el estilo SDK. Esta actualización trae paridad con la ruta VSSDK clásica. El único requisito es la carga de trabajo de desarrollo de extensiones de Visual Studio.

Detalles completos en el [post oficial](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
