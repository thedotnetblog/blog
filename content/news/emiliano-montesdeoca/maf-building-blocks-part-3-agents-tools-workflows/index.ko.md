---
title: "Microsoft Agent Framework 3부: 도구에서 워크플로우까지 — 빌딩 블록이 딱 맞게 자리를 잡다"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: ".NET AI 빌딩 블록 시리즈 3부에서는 Microsoft Agent Framework를 다룹니다 — 도구가 있는 단일 에이전트부터 메모리를 갖춘 멀티 에이전트 워크플로우까지. 진짜 중요한 것이 무엇인지 살펴봅니다."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기]({{< ref "index.md" >}})를 클릭하세요.*

.NET의 Building Blocks for AI 시리즈를 따라왔다면, 1부에서 `IChatClient`(범용 모델 인터페이스)를, 2부에서 `Microsoft.Extensions.VectorData`(시맨틱 검색 및 RAG)를 다뤘다는 것을 알 것입니다. 둘 다 기본적이고 각각 유용합니다. 하지만 여기서부터 모든 것이 연결되기 시작합니다.

3부는 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)에 관한 것입니다 — 솔직히 말하면, .NET에서 보고 싶었던 바로 그 피스입니다. 1.0은 4월에 출시되었습니다. API는 안정적입니다. 이제 진짜 에이전트를 만들 때가 됐습니다.

## 에이전트란 무엇인가 (vs. 챗봇)

코드로 들어가기 전에 이 구분을 명확히 해봅시다. 챗봇은 입력을 받고, 모델을 호출하고, 출력을 반환합니다. 단순한 루프입니다.

에이전트는 *자율성*을 갖습니다. 작업에 대해 추론하고, 어떤 도구를 사용할지 결정하고, 그 도구를 호출하고, 결과를 평가하고, 다음에 무엇을 할지 결정할 수 있습니다 — 모든 시나리오에 대해 단계별 로직을 작성할 필요 없이. 도구와 지침을 주면, 오케스트레이션을 알아서 처리합니다.

이렇게 생각해보세요: `IChatClient`는 대화를 나누는 것과 같습니다. 에이전트는 누군가에게 할 일 목록을 위임하는 것과 같습니다.

## 10줄로 첫 번째 에이전트 만들기

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

`.AsAIAgent()` 확장 메서드가 다리 역할을 합니다. MEAI의 `.AsIChatClient()`와 같은 패턴 — 프로바이더의 SDK를 안정적인 추상화로 래핑합니다. Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry 또는 로컬 모델과 함께 작동합니다.

스트리밍도 가능합니다:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## 에이전트에게 도구 제공하기

여기서 에이전트가 정교한 챗봇에서 벗어납니다. 도구는 사용자의 요청에 따라 모델이 호출하기로 결정할 수 있는 함수입니다. 라우팅 로직이 필요 없습니다 — 모델이 스스로 파악합니다.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

두 가지에 주목하세요. 첫째, `AIFunctionFactory`는 MEAI에서 옵니다 — 일반 `IChatClient`와 함께 사용하는 것과 같은 도구 팩토리입니다. 채팅 시나리오용으로 이미 도구를 정의했다면 여기서도 작동합니다.

둘째, `Description` 속성이 매우 중요합니다. 이것이 모델이 도구가 무엇을 하는지, 언제 사용해야 하는지 이해하는 방법입니다. 인간이 아닌 AI를 위한 문서로 취급하세요.

## 세션: 진짜 기억하는 대화

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

세션 없이는 각 `RunAsync` 호출이 상태 비저장입니다. 세션이 있으면 에이전트는 어떤 농담을 말하는지 알고 있습니다. `AgentSession`은 턴 사이에 대화 기록을 보존합니다.

프로덕션 상태 비저장 서비스의 경우 세션은 깔끔하게 직렬화됩니다:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... 어딘가에 저장 ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

에이전트가 서버리스 또는 수평 확장 환경에서 실행되는 경우 매우 중요합니다.

## AIContextProvider: 세션을 넘나드는 영구 메모리

세션은 세션 *내의* 대화 기록을 보존합니다. 그렇다면 세션 간에 사용자에 대한 정보를 알고 있는 것은 어떨까요? `AIContextProvider`가 이를 처리합니다.

두 가지 훅이 있습니다:
- **`ProvideAIContextAsync`** — 각 인터랙션 *이전에* 실행되어 에이전트에 컨텍스트를 주입
- **`StoreAIContextAsync`** — 각 인터랙션 *이후에* 실행되어 학습하고 지속

패턴이 우아합니다: 여러 프로바이더를 쌓을 수 있습니다 — 사용자 선호도용, 최근 인터랙션용, 관련 문서를 위해 VectorData 스토어를 쿼리하는 것 등. 마지막 것이 바로 2부의 RAG 패턴이며, 이제 모든 에이전트 호출의 일부로 자동으로 실행됩니다.

## 멀티 에이전트 워크플로우

여기서 프레임워크가 이름값을 합니다. 익스큐터(에이전트, 함수, 무엇이든)가 엣지를 통해 연결되는 그래프 기반 워크플로우 시스템을 포함합니다.

기본으로 지원되는 패턴:

- **순차적**: 에이전트 A의 출력이 에이전트 B에게 흘러들어감
- **동시(팬아웃/팬인)**: 여러 에이전트에 병렬 디스패치, 결과 수집
- **조건부 라우팅**: 출력에 따라 다른 에이전트에게 작업 라우팅
- **작가-비평가 루프**: 한 에이전트가 쓰고, 다른 에이전트가 평가하고, 승인될 때까지 루프
- **서브 워크플로우**: 계층적으로 워크플로우 구성

작가-비평가 예시:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

깔끔하고 읽기 쉬우며, 조건 기반 라우팅 덕분에 루프 로직을 직접 작성할 필요가 없습니다.

## 휴먼-인-더-루프

모든 것이 완전 자율적으로 실행되어서는 안 됩니다. 민감한 작업 — 데이터베이스 쓰기, 금융 거래, 통신 발송 — 에는 에이전트가 실행하기 전에 사람의 승인이 필요합니다.

프레임워크는 `FunctionApprovalRequestContent`와 `FunctionApprovalResponseContent`를 통해 이에 대한 내장 지원을 제공합니다. 에이전트가 도구 호출을 제안하면 애플리케이션 코드가 사용자에게 제시하고, 응답이 실행 계속 여부를 결정합니다.

이것이 엔터프라이즈 환경에서 에이전트를 생각하는 올바른 방식입니다: 완전 자율이 아니라 *가드레일이 있는 자율성*.

## 전체 그림

한 발 물러서면:

- **MEAI**는 어떤 모델에도 범용 인터페이스를 제공
- **VectorData**는 시맨틱 검색을 통해 에이전트가 조직의 지식에 접근하도록 지원
- **Agent Framework**는 모든 것을 오케스트레이션 — 내부적으로 `IChatClient` 사용, 컨텍스트 프로바이더와 결합, 워크플로우를 통해 조율

각 부분은 다른 부분과 구성되도록 설계되었습니다. [Jeremy Likness의 원본 포스트](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/)와 [Agent Framework GitHub 레포지토리](https://github.com/microsoft/agent-framework/tree/main/dotnet)에서 전체 샘플을 확인하세요.

## 마무리

Microsoft Agent Framework 3부 포스트는 빌딩 블록 시리즈의 루프를 닫습니다. 도구를 사용하고, 기억하고, 조율하는 진짜 AI 에이전트를 구축하고 싶은 .NET 개발자라면 이것이 바로 앞으로 나아가는 길입니다.

안정적인 1.0 릴리스는 프로덕션에서 이것을 기반으로 구축할 수 있음을 의미합니다. .NET에서 에이전트 개발에 뛰어들 기회를 기다리고 있었다면, 지금이 바로 그 시입니다.
