---
title: "Microsoft Agent Framework의 지속적 워크플로우: In-Memory에서 Azure Functions까지"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAF의 워크플로우 프로그래밍 모델이 이제 Durable Task로 지원되는 지속적 실행을 지원합니다. 프로세스 재시작을 견디고 Azure Functions에서 확장되는 구성 가능한 에이전트 워크플로우를 구축하는 방법을 알아보세요."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

초기 AI 에이전트 워크플로우의 문제점 중 하나: 취약성입니다. 단일 프로세스에 묶인 장시간 실행 멀티스텝 워크플로우는 프로세스 재시작 = 상태 손실을 의미합니다. 간단한 데모에는 괜찮습니다. 프로덕션 워크로드에는 그렇지 않습니다.

Microsoft Agent Framework의 워크플로우 프로그래밍 모델이 이제 Azure Functions 호스팅으로 Durable Task 프레임워크를 기반으로 한 **지속적 실행**을 지원합니다. 프로그래밍 모델이 어떻게 작동하는지, 그리고 내구성 이야기가 왜 중요한지 알아보겠습니다.

## 핵심 구성 요소

**Executor**는 작업의 기본 단위입니다. 각각은 타입이 지정되어 있어 특정 입력을 받아 특정 출력을 생성합니다:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // 주문 조회, 반환
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflow**는 Fluent 빌더를 사용해 executor를 방향 그래프로 연결합니다. 프레임워크가 실행, 단계 간 데이터 흐름, 오류 전파를 처리합니다.

모델링할 수 있는 것:
- 순차 체인 (단계 A → 단계 B → 단계 C)
- 병렬 Fan-out/Fan-in (에이전트 A, B, C를 병렬로 실행하고 결과 집계)
- 조건부 분기
- Human-in-the-loop 승인 (워크플로우 일시 중지, 외부 신호 대기)

## 로컬 개발을 위한 In-Memory 러너

시작은 빠릅니다:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

핵심 패키지에는 가벼운 인프로세스 러너가 포함되어 있습니다. 외부 종속성 없음, 데이터베이스 없음, Azure 리소스 없음. 로컬 개발과 단위 테스트에 완벽합니다.

## Durable Task로 지속성 추가

워크플로우가 프로세스 재시작을 견뎌야 할 때 — 장시간 실행이기 때문에, human-in-the-loop 단계가 있기 때문에, 많은 병렬 에이전트 호출에 분산되기 때문에 — in-memory 러너로는 충분하지 않습니다.

MAF의 Durable Task 통합은 워크플로우 상태를 Azure Storage에 저장합니다. 프로세스가 재시작되면 워크플로우는 중단된 곳에서 재개됩니다. 프로그래밍 모델은 동일하게 유지됩니다. 러너만 교체하면 됩니다.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

동일한 executor, 동일한 워크플로우 그래프 — 지속적인 상태로 지원됩니다.

## Azure Functions 호스팅

세 번째 레이어는 Azure Functions 호스팅입니다. 워크플로우가 Function 앱이 됩니다. HTTP 엔드포인트를 통해 워크플로우를 트리거하고, 지속적 런타임이 확장, 상태, 안정성을 관리합니다.

이는 병렬 호출, 조건부 분기, 인간 승인을 포함하는 멀티에이전트 워크플로우가 사용자 정의 상태 관리 없이 서버리스 Functions 환경에서 확장될 수 있음을 의미합니다.

## 왜 이것이 중요한가

이 조합은 실제 AI 시스템에 중요합니다:

- **병렬 에이전트 호출** — 차단 없이 여러 전문 에이전트에 동시에 분산하고 모두 완료되면 결과 집계
- **장시간 실행 프로세스** — 인간 승인이나 외부 이벤트를 포함하는 워크플로우가 시간이나 일에 걸쳐 일시 중지하고 재개 가능
- **확장성** — Azure Functions가 실행을 수평 확장; Durable Task 프레임워크가 병렬 상태 조정 관리

간단한 로컬 데모를 넘어 MAF 워크플로우를 구축하고 있다면, 이것이 프로덕션 품질 실행으로 가는 길입니다.

원본 게시물: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
