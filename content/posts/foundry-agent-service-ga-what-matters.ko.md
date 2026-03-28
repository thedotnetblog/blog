---
title: "Foundry Agent Service GA: .NET 에이전트 개발자에게 정말 중요한 것"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft의 Foundry Agent Service가 프라이빗 네트워킹, Voice Live, 프로덕션 평가, 오픈 멀티모델 런타임으로 GA에 도달했습니다. 알아야 할 것들을 정리합니다."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

솔직히 말하면 — AI 에이전트 프로토타입을 만드는 건 쉬운 부분입니다. 어려운 건 그 이후의 모든 것: 적절한 네트워크 격리로 프로덕션에 올리기, 실제로 의미 있는 평가를 실행하기, 컴플라이언스 요구사항 처리하기, 새벽 2시에 아무것도 안 깨뜨리기.

[Foundry Agent Service가 GA에 도달했습니다](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/). 이 릴리스는 "그 이후의 모든 것" 간극에 레이저처럼 집중하고 있습니다.

## Responses API 위에 구축

헤드라인: 차세대 Foundry Agent Service는 OpenAI Responses API 위에 구축되었습니다. 이미 그 와이어 프로토콜로 개발하고 있다면 Foundry로의 마이그레이션은 최소한의 코드 변경으로 가능합니다. 얻는 것: 엔터프라이즈 보안, 프라이빗 네트워킹, Entra RBAC, 완전한 트레이싱, 평가 — 기존 에이전트 로직 위에.

아키텍처는 의도적으로 열려 있습니다. 하나의 모델 제공자나 하나의 오케스트레이션 프레임워크에 종속되지 않습니다. 계획에 DeepSeek, 생성에 OpenAI, 오케스트레이션에 LangGraph — 런타임이 일관성 레이어를 처리합니다.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> `azure-ai-agents` 패키지에서 오는 경우, 에이전트는 이제 `azure-ai-projects`의 `AIProjectClient`에서 퍼스트 클래스 작업입니다. 독립 의존성을 제거하고 `get_openai_client()`를 사용하여 응답을 구동하세요.

## 프라이빗 네트워킹: 엔터프라이즈 블로커 제거

이것이 엔터프라이즈 채택의 잠금을 해제하는 기능입니다. Foundry는 이제 BYO VNet으로 완전한 엔드투엔드 프라이빗 네트워킹을 지원합니다:

- **퍼블릭 이그레스 없음** — 에이전트 트래픽이 공개 인터넷에 접촉하지 않음
- **컨테이너/서브넷 인젝션**으로 로컬 통신을 위해 네트워크에 주입
- **도구 연결성 포함** — MCP 서버, Azure AI Search, Fabric 데이터 에이전트 모두 프라이빗 경로로 작동

마지막 포인트가 중요합니다. 프라이빗으로 유지되는 건 추론 호출만이 아닙니다 — 모든 도구 호출과 검색 콜도 네트워크 경계 내에 머무릅니다. 외부 라우팅을 금지하는 데이터 분류 정책 하에서 운영하는 팀에게 이것이 빠져있던 것입니다.

## MCP 인증 제대로 하기

MCP 서버 연결은 이제 인증 패턴의 전체 스펙트럼을 지원합니다:

| 인증 방식 | 사용 시점 |
|-----------|-----------|
| 키 기반 | 조직 전체 내부 도구의 간단한 공유 액세스 |
| Entra Agent Identity | 서비스 간; 에이전트가 자기 자신으로 인증 |
| Entra Managed Identity | 프로젝트별 격리; 자격증명 관리 불필요 |
| OAuth Identity Passthrough | 사용자 위임 액세스; 에이전트가 사용자를 대신하여 행동 |

OAuth Identity Passthrough가 흥미로운 것입니다. 사용자가 에이전트에 개인 데이터 — OneDrive, Salesforce 조직, 사용자별 스코프 SaaS API — 에 대한 액세스를 부여해야 할 때, 에이전트는 표준 OAuth 플로우로 사용자를 대신하여 행동합니다. 모든 사람인 척하는 공유 시스템 ID는 없습니다.

## Voice Live: 배관 없는 음성 대 음성

에이전트에 음성을 추가하는 것은 STT, LLM, TTS를 연결하는 것을 의미했습니다 — 세 개의 서비스, 세 번의 지연 홉, 세 개의 과금 표면, 모두 수동 동기화. **Voice Live**는 이것을 단일 관리 API로 압축합니다:

- 시맨틱 음성 활동 및 턴 종료 감지 (침묵이 아닌 의미를 이해)
- 서버 측 노이즈 억제 및 에코 캔슬레이션
- 끼어들기 지원 (사용자가 응답 중간에 끼어들 수 있음)

음성 상호작용은 텍스트와 같은 에이전트 런타임을 통과합니다. 같은 평가자, 같은 트레이스, 같은 비용 가시성. 고객 지원, 현장 서비스, 접근성 시나리오에서 이전에 커스텀 오디오 파이프라인이 필요했던 것을 대체합니다.

## 평가: 체크박스에서 지속적 모니터링으로

여기서 Foundry는 프로덕션 품질에 대해 진지해집니다. 평가 시스템에는 이제 세 개의 레이어가 있습니다:

1. **기본 제공 평가자** — 일관성, 관련성, 근거성, 검색 품질, 안전성. 데이터셋이나 라이브 트래픽에 연결하여 점수를 받으세요.

2. **커스텀 평가자** — 자체 비즈니스 로직, 톤 표준, 도메인별 컴플라이언스 규칙을 인코딩하세요.

3. **지속적 평가** — Foundry가 라이브 프로덕션 트래픽을 샘플링하고, 평가자 스위트를 실행하고, 대시보드에 결과를 표시합니다. 근거성이 떨어지거나 안전 임계값이 초과되면 Azure Monitor 알림을 설정하세요.

모든 것이 Azure Monitor Application Insights에 게시됩니다. 에이전트 품질, 인프라 상태, 비용, 앱 텔레메트리 — 모두 한 곳에.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## 호스티드 에이전트를 위한 6개 새 지역

호스티드 에이전트가 East US, North Central US, Sweden Central, Southeast Asia, Japan East 등에서 사용 가능합니다. 데이터 거주 요구사항과 에이전트가 데이터 소스 가까이에서 실행될 때 지연 시간을 압축하는 데 중요합니다.

## .NET 개발자에게 왜 중요한가

GA 공지의 코드 샘플은 Python 우선이지만, 기반 인프라는 언어에 구애받지 않습니다 — 그리고 `azure-ai-projects`의 .NET SDK도 같은 패턴을 따릅니다. Responses API, 평가 프레임워크, 프라이빗 네트워킹, MCP 인증 — 이 모든 것이 .NET에서 사용 가능합니다.

AI 에이전트가 "멋진 데모"에서 "실제로 직장에서 출하할 수 있는 것"으로 바뀌기를 기다리고 있었다면, 이 GA 릴리스가 그 신호입니다. 프라이빗 네트워킹, 적절한 인증, 지속적 평가, 프로덕션 모니터링이 빠져있던 퍼즐 조각입니다.

## 마무리

Foundry Agent Service는 지금 사용할 수 있습니다. SDK를 설치하고, [포털](https://ai.azure.com)을 열고, 빌드를 시작하세요. [빠른 시작 가이드](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code)가 몇 분 만에 제로에서 동작하는 에이전트까지 안내합니다.

모든 코드 샘플이 포함된 전체 기술 딥다이브는 [GA 공지](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)를 확인하세요.
