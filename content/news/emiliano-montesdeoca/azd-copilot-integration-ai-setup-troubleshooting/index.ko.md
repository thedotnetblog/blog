---
title: "azd + GitHub Copilot: AI 기반 프로젝트 설정과 스마트 오류 해결"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI가 GitHub Copilot과 통합되어 프로젝트 인프라를 생성하고 배포 오류를 해결합니다 — 터미널을 벗어날 필요 없이."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *이 글은 자동 번역되었습니다. 영어 원문은 [여기]({{< ref "index.md" >}})에서 확인할 수 있습니다.*

기존 앱을 Azure에 배포하려고 할 때, 빈 `azure.yaml` 파일을 보며 Express API가 Container Apps를 써야 할지 App Service를 써야 할지 떠올리려 했던 경험 있으신가요? 그런 순간이 이제 훨씬 짧아집니다.

Azure Developer CLI(`azd`)가 GitHub Copilot과 두 가지 방식으로 통합되었습니다: `azd init` 실행 시 AI 지원 프로젝트 스캐폴딩, 그리고 배포 실패 시 지능형 오류 트러블슈팅. 두 기능 모두 터미널 안에서 완전히 동작합니다 — 딱 원하는 방식입니다.

## azd init에서 Copilot 설정

`azd init`을 실행하면 이제 "Set up with GitHub Copilot (Preview)" 옵션이 나타납니다. 선택하면 Copilot이 코드베이스를 분석하여 실제 코드를 기반으로 `azure.yaml`, 인프라 템플릿, Bicep 모듈을 생성합니다.

```
azd init
# 선택: "Set up with GitHub Copilot (Preview)"
```

필요한 것들:

- **azd 1.23.11 이상** — `azd version`으로 확인하거나 `azd update`로 업데이트
- **활성 GitHub Copilot 구독** (Individual, Business 또는 Enterprise)
- **GitHub CLI (`gh`)** — 필요 시 `azd`가 로그인을 요청함

정말 유용한 점은 양방향으로 동작한다는 것입니다. 처음부터 빌드한다면? Copilot이 처음부터 올바른 Azure 서비스를 설정하도록 도와줍니다. 배포하고 싶은 기존 앱이 있다면? Copilot을 그쪽으로 지향하면 코드 구조를 바꾸지 않고도 설정을 생성해 줍니다.

### 실제로 무엇을 하나

PostgreSQL 의존성이 있는 Node.js Express API가 있다고 합시다. Container Apps와 App Service 중 무엇을 선택할지 수동으로 결정하고 Bicep을 처음부터 작성하는 대신, Copilot이 스택을 감지하고 다음을 생성합니다:

- 올바른 `language`, `host`, `build` 설정이 담긴 `azure.yaml`
- Azure Container Apps를 위한 Bicep 모듈
- Azure Database for PostgreSQL을 위한 Bicep 모듈

그리고 무언가를 변경하기 전에 사전 검사를 실행합니다 — git 작업 디렉토리가 깨끗한지 확인하고, MCP 서버 도구 동의를 미리 요청합니다. 무엇이 바뀌는지 정확히 알고 난 뒤에만 진행됩니다.

## Copilot 기반 오류 트러블슈팅

배포 오류는 피할 수 없습니다. 누락된 파라미터, 권한 문제, SKU 가용성 문제 — 그리고 오류 메시지는 정작 필요한 것을 알려주지 않습니다: *어떻게 고치는가*.

Copilot 없이는: 오류 복사 → 문서 검색 → 관련 없는 Stack Overflow 답변 3개 읽기 → `az` CLI 명령어 실행 → 다시 시도하며 기도. `azd`에 Copilot이 통합되면 이 루프가 사라집니다. `azd` 명령이 실패하면 즉시 4가지 옵션을 제공합니다:

- **Explain** — 무엇이 잘못됐는지 알기 쉬운 설명
- **Guidance** — 수정을 위한 단계별 지침
- **Diagnose and Guide** — 완전한 분석 + Copilot이 수정 적용 (승인 후) + 선택적 재시도
- **Skip** — 직접 처리

핵심: Copilot은 이미 프로젝트, 실패한 명령, 오류 세부 정보의 컨텍스트를 갖고 있습니다. 제안은 *여러분의 상황*에 맞게 구체적입니다.

### 기본 동작 설정

항상 같은 옵션을 선택한다면, 인터랙티브 프롬프트를 건너뛸 수 있습니다:

```
azd config set copilot.errorHandling.category troubleshoot
```

값: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. 자동 수정 및 재시도도 활성화할 수 있습니다:

```
azd config set copilot.errorHandling.fix allow
```

언제든지 인터랙티브 모드로 되돌리기:

```
azd config unset copilot.errorHandling.category
```

## 마무리

`azd update`로 최신 버전을 받고 다음 프로젝트에서 `azd init`을 써보세요. 진정한 가치를 주는 Copilot 통합입니다.

[원문 발표를 여기서 읽어보세요](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
