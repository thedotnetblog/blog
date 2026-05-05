---
title: "터미널 감시는 그만: Aspire의 분리 모드가 워크플로를 바꾼다"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2에서는 AppHost를 백그라운드에서 실행하고 터미널을 되찾을 수 있습니다. 새로운 CLI 명령과 에이전트 지원과 결합하면, 생각보다 훨씬 큰 변화입니다."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "aspire-detached-mode-free-your-terminal" >}})에서 확인하세요.*

Aspire AppHost를 실행할 때마다 터미널이 사라집니다. 잠겨버립니다. Ctrl+C를 누를 때까지 점유된 상태입니다. 빠르게 명령어를 실행해야 하나요? 다른 탭을 엽니다. 로그를 확인하고 싶나요? 또 다른 탭. 작은 불편함이지만 빠르게 쌓입니다.

Aspire 13.2가 이 문제를 해결합니다. James Newton-King이 [자세한 내용을 작성했는데](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), 솔직히 이건 사용하는 순간 바로 작업 방식이 바뀌는 기능 중 하나입니다.

## 분리 모드: 명령어 하나로 터미널 되찾기

```bash
aspire start
```

이것은 `aspire run --detach`의 단축 명령입니다. AppHost가 백그라운드에서 시작되고 터미널이 즉시 돌아옵니다. 추가 탭 없이. 터미널 멀티플렉서 없이. 프롬프트만 준비된 상태로요.

## 실행 중인 프로세스 관리하기

핵심은 이겁니다 — 백그라운드 실행은 실행 중인 것을 관리할 수 있어야만 의미가 있습니다. Aspire 13.2는 바로 이를 위한 완전한 CLI 명령 세트를 제공합니다:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

이로써 Aspire CLI가 본격적인 프로세스 관리자가 됩니다. 여러 AppHost를 시작하고, 상태를 확인하고, 로그를 추적하고, 종료할 수 있습니다 — 모두 하나의 터미널 세션에서.

## 격리 모드와 결합하기

분리 모드는 격리 모드와 자연스럽게 어울립니다. 포트 충돌 없이 같은 프로젝트의 인스턴스 두 개를 백그라운드에서 실행하고 싶다면?

```bash
aspire start --isolated
aspire start --isolated
```

각각 랜덤 포트, 별도의 시크릿, 자체 라이프사이클을 갖습니다. `aspire ps`로 둘 다 확인하고, `aspire stop`으로 필요 없는 것을 중지하세요.

## 코딩 에이전트에게 이것이 중요한 이유

여기서부터 정말 흥미로워집니다. 터미널에서 작업하는 코딩 에이전트가 이제 다음을 할 수 있습니다:

1. `aspire start`로 앱 시작
2. `aspire describe`로 상태 조회
3. `aspire logs`로 로그를 확인하여 문제 진단
4. 완료 후 `aspire stop`으로 중지

모두 터미널 세션을 잃지 않고 수행할 수 있습니다. 분리 모드 이전에는 AppHost를 실행한 에이전트가 자신의 터미널에 갇혀버렸습니다. 이제는 시작, 관찰, 반복, 정리가 가능합니다 — 자율 에이전트에게 기대하는 바로 그 동작입니다.

Aspire 팀은 이 부분에 공을 들였습니다. `aspire agent init`을 실행하면 에이전트에게 이러한 명령을 가르치는 Aspire 스킬 파일이 설정됩니다. 이를 통해 Copilot의 코딩 에이전트 같은 도구가 바로 Aspire 워크로드를 관리할 수 있습니다.

## 마무리

분리 모드는 단순한 플래그로 위장한 워크플로 업그레이드입니다. 터미널 간 컨텍스트 전환이 사라지고, 에이전트가 스스로를 차단하지 않으며, 새로운 CLI 명령으로 실행 중인 것을 실시간으로 파악할 수 있습니다. 실용적이고, 깔끔하며, 일상 개발 사이클이 눈에 띄게 매끄러워집니다.

[전체 글](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/)에서 모든 세부 사항을 확인하고, `aspire update --self`로 Aspire 13.2를 설치하세요.
