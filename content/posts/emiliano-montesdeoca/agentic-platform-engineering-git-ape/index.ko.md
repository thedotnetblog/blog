---
title: "에이전틱 플랫폼 엔지니어링이 현실이 되고 있다 — Git-APE가 방법을 보여준다"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft의 Git-APE 프로젝트가 에이전틱 플랫폼 엔지니어링을 실전에 적용합니다 — GitHub Copilot 에이전트와 Azure MCP를 사용하여 자연어 요청을 검증된 클라우드 인프라로 전환합니다."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "agentic-platform-engineering-git-ape" >}})에서 확인하세요.*

플랫폼 엔지니어링은 컨퍼런스에서는 멋지게 들리지만 보통 "내부 포털과 Terraform 래퍼를 만들었습니다"를 의미하는 용어 중 하나였습니다. 진정한 약속 — 실제로 안전하고, 거버넌스가 적용되고, 빠른 셀프 서비스 인프라 — 는 항상 몇 발짝 떨어져 있었습니다.

Azure 팀이 [에이전틱 플랫폼 엔지니어링 시리즈의 파트 2](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/)를 발표했는데, 이번에는 실전 구현에 대한 내용입니다. **Git-APE**라고 부릅니다 (네, 약어는 의도적입니다). 이것은 GitHub Copilot 에이전트와 Azure MCP 서버를 사용하여 자연어 요청을 검증되고 배포된 인프라로 전환하는 오픈소스 프로젝트입니다.

## Git-APE가 실제로 하는 것

핵심 아이디어: 개발자가 Terraform 모듈을 배우거나, 포털 UI를 탐색하거나, 플랫폼 팀에 티켓을 올리는 대신, Copilot 에이전트와 대화합니다. 에이전트가 의도를 해석하고, Infrastructure-as-Code를 생성하고, 정책에 대해 검증하고, 배포합니다 — 모두 VS Code 안에서.

설정은 이렇습니다:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

VS Code에서 워크스페이스를 열면 에이전트 설정 파일이 GitHub Copilot에 의해 자동 검색됩니다. 에이전트와 직접 상호작용합니다:

```
@git-ape deploy a function app with storage in West Europe
```

에이전트는 내부적으로 Azure MCP Server를 사용하여 Azure 서비스와 상호작용합니다. VS Code 설정의 MCP 구성이 특정 기능을 활성화합니다:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## 왜 이게 중요한가

Azure에서 개발하는 우리에게 이것은 플랫폼 엔지니어링 대화를 "포털을 어떻게 만들까"에서 "가드레일을 API로 어떻게 기술할까"로 전환시킵니다. 플랫폼의 인터페이스가 AI 에이전트가 되면, 제약 조건과 정책의 품질이 곧 제품이 됩니다.

파트 1 블로그는 이론을 제시했습니다: 잘 기술된 API, 제어 스키마, 그리고 명시적인 가드레일이 플랫폼을 에이전트 대응(agent-ready)으로 만듭니다. 파트 2는 실제 도구를 제공하여 이것이 작동한다는 것을 증명합니다. 에이전트는 리소스를 무작정 생성하지 않습니다 — 모범 사례에 대해 검증하고, 명명 규칙을 존중하며, 조직의 정책을 적용합니다.

정리도 마찬가지로 간단합니다:

```
@git-ape destroy my-resource-group
```

## 내 생각

솔직히 — 이건 특정 도구보다는 패턴에 대한 이야기입니다. Git-APE 자체는 데모/참조 아키텍처입니다. 하지만 근본적인 아이디어 — 플랫폼의 인터페이스로서의 에이전트, 프로토콜로서의 MCP, 호스트로서의 GitHub Copilot — 이것이 엔터프라이즈 개발자 경험이 향하는 방향입니다.

내부 도구를 에이전트 친화적으로 만드는 방법을 찾는 플랫폼 팀이라면, 이보다 나은 출발점은 없습니다. 그리고 .NET 개발자로서 이것이 자신의 세계와 어떻게 연결되는지 궁금하다면: Azure MCP Server와 GitHub Copilot 에이전트는 모든 Azure 워크로드에서 작동합니다. ASP.NET Core API, .NET Aspire 스택, 컨테이너화된 마이크로서비스 — 모두가 에이전틱 배포 플로우의 대상이 될 수 있습니다.

## 마무리

Git-APE는 에이전틱 플랫폼 엔지니어링 실전의 초기이지만 구체적인 모습입니다. [저장소](https://github.com/Azure/git-ape)를 클론하고, 데모를 시도하고, 에이전트가 안전하게 사용할 수 있도록 플랫폼의 API와 정책이 어떤 모습이어야 하는지 생각해 보세요.

자세한 워크스루와 데모 비디오는 [전체 포스트](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/)를 읽어보세요.
