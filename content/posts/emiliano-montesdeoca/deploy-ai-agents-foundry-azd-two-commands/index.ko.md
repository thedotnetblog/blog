---
title: "노트북에서 프로덕션까지: 두 개의 명령으로 AI 에이전트를 Microsoft Foundry에 배포"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI에 'azd ai agent' 명령이 추가되어 AI 에이전트를 로컬 개발에서 몇 분 만에 Foundry 프로덕션 엔드포인트로 가져갑니다. 전체 워크플로를 소개합니다."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

"내 컴퓨터에서는 되는데"와 "배포되어 트래픽을 처리 중"—이 사이의 간극을 아시나요? AI 에이전트의 경우 이 간극은 고통스럽게 넓었습니다. 리소스 프로비저닝, 모델 배포, ID 설정, 모니터링 구축 — 이 모든 것이 누군가가 실제로 에이전트를 호출할 수 있기 전에 필요한 작업입니다.

Azure Developer CLI가 이것을 [두 개의 명령으로 해결](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/)했습니다.

## 새로운 `azd ai agent` 워크플로

실제로 어떤 모습인지 보여드리겠습니다. AI 에이전트 프로젝트가 있다고 합시다 — 호텔 컨시어지 에이전트라고 하죠. 로컬에서 동작합니다. Microsoft Foundry에서 실행하고 싶습니다.

```bash
azd ai agent init
azd up
```

끝입니다. 두 개의 명령. `azd ai agent init`이 저장소에 Infrastructure as Code를 생성하고, `azd up`이 Azure에서 모든 것을 프로비저닝하고 에이전트를 퍼블리시합니다. Foundry 포털에서 에이전트로의 직접 링크를 받게 됩니다.

## 내부에서 일어나는 일

`init` 명령은 저장소에 실제 검사 가능한 Bicep 템플릿을 생성합니다:

- **Foundry Resource** (최상위 컨테이너)
- **Foundry Project** (에이전트가 존재하는 곳)
- **모델 배포** 설정 (GPT-4o 등)
- 적절한 RBAC 역할 할당이 있는 **관리 ID**
- 서비스 맵용 `azure.yaml`
- 에이전트 메타데이터와 환경 변수가 있는 `agent.yaml`

핵심 포인트: 이 모든 것은 여러분 것입니다. 저장소에 버전 관리되는 Bicep입니다. 검사하고, 커스터마이즈하고, 에이전트 코드와 함께 커밋할 수 있습니다. 마법의 블랙박스는 없습니다.

## 개발 내부 루프

정말 마음에 드는 것은 로컬 개발 경험입니다. 에이전트 로직을 반복할 때, 프롬프트를 바꿀 때마다 재배포하고 싶지 않죠:

```bash
azd ai agent run
```

이것으로 에이전트를 로컬에서 시작합니다. `azd ai agent invoke`와 결합하여 테스트 프롬프트를 보내면 빠른 피드백 루프를 얻습니다. 코드 편집, 재시작, 호출, 반복.

`invoke` 명령은 라우팅도 똑똑합니다 — 로컬 에이전트가 실행 중이면 자동으로 그쪽을 타겟합니다. 실행 중이 아니면 원격 엔드포인트로 갑니다.

## 실시간 모니터링

이것이 저를 설득한 기능입니다. 에이전트가 배포되면:

```bash
azd ai agent monitor --follow
```

에이전트를 통과하는 모든 요청과 응답이 실시간으로 터미널에 스트리밍됩니다. 프로덕션 문제를 디버깅하는 데 이것은 값으로 매길 수 없습니다. Log Analytics를 뒤질 필요 없이, 메트릭이 집계되길 기다릴 필요 없이 — 지금 무슨 일이 일어나고 있는지 볼 수 있습니다.

## 전체 명령 세트

빠른 참조:

| 명령 | 기능 |
|------|------|
| `azd ai agent init` | IaC로 Foundry 에이전트 프로젝트 스캐폴드 |
| `azd up` | Azure 리소스 프로비저닝 및 에이전트 배포 |
| `azd ai agent invoke` | 원격 또는 로컬 에이전트에 프롬프트 전송 |
| `azd ai agent run` | 개발용으로 에이전트를 로컬에서 실행 |
| `azd ai agent monitor` | 퍼블리시된 에이전트의 실시간 로그 스트리밍 |
| `azd ai agent show` | 에이전트 상태 및 건강 확인 |
| `azd down` | 모든 Azure 리소스 정리 |

## .NET 개발자에게 왜 중요한가

공지의 예제는 Python 기반이지만, 인프라 이야기는 언어에 구애받지 않습니다. .NET 에이전트도 동일한 Bicep 스캐폴딩, 동일한 관리 ID 설정, 동일한 모니터링 파이프라인을 받습니다. 그리고 이미 .NET Aspire 앱이나 Azure 배포에 `azd`를 사용하고 있다면, 기존 워크플로에 바로 통합됩니다.

AI 에이전트의 배포 간극은 생태계에서 가장 큰 마찰 포인트 중 하나였습니다. 작동하는 프로토타입에서 적절한 ID, 네트워킹, 모니터링을 갖춘 프로덕션 엔드포인트로 전환하는 데 일주일의 DevOps 작업이 필요해서는 안 됩니다. 이제 두 개의 명령과 몇 분이면 됩니다.

## 마무리

`azd ai agent`는 지금 사용할 수 있습니다. 인프라 설정이 너무 많은 작업처럼 보여서 AI 에이전트 배포를 미루고 있었다면 시도해 보세요. 프론트엔드 채팅 앱 통합을 포함한 완전한 단계별 가이드는 [전체 워크스루](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/)를 확인하세요.
