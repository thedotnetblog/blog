---
title: "Microsoft Foundry 2026년 4월: Foundry Local GA, GPT-5.5, Hyperlight를 통한 CodeAct"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "4월 Foundry 요약은 내용이 풍부합니다: Foundry Local이 GA에 도달하고, GPT-5.5가 등장하며, Agent Framework가 OpenTelemetry 추적을 받고, CodeAct가 Hyperlight 마이크로 VM에서 Python을 실행하고, 에이전트 모니터링 대시보드가 출시됩니다."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Microsoft Foundry에게 바쁜 달이었습니다. 가장 중요한 발표들을 소개합니다.

## Foundry Local이 일반 출시됨

Foundry Local — Microsoft의 크로스플랫폼 로컬 AI 런타임 — 이 Windows, macOS (Apple Silicon) 및 Linux x64에서 미리 보기에서 GA로 전환됩니다. 개발자 친화적인 SDK를 갖춘 프로덕션 준비 로컬 모델 추론입니다. 버전 1.1에서는 전사, embeddings 및 Responses API 지원이 추가됩니다.

## GPT-5.5

GPT-5 패밀리의 최신 모델이 이제 Foundry에서 사용 가능합니다. Tier 5 및 Tier 6 구독의 기본 할당량. 이전 GPT-5 변형으로 작업해왔다면 사용 사례에 맞게 평가해볼 가치가 있습니다.

## Foundry에서의 Agent Framework 추적

이번 달 두 가지 추적 기능이 미리 보기로 제공됩니다:

**Microsoft Agent Framework 추적** — MAF 에이전트가 이제 Foundry에 OpenTelemetry 추적을 내보낼 수 있습니다. 에이전트 동작을 디버그하고, 다단계 실행을 추적하고, 도구 호출 전반의 지연 및 오류를 표면화합니다. 이것은 실제 격차를 채웁니다: 반환한 것뿐만 아니라 *에이전트가 프로덕션에서 실제로 무엇을 했는지* 알기.

**호스팅된 에이전트 추적** — 호스팅된 에이전트의 세션, 도구 호출 및 실행 단계도 Foundry 추적에 나타납니다. 동일한 관찰 가능성 스토리가 호스팅 계층으로 확장됩니다.

## Hyperlight를 통한 CodeAct (Alpha)

이것이 기술적으로 가장 흥미로운 추가 기능입니다: Agent Framework가 이제 [Hyperlight](https://github.com/hyperlight-dev/hyperlight) 마이크로 가상 머신 내에서 Python 코드를 실행할 수 있습니다.

CodeAct는 에이전트가 도구로 Python 코드를 생성하고 실행하는 패턴입니다. 명백한 우려는 보안 — 모델이 생성한 코드를 실행하고 있습니다. Hyperlight의 마이크로 VM은 네이티브에 가까운 시작 시간으로 프로세스 수준의 격리를 제공하여, 전체 컨테이너나 VM의 오버헤드 없이 샌드박스 코드 실행을 실용적으로 만듭니다.

코드 실행이 필요한 에이전트 워크플로우에서 이것은 호스트 프로세스에서 코드를 실행하는 것보다 상당한 보안 개선입니다.

## 에이전트 모니터링 대시보드 (미리 보기)

토큰 사용량, 지연, 실행 성공률 및 평가자 점수를 한 뷰에 결합한 통합 운영 대시보드. 일반 관찰 가능성 대시보드와의 차이점: 운영 메트릭과 함께 평가 결과가 포함되어 "에이전트가 더 느려졌다"를 "평가자 점수가 하락했다"와 상관시키거나 관련이 없음을 확인할 수 있습니다.

## 지속적 평가 커스텀 평가자 (미리 보기)

이제 지속적 평가 파이프라인에 자체 코드 기반 또는 프롬프트 기반 평가자를 가져올 수 있습니다. 이전에는 지속적 평가가 내장 평가자로 제한되었습니다. 커스텀 평가자를 사용하면 프로덕션 모니터링 루프에서 팀별 품질 기준을 적용할 수 있습니다.

## 제어 플레인의 에이전트 인벤토리

Foundry 제어 플레인 Operate 뷰에서 이제 구독 전체의 모든 지원되는 에이전트가 표시됩니다: Foundry 에이전트, Azure SRE Agent, Logic Apps 에이전트 루프 및 등록된 커스텀 에이전트. 무엇이 어디에 배포되어 있는지 이해하기 위한 하나의 뷰.

원본 게시물: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
