---
title: "A2A v1 Jest Tutaj: Komunikacja Agentów Cross-Platform w Microsoft Agent Framework dla .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Protokół A2A v1.0 został wydany, a pakiety Microsoft Agent Framework dla .NET zostały zaktualizowane — stabilny standard interoperacyjności do łączenia i udostępniania agentów AI."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[A2A v1 Jest Tutaj: Komunikacja Agentów Cross-Platform w Microsoft Agent Framework dla .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — Protokół A2A właśnie osiągnął wersję 1.0, a pakiety A2A Agent (klient) i A2A Hosting (serwer) dla .NET zostały zaktualizowane.

## Czym naprawdę jest A2A v1

A2A to otwarty protokół interoperacyjności dla agentów AI, wspierany przez komitet sterujący z przedstawicielami AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP i ServiceNow. Etykieta v1 oznacza, że jest to teraz stabilny standard gotowy do produkcji. Pakiety SDK i Agent Framework, które go implementują, nadal są w wersji zapoznawczej, ale sam protokół jest zamrożony.

v1 ulepsza v0.3 o obsługę wielu dzierżawców, podpisane Agent Cards dla tożsamości kryptograficznej, ulepszone przepływy bezpieczeństwa i architekturę zgodną z webem.

## Łączenie z zdalnym agentem A2A

Zdalny agent A2A to po prostu `AIAgent` w Twoim kodzie — ten sam `RunAsync`, to samo strumieniowanie, ta sama obsługa sesji:

```csharp
// Odkrywanie przez well-known URI
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Bezpośrednia konfiguracja
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Strumieniowanie działa tak samo
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Udostępnianie agenta jako endpoint A2A

Każdy `AIAgent`, który zbudowałeś — na Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic lub AWS Bedrock — może być udostępniony jako endpoint A2A za pomocą dwóch linii w ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

Karta agenta jest automatycznie udostępniana pod `/.well-known/agent-card.json`.

## Co to oznacza w praktyce

Stabilny protokół v1 oznacza, że możesz połączyć swoich agentów .NET z agentami zbudowanymi w Pythonie, Javie lub innym języku bez obaw o zmiany powodujące błędy. Tożsamość kryptograficzna w podpisanych Agent Cards zapewnia również podstawę do weryfikacji zaufania między agentami.

Zobacz [pełny post](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) dla kompletnego dziennika zmian i notatek migracyjnych z v0.3.
