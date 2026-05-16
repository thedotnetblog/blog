---
title: "A2A v1 출시: Microsoft Agent Framework for .NET의 크로스플랫폼 에이전트 통신"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "A2A 프로토콜 v1.0이 출시되고 Microsoft Agent Framework .NET 패키지가 업데이트되었습니다 — 공급자 간 AI 에이전트를 연결하고 노출하기 위한 안정적인 상호운용성 표준."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[A2A v1 출시: Microsoft Agent Framework for .NET의 크로스플랫폼 에이전트 통신](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — A2A 프로토콜이 v1.0에 도달했으며, .NET용 A2A Agent(클라이언트)와 A2A Hosting(서버) 패키지가 모두 업데이트되었습니다.

## A2A v1이 실제로 무엇인가

A2A는 AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, ServiceNow의 대표자들로 구성된 기술 운영 위원회가 지원하는 AI 에이전트를 위한 오픈 상호운용 프로토콜입니다. v1 레이블은 이제 안정적이고 프로덕션 준비가 된 표준임을 의미합니다. 이를 구현하는 SDK 및 Agent Framework 패키지는 아직 프리뷰 상태이지만, 프로토콜 자체는 확정되었습니다.

v1은 멀티 테넌시 지원, 암호화 ID를 위한 서명된 Agent Cards, 개선된 보안 흐름, 웹 정렬 아키텍처로 v0.3을 개선합니다.

## 원격 A2A 에이전트에 연결하기

원격 A2A 에이전트는 코드에서 단순히 `AIAgent`입니다 — 동일한 `RunAsync`, 동일한 스트리밍, 동일한 세션 처리:

```csharp
// Well-known URI를 통한 검색
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// 직접 구성
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// 스트리밍도 동일하게 작동
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## 에이전트를 A2A 엔드포인트로 노출하기

Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic 또는 AWS Bedrock에서 구축한 모든 `AIAgent`를 ASP.NET Core에서 두 줄로 A2A 엔드포인트로 노출할 수 있습니다:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

에이전트 카드는 `/.well-known/agent-card.json`에서 자동으로 제공됩니다.

## 실제로 이것이 의미하는 바

안정적인 v1 프로토콜은 파괴적 변경에 대한 걱정 없이 .NET 에이전트를 Python, Java 또는 다른 언어로 구축된 에이전트와 연결할 수 있음을 의미합니다. 서명된 Agent Cards의 암호화 ID는 에이전트 간 신뢰 검증의 기반도 제공합니다.

전체 변경 로그와 v0.3에서의 마이그레이션 노트는 [전체 게시물](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/)을 참조하세요.
