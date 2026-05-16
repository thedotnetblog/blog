---
title: "A2A v1 Est Là : Communication Inter-Agents Cross-Platform dans Microsoft Agent Framework pour .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Le Protocole A2A v1.0 est sorti et les paquets Microsoft Agent Framework pour .NET sont mis à jour — interopérabilité stable pour connecter et exposer des agents IA entre fournisseurs."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[A2A v1 Est Là : Communication Inter-Agents Cross-Platform dans Microsoft Agent Framework pour .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — le Protocole A2A vient d'atteindre v1.0, et les paquets A2A Agent (client) et A2A Hosting (serveur) pour .NET ont été mis à jour.

## Ce qu'est réellement A2A v1

A2A est un protocole d'interopérabilité ouvert pour les agents IA soutenu par un comité de direction technique avec des représentants d'AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow. L'étiquette v1 signifie que c'est maintenant un standard stable et prêt pour la production. Les paquets SDK et Agent Framework qui l'implémentent sont toujours en preview, mais le protocole lui-même est figé.

v1 améliore v0.3 avec le support multi-tenant, des Agent Cards signées pour l'identité cryptographique, des flux de sécurité améliorés et une architecture alignée sur le web.

## Se connecter à un agent A2A distant

Un agent A2A distant est simplement un `AIAgent` dans votre code — même `RunAsync`, même streaming, même gestion de sessions :

```csharp
// Découverte via URI well-known
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Configuration directe
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Le streaming fonctionne de la même façon
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Exposer votre agent comme endpoint A2A

N'importe quel `AIAgent` que vous avez construit — sur Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic ou AWS Bedrock — peut être exposé comme endpoint A2A avec deux lignes dans ASP.NET Core :

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

La carte de l'agent est servie automatiquement à `/.well-known/agent-card.json`.

## Ce que cela signifie en pratique

Le protocole stable v1 signifie que vous pouvez connecter vos agents .NET à des agents construits en Python, Java ou tout autre langage sans vous soucier des changements cassants. L'identité cryptographique dans les Agent Cards signées vous fournit également une base pour la vérification de confiance entre agents.

Consultez le [post complet](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) pour le journal des modifications complet et les notes de migration depuis v0.3.
