---
title: "Visual Studio 확장 프로젝트에 대한 SDK 스타일 지원"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5가 VSSDK 기반 확장에 공식적으로 지원되는 SDK 스타일 프로젝트 형식을 도입하여 빌드 시간을 최대 75% 단축하고 프로젝트 파일을 약 20줄로 간소화합니다."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[VSSDK 기반 확장 프로젝트에 대한 SDK 스타일 지원](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)이 이제 Visual Studio 18.5에서 공식적으로 지원됩니다 — 클래식 VSIX 확장 프로젝트는 오래된 MPF 스타일 `.csproj` 형식을 버릴 수 있습니다.

## 프로젝트 파일의 변화

가장 눈에 띄는 변화는 프로젝트 파일이 얼마나 작아지는지입니다. 일반적인 VSSDK 확장은 이제 다음과 같이 보입니다:

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

`VSSDKBuildToolsAutoSetup=true`는 합리적인 기본값을 적용합니다: `CreateVsixContainer=true`와 레거시 `DeployExtension=false`. 이 단일 속성이 이전에 명시적으로 지정해야 했던 상당 부분을 대체합니다.

## 빌드 시간 개선

Fast Up-To-Date Check와 증분 빌드 지원이 포함됩니다. 대규모 솔루션에서 작은 변경의 경우 **빌드 시간이 최대 75% 단축**됩니다 — 대규모 호스트 솔루션 내에서 확장을 반복 개발할 때 의미가 있습니다.

## 신규 프로젝트 vs 기존 프로젝트

18.5에서 생성한 새 확장 프로젝트는 자동으로 SDK 스타일을 사용합니다. 기존 MPF 스타일 확장은 계속 작동합니다 — 마이그레이션은 선택 사항입니다. 마이그레이션 시 주의할 점: 확장이 XAML을 사용하면 `<UseWpf>true</UseWpf>`를 추가하세요. `.sln` 또는 `.slnx` 파일에서 확장을 배포 가능으로 표시해야 합니다.

vsixmanifest 디자이너는 기본적으로 XML 편집기로 대체됩니다 — 이전 디자이너가 필요하면 우클릭 → 연결 프로그램.

## 에이전트 기반 마이그레이션 경로

[vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins)의 Modernize 에이전트가 마이그레이션을 자동화할 수 있습니다. Mads Kristensen의 Smart Screen, Command Explorer, Postfix Templates, Whitespace Visualizer 등 여러 실제 확장이 이미 이 방법으로 변환되었습니다.

## 참고 사항

VisualStudio.Extensibility(최신 확장성 프레임워크)는 이미 SDK 스타일을 지원했습니다. 이번 업데이트는 클래식 VSSDK 경로와의 동등성을 가져옵니다. 유일한 요구 사항은 Visual Studio 확장 개발 워크로드입니다.

자세한 내용은 [공식 게시물](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)에서 확인하세요.
