---
title: ".NET의 Composable Stack으로 AI 기반 컨퍼런스 앱 만들기"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft는 ConferencePulse를 구축했습니다 — Microsoft.Extensions.AI, DataIngestion, VectorData, MCP, Agent Framework를 조합한 라이브 컨퍼런스 Blazor 앱. 각 부분이 어떻게 맞아 떨어지는지 설명합니다."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[.NET의 Composable Stack으로 AI 기반 컨퍼런스 앱 만들기](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft는 다섯 개의 .NET 확장 라이브러리를 조합하여 라이브 컨퍼런스 세션용 Blazor Server 앱인 ConferencePulse를 구축했습니다. MVP Summit에서 사용되었습니다.

## ConferencePulse가 하는 일

ConferencePulse는 라이브 세션 중에 실행되며 다음을 제공합니다: 세션 콘텐츠에서 AI가 생성하는 폴, 라이브 지식 베이스에서 가져오는 RAG 파이프라인을 통한 청중 Q&A, 자동 생성된 인사이트, 여러 동시 AI 에이전트가 생성하는 세션 요약. 스택은 .NET 10, Blazor Server, Aspire이며 다섯 개의 프로젝트로 분할됩니다: Web, Core, Ingestion, Agents, Mcp, AppHost.

## Microsoft.Extensions.AI: 모든 것을 위한 하나의 추상화

`IChatClient`는 통합 추상화입니다 — 한 번 설정하면 동일한 인터페이스가 Azure OpenAI, OpenAI, Anthropic 또는 다른 공급자에서 작동합니다. 함수 호출, OpenTelemetry 추적 및 로깅 미들웨어가 포함된 완전히 구성된 클라이언트를 얻기 위한 여섯 줄:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

동일한 `IChatClient`는 나중에 데이터 수집 보강 단계에 재사용됩니다 — 그를 위한 별도의 클라이언트가 필요 없습니다.

## DataIngestion 파이프라인

세션 콘텐츠는 파이프라인을 통해 흐릅니다: `MarkdownReader` → `HeaderChunker` (500 토큰, 50 토큰 오버랩) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). 보강기는 인덱싱 전에 요약을 생성하고 키워드를 추출하기 위해 동일한 `IChatClient`를 사용합니다. 청중 질문, Q&A 쌍, 폴 결과는 세션이 진행되면서 실시간으로 수집됩니다 — 지식 베이스는 발표 중에 성장합니다.

## VectorData: 공급자에 독립적인 검색

`VectorStoreCollection.SearchAsync()`는 백킹 스토어가 Qdrant이든 Azure AI Search이든 동일하게 작동합니다. 하이브리드 검색 (벡터 + 전체 텍스트)이 지원됩니다. 청중 Q&A를 위한 RAG 파이프라인은 이 컬렉션을 쿼리하고 채팅 클라이언트에 컨텍스트로 전달할 관련 청크를 가져옵니다.

## MCP: 도구로서의 세션 콘텐츠

세션 콘텐츠는 MCP를 통해 노출되어 MCP 호환 클라이언트가 접근할 수 있습니다. 서버와 클라이언트 모두 구현됩니다 — 서버는 세션 지식을 MCP 도구로 노출하고, 클라이언트는 에이전트 파이프라인 내에서 해당 도구를 호출할 수 있게 합니다.

## Agent Framework: 병렬 멀티 에이전트 요약

세션 요약은 동시에 실행되는 세 에이전트에 의해 생성됩니다 — `PollSummaryAgent`, `QuestionSummaryAgent`, `InsightSummaryAgent` — 그런 다음 병합됩니다. 이는 Microsoft Agent Framework의 그룹 채팅 또는 병렬 실행 패턴을 사용합니다. 각 에이전트는 하나의 관심사를 처리하고, 오케스트레이터가 출력을 병합합니다.

## 설계 원칙

이 게시물은 기억할 만한 포인트를 제시합니다: 맞는 가장 단순한 도구를 사용하세요. 간단한 생성 작업에는 직접 `IChatClient` 호출. 구조화된 데이터 추출에는 도구/함수 호출. 자율적인 멀티 스텝 추론이 필요할 때만 전체 에이전트를 사용. 라이브러리 레이어링이 이를 강제합니다 — 전체 Agent Framework를 가져오지 않고도 `Microsoft.Extensions.AI`를 사용할 수 있습니다.

전체 프로젝트 구조와 소스 링크를 보려면 [전체 게시물](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/)을 참조하세요.
