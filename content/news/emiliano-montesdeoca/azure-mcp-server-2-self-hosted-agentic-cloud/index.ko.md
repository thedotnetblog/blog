---
title: "Azure MCP Server 2.0 출시 — 자체 호스팅 에이전트형 클라우드 자동화가 이제 시작됩니다"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0이 자체 호스팅 원격 배포, 57개 Azure 서비스에 걸친 276개 도구, 엔터프라이즈급 보안과 함께 안정화되었습니다. .NET 개발자들이 에이전트형 워크플로우를 구축할 때 알아야 할 내용을 정리했습니다."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *이 글은 자동 번역되었습니다. 원본은 [여기]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud.md" >}})에서 확인하세요.*

최근에 MCP와 Azure로 뭔가를 구축해본 분이라면 로컬 환경에서는 잘 작동한다는 걸 아실 겁니다. MCP 서버를 연결하고, AI 에이전트가 Azure 리소스와 대화하도록 하고, 끝. 하지만 그 설정을 팀 전체에서 공유해야 하는 순간? 그곳이 바로 복잡해지던 지점이었습니다.

이제 더 이상 그럴 필요 없습니다. Azure MCP Server [방금 2.0 안정 버전에 도달했고](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), 이번 주요 기능은 정확히 엔터프라이즈 팀들이 요청해온 것입니다: **자체 호스팅 원격 MCP 서버 지원**.

## Azure MCP Server란?

간단히 정리하겠습니다. Azure MCP Server는 [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) 명세를 구현하고 Azure의 기능을 구조화되고 발견 가능한 도구로 노출하여 AI 에이전트가 호출할 수 있도록 합니다. 에이전트와 Azure 사이의 표준화된 브릿지라고 생각하면 됩니다. 프로비저닝, 배포, 모니터링, 진단, 모든 것이 하나의 일관된 인터페이스를 통해 이루어집니다.

숫자만 봐도 충분합니다: **57개 Azure 서비스에 걸친 276개의 MCP 도구**. 정말 강력한 커버리지입니다.

## 핵심: 자체 호스팅 원격 배포

이게 중요한 이유는 뭘까요. 로컬 머신에서 MCP를 실행하는 건 개발과 실험에는 충분합니다. 하지만 실제 팀 환경에서는 다음이 필요합니다:

- 개발자와 내부 에이전트 시스템을 위한 공유 액세스
- 중앙 집중식 구성(테넌트 컨텍스트, 구독 기본값, 텔레메트리)
- 엔터프라이즈 네트워크 및 정책 경계
- CI/CD 파이프라인 통합

Azure MCP Server 2.0은 이 모든 것을 다룹니다. HTTP 기반 전송, 적절한 인증, 일관된 거버넌스와 함께 중앙에서 관리되는 내부 서비스로 배포할 수 있습니다.

인증에 대해서는 두 가지 견고한 옵션이 있습니다:

1. **Managed Identity** — [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)와 함께 실행할 때
2. **On-Behalf-Of (OBO) flow** — 로그인한 사용자의 컨텍스트를 사용하여 Azure API를 호출하는 OpenID Connect 위임

이 OBO 흐름은 우리 .NET 개발자들에게 특히 흥미롭습니다. 이는 에이전트형 워크플로우가 과도한 권한을 가진 서비스 계정이 아닌 실제 사용자의 권한으로 작동할 수 있다는 의미입니다. 최소 권한 원칙이 처음부터 내장되어 있는 것입니다.

## 보안 강화

단순한 기능 릴리스가 아닙니다. 보안 측면의 업그레이드이기도 합니다. 2.0 릴리스는 다음을 추가합니다:

- 더 강화된 엔드포인트 검증
- 쿼리 지향 도구의 주입 패턴에 대한 보호
- 개발 환경을 위한 더 엄격한 격리 제어

MCP를 공유 서비스로 노출할 거라면, 이러한 보안 조치들은 정말 중요합니다.

## 어디서 사용할 수 있나요?

클라이언트 호환성 범위는 매우 넓습니다. Azure MCP Server 2.0은 다음과 함께 작동합니다:

- **IDE**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **CLI 에이전트**: GitHub Copilot CLI, Claude Code
- **독립 실행형**: 간단한 설정을 위한 로컬 서버
- **자체 호스팅 원격**: 2.0의 새로운 주인공

또한 Azure US Government와 21Vianet에 의해 운영되는 Azure를 위한 소버린 클라우드 지원이 있으며, 이는 규제 대상 배포에 필수적입니다.

## .NET 개발자에게 왜 중요한가요?

Semantic Kernel, Microsoft Agent Framework, 또는 자체 오케스트레이션이든 .NET으로 에이전트형 애플리케이션을 구축하고 있다면, Azure MCP Server 2.0은 에이전트가 Azure 인프라와 상호작용할 수 있는 프로덕션 준비 방식을 제공합니다. 커스텀 REST 래퍼 없음. 서비스별 통합 패턴 없음. 오직 MCP뿐입니다.

며칠 전에 출시된 [MCP Apps용 유창한 API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)와 함께라면, .NET MCP 생태계는 빠르게 성숙해지고 있습니다.

## 시작하기

자신의 경로를 선택하세요:

- **[GitHub Repo](https://aka.ms/azmcp)** — 소스 코드, 문서, 모든 것
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — 컨테이너화된 배포
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — IDE 통합
- **[Self-hosting guide](https://aka.ms/azmcp/self-host)** — 2.0의 주요 기능

## 마치며

Azure MCP Server 2.0은 데모에서는 화려해 보이지 않지만 실제로는 모든 것을 바꾸는 인프라 업그레이드입니다. 적절한 인증, 보안 강화, 소버린 클라우드 지원과 함께하는 자체 호스팅 원격 MCP는 MCP가 Azure에서 실제 에이전트형 워크플로우를 구축하는 실제 팀을 위해 준비되었다는 의미입니다. "엔터프라이즈 준비 완료"라는 신호를 기다리고 있었다면, 이것이 바로 그 신호입니다.
