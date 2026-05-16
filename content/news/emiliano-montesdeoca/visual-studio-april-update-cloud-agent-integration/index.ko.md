---
title: "Visual Studio 2026 4월 업데이트: 클라우드 에이전트, 사용자 지정 에이전트, 디버거 에이전트"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026 (18.5) 4월 업데이트에서 클라우드 에이전트 통합, 사용자 수준 사용자 지정 에이전트, C++ 도구 GA, 실제 런타임 동작에 대해 수정 사항을 검증하는 디버거 에이전트가 추가됩니다."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[Visual Studio 2026 (18.5) 4월 업데이트](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/)는 클라우드 에이전트 통합, 사용자 수준 사용자 지정 에이전트, GA에 도달하는 C++ 도구, 새로운 디버거 에이전트를 제공합니다.

## 클라우드 에이전트: 원격 Copilot 세션에 작업 위임

Chat 창의 에이전트 선택기에서 **Cloud**를 선택하면 원격 Copilot 코딩 에이전트에게 작업을 위임할 수 있습니다. 작업을 설명하면 에이전트가 리포지토리에 GitHub 이슈를 생성한 후 완료되면 PR을 엽니다. "View PR" / "Open in browser"와 함께 알림을 받습니다 — 코딩을 계속하는 동안, 또는 IDE를 닫은 상태에서도 동작합니다.

## 사용자 지정 에이전트가 이제 어디서나 따라옵니다

`%USERPROFILE%/.github/agents/`에 저장된 사용자 수준 사용자 지정 에이전트는 더 이상 리포지토리에 국한되지 않습니다 — 프로젝트 전반에 걸쳐 따라옵니다. 저장 경로는 Tools > Options > GitHub > Copilot > Chat에서 구성할 수 있습니다. 에이전트 선택기의 `+` 버튼으로 새 에이전트를 직접 만들 수 있습니다. 리포지토리 범위 에이전트와 동일한 기능을 갖습니다: 작업 공간 인식, 도구, 모델 선택, MCP 연결.

기본 제공 에이전트: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## C++ 코드 편집 도구가 GA로

두 가지 도구 — `get_symbol_call_hierarchy`와 `get_symbol_class_hierarchy` — 가 이제 기본적으로 활성화됩니다. C++ 코드베이스에서 상속 계층 구조와 함수 호출 체인을 Copilot이 언어 인식 탐색으로 파악합니다. Copilot Chat의 도구 아이콘으로 활성화합니다. 도구 호출 모델과 함께 사용할 때 가장 효과적입니다.

## 디버거 에이전트: 실제 런타임 동작에 대해 수정 사항 검증

GitHub 또는 Azure DevOps 이슈(또는 자연어 설명)에서 시작하여 Debugger 모드로 전환하면 에이전트는:

1. 최소 재현 코드 생성
2. 실패 가설 생성
3. 트레이스포인트와 조건부 중단점으로 앱 계측
4. 실제 디버그 세션 실행
5. 라이브 원격 측정 분석
6. 정확한 수정 제안

전체 과정에서 루프에 머물러 있습니다 — 인터랙티브하며 완전히 자율적이지 않습니다.

## IntelliSense 우선순위 수정

IntelliSense 목록이 활성 상태일 때 VS는 이제 Copilot 완성을 억제합니다. 한 번에 하나의 제안만. 자주 발생하는 마찰 포인트였으며 이제 기본적으로 활성화됩니다.

전체 릴리스 노트와 다운로드는 [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/)에서.
