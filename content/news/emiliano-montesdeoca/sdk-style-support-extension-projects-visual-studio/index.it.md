---
title: "Supporto SDK-Style per i Progetti di Estensione in Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 porta il supporto ufficiale al formato di progetto SDK-style per le estensioni VSSDK, riducendo i tempi di build fino al 75% e semplificando i file di progetto a ~20 righe."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Il supporto SDK-style per i progetti di estensione basati su VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) è ora ufficiale in Visual Studio 18.5 — i progetti di estensione VSIX classici possono abbandonare il vecchio formato `.csproj` in stile MPF.

## Cosa cambia nel file di progetto

Il cambiamento più visibile è quanto diventa più piccolo il file di progetto. Una tipica estensione VSSDK ora si presenta così:

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

`VSSDKBuildToolsAutoSetup=true` applica valori predefiniti ragionevoli: `CreateVsixContainer=true` e il legacy `DeployExtension=false`. Questa singola proprietà sostituisce una parte significativa di ciò che in precedenza doveva essere specificato esplicitamente.

## Miglioramenti dei tempi di build

Sono inclusi Fast Up-To-Date Check e supporto per la build incrementale. Per soluzioni grandi con piccole modifiche, questo si traduce in una **riduzione del tempo di build fino al 75%** — significativa se si sta iterando su un'estensione all'interno di una grande soluzione host.

## Nuovi progetti vs. esistenti

I nuovi progetti di estensione creati in 18.5 utilizzano automaticamente lo stile SDK. Le estensioni in stile MPF esistenti continuano a funzionare — la migrazione è opzionale. Da tenere presente durante la migrazione: aggiungere `<UseWpf>true</UseWpf>` se l'estensione usa XAML. È inoltre necessario contrassegnare l'estensione come distribuibile nel file `.sln` o `.slnx`.

Il designer vsixmanifest viene sostituito dall'editor XML come predefinito — clic destro → Apri con se si desidera il vecchio designer.

## Percorso di migrazione agentivo

L'agente Modernize in [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) può automatizzare la migrazione. Diverse estensioni reali sono già state convertite in questo modo: Smart Screen, Command Explorer, Postfix Templates e Whitespace Visualizer di Mads Kristensen.

## Da notare

VisualStudio.Extensibility (il framework di estensibilità più recente) supportava già lo stile SDK. Questo aggiornamento porta la parità con il percorso VSSDK classico. L'unico requisito è il carico di lavoro per lo sviluppo di estensioni di Visual Studio.

Dettagli completi nel [post ufficiale](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
