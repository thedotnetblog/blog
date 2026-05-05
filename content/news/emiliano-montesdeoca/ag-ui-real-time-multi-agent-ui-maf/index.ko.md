---
title: "블랙박스처럼 느껴지지 않는 실시간 멀티 에이전트 UI 구축하기"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI와 Microsoft Agent Framework가 멀티 에이전트 워크플로우에 진정한 프론트엔드를 제공합니다 — 실시간 스트리밍, 인간 승인, 에이전트 동작의 완전한 가시성을 갖추고 있습니다."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}})에서 확인하세요.*

멀티 에이전트 시스템의 문제는 이렇습니다: 데모에서는 놀라울 정도로 멋져 보입니다. 세 개의 에이전트가 작업을 주고받고, 문제를 해결하고, 의사결정을 내립니다. 그런데 실제 사용자 앞에 놓으면... 침묵. 돌아가는 로딩 인디케이터. 어떤 에이전트가 뭘 하고 있는지, 왜 시스템이 멈췄는지 전혀 알 수 없습니다. 이건 제품이 아닙니다 — 신뢰 문제입니다.

Microsoft Agent Framework 팀이 MAF 워크플로우를 [AG-UI](https://github.com/ag-ui-protocol/ag-ui)와 결합하는 [훌륭한 워크스루](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/)를 발표했습니다. AG-UI는 Server-Sent Events를 통해 에이전트 실행 이벤트를 프론트엔드로 스트리밍하는 오픈 프로토콜입니다. 솔직히? 이건 우리에게 빠져있던 바로 그 다리입니다.

## .NET 개발자에게 중요한 이유

AI 기반 앱을 만들고 있다면, 아마 이 벽에 부딪혀 봤을 겁니다. 백엔드 오케스트레이션은 완벽하게 동작합니다 — 에이전트들이 서로 작업을 넘기고, 도구가 실행되고, 결정이 내려집니다. 하지만 프론트엔드는 뒤에서 무슨 일이 벌어지고 있는지 전혀 모릅니다. AG-UI는 에이전트 이벤트(`RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*` 등)를 SSE를 통해 UI 레이어로 직접 스트리밍하는 표준 프로토콜을 정의하여 이 문제를 해결합니다.

데모는 세 개의 에이전트로 구성된 고객 지원 워크플로우입니다: 요청을 라우팅하는 트리아지 에이전트, 환불을 처리하는 환불 에이전트, 교체를 관리하는 주문 에이전트. 각 에이전트는 자체 도구를 가지고 있으며, 핸드오프 토폴로지가 명시적으로 정의되어 있습니다 — "프롬프트에서 알아내라"는 식이 아닙니다.

## 핸드오프 토폴로지가 진짜 주인공

제 눈을 사로잡은 것은 `HandoffBuilder`로 에이전트 간 방향성 라우팅 그래프를 선언할 수 있다는 점입니다:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

각 `add_handoff`는 자연어 설명이 포함된 방향성 엣지를 생성합니다. 프레임워크는 이 토폴로지를 기반으로 각 에이전트의 핸드오프 도구를 생성합니다. 따라서 라우팅 결정은 오케스트레이션 구조에 기반하며, LLM이 마음대로 결정하는 것이 아닙니다. 이것은 프로덕션 안정성에 있어 엄청난 차이입니다.

## 실제로 작동하는 Human-in-the-loop

데모는 실제 에이전트 앱에 필요한 두 가지 인터럽트 패턴을 보여줍니다:

**도구 승인 인터럽트** — 에이전트가 `approval_mode="always_require"`로 표시된 도구를 호출하면, 워크플로우가 일시 중지되고 이벤트를 발생시킵니다. 프론트엔드는 도구 이름과 인수가 포함된 승인 모달을 렌더링합니다. 토큰을 소모하는 재시도 루프 없이, 깔끔한 일시중지-승인-재개 흐름입니다.

**정보 요청 인터럽트** — 에이전트가 사용자로부터 더 많은 컨텍스트(예: 주문 ID)가 필요할 때, 일시 중지하고 질문합니다. 프론트엔드가 질문을 표시하고, 사용자가 응답하면, 실행이 멈춘 바로 그 지점에서 재개됩니다.

두 패턴 모두 표준 AG-UI 이벤트로 스트리밍되므로, 프론트엔드에 에이전트별 커스텀 로직이 필요 없습니다 — SSE 연결을 통해 들어오는 이벤트를 그대로 렌더링하면 됩니다.

## 연결이 놀라울 정도로 간단합니다

MAF와 AG-UI의 통합은 단 하나의 함수 호출입니다:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

`workflow_factory`는 스레드마다 새로운 워크플로우를 생성하여, 각 대화가 격리된 상태를 가집니다. 엔드포인트는 모든 SSE 배관을 자동으로 처리합니다. 이미 FastAPI를 사용하고 있다면(또는 경량 레이어로 추가할 수 있다면), 거의 마찰 없이 사용할 수 있습니다.

## 제 생각

우리 .NET 개발자들에게 즉각적인 질문은 "C#으로 할 수 있나?"입니다. Agent Framework는 .NET과 Python 모두에서 사용 가능하고, AG-UI 프로토콜은 언어에 구애받지 않습니다(그냥 SSE입니다). 따라서 이 특정 데모가 Python과 FastAPI를 사용하지만, 패턴은 직접 적용할 수 있습니다. 동일한 AG-UI 이벤트 스키마를 따르는 SSE 엔드포인트가 있는 ASP.NET Core 최소 API를 구성할 수 있습니다.

더 큰 시사점은 멀티 에이전트 UI가 사후 고려사항이 아닌 일급 관심사가 되고 있다는 것입니다. 에이전트가 인간과 상호작용하는 무엇이든 구축하고 있다면 — 고객 지원, 승인 워크플로우, 문서 처리 — MAF 오케스트레이션과 AG-UI 투명성의 조합이 따라야 할 패턴입니다.

## 마무리

AG-UI + Microsoft Agent Framework는 두 세계의 장점을 모두 제공합니다: 백엔드의 강력한 멀티 에이전트 오케스트레이션과 프론트엔드의 실시간 가시성. 더 이상 블랙박스 에이전트 인터랙션은 없습니다.

[전체 워크스루](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/)와 [AG-UI 프로토콜 저장소](https://github.com/ag-ui-protocol/ag-ui)를 확인하여 더 깊이 알아보세요.
