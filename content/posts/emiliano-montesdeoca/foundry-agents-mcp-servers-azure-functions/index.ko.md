---
title: "Azure Functions의 MCP 서버를 Foundry 에이전트에 연결하는 방법"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "MCP 서버를 한 번 구축하고 Azure Functions에 배포한 다음, 적절한 인증으로 Microsoft Foundry 에이전트에 연결하세요. 도구는 어디서나 작동합니다 — VS Code, Cursor, 그리고 이제 엔터프라이즈 AI 에이전트에서도."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}})에서 확인하세요.*

MCP 생태계에서 제가 좋아하는 점이 있습니다: 서버를 한 번 구축하면 어디서나 작동한다는 것입니다. VS Code, Visual Studio, Cursor, ChatGPT — 모든 MCP 클라이언트가 여러분의 도구를 발견하고 사용할 수 있습니다. 이제 Microsoft가 그 목록에 또 다른 소비자를 추가하고 있습니다: Foundry 에이전트입니다.

Azure SDK 팀의 Lily Ma가 Azure Functions에 배포된 MCP 서버를 Microsoft Foundry 에이전트에 연결하는 [실용 가이드를 발표](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/)했습니다. 이미 MCP 서버가 있다면 순수한 부가가치입니다 — 재구축이 필요 없습니다.

## 이 조합이 합리적인 이유

Azure Functions는 MCP 서버 호스팅을 위한 확장 가능한 인프라, 기본 제공 인증, 서버리스 과금을 제공합니다. Microsoft Foundry는 추론하고, 계획하고, 행동할 수 있는 AI 에이전트를 제공합니다. 둘을 연결하면 커스텀 도구 — 데이터베이스 쿼리, 비즈니스 API 호출, 검증 로직 실행 — 가 엔터프라이즈 AI 에이전트가 자율적으로 발견하고 사용할 수 있는 기능이 됩니다.

핵심 포인트: MCP 서버는 그대로 유지됩니다. Foundry를 또 다른 소비자로 추가하는 것뿐입니다. VS Code 설정에서 작동하는 동일한 도구가 이제 팀이나 고객이 상호작용하는 AI 에이전트를 구동합니다.

## 인증 옵션

여기서 이 글이 진정한 가치를 제공합니다. 시나리오에 따른 네 가지 인증 방법:

| 방법 | 사용 사례 |
|------|---------|
| **키 기반** (기본) | 개발 또는 Entra 인증 없는 서버 |
| **Microsoft Entra** | 관리 ID를 사용한 프로덕션 |
| **OAuth 아이덴티티 패스스루** | 각 사용자가 개별 인증하는 프로덕션 |
| **인증 없음** | 개발/테스트 또는 공개 데이터만 |

프로덕션에서는 에이전트 ID를 사용한 Microsoft Entra가 권장 경로입니다. OAuth 아이덴티티 패스스루는 사용자 컨텍스트가 중요할 때 사용합니다 — 에이전트가 사용자에게 로그인을 요청하고, 각 요청이 사용자 자신의 토큰을 전달합니다.

## 설정하기

대략적인 흐름:

1. **MCP 서버를 Azure Functions에 배포** — [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript, Java 샘플 제공
2. **함수 앱에서 기본 제공 MCP 인증 활성화**
3. **엔드포인트 URL 가져오기** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Foundry에 MCP 서버를 도구로 추가** — 포털에서 에이전트로 이동, 새 MCP 도구 추가, 엔드포인트와 자격 증명 제공

그런 다음 Agent Builder 플레이그라운드에서 도구 중 하나를 트리거할 프롬프트를 보내 테스트합니다.

## 제 의견

여기서의 조합성 이야기는 정말 강력해지고 있습니다. .NET(또는 Python, TypeScript, Java)으로 MCP 서버를 한 번 구축하고, Azure Functions에 배포하면, 모든 MCP 호환 클라이언트가 사용할 수 있습니다 — 코딩 도구, 채팅 앱, 그리고 이제 엔터프라이즈 AI 에이전트. 실제로 작동하는 "한 번 작성, 어디서나 사용" 패턴입니다.

특히 .NET 개발자에게 [Azure Functions MCP 확장](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)이 이를 간단하게 만들어줍니다. 도구를 Azure Functions로 정의하고, 배포하면, Azure Functions가 제공하는 모든 보안과 확장성을 갖춘 프로덕션 등급의 MCP 서버를 갖게 됩니다.

## 마무리

Azure Functions에서 MCP 도구를 실행하고 있다면, Foundry 에이전트에 연결하는 것은 빠른 성과입니다 — 커스텀 도구가 적절한 인증을 갖춘 엔터프라이즈 AI 기능이 되며, 서버 자체의 코드 변경은 없습니다.

각 인증 방법에 대한 단계별 안내는 [전체 가이드](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/)를, 프로덕션 설정에 대해서는 [상세 문서](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry)를 확인하세요.
