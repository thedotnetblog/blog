---
title: "Azure DevOps MCP Server가 Microsoft Foundry에 등장: AI 에이전트에 어떤 의미인가"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server가 이제 Microsoft Foundry에서 사용 가능합니다. 몇 번의 클릭으로 AI 에이전트를 DevOps 워크플로 — 작업 항목, 저장소, 파이프라인 — 에 직접 연결하세요."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP(Model Context Protocol)가 주목받고 있습니다. AI 에이전트 생태계를 따라가고 있다면, MCP 서버가 곳곳에서 등장하고 있다는 것을 알아차렸을 것입니다 — 표준화된 프로토콜을 통해 에이전트가 외부 도구 및 서비스와 상호 작용할 수 있게 해줍니다.

이제 [Azure DevOps MCP Server가 Microsoft Foundry에서 사용 가능](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/)하며, 이것은 실용적인 가능성에 대해 생각하게 만드는 통합 중 하나입니다.

## 실제로 무슨 일이 일어나고 있는가

Microsoft는 이미 Azure DevOps MCP Server를 [퍼블릭 프리뷰](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview)로 출시했습니다 — 그것이 MCP 서버 자체입니다. 새로운 것은 Foundry 통합입니다. 이제 도구 카탈로그에서 직접 Azure DevOps MCP Server를 Foundry 에이전트에 추가할 수 있습니다.

아직 Foundry를 모르는 분들을 위해: 대규모로 AI 기반 애플리케이션과 에이전트를 구축하고 관리하기 위한 Microsoft의 통합 플랫폼입니다. 모델 접근, 오케스트레이션, 평가, 배포 — 모두 한 곳에서.

## 설정하기

설정은 놀라울 정도로 간단합니다:

1. Foundry 에이전트에서 **Add Tools** > **Catalog**으로 이동
2. "Azure DevOps" 검색
3. Azure DevOps MCP Server(preview)를 선택하고 **Create** 클릭
4. 조직 이름을 입력하고 연결

그게 전부입니다. 이제 에이전트가 Azure DevOps 도구에 접근할 수 있습니다.

## 에이전트가 접근할 수 있는 것 제어하기

제가 높이 평가하는 부분입니다: 전부 아니면 전무 방식에 갇히지 않습니다. 에이전트에 사용 가능한 도구를 지정할 수 있습니다. 작업 항목만 읽고 파이프라인은 건드리지 않도록 하려면 그렇게 설정할 수 있습니다. 최소 권한 원칙을 AI 에이전트에 적용하는 것이죠.

이것은 누군가가 "릴리스를 도와줘"라고 요청했다고 해서 에이전트가 실수로 배포 파이프라인을 트리거하는 것을 원하지 않는 엔터프라이즈 시나리오에서 중요합니다.

## .NET 팀에게 왜 흥미로운가

실제로 이것이 무엇을 가능하게 하는지 생각해 보세요:

- **스프린트 계획 어시스턴트** — 작업 항목을 가져오고, 속도 데이터를 분석하고, 스프린트 용량을 제안할 수 있는 에이전트
- **코드 리뷰 봇** — 실제로 저장소와 연결된 작업 항목을 읽을 수 있기 때문에 PR 컨텍스트를 이해하는 에이전트
- **인시던트 대응** — 작업 항목을 생성하고, 최근 배포를 조회하고, 버그와 최근 변경 사항을 상관시킬 수 있는 에이전트
- **개발자 온보딩** — "무엇을 해야 하나요?"가 실제 프로젝트 데이터에 기반한 진짜 답변을 받게 됩니다

CI/CD 파이프라인과 프로젝트 관리에 이미 Azure DevOps를 사용하는 .NET 팀에게, 이러한 시스템과 직접 상호 작용할 수 있는 AI 에이전트는 유용한 자동화를 향한 의미 있는 한 걸음입니다.

## 더 큰 MCP 그림

이것은 더 넓은 트렌드의 일부입니다: MCP 서버는 AI 에이전트가 외부 세계와 상호 작용하는 표준 방식이 되어가고 있습니다. GitHub, Azure DevOps, 데이터베이스, SaaS API에서 볼 수 있으며 — Foundry는 이 모든 연결이 모이는 허브가 되고 있습니다.

.NET 생태계에서 에이전트를 구축하고 있다면, MCP에 주목할 가치가 있습니다. 프로토콜은 표준화되고, 도구는 성숙해지고 있으며, Foundry 통합은 수동으로 서버 연결을 설정할 필요 없이 접근 가능하게 해줍니다.

## 마무리

Foundry의 Azure DevOps MCP Server는 프리뷰 상태이므로 발전을 기대하세요. 하지만 핵심 워크플로는 견고합니다: 연결하고, 도구 접근을 설정하고, 에이전트가 DevOps 데이터로 작업하게 하세요. 이미 Foundry 생태계에 있다면 몇 번의 클릭이면 됩니다. 시도해보고 어떤 워크플로를 구축할 수 있는지 확인해 보세요.

단계별 설정과 자세한 내용은 [전체 공지](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/)를 확인하세요.
