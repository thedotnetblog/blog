---
title: "Visual Studio 3월 업데이트로 커스텀 Copilot 에이전트 제작 가능 — find_symbol이 큰 변화"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026년 3월 업데이트가 커스텀 Copilot 에이전트, 재사용 가능한 스킬, 언어 인식 find_symbol 도구, Test Explorer에서의 Copilot 프로파일링을 제공합니다."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *이 글은 자동 번역되었습니다. 원본은 [여기]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}})에서 확인하세요.*

Visual Studio가 가장 중요한 Copilot 업데이트를 받았습니다. Mark Downie가 [3월 릴리스를 발표](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/)했는데, 헤드라인은 커스텀 에이전트이지만 솔직히 `find_symbol` 도구가 워크플로를 가장 많이 바꿀 기능일 수 있습니다.

## 리포에 커스텀 Copilot 에이전트

Copilot이 팀의 코딩 표준을 따르게 하고 싶으세요? 커스텀 에이전트는 리포의 `.github/agents/`에 `.agent.md` 파일로 정의됩니다. 각 에이전트는 워크스페이스 인식, 코드 이해, 도구, 선호 모델, MCP 연결에 대한 전체 접근 권한을 가집니다.

## 에이전트 스킬: 재사용 가능한 인스트럭션 팩

스킬은 리포의 `.github/skills/`나 프로필의 `~/.copilot/skills/`에서 자동 로드됩니다.

## find_symbol: 언어 인식 내비게이션

새로운 `find_symbol` 도구는 Copilot의 에이전트 모드에 언어 서비스 기반 심볼 내비게이션을 제공합니다. 텍스트 검색 대신 심볼의 모든 참조를 찾고 타입 정보와 스코프에 접근할 수 있습니다.

.NET 개발자에게 이것은 엄청난 개선입니다 — 깊은 타입 계층 구조를 가진 C# 코드베이스가 크게 혜택을 받습니다.

## Copilot으로 테스트 프로파일링

Test Explorer 컨텍스트 메뉴에 **Profile with Copilot**이 추가됐습니다. Profiling Agent가 테스트를 실행하고 자동으로 성능을 분석합니다.

## 라이브 디버깅 중 Perf Tips

성능 최적화가 이제 디버깅 중에 이루어집니다. Visual Studio가 인라인으로 실행 시간을 표시합니다. 느린 라인을 발견하면 Perf Tip을 클릭하고 Copilot에게 최적화 제안을 요청하세요.

## Solution Explorer에서 NuGet 취약점 수정

NuGet 패키지 취약점이 감지되면 Solution Explorer에 직접 **Fix with GitHub Copilot** 링크가 표시됩니다.

## 마무리

커스텀 에이전트와 스킬이 헤드라인이지만, `find_symbol`이 숨겨진 보석입니다 — .NET 코드 리팩토링 시 Copilot의 정확도를 근본적으로 바꿉니다. [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/)를 다운로드해서 모든 기능을 체험해보세요.
