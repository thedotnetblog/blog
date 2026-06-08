---
title: "GitHub Copilot과 Claude Code를 위한 WinUI 에이전트 플러그인"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft가 WinUI 개발을 위한 에이전트 스킬을 출시했습니다: 스캐폴드, 빌드, 실행, 테스트, 반복 - 모두 GitHub Copilot CLI 또는 Claude Code로. 핵심 혁신: WinUI 특정 사실에 에이전트를 고정하는 전용 도구."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft가 WinUI 애플리케이션 개발을 위한 오픈 소스 에이전트 스킬 세트를 공개했습니다. [aka.ms/winui-skills](https://aka.ms/winui-skills)에서 이용할 수 있습니다.

## 설치 및 설정

`/plugin install winui@awesome-copilot`으로 플러그인을 설치한 다음 `/winui:winui-setup`으로 초기 설정을 실행합니다. 설정 프로세스는 사전 요구 사항을 확인하고 필요한 종속성을 설치하며 WinUI 애플리케이션 개발을 위한 환경을 구성합니다.

## 엔드투엔드 개발 루프

스킬은 완전한 개발 주기를 커버합니다:

- **스캐폴드:** 적절한 매개변수로 `dotnet new WinUI`를 사용하여 올바른 프로젝트 템플릿을 생성합니다 — 에이전트는 올바른 템플릿과 기본 구성 값을 알고 있습니다.
- **빌드:** WinUI 애플리케이션이 필요로 하는 패키지화된 실행 모델을 관리하며, 패키지 서명 및 매니페스트 구성을 포함합니다.
- **상호작용 및 검증:** 애플리케이션을 시작하고 상호작용하며 동작을 검증합니다.
- **컴파일 오류 수정:** 에이전트는 WinUI 특정 오류 메시지를 이해하고 해결 방법을 알고 있습니다.

## 전용 도구를 통한 토큰 효율성

핵심 혁신은 스킬에 필요 시 구체적인 참조 데이터를 가져오는 전용 도구가 포함된다는 것입니다:

- WinUI 및 Fluent Design API 세부 정보
- MVVM 패턴 및 모범 사례
- MSIX 패키징, 코드 서명 및 Store 제출
- 접근성, 테마 및 UI 자동화

WinUI 문서 전체를 컨텍스트에 주입하는 대신, 도구는 에이전트가 필요한 순간에 정확히 필요한 것을 가져옵니다. 이것은 에이전트가 수천 줄의 출력을 생성할 수 있는 빌드 사이클이나 테스트 스위트를 실행할 때 컨텍스트 사용을 효율적으로 유지하고 전문 도메인에서의 정확성을 향상시킵니다.

## 전용 스킬이 중요한 이유

범용 언어 모델은 WinUI 특정 뉘앙스에 대한 제한된 지식을 가지고 있습니다: 패키지화된 실행 모델, Fluent Design API, MSIX 통합 또는 Windows App SDK가 Win32 기능을 래핑하는 특정 방식. 전용 도구는 잠재적으로 오래되거나 부정확한 모델 지식 대신 검증된 WinUI 사실에 에이전트를 고정함으로써 이를 해결합니다.

동일한 패턴은 일반적인 개발 패턴과 다른 고유한 규칙 및 요구 사항을 가진 모든 특수 프레임워크나 SDK에 적용됩니다.

원본 게시물: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
