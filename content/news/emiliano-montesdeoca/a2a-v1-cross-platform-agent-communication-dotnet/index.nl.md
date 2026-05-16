---
title: "A2A v1 Is Er: Cross-Platform Agentcommunicatie in Microsoft Agent Framework voor .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Het A2A Protocol v1.0 is uitgebracht en de Microsoft Agent Framework .NET-pakketten zijn bijgewerkt — stabiele interoperabiliteitsstandaard voor het verbinden en blootstellen van AI-agenten."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[A2A v1 Is Er: Cross-Platform Agentcommunicatie in Microsoft Agent Framework voor .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — het A2A Protocol heeft v1.0 bereikt, en zowel het A2A Agent (client)- als het A2A Hosting (server)-pakket voor .NET zijn bijgewerkt.

## Wat A2A v1 werkelijk is

A2A is een open interoperabiliteitsprotocol voor AI-agenten dat wordt ondersteund door een technisch stuurcomité met vertegenwoordigers van AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP en ServiceNow. Het v1-label betekent dat het nu een stabiele, productie-klare standaard is. De SDK- en Agent Framework-pakketten die het implementeren zijn nog in preview, maar het protocol zelf is vergrendeld.

v1 verbetert v0.3 met multi-tenant ondersteuning, ondertekende Agent Cards voor cryptografische identiteit, verbeterde beveiligingsstromen en een web-gealigneerde architectuur.

## Verbinding maken met een remote A2A-agent

Een remote A2A-agent is gewoon een `AIAgent` in uw code — dezelfde `RunAsync`, hetzelfde streaming, dezelfde sessiebeheer:

```csharp
// Ontdekking via well-known URI
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Directe configuratie
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Streaming werkt hetzelfde
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Uw agent blootstellen als A2A-endpoint

Elke `AIAgent` die u heeft gebouwd — op Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic of AWS Bedrock — kan worden blootgesteld als A2A-endpoint met twee regels in ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

De agentkaart wordt automatisch aangeboden op `/.well-known/agent-card.json`.

## Wat dit in de praktijk betekent

Het stabiele v1-protocol betekent dat u uw .NET-agenten kunt verbinden met agenten gebouwd in Python, Java of een andere taal zonder u zorgen te maken over breaking changes. De cryptografische identiteit in ondertekende Agent Cards biedt ook een basis voor vertrouwensverificatie tussen agenten.

Zie het [volledige bericht](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) voor het volledige changelog en migratienotities van v0.3.
