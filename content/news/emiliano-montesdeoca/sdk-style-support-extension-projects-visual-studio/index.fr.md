---
title: "Prise en charge du style SDK pour les projets d'extension dans Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 apporte la prise en charge officielle du format de projet SDK-style pour les extensions VSSDK, avec jusqu'à 75 % de réduction du temps de compilation et des fichiers de projet de ~20 lignes."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[La prise en charge du style SDK pour les projets d'extension VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) est maintenant officielle dans Visual Studio 18.5 — les projets d'extension VSIX classiques peuvent abandonner l'ancien format `.csproj` style MPF.

## Ce qui change dans le fichier de projet

Le changement le plus visible est la taille réduite du fichier de projet. Une extension VSSDK typique ressemble maintenant à ceci :

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

`VSSDKBuildToolsAutoSetup=true` applique des valeurs par défaut sensées : `CreateVsixContainer=true` et l'ancien `DeployExtension=false`. Cette unique propriété remplace une partie significative de ce qui devait auparavant être spécifié explicitement.

## Améliorations du temps de compilation

Fast Up-To-Date Check et le support de la compilation incrémentale sont inclus. Pour les grandes solutions avec de petits changements, cela se traduit par une **réduction du temps de compilation allant jusqu'à 75 %** — significative si vous itérez sur une extension dans une grande solution hôte.

## Nouveaux projets vs. existants

Les nouveaux projets d'extension créés en 18.5 utilisent automatiquement le style SDK. Les extensions de style MPF existantes continuent de fonctionner — la migration est optionnelle. Un point à surveiller lors de la migration : ajoutez `<UseWpf>true</UseWpf>` si votre extension utilise XAML. Vous devez également marquer l'extension comme déployable dans votre fichier `.sln` ou `.slnx`.

Le concepteur vsixmanifest est remplacé par l'éditeur XML par défaut — clic droit → Ouvrir avec si vous voulez l'ancien concepteur.

## Chemin de migration agentique

L'agent Modernize dans [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) peut automatiser la migration. Plusieurs vraies extensions ont déjà été converties de cette façon : Smart Screen, Command Explorer, Postfix Templates et Whitespace Visualizer de Mads Kristensen.

## À noter

VisualStudio.Extensibility (le framework d'extensibilité plus récent) prenait déjà en charge le style SDK. Cette mise à jour apporte la parité avec le chemin VSSDK classique. La seule exigence est la charge de travail de développement d'extensions Visual Studio.

Détails complets dans le [post officiel](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
