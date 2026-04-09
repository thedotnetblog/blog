---
title: "Aspire의 격리 모드가 병렬 개발의 포트 충돌 악몽을 해결한다"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2가 --isolated 모드를 도입합니다: 랜덤 포트, 분리된 시크릿, 동일한 AppHost의 여러 인스턴스를 실행할 때 충돌 제로. AI 에이전트, worktree, 병렬 워크플로우에 완벽합니다."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "aspire-isolated-mode-parallel-instances" >}})에서 확인하세요.*

같은 프로젝트의 두 인스턴스를 동시에 실행하려고 해본 적이 있다면, 그 고통을 알 것입니다. 포트 8080이 이미 사용 중입니다. 포트 17370이 점유되어 있습니다. 뭔가를 kill하고, 재시작하고, 환경 변수를 저글링하는 — 생산성 킬러입니다.

이 문제는 나아지는 게 아니라 악화되고 있습니다. AI 에이전트가 독립적으로 작업하기 위해 git worktree를 만듭니다. 백그라운드 에이전트가 별도의 환경을 생성합니다. 개발자가 피처 브랜치를 위해 같은 레포를 두 번 체크아웃합니다. 이 모든 시나리오가 같은 벽에 부딪힙니다: 같은 앱의 두 인스턴스가 같은 포트를 놓고 싸우는 것입니다.

Aspire 13.2가 단 하나의 플래그로 이것을 해결합니다. Aspire 팀의 James Newton-King이 [전체 상세 내용을 작성했는데](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), "왜 진작 이게 없었지?"라는 기능 중 하나입니다.

## 해결책: `--isolated`

```bash
aspire run --isolated
```

끝입니다. 각 실행이 다음을 얻습니다:

- **랜덤 포트** — 인스턴스 간 충돌 없음
- **격리된 사용자 시크릿** — 연결 문자열과 API 키가 인스턴스별로 분리

수동 포트 재할당이 필요 없습니다. 환경 변수 저글링도 필요 없습니다. 각 실행이 자동으로 깨끗하고 충돌 없는 환경을 얻습니다.

## 이 기능이 빛나는 실제 시나리오

**다중 체크아웃.** 한 디렉토리에 피처 브랜치가 있고 다른 디렉토리에 버그픽스가 있는 경우:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

둘 다 충돌 없이 실행됩니다. 대시보드에서 무엇이 어디서 실행 중인지 확인할 수 있습니다.

**VS Code의 백그라운드 에이전트.** Copilot Chat의 백그라운드 에이전트가 코드에 독립적으로 작업하기 위해 git worktree를 만들면, Aspire AppHost를 실행해야 할 수 있습니다. `--isolated` 없이는 기본 worktree와 포트 충돌이 발생합니다. 이것이 있으면 두 인스턴스 모두 문제없이 동작합니다.

`aspire agent init`에 포함된 Aspire 스킬은 worktree에서 작업할 때 `--isolated`를 사용하도록 에이전트에게 자동으로 지시합니다. 따라서 Copilot의 백그라운드 에이전트는 이것을 기본적으로 처리할 것입니다.

**개발과 병행하는 통합 테스트.** 기능을 계속 만들면서 라이브 AppHost에 대해 테스트를 실행해야 하나요? 격리 모드는 각 컨텍스트에 자체 포트와 설정을 제공합니다.

## 내부 작동 원리

`--isolated`를 전달하면, CLI가 해당 실행을 위한 고유 인스턴스 ID를 생성합니다. 이것이 두 가지 동작을 구동합니다:

1. **포트 랜덤화** — AppHost 설정에 정의된 예측 가능한 포트에 바인딩하는 대신, 격리 모드는 모든 것에 대해 사용 가능한 랜덤 포트를 선택합니다 — 대시보드, 서비스 엔드포인트, 전부. 서비스 디스커버리가 자동으로 조정되어 어떤 포트에 할당되든 서비스들이 서로를 찾습니다.

2. **시크릿 격리** — 각 격리된 실행은 인스턴스 ID로 키가 지정된 자체 사용자 시크릿 저장소를 갖습니다. 한 실행의 연결 문자열과 API 키가 다른 실행으로 누출되지 않습니다.

코드 변경은 필요 없습니다. Aspire의 서비스 디스커버리가 런타임에 엔드포인트를 해석하므로, 포트 할당에 관계없이 모든 것이 올바르게 연결됩니다.

## 언제 사용할 것인가

같은 AppHost의 여러 인스턴스를 동시에 실행할 때 `--isolated`를 사용하세요 — 병렬 개발, 자동화된 테스트, AI 에이전트, 또는 git worktree 어떤 경우든. 예측 가능한 포트를 선호하는 단일 인스턴스 개발에는 일반 `aspire run`이 여전히 잘 작동합니다.

## 마무리

격리 모드는 실제적이고 점점 더 흔해지는 문제를 해결하는 작은 기능입니다. AI 지원 개발이 더 많은 병렬 워크플로우 — 다중 에이전트, 다중 worktree, 다중 컨텍스트 — 로 우리를 밀어붙이는 만큼, 포트 경쟁 없이 또 다른 인스턴스를 간단히 띄울 수 있는 능력은 필수적입니다.

[전체 포스트](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/)에서 모든 기술적 세부사항을 확인하고, `aspire update --self`로 13.2를 받아 시도해 보세요.
