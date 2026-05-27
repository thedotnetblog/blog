---
title: "dotnet new WinUI: Visual Studio 없이 Windows 앱 만들기"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI 프로젝트 템플릿이 이제 dotnet new에서 작동합니다 — 빈 앱, NavigationView 패턴 등. VS Code 지원, Visual Studio 불필요, Fluent Design 기본값 내장."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI 개발에는 이전에 Visual Studio가 필요했습니다. 이것이 바뀌고 있습니다: Microsoft가 `dotnet new`에서 작동하는 WinUI용 오픈 소스 프로젝트 및 항목 템플릿을 공개하여 Windows 앱 개발을 표준 CLI 워크플로우에 통합했습니다.

## 세 가지 명령으로 시작하기

```shell
# 템플릿 설치
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# NavigationView 앱 만들기
dotnet new winui-navview -n MyApp

# 실행
cd MyApp
dotnet run
```

Visual Studio 없음, 수동 프로젝트 설정 없음. 앱은 `dotnet run`으로 실행됩니다.

## 포함된 내용

**빈 템플릿** (`dotnet new winui`) — Fluent 제목 표시줄이 이미 연결된 현대적인 출발점. `.ico` 에셋이 포함된 업데이트된 기본 앱 아이콘, 올바른 밝은/어두운 모드 기본값. 기본 사항을 직접 설정해야 했던 이전 빈 템플릿보다 낫습니다.

**NavigationView 템플릿** (`dotnet new winui-navview`) — 마스터-상세 탐색 패턴, NavigationView, 현대적인 제목 표시줄, 다중 페이지 탐색 구조가 완전히 연결되어 있습니다. 탐색 기반 앱을 위한 표준 Windows 앱 실루엣을 따릅니다. 사이드 탐색이 있는 것을 빌드하는 경우 여기서 시작하세요.

두 템플릿 모두 [Windows 앱 실루엣](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — 레이아웃, 탐색, 시각적 구조를 위한 현대적인 Fluent Design 패턴 — 을 즉시 따릅니다.

## Visual Studio를 사용하지 않는 개발자에게 중요한 이유

VS Code, Rider 또는 명령줄 도구를 사용하는 WinUI 개발자들은 홀대받아 왔습니다. 기존 Visual Studio 템플릿은 VS 외부에서 사용할 수 없었고, 프로젝트 구조를 수동으로 다시 만들고 기본 사항을 연결해야 했습니다.

이 템플릿들은 오픈 소스입니다 ([WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407) 참조). [커뮤니티 피드백](https://github.com/microsoft/microsoft-ui-xaml/issues/10388)에서 개발되었으며 지금 사용 가능합니다. Visual Studio 지원도 진행 중 — 이 동일한 템플릿들은 결국 거기서도 작동할 것입니다.

WinUI 프로젝트 설정을 스크립트로 작성하거나, CI에 통합하거나, 단순히 Visual Studio가 아닌 다른 에디터를 사용하려는 팀에게 이것은 의미 있는 개선입니다.

원본 게시물: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
