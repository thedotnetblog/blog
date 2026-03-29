---
title: "Background Responses in Microsoft Agent Framework: No More Timeout Anxiety"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework now lets you offload long-running AI tasks with continuation tokens. Here's how background responses work and why they matter for your .NET agents."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

If you've built anything with reasoning models like o3 or GPT-5.2, you know the pain. Your agent starts thinking through a complex task, the client sits there waiting, and somewhere between "this is fine" and "did it crash?" your connection times out. All that work? Gone.

Microsoft Agent Framework just shipped [background responses](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — and honestly, this is one of those features that should've existed from day one.

## The problem with blocking calls

In a traditional request-response pattern, your client blocks until the agent finishes. That works fine for quick tasks. But when you're asking a reasoning model to do deep research, multi-step analysis, or generate a 20-page report? You're looking at minutes of wall-clock time. During that window:

- HTTP connections can time out
- Network blips kill the entire operation
- Your user stares at a spinner wondering if anything is happening

Background responses flip this on its head.

## How continuation tokens work

Instead of blocking, you kick off the agent task and get back a **continuation token**. Think of it like a claim ticket at a repair shop — you don't stand at the counter waiting, you come back when it's ready.

The flow is straightforward:

1. Send your request with `AllowBackgroundResponses = true`
2. If the agent supports background processing, you get a continuation token
3. Poll on your schedule until the token comes back `null` — that means the result is ready

Here's the .NET version:

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

// Poll until complete
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

If the agent completes immediately (simple tasks, models that don't need background processing), no continuation token is returned. Your code just works — no special handling needed.

## Streaming with resume: the real magic

Polling is fine for fire-and-forget scenarios, but what about when you want real-time progress? Background responses also support streaming with built-in resumption.

Each streamed update carries its own continuation token. If your connection drops mid-stream, you pick up exactly where you left off:

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
    break; // Simulate a network interruption
}

// Resume from exactly where we left off
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

The agent keeps processing server-side regardless of what's happening with your client. That's built-in fault tolerance without you writing retry logic or circuit breakers.

## When to actually use this

Not every agent call needs background responses. For quick completions, you're adding complexity for no reason. But here's where they shine:

- **Complex reasoning tasks** — multi-step analysis, deep research, anything that makes a reasoning model actually think
- **Long content generation** — detailed reports, multi-part documents, extensive analysis
- **Unreliable networks** — mobile clients, edge deployments, flaky corporate VPNs
- **Async UX patterns** — submit a task, go do something else, come back for results

For us .NET developers building enterprise apps, that last one is particularly interesting. Think about a Blazor app where a user requests a complex report — you fire off the agent task, show them a progress indicator, and let them keep working. No WebSocket gymnastics, no custom queue infrastructure, just a token and a poll loop.

## Wrapping up

Background responses are available now in both .NET and Python through Microsoft Agent Framework. If you're building agents that do anything more complex than simple Q&A, this is worth adding to your toolkit. The continuation token pattern keeps things simple while solving a very real production problem.

Check out the [full documentation](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) for the complete API reference and more examples.
