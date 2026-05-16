---
title: "A2A v1 Is Here: Cross-Platform Agent Communication in Microsoft Agent Framework for .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "The A2A Protocol v1.0 has shipped and the Microsoft Agent Framework .NET packages are updated to match — stable interoperability for connecting and exposing AI agents across providers."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

[A2A v1 Is Here: Cross-Platform Agent Communication in Microsoft Agent Framework for .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — the A2A Protocol just hit v1.0, and both the A2A Agent (client) and A2A Hosting (server) packages for .NET are updated to match.

## What A2A v1 actually is

A2A is an open interoperability protocol for AI agents backed by a technical steering committee with representatives from AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, and ServiceNow. The v1 label means it is now a stable, production-ready standard — not a moving target. The SDK and Agent Framework packages that implement it are still in preview, but the protocol itself is locked.

v1 improves on v0.3 with multi-tenancy support, signed Agent Cards for cryptographic identity, improved security flows, and a web-aligned architecture overall.

## Connecting to a remote A2A agent

A remote A2A agent is just an `AIAgent` in your code — same `RunAsync`, same streaming, same session handling. Two ways to get one:

```csharp
using A2A;
using Microsoft.Agents.AI;

// Discovery via well-known URI
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Direct configuration
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Streaming works the same way
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

The `A2ACardResolver` approach does automatic discovery via the `/.well-known/agent-card.json` endpoint. The direct `A2AClient` path gives you explicit control over the name and description surfaced to your orchestration layer.

## Exposing your agent as an A2A endpoint

Any `AIAgent` you've already built — on Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, or AWS Bedrock — can be exposed as an A2A endpoint with two lines in ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
// agent card auto-discovered at /.well-known/agent-card.json
```

The agent card is served automatically at the well-known URI, so any A2A-compliant client can discover and call your agent without extra configuration.

## What this means in practice

The stable v1 protocol means you can wire your .NET agents to agents built in Python, Java, or any other language without worrying about breaking changes. The cryptographic identity in signed Agent Cards also gives you a foundation for trust verification between agents — useful once you're operating more than a handful of them.

See the [full post](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) for the complete changelog and migration notes from v0.3.
