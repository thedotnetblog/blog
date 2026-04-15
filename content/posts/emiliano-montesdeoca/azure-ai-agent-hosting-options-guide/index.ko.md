---
title: "Azure에서 AI 에이전트를 어디에 호스팅해야 할까? 실용적인 의사결정 가이드"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure는 원시 컨테이너부터 완전 관리형 Foundry Hosted Agents까지 AI 에이전트를 호스팅하는 6가지 방법을 제공합니다. .NET 워크로드에 적합한 것을 선택하는 방법을 알아보세요."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "azure-ai-agent-hosting-options-guide.md" >}})를 참조하세요.*

지금 .NET으로 AI 에이전트를 구축하고 있다면, 아마 눈치챘을 겁니다: Azure에서 호스팅하는 방법이 *정말 많다*는 것을. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — 실제로 하나를 선택해야 할 때까지는 모두 합리적으로 들립니다. Microsoft가 방금 [Azure AI 에이전트 호스팅에 대한 종합 가이드](https://devblogs.microsoft.com/all-things-azure/hostedagent/)를 발표했고, .NET 개발자의 실용적인 관점에서 정리해 보겠습니다.

## 6가지 옵션 한눈에 보기

| 옵션 | 최적 용도 | 관리 대상 |
|------|----------|-----------|
| **Container Apps** | K8s 복잡성 없이 전체 컨테이너 제어 | 관측성, 상태, 라이프사이클 |
| **AKS** | 엔터프라이즈 컴플라이언스, 멀티 클러스터, 커스텀 네트워킹 | 모든 것 (그것이 포인트) |
| **Azure Functions** | 이벤트 기반 단기 에이전트 작업 | 거의 없음 — 진정한 서버리스 |
| **App Service** | 단순 HTTP 에이전트, 예측 가능한 트래픽 | 배포, 스케일링 설정 |
| **Foundry Agents** | 포털/SDK를 통한 코드 불필요 에이전트 | 거의 없음 |
| **Foundry Hosted Agents** | 관리형 인프라의 커스텀 프레임워크 에이전트 | 에이전트 코드만 |

처음 4개는 범용 컴퓨팅입니다 — 에이전트를 실행*할 수는* 있지만 그것을 위해 설계된 것은 아닙니다. 마지막 2개는 에이전트 네이티브로, 대화, 도구 호출, 에이전트 라이프사이클을 일급 개념으로 이해합니다.

## Foundry Hosted Agents — .NET 에이전트 개발자를 위한 최적점

제 주목을 끈 부분입니다. Foundry Hosted Agents는 정확히 중간에 위치합니다: 자신의 코드를 실행할 수 있는 유연성(Semantic Kernel, Agent Framework, LangGraph — 무엇이든)을 얻으면서 플랫폼이 인프라, 관측성, 대화 관리를 처리합니다.

핵심은 **Hosting Adapter**입니다 — 에이전트 프레임워크를 Foundry 플랫폼에 연결하는 얇은 추상화 레이어입니다. Microsoft Agent Framework의 경우:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

이것이 호스팅의 전부입니다. 어댑터가 프로토콜 변환, server-sent events를 통한 스트리밍, 대화 이력, OpenTelemetry 트레이싱을 자동으로 처리합니다. 커스텀 미들웨어도, 수동 배관 작업도 필요 없습니다.

## 배포가 진짜 간단합니다

이전에 Container Apps에 에이전트를 배포해 봤고 작동하지만, 상태 관리와 관측성을 위한 글루 코드를 많이 작성하게 됩니다. Hosted Agents와 `azd`를 사용하면:

```bash
# AI 에이전트 익스텐션 설치
azd ext install azure.ai.agents

# 템플릿에서 초기화
azd ai agent init

# 빌드, 푸시, 배포 — 완료
azd up
```

이 하나의 `azd up`이 컨테이너를 빌드하고, ACR에 푸시하고, Foundry 프로젝트를 프로비저닝하고, 모델 엔드포인트를 배포하고, 에이전트를 시작합니다. 다섯 단계가 하나의 명령어로 압축됩니다.

## 내장 대화 관리

프로덕션에서 가장 많은 시간을 절약하는 부분입니다. 자체 대화 상태 저장소를 구축하는 대신 Hosted Agents가 네이티브로 처리합니다:

```python
# 영구 대화 생성
conversation = openai_client.conversations.create()

# 첫 번째 턴
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# 두 번째 턴 — 컨텍스트 유지
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Redis 불필요. Cosmos DB 세션 스토어 불필요. 메시지 직렬화를 위한 커스텀 미들웨어 불필요. 플랫폼이 그냥 처리합니다.

## 나의 결정 프레임워크

6가지 옵션을 모두 검토한 후의 빠른 멘탈 모델:

1. **인프라가 필요 없다면?** → Foundry Agents (포털/SDK, 컨테이너 없음)
2. **커스텀 에이전트 코드가 있지만 관리형 호스팅을 원한다면?** → Foundry Hosted Agents
3. **이벤트 기반 단기 에이전트 작업이 필요하다면?** → Azure Functions
4. **K8s 없이 최대한의 컨테이너 제어가 필요하다면?** → Container Apps
5. **엄격한 컴플라이언스와 멀티 클러스터가 필요하다면?** → AKS
6. **예측 가능한 트래픽의 간단한 HTTP 에이전트라면?** → App Service

Semantic Kernel이나 Microsoft Agent Framework로 구축하는 대부분의 .NET 개발자에게 Hosted Agents가 적절한 출발점일 것입니다. Kubernetes를 관리하거나 자체 관측성 스택을 구축하지 않고도 scale-to-zero, 내장 OpenTelemetry, 대화 관리, 프레임워크 유연성을 얻을 수 있습니다.

## 마무리

Azure의 에이전트 호스팅 환경은 빠르게 성숙하고 있습니다. 오늘 새 AI 에이전트 프로젝트를 시작한다면, 습관적으로 Container Apps나 AKS를 선택하기 전에 Foundry Hosted Agents를 진지하게 고려해 보세요. 관리형 인프라가 실질적인 시간을 절약하고, hosting adapter 패턴으로 프레임워크 선택을 유지할 수 있습니다.

[Microsoft의 전체 가이드](https://devblogs.microsoft.com/all-things-azure/hostedagent/)와 [Foundry Samples 저장소](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents)에서 작동하는 예제를 확인하세요.
