---
title: "Suporte ao Estilo SDK para Projetos de Extensão no Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "O Visual Studio 18.5 traz suporte oficial ao formato de projeto SDK-style para extensões VSSDK, reduzindo o tempo de compilação em até 75% e simplificando arquivos de projeto para ~20 linhas."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[O suporte ao estilo SDK para projetos de extensão baseados em VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) é agora oficial no Visual Studio 18.5 — projetos de extensão VSIX clássicos podem abandonar o antigo formato `.csproj` estilo MPF.

## O que muda no arquivo de projeto

A maior mudança visível é o quanto o arquivo de projeto fica menor. Uma extensão VSSDK típica agora se parece com isso:

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

`VSSDKBuildToolsAutoSetup=true` aplica padrões sensatos: `CreateVsixContainer=true` e o legado `DeployExtension=false`. Essa única propriedade substitui uma parte significativa do que antes precisava ser especificado explicitamente.

## Melhorias no tempo de compilação

Fast Up-To-Date Check e suporte para build incremental estão incluídos. Para soluções grandes com pequenas alterações, isso se traduz em uma **redução do tempo de build de até 75%** — significativa se você estiver iterando em uma extensão dentro de uma grande solução host.

## Projetos novos vs. existentes

Novos projetos de extensão criados na versão 18.5 usam automaticamente o estilo SDK. Extensões no estilo MPF existentes continuam funcionando — a migração é opcional. Algo a observar durante a migração: adicione `<UseWpf>true</UseWpf>` se a sua extensão usa XAML. Você também precisa marcar a extensão como implantável no seu arquivo `.sln` ou `.slnx`.

O designer do vsixmanifest é substituído pelo editor XML como padrão — clique com o botão direito → Abrir com se quiser o designer antigo.

## Caminho de migração agêntico

O agente Modernize no [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) pode automatizar a migração. Várias extensões reais já foram convertidas dessa forma: Smart Screen, Command Explorer, Postfix Templates e Whitespace Visualizer de Mads Kristensen.

## Vale notar

VisualStudio.Extensibility (o framework de extensibilidade mais novo) já suportava o estilo SDK. Esta atualização traz paridade com o caminho VSSDK clássico. O único requisito é a carga de trabalho de desenvolvimento de extensões do Visual Studio.

Detalhes completos no [post oficial](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
