---
title: "Microsoft Foundry 2026년 3월 — GPT-5.4, Agent Service GA, 그리고 모든 것을 바꾸는 SDK 리프레시"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry의 2026년 3월 업데이트는 대규모입니다: Agent Service가 GA에 도달, GPT-5.4가 안정적인 추론을 제공, azure-ai-projects SDK가 모든 언어에서 안정화, Fireworks AI가 오픈 모델을 Azure에 제공합니다."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}})에서 확인하세요.*

월간 "Microsoft Foundry 새 소식" 포스트는 보통 점진적 개선과 가끔의 헤드라인 기능이 섞여 있습니다. [2026년 3월판](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)은요? 기본적으로 전부 헤드라인 기능입니다. Foundry Agent Service가 GA에 도달하고, GPT-5.4가 프로덕션용으로 출시되고, SDK가 대규모 안정 릴리스를 받고, Fireworks AI가 오픈 모델 추론을 Azure에 가져옵니다. .NET 개발자에게 중요한 것이 무엇인지 살펴보겠습니다.

## Foundry Agent Service가 프로덕션 준비 완료

이것이 가장 큰 뉴스입니다. 차세대 에이전트 런타임이 정식 출시되었습니다 — OpenAI Responses API 위에 구축되었으며, OpenAI 에이전트와 와이어 호환되고, 여러 제공업체의 모델에 개방되어 있습니다. 오늘 Responses API로 구축하고 있다면, Foundry로 마이그레이션하면 기존 에이전트 로직 위에 엔터프라이즈 보안, 프라이빗 네트워킹, Entra RBAC, 전체 트레이싱, 그리고 평가가 추가됩니다.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

주요 추가 사항: 엔드투엔드 프라이빗 네트워킹, MCP 인증 확장(OAuth 패스스루 포함), 음성 대 음성 에이전트를 위한 Voice Live 프리뷰, 6개 신규 리전에서의 호스팅 에이전트.

## GPT-5.4 — 순수한 지능보다 신뢰성

GPT-5.4는 더 똑똑해지는 것이 아닙니다. 더 신뢰할 수 있게 되는 것입니다. 긴 상호작용에서의 강력한 추론, 더 나은 지시 준수, 워크플로 중간 실패 감소, 통합된 컴퓨터 사용 기능. 프로덕션 에이전트에게는 이러한 신뢰성이 벤치마크 점수보다 훨씬 중요합니다.

| 모델 | 가격 (백만 토큰당) | 최적 용도 |
|------|-------------------|----------|
| GPT-5.4 (≤272K) | $2.50 / $15 출력 | 프로덕션 에이전트, 코딩, 문서 워크플로 |
| GPT-5.4 Pro | $30 / $180 출력 | 심층 분석, 과학적 추론 |
| GPT-5.4 Mini | 비용 효율적 | 분류, 추출, 경량 도구 호출 |

스마트한 전략은 라우팅입니다: GPT-5.4 Mini가 대용량·저지연 작업을 처리하고 GPT-5.4가 추론이 무거운 요청을 담당합니다.

## SDK가 드디어 안정화

`azure-ai-projects` SDK가 모든 언어에서 안정 릴리스를 발표했습니다 — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0, 그리고 .NET 2.0.0 (4월 1일). `azure-ai-agents` 의존성은 사라졌습니다 — 모든 것이 `AIProjectClient` 아래에 있습니다. `pip install azure-ai-projects`로 설치하면 패키지가 `openai`과 `azure-identity`를 직접 의존성으로 번들합니다.

.NET 개발자에게 이는 Foundry 전체 기능에 대한 단일 NuGet 패키지를 의미합니다. 더 이상 별도의 에이전트 SDK를 겹쳐 사용할 필요가 없습니다.

## Fireworks AI가 오픈 모델을 Azure에 제공

아마도 아키텍처적으로 가장 흥미로운 추가: Fireworks AI가 매일 13조 이상의 토큰을 ~180K 요청/초로 처리하며, 이제 Foundry를 통해 사용 가능합니다. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5, MiniMax M2.5가 출시 시 제공됩니다.

진짜 이야기는 **bring-your-own-weights** — 서빙 스택을 변경하지 않고 어디에서나 양자화되거나 파인튜닝된 가중치를 업로드할 수 있습니다. 서버리스 토큰당 과금 또는 프로비저닝된 처리량으로 배포하세요.

## 기타 하이라이트

- **Phi-4 Reasoning Vision 15B** — 차트, 다이어그램, 문서 레이아웃을 위한 멀티모달 추론
- **Evaluations GA** — Azure Monitor에 연결된 지속적 프로덕션 모니터링과 함께 즉시 사용 가능한 평가기
- **Priority Processing** (프리뷰) — 지연 민감 워크로드를 위한 전용 컴퓨트 레인
- **Voice Live** — Foundry 에이전트에 직접 연결되는 음성 대 음성 런타임
- **Tracing GA** — 정렬 및 필터링이 가능한 엔드투엔드 에이전트 트레이스 검사
- **PromptFlow 지원 종료** — 2027년 1월까지 Microsoft Framework Workflows로 마이그레이션

## 마무리

2026년 3월은 Foundry의 전환점입니다. Agent Service GA, 모든 언어의 안정 SDK, 신뢰할 수 있는 프로덕션 에이전트를 위한 GPT-5.4, Fireworks AI를 통한 오픈 모델 추론 — 플랫폼이 본격적인 워크로드를 위해 준비되었습니다.

[전체 요약](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)을 읽고 [첫 번째 에이전트를 구축](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code)하여 시작하세요.
