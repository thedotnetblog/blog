---
title: "Obsługa stylu SDK dla projektów rozszerzeń w Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 wprowadza oficjalnie obsługiwany format projektu SDK-style dla rozszerzeń VSSDK, skracając czas kompilacji o nawet 75% i upraszczając pliki projektu do ~20 linii."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Obsługa stylu SDK dla projektów rozszerzeń opartych na VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) jest teraz oficjalna w Visual Studio 18.5 — klasyczne projekty rozszerzeń VSIX mogą porzucić stary format `.csproj` w stylu MPF.

## Co zmienia się w pliku projektu

Największa widoczna zmiana to to, jak bardzo zmniejsza się plik projektu. Typowe rozszerzenie VSSDK wygląda teraz tak:

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

`VSSDKBuildToolsAutoSetup=true` stosuje rozsądne wartości domyślne: `CreateVsixContainer=true` i starsze `DeployExtension=false`. Ta jedna właściwość zastępuje znaczną część tego, co wcześniej trzeba było podawać jawnie.

## Skrócenie czasu kompilacji

Dołączono Fast Up-To-Date Check i obsługę kompilacji przyrostowej. W przypadku dużych rozwiązań z małymi zmianami przekłada się to na **skrócenie czasu kompilacji o nawet 75%** — znaczące, jeśli iterujesz nad rozszerzeniem w dużym rozwiązaniu hosta.

## Nowe vs. istniejące projekty

Nowe projekty rozszerzeń tworzone w 18.5 automatycznie używają stylu SDK. Istniejące rozszerzenia w stylu MPF nadal działają — migracja jest opcjonalna. Ważna uwaga podczas migracji: dodaj `<UseWpf>true</UseWpf>`, jeśli rozszerzenie używa XAML. Musisz też oznaczyć rozszerzenie jako możliwe do wdrożenia w pliku `.sln` lub `.slnx`.

Projektant vsixmanifest jest domyślnie zastąpiony przez edytor XML — prawy klik → Otwórz za pomocą, jeśli chcesz stary projektant.

## Ścieżka migracji agentycznej

Agent Modernize w [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) może zautomatyzować migrację. Kilka prawdziwych rozszerzeń zostało już w ten sposób przekonwertowanych: Smart Screen, Command Explorer, Postfix Templates i Whitespace Visualizer autorstwa Madsa Kristensena.

## Warto wiedzieć

VisualStudio.Extensibility (nowszy framework rozszerzalności) już obsługiwał styl SDK. Ta aktualizacja przynosi parytet z klasyczną ścieżką VSSDK. Jedynym wymaganiem jest obciążenie deweloperskie rozszerzeń Visual Studio.

Pełne szczegóły w [oficjalnym poście](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
