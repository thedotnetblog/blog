---
title: "A2A v1 ist da: Plattformübergreifende Agentenkommunikation im Microsoft Agent Framework für .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Das A2A-Protokoll v1.0 ist veröffentlicht und die Microsoft Agent Framework .NET-Pakete sind aktualisiert — stabiles Interoperabilitätsstandard zum Verbinden und Exponieren von KI-Agenten."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[A2A v1 ist da: Plattformübergreifende Agentenkommunikation im Microsoft Agent Framework für .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — das A2A-Protokoll hat gerade v1.0 erreicht, und sowohl das A2A Agent (Client)- als auch das A2A Hosting (Server)-Paket für .NET wurden aktualisiert.

## Was A2A v1 wirklich ist

A2A ist ein offenes Interoperabilitätsprotokoll für KI-Agenten, das von einem technischen Lenkungsausschuss mit Vertretern von AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP und ServiceNow unterstützt wird. Das v1-Label bedeutet, dass es nun ein stabiler, produktionsreifer Standard ist. Die SDK- und Agent-Framework-Pakete, die es implementieren, befinden sich noch in der Vorschau, aber das Protokoll selbst ist eingefroren.

v1 verbessert v0.3 mit Multi-Tenant-Unterstützung, signierten Agent Cards für kryptografische Identität, verbesserten Sicherheitsabläufen und einer webalignierten Architektur.

## Verbindung zu einem Remote-A2A-Agenten

Ein Remote-A2A-Agent ist in Ihrem Code einfach ein `AIAgent` — dasselbe `RunAsync`, dasselbe Streaming, dieselbe Sitzungsverwaltung:

```csharp
// Entdeckung über bekannte URI
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Direkte Konfiguration
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Streaming funktioniert genauso
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Ihren Agenten als A2A-Endpunkt exponieren

Jeder `AIAgent`, den Sie bereits gebaut haben — auf Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic oder AWS Bedrock — kann mit zwei Zeilen in ASP.NET Core als A2A-Endpunkt exponiert werden:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

Die Agent Card wird automatisch unter `/.well-known/agent-card.json` bereitgestellt.

## Was das in der Praxis bedeutet

Das stabile v1-Protokoll bedeutet, dass Sie Ihre .NET-Agenten mit Agenten verbinden können, die in Python, Java oder einer anderen Sprache gebaut wurden, ohne sich um Breaking Changes zu sorgen. Die kryptografische Identität in signierten Agent Cards liefert außerdem eine Grundlage für die Vertrauensverifizierung zwischen Agenten.

Den vollständigen [Beitrag](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) mit dem kompletten Änderungsprotokoll und den Migrationshinweisen von v0.3 finden Sie hier.
