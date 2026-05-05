---
title: "Foundry Toolboxes: AI 에이전트 도구를 위한 단일 엔드포인트"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry가 Toolboxes를 공개 프리뷰로 출시했습니다. AI 에이전트 도구를 단일 MCP 호환 엔드포인트를 통해 관리하고 노출하는 방법입니다."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

직접 겪기 전까지는 사소해 보이는 문제가 있다: 조직이 여러 AI 에이전트를 구축하고, 각 에이전트는 도구가 필요하며, 각 팀은 처음부터 다시 구성한다. 같은 웹 검색 통합, 같은 Azure AI Search 설정, 같은 GitHub MCP 서버 연결 — 하지만 다른 저장소에, 다른 팀이, 다른 자격증명으로, 공유 거버넌스 없이.

Microsoft Foundry가 공개 프리뷰로 [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)를 출시했으며, 이는 그 문제에 대한 직접적인 해답이다.

## Toolbox란

Toolbox는 Foundry에서 한 번 정의하고 단일 MCP 호환 엔드포인트를 통해 노출하는 명명된 재사용 가능한 도구 번들이다. MCP를 사용하는 모든 에이전트 런타임이 소비할 수 있다 — Foundry Agents에 종속되지 않는다.

제안은 간단하다: **build once, consume anywhere**. 도구를 정의하고, 인증을 중앙에서 설정하고 (OAuth 패스스루, Entra 관리 ID), 엔드포인트를 게시한다. 그 도구가 필요한 각 에이전트는 엔드포인트에 연결하면 모두 가져온다.

## 4개의 기둥 (오늘 2개 사용 가능)

| 기둥 | 상태 | 기능 |
|------|------|------|
| **Discover** | 출시 예정 | 수동 검색 없이 승인된 도구 발견 |
| **Build** | 사용 가능 | 도구를 재사용 가능한 번들로 구성 |
| **Consume** | 사용 가능 | 단일 MCP 엔드포인트가 모든 도구 노출 |
| **Govern** | 출시 예정 | 모든 도구 호출의 중앙 인증 + 가시성 |

## 실제 예시

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="문서를 검색하고 GitHub 이슈에 응답",
    tools=[
        {"type": "web_search", "description": "공개 문서 검색"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

게시 후 Foundry는 통합 엔드포인트를 제공한다. 한 번 연결하면 모든 도구를 사용할 수 있다.

## Foundry Agents에 종속되지 않는다

Toolboxes는 Foundry에서 **생성·관리**되지만 소비 면은 오픈 MCP 프로토콜이다. Microsoft Agent Framework나 LangGraph로 만든 커스텀 에이전트, GitHub Copilot 및 기타 MCP 지원 IDE에서 사용할 수 있다.

## 지금 왜 중요한가

멀티 에이전트 물결이 프로덕션에 도달하고 있다. 새로운 에이전트마다 중복 설정, 오래된 자격증명, 일관성 없는 동작의 새로운 표면이 생긴다. Build + Consume 기반은 중앙화를 시작하기에 충분하다. Govern 기둥이 출시되면 전체 에이전트 플리트에 완전히 관찰 가능하고 중앙 제어되는 도구 계층을 갖게 된다.

## 마무리

아직 초기 단계다 — 공개 프리뷰, Python SDK 우선, Discover와 Govern은 예정되어 있다. 하지만 모델은 견고하고, MCP 네이티브 설계는 이미 구축 중인 도구와 함께 작동한다는 것을 의미한다. [공식 발표](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)를 확인해 시작해보자.
