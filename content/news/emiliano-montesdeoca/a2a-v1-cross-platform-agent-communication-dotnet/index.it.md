---
title: "A2A v1 È Arrivato: Comunicazione tra Agenti Cross-Platform in Microsoft Agent Framework per .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Il Protocollo A2A v1.0 è stato rilasciato e i pacchetti Microsoft Agent Framework per .NET sono aggiornati — standard di interoperabilità stabile per connettere ed esporre agenti IA tra provider."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[A2A v1 È Arrivato: Comunicazione tra Agenti Cross-Platform in Microsoft Agent Framework per .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — il Protocollo A2A ha appena raggiunto la v1.0, e sia il pacchetto A2A Agent (client) che A2A Hosting (server) per .NET sono stati aggiornati.

## Cosa è Realmente A2A v1

A2A è un protocollo di interoperabilità aperto per agenti IA supportato da un comitato direttivo tecnico con rappresentanti di AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP e ServiceNow. L'etichetta v1 significa che ora è uno standard stabile e pronto per la produzione. I pacchetti SDK e Agent Framework che lo implementano sono ancora in preview, ma il protocollo stesso è bloccato.

v1 migliora v0.3 con supporto multi-tenant, Agent Cards firmate per identità crittografica, flussi di sicurezza migliorati e un'architettura allineata al web.

## Connettersi a un Agente A2A Remoto

Un agente A2A remoto è semplicemente un `AIAgent` nel tuo codice — stesso `RunAsync`, stesso streaming, stessa gestione delle sessioni:

```csharp
// Scoperta tramite URI well-known
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Configurazione diretta
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Lo streaming funziona allo stesso modo
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Esporre il Tuo Agente come Endpoint A2A

Qualsiasi `AIAgent` che hai costruito — su Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic o AWS Bedrock — può essere esposto come endpoint A2A con due righe in ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

La card dell'agente viene servita automaticamente su `/.well-known/agent-card.json`.

## Cosa Significa Questo in Pratica

Il protocollo stabile v1 significa che puoi collegare i tuoi agenti .NET con agenti costruiti in Python, Java o qualsiasi altro linguaggio senza preoccuparti di breaking changes. L'identità crittografica nelle Agent Cards firmate fornisce anche una base per la verifica della fiducia tra agenti.

Consulta il [post completo](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) per il changelog completo e le note di migrazione da v0.3.
