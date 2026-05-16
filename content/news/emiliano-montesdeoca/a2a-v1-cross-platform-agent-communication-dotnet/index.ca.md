---
title: "A2A v1 Ha Arribat: Comunicació entre Agents Cross-Platform a Microsoft Agent Framework per a .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "El Protocol A2A v1.0 ha arribat i els paquets de Microsoft Agent Framework per a .NET estan actualitzats — interoperabilitat estable per connectar i exposar agents d'IA entre proveïdors."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[A2A v1 Ha Arribat: Comunicació entre Agents Cross-Platform a Microsoft Agent Framework per a .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — el Protocol A2A acaba d'assolir la v1.0, i tant el paquet A2A Agent (client) com A2A Hosting (servidor) per a .NET estan actualitzats.

## Què és A2A v1 realment

A2A és un protocol d'interoperabilitat obert per a agents d'IA recolzat per un comitè tècnic director amb representants d'AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP i ServiceNow. L'etiqueta v1 significa que ara és un estàndard estable i llest per a producció. Els paquets SDK i Agent Framework que l'implementen encara estan en preview, però el protocol en si és estable.

La v1 millora la v0.3 amb suport multi-tenant, Agent Cards signades per identitat criptogràfica, fluxos de seguretat millorats i una arquitectura alineada amb el web.

## Connectar-se a un agent A2A remot

Un agent A2A remot és simplement un `AIAgent` al teu codi — el mateix `RunAsync`, el mateix streaming, el mateix maneig de sessions:

```csharp
// Descoberta via URI well-known
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Configuració directa
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// El streaming funciona igual
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Exposar el teu agent com a endpoint A2A

Qualsevol `AIAgent` que hagis construït — a Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic o AWS Bedrock — es pot exposar com a endpoint A2A amb dues línies a ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

La tarjeta de l'agent es serveix automàticament a `/.well-known/agent-card.json`.

## Què significa això a la pràctica

El protocol estable v1 permet connectar agents .NET amb agents construïts en Python, Java o qualsevol altre llenguatge sense preocupar-se per canvis que trenquin compatibilitat. La identitat criptogràfica a les Agent Cards signades proporciona una base per a la verificació de confiança entre agents.

Consulta el [post complet](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) per al registre de canvis complet i les notes de migració des de v0.3.
