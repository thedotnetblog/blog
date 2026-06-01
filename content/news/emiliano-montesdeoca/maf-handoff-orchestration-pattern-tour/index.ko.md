---
title: "핸드오프 패턴: 에이전트 하나로는 부족할 때"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework의 Handoff 오케스트레이션 패턴을 통해 에이전트는 대화 컨텍스트를 잃거나 토폴로지 규칙을 위반하지 않고 다음 턴을 누가 처리할지 결정할 수 있습니다."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

어느 시점에서 모든 멀티에이전트 시스템은 단순한 라우터를 넘어섭니다. 첫 번째 신호는 보통 전문 에이전트가 후속 질문을 해야 할 때, 또는 턴 중간에 다른 에이전트가 계속해야 한다는 것을 깨달을 때입니다. 고정 파이프라인은 거기서 실패합니다. 원샷 라우터도 거기서 실패합니다.

그것이 바로 Microsoft Agent Framework의 Handoff 오케스트레이션 패턴이 해결하도록 설계된 문제입니다.

## Handoff 작동 방식

개발자가 그래프를 선언합니다: 에이전트들과 그들 사이의 엣지들. 프레임워크가 나머지를 합니다 — 각 출력 엣지마다 핸드오프 도구를 합성하고 각 에이전트에 주입합니다. 에이전트가 제어를 넘기기로 결정하면 도구를 호출합니다. 프레임워크가 토폴로지를 강제합니다.

이것을 단순히 에이전트들이 서로를 호출하는 것과 다르게 만드는 세 가지:

1. **하나의 공유 트랜스크립트** — 수신 에이전트는 전체 대화 기록을 봅니다. 처음부터 다시 시작하지 않습니다.
2. **토폴로지 강제** — 에이전트는 선언된 대상에만 핸드오프할 수 있습니다. 라우팅 버그는 작성 시점에 감지되고 프로덕션에서는 감지되지 않습니다.
3. **자연스러운 종료** — 활성 에이전트가 핸드오프 도구를 호출하지 않고 턴을 마치면 워크플로가 사용자에게 양보합니다. 폴링 없음, 명시적 종료 조건 없음.

## 최소한의 예

.NET에서 handoff 워크플로 구축은 이렇게 보입니다:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage는 두 전문가 모두에게 보낼 수 있습니다. 두 전문가 모두 triage로 다시 보낼 수 있습니다. 그래프는 비순환을 지원하지만 필요할 때 ("더 많은 정보가 필요해" → 연구로 돌아가기) 백엣지를 지원합니다.

## Handoff를 사용할 때 (그리고 언제 사용하지 않을 때)

Handoff가 좋은 선택인 경우:

- **소유권이 대화 중간에 바뀔 수 있음** — 에이전트가 자신이 잘못된 전문가라는 것을 깨달을 수 있음
- **백엣지가 중요함** — 재시작 없이 이전 단계를 재방문해야 할 수 있음
- **라우팅 결정이 미묘함** — 핸드오프 결정이 상황에 따라 다르고 타입된 술어보다 모델이 결정하는 것이 더 나음

*적합하지 않은* 경우:

- 파이프라인이 고정되고 순차적 — 그런 경우 `Sequential` 워크플로 사용
- 각 단계가 독립적 — 에이전트들이 한 명만 필요했던 트랜스크립트를 공유하는 것은 노이즈
- 엄격한 처리 보장이 필요 — 모델 기반 라우팅의 비결정론은 원하는 것이 아님

## 백엣지와 Human-in-the-Loop

Handoff가 가능하게 하는 가장 흥미로운 형태 중 하나는 진정한 백엣지입니다. 에이전트는 "정보가 충분하지 않다"고 결정하고 연구 단계로 다시 라우팅할 수 있습니다 — 하드코딩된 루프가 아니라 모델이 그것이 올바른 결정이라고 결정하기 때문입니다.

Human-in-the-loop 상호작용도 자연스럽게 구성됩니다. 전문가가 사용자 입력이 필요할 때 워크플로는 기본 턴 루프를 통해 사용자에게 양보하고, 응답을 수집하고, 완전한 컨텍스트로 재개합니다. 에이전트는 대화를 잃지 않았습니다.

## 마무리

Handoff는 내면화하면 많은 것을 가능하게 하는 단순해 보이는 패턴 중 하나입니다: 분산 라우팅, 공유 컨텍스트, 강제된 토폴로지, 자연스러운 종료. 에이전트들이 "실제로 다른 사람이 이것을 처리해야 한다"고 말하기 시작할 때 올바른 다음 단계입니다.

원본 포스트에서 전체 튜토리얼 읽기: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
