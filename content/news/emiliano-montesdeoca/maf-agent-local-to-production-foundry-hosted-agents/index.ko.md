---
title: "로컬 MAF 에이전트가 드디어 프로덕션에 자리를 잡았습니다"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents는 Microsoft Agent Framework 에이전트에 ID, 스케일링, 세션 지속성, 추가 설정 없는 관찰성을 제공합니다. 실제로 어떻게 보이는지 살펴보겠습니다."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

에이전트를 로컬에서 작동시키는 것은 재미있는 부분입니다. 어려운 부분은 그 이후의 모든 것입니다: 정신을 잃지 않고 배포하기, 세션 관리, ID 설정, 관찰성 연결. 보통 이는 많은 커스텀 인프라 연결 작업을 의미합니다.

Foundry Hosted Agents는 Microsoft Agent Framework (MAF) 사용자를 위해 그러한 연결 작업의 대부분을 제거했습니다.

## Foundry Hosted Agents가 실제로 하는 것

MAF 에이전트를 Foundry Hosted Agents에 배포하면, 플랫폼이 직접 만들어야 했을 놀랍도록 긴 목록의 것들을 처리합니다:

- **제로로 스케일** — 에이전트가 유휴 상태일 때 비용이 들지 않고 자동으로 재시작됩니다
- **세션당 VM 격리 샌드박스** — 각 사용자 세션은 스케일 다운 이벤트를 견디는 파일시스템 지속성을 가진 자체 샌드박스를 얻습니다
- **내장 Entra ID** — 각 에이전트는 이미지에 시크릿 없이 Foundry 모델, Toolbox, Azure 서비스를 호출할 수 있는 자체 ID를 얻습니다
- **버전이 지정된 배포** — 각 배포는 불변 스냅샷으로, blue/green 및 카나리 롤아웃 지원이 있습니다
- **설정 없는 관찰성** — `APPLICATIONINSIGHTS_CONNECTION_STRING`이 런타임에 주입되어 MAF의 OpenTelemetry 트레이스가 App Insights로 자동으로 흐릅니다

마지막은 정말 편리합니다. 추가 배선 없음, 추가 설정 없음. 트레이스가 그냥 나타납니다.

## 코드 차이는 최소

이 통합에서 가장 마음에 드는 부분입니다. 에이전트를 다시 작성할 필요가 없습니다. 그냥 래핑하면 됩니다:

**.NET의 경우:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Python의 경우:**

```python
server = ResponsesHostServer(agent)
server.run()
```

그게 다입니다. 로컬에서 테스트한 것과 동일한 로직이 프로덕션에서 실행됩니다. 플랫폼은 세션 관리, ID, 스케일링 인프라로 이를 래핑합니다.

## 두 가지 프로토콜, 하나의 에이전트

Hosted Agents는 두 가지 엔드포인트 스타일을 지원합니다:

- **Responses** (`/responses`) — OpenAI 호환, 대화 기록과 스트리밍을 관리합니다. 채팅 형태의 에이전트에 좋은 기본값.
- **Invocations** (`/invocations`) — 요청/응답 스키마를 직접 정의합니다. 비대화적 워크플로우에 적합.

대화처럼 보이는 것을 만들고 있다면 Responses로 시작하세요. 구조화된 입력을 받아 구조화된 출력을 반환하는 API 형태의 에이전트를 만들고 있다면 Invocations가 유연성을 제공합니다.

## `azd`를 사용한 배포 흐름

MAF 에이전트로 `azd up`을 실행하면:

1. 선택적으로 Foundry 프로젝트를 생성하고 모델을 배포
2. 코드를 패키징하고 Azure Container Registry에 이미지를 푸시
3. ACR 이미지에서 컴퓨팅 프로비저닝
4. 에이전트에 전용 Entra ID 할당
5. 안정적인 엔드포인트 노출 (`https://{project_endpoint}/agents/{agent_name}`)
6. 그 이후 모든 것을 처리

세션은 최대 30일 동안 지속됩니다. 유휴 컴퓨팅은 15분 후 디프로비저닝되고 다음 요청 시 투명하게 복원됩니다. 에이전트 입장에서는 아무것도 변하지 않았습니다.

## 마무리

"로컬에서 작동"에서 "프로덕션에서 실행"까지의 거리는 AI 에이전트에게 역사적으로 길고 고통스러웠습니다. Foundry Hosted Agents + MAF는 그 격차를 크게 줄입니다. Agent Framework로 구축된 로컬 에이전트가 이미 있다면 오늘 시도해볼 만합니다.

팀은 GA가 곧 온다고 합니다 — 현재 프리뷰 중입니다. 시작하려면 [MAF Hosted Agent 통합 문서](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent)와 [.NET 샘플](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents)을 확인하세요.

원본 게시물: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
