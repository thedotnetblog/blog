---
title: "VS Code 1.119: 에이전트 세션용 OpenTelemetry, 브라우저 통합, 보안"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (2026년 5월)은 에이전트 세션을 위한 OpenTelemetry 추적, 브라우저 탭 공유, 신뢰 및 보안 개선, 1.119.1 보안 패치를 추가합니다."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119)는 2026년 5월 6일 출시되었습니다 (직후 1.119.1 보안 패치 포함). 이 릴리스는 에이전트 관찰 가능성, 브라우저 상호 작용, 중단 감소에 중점을 둡니다.

## 에이전트 세션용 OpenTelemetry 추적

프로덕션에서 에이전트를 실행하거나 에이전트 워크플로를 디버깅하는 누구에게나 주목할 기능입니다. 두 가지 설정으로 활성화합니다:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

추적은 GenAI 의미 규약을 따릅니다. 각 에이전트 요청은 중첩된 하위 스팬을 포함하는 `invoke_agent` 루트 스팬을 생성합니다: `chat`, `execute_tool`, `execute_hook`. 토큰 사용량은 요청별로 보고됩니다 — 캐시 읽기 및 생성 횟수 포함.

로컬 에이전트, Copilot CLI 백그라운드 에이전트, Claude 에이전트와 함께 작동합니다. OTLP 호환 백엔드에서 추적을 수신할 수 있습니다 — 로컬 개발에는 [Aspire Dashboard 독립 실행형](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone)이 잘 작동합니다.

## 에이전트가 이제 브라우저 탭에 접근 가능

에이전트는 통합 브라우저 탭에 대한 접근을 요청할 수 있습니다 — 하지만 자동이 아닙니다. 컨텍스트 선택기, 드래그 앤 드롭, 또는 제안된 컨텍스트를 통해 명시적으로 탭을 공유해야 합니다. 브라우저에 접근을 취소하는 공유 버튼이 있습니다. 에이전트가 이미 열린 (공유되지 않은) 탭과 같은 도메인에 새 탭을 열려고 할 때, VS Code는 기존 탭을 재사용하도록 안내합니다.

## 최적화된 토큰 사용량

실험적 경량 모델이 에이전트 할 일 목록 관리를 처리하여 이 관리 작업을 더 비싼 기본 모델에서 분리합니다. 전체 추론 능력이 필요하지 않은 작업의 토큰 소비를 줄입니다.

## 신뢰 및 보안

중단 감소: VS Code 1.119는 에이전트에 의한 네트워크 접근 요청과 임시 폴더 쓰기 프롬프트를 줄입니다. 1.119.1 패치는 특정 보안 문제를 해결합니다 — 아직 업데이트하지 않았다면 업데이트할 가치가 있습니다.

## 마크다운 미리보기 빠른 전환

작지만 유용합니다: 이제 탐색 없이 현재 편집기를 마크다운 미리보기로 빠르게 전환할 수 있습니다.

## VS Code Agents (Insiders 미리보기)

재설계된 에이전트 세션 UI — 새로운 리포지토리 선택기 (로컬/repos/원격), 하위 세션 개선, 웹 및 모바일 개선, 진행 애니메이션 — 는 Insiders의 [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents)에서 이용 가능합니다.

전체 변경 로그: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
