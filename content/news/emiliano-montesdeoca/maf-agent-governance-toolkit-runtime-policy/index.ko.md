---
title: "에이전트를 만드는 건 쉬운 부분 — 안전하게 실행하는 게 어려운 부분"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework와 Agent Governance Toolkit이 결합하여 런타임 정책을 적용하고, 도구 호출을 제어하며, Merkle 체인 감사 로그를 제공합니다 — 에이전트 프롬프트를 건드리지 않고."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

AI 에이전트 개발에서 "데모 후회"라고 부르기 시작한 패턴이 있습니다. 에이전트는 데모에서 완벽하게 작동합니다. 그런 다음 누군가가 묻습니다: 잘못된 도구를 호출하면 어떻게 되나요? 접근하면 안 되는 데이터에 접근한다면? 누가 감사했나요?

Microsoft Agent Framework는 구축과 오케스트레이션을 지원합니다. Agent Governance Toolkit(AGT)은 그 이후 부분을 담당합니다 — 거버넌스, 정책 적용, 런타임 감사 가능성.

## 각 프로젝트가 실제로 하는 것

**Microsoft Agent Framework (MAF)**는 프로그래밍 모델을 제공합니다: 멀티 에이전트 워크플로우, A2A 프로토콜 상호 운용성, 미들웨어 훅, 메모리, Foundry Agent Service를 통한 관리형 호스팅. 모델 입출력 레벨에서 콘텐츠 안전성을 처리합니다.

**Agent Governance Toolkit (AGT)**는 동일한 미들웨어 파이프라인에 연결되어 *액션*을 제어합니다. 모든 도구 호출, 리소스 접근, 에이전트 간 메시지가 실행 전에 정책에 대해 평가됩니다. 서브밀리초 오버헤드. 사이드카 없음, 프록시 없음, 수정된 프롬프트 없음.

```
에이전트 액션 --> 정책 검사 --> 허용 / 거부 --> 감사 로그    (< 0.1 ms)
```

서로 다른 레이어, 완전한 커버리지, 하나의 파이프라인.

## 연결은 미들웨어 추가만 하면 됩니다

Python에서 AGT는 로깅이나 콘텐츠 필터에 사용하는 것과 동일한 `middleware` 매개변수에 추가됩니다:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

.NET에서는 `.Use()`를 통해 같은 패턴:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

같은 에이전트, 같은 오케스트레이션, 같은 도구. AGT는 에이전트 로직을 건드리지 않고 거버넌스 기능을 추가합니다.

## 무엇을 얻나요

- **GovernancePolicyMiddleware** — 선언적 정책 규칙에 대해 모든 액션 평가
- **CapabilityGuardMiddleware** — 에이전트가 호출 가능한 도구의 허용 목록(`approve_small_loan` 도구는 위 허용 목록에 의도적으로 없음)
- **RogueDetectionMiddleware** — 런타임에서 비정상적인 동작 패턴 감지
- **AuditTrailMiddleware** — 모든 액션을 암호학적으로 변조 방지하는 Merkle 체인 감사 로그

마지막 것은 규정 준수에 중요합니다. Merkle 체인은 누군가 로그를 수정하면 체인이 끊긴다는 것을 의미합니다. 감사가 증거입니다.

## 다섯 가지 산업 시나리오

AGT 저장소에는 5개의 완전한 엔드투엔드 시나리오가 포함되어 있습니다: 금융 서비스(대출 담당자), 의료(환자 데이터), 법률(계약 검토), 정부(시민 서비스), 제조(품질 관리). 각각은 실제 MAF 에이전트와 실제 AGT 거버넌스 미들웨어를 결합합니다.

장난감 데모가 아닙니다. 실제로 프로덕션에서 거버넌스가 필요한 시나리오입니다.

## 결론

실제 데이터를 다루거나, 결과를 수반하는 결정을 내리거나, 프로덕션에서 무인으로 실행되는 에이전트를 구축하고 있다면 — 거버넌스는 선택 사항이 아닙니다. MAF + AGT의 조합이 전체 스택을 제공합니다: Agent Framework로 구축하고, AGT로 관리하세요.

두 프로젝트 모두 오픈 소스입니다. 원본 문서에는 전체 코드 샘플 링크가 있습니다.

원본 게시글: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
