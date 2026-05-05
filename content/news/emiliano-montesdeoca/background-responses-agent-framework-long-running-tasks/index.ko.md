---
title: "Microsoft Agent Framework의 백그라운드 응답: 더 이상 타임아웃 걱정 없이"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework가 이제 연속 토큰으로 장시간 실행 AI 작업을 오프로드할 수 있습니다. 백그라운드 응답의 작동 방식과 .NET 에이전트에 중요한 이유를 알아보세요."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

o3나 GPT-5.2 같은 추론 모델로 무언가를 만들어 본 적이 있다면, 그 고통을 알 것입니다. 에이전트가 복잡한 작업을 생각하기 시작하고, 클라이언트는 기다리고, "괜찮아"와 "크래시한 건가?" 사이 어딘가에서 연결이 타임아웃됩니다. 그 모든 작업은? 사라집니다.

Microsoft Agent Framework가 [백그라운드 응답](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/)을 출시했습니다 — 솔직히, 이건 처음부터 있었어야 할 기능 중 하나입니다.

## 블로킹 호출의 문제

전통적인 요청-응답 패턴에서는 에이전트가 끝날 때까지 클라이언트가 블로킹됩니다. 빠른 작업에는 잘 작동합니다. 하지만 추론 모델에 깊은 연구, 다단계 분석, 20페이지 보고서 생성을 요청하면? 실제 시간으로 몇 분이 걸립니다. 그 시간 동안:

- HTTP 연결이 타임아웃될 수 있음
- 네트워크 끊김이 전체 작업을 죽임
- 사용자는 스피너를 보며 무슨 일이 일어나고 있는지 궁금해 함

백그라운드 응답은 이것을 뒤집습니다.

## 연속 토큰의 작동 방식

블로킹 대신, 에이전트 작업을 시작하고 **연속 토큰**을 받습니다. 수리점의 픽업 티켓처럼 생각하세요 — 카운터에서 서서 기다릴 필요 없이, 준비되면 돌아오면 됩니다.

흐름은 간단합니다:

1. `AllowBackgroundResponses = true`로 요청 전송
2. 에이전트가 백그라운드 처리를 지원하면 연속 토큰을 받음
3. 토큰이 `null`을 반환할 때까지 폴링 — 결과가 준비되었다는 의미

.NET 버전은 다음과 같습니다:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// 완료까지 폴링
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

에이전트가 즉시 완료하면(간단한 작업, 백그라운드 처리가 필요 없는 모델), 연속 토큰이 반환되지 않습니다. 코드는 그냥 작동합니다 — 특별한 처리가 필요 없습니다.

## 재개가 가능한 스트리밍: 진짜 마법

폴링은 fire-and-forget 시나리오에 괜찮지만, 실시간 진행 상황을 원한다면? 백그라운드 응답은 내장 재개 기능이 있는 스트리밍도 지원합니다.

각 스트리밍 업데이트는 자체 연속 토큰을 가집니다. 스트리밍 중에 연결이 끊기면, 중단된 정확한 지점에서 재개합니다:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // 네트워크 중단 시뮬레이션
}

// 중단된 정확한 지점에서 재개
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

클라이언트에 무슨 일이 일어나든 에이전트는 서버 측에서 계속 처리합니다. 재시도 로직이나 서킷 브레이커를 작성하지 않고도 내장된 장애 허용입니다.

## 언제 실제로 사용해야 하나

모든 에이전트 호출에 백그라운드 응답이 필요한 것은 아닙니다. 빠른 완료에는 이유 없이 복잡성을 추가하는 것입니다. 하지만 다음에서 빛을 발합니다:

- **복잡한 추론 작업** — 다단계 분석, 깊은 연구, 추론 모델을 진지하게 생각하게 만드는 모든 것
- **긴 콘텐츠 생성** — 상세 보고서, 다중 파트 문서, 광범위한 분석
- **불안정한 네트워크** — 모바일 클라이언트, 엣지 배포, 불안정한 기업 VPN
- **비동기 UX 패턴** — 작업을 제출하고, 다른 일을 하고, 결과를 가지러 돌아옴

엔터프라이즈 앱을 구축하는 .NET 개발자에게 마지막 포인트가 특히 흥미롭습니다. 사용자가 복잡한 보고서를 요청하는 Blazor 앱을 생각해 보세요 — 에이전트 작업을 시작하고, 프로그레스 인디케이터를 보여주고, 계속 작업하게 합니다. WebSocket 곡예 없이, 커스텀 큐 인프라 없이, 토큰과 폴링 루프만 있으면 됩니다.

## 마무리

백그라운드 응답은 Microsoft Agent Framework를 통해 .NET과 Python 모두에서 지금 사용할 수 있습니다. 단순한 Q&A 이상을 하는 에이전트를 구축하고 있다면, 툴킷에 추가할 가치가 있습니다. 연속 토큰 패턴은 매우 현실적인 프로덕션 문제를 해결하면서 것을 심플하게 유지합니다.

전체 API 참조와 더 많은 예제는 [전체 문서](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/)를 확인하세요.
