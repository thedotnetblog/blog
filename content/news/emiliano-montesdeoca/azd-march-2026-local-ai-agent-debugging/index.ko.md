---
title: "azd로 AI 에이전트를 로컬에서 실행하고 디버깅할 수 있게 됐다 — 2026년 3월 변경사항 정리"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI가 2026년 3월에 7개 릴리스를 발행했습니다. 하이라이트: AI 에이전트의 로컬 실행 및 디버그 루프, GitHub Copilot 프로젝트 설정 통합, Container App Jobs 지원."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *이 글은 자동 번역되었습니다. 원본은 [여기]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}})에서 확인하세요.*

한 달에 7개 릴리스. Azure Developer CLI (`azd`) 팀이 2026년 3월에 발행한 것이며, 메인 기능은 제가 기다리던 것입니다: **AI 에이전트를 위한 로컬 실행 및 디버그 루프**.

PC Chan이 [전체 요약을 게시](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/)했는데, 내용이 많지만 AI 기반 앱을 구축하는 .NET 개발자에게 실제로 중요한 것만 걸러보겠습니다.

## 배포 없이 AI 에이전트 실행 및 디버깅

이것이 핵심입니다. 새로운 `azure.ai.agents` 확장이 AI 에이전트를 위한 적절한 이너 루프 경험을 제공하는 명령을 추가합니다:

- `azd ai agent run` — 에이전트를 로컬에서 시작
- `azd ai agent invoke` — 메시지 전송 (로컬 또는 배포된 에이전트)
- `azd ai agent show` — 컨테이너 상태 및 건강 표시
- `azd ai agent monitor` — 컨테이너 로그를 실시간 스트리밍

이전에는 AI 에이전트 테스트가 변경할 때마다 Microsoft Foundry로 배포하는 것을 의미했습니다. 이제 로컬에서 반복하고, 에이전트 동작을 테스트하고, 준비가 되면 배포할 수 있습니다.

## GitHub Copilot이 azd 프로젝트를 설정

`azd init`에 "Set up with GitHub Copilot (Preview)" 옵션이 추가됐습니다. 프로젝트 구조에 대한 프롬프트에 수동으로 답하는 대신, Copilot 에이전트가 구성을 생성합니다. 명령이 실패하면 `azd`가 AI 지원 문제 해결을 제공합니다.

## Container App Jobs 및 배포 개선

- **Container App Jobs**: `azd`가 기존 `host: containerapp` 설정으로 `Microsoft.App/jobs` 배포
- **설정 가능한 배포 타임아웃**: `azd deploy`의 새 `--timeout` 플래그와 `azure.yaml`의 `deployTimeout` 필드
- **원격 빌드 폴백**: ACR 빌드 실패 시 로컬 Docker/Podman 빌드로 자동 폴백
- **로컬 프리플라이트 검증**: 배포 전 Bicep 매개변수를 로컬에서 검증

## DX 개선

- **자동 pnpm/yarn 감지** — JS/TS 프로젝트용
- **pyproject.toml 지원** — Python 패키징용
- **로컬 템플릿 디렉토리** — `azd init --template`이 파일시스템 경로 허용
- **개선된 오류 메시지** — `--no-prompt` 모드
- **빌드 환경 변수** — 모든 프레임워크 빌드 서브프로세스에 주입 (.NET, Node.js, Java, Python)

## 마무리

로컬 AI 에이전트 디버그 루프가 이번 릴리스의 스타이지만, 배포 개선과 DX 폴리시의 축적으로 `azd`가 그 어느 때보다 성숙해졌습니다. Azure에 .NET 앱을 배포하고 있다면 — 특히 AI 에이전트라면 — 이번 업데이트는 가치가 있습니다.

[전체 릴리스 노트](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/)에서 모든 세부사항을 확인하세요.
