---
title: "A2A v1 Chegou: Comunicação Entre Agentes Cross-Platform no Microsoft Agent Framework para .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "O Protocolo A2A v1.0 foi lançado e os pacotes Microsoft Agent Framework para .NET estão atualizados — padrão de interoperabilidade estável para conectar e expor agentes de IA entre provedores."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[A2A v1 Chegou: Comunicação Entre Agentes Cross-Platform no Microsoft Agent Framework para .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — o Protocolo A2A acaba de atingir v1.0, e os pacotes A2A Agent (cliente) e A2A Hosting (servidor) para .NET foram atualizados.

## O que é Realmente A2A v1

A2A é um protocolo de interoperabilidade aberto para agentes de IA apoiado por um comitê diretor técnico com representantes da AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP e ServiceNow. O rótulo v1 significa que agora é um padrão estável e pronto para produção. Os pacotes SDK e Agent Framework que o implementam ainda estão em preview, mas o protocolo em si está bloqueado.

v1 melhora v0.3 com suporte multi-tenant, Agent Cards assinadas para identidade criptográfica, fluxos de segurança melhorados e uma arquitetura alinhada com a web.

## Conectar-se a um Agente A2A Remoto

Um agente A2A remoto é simplesmente um `AIAgent` no seu código — mesmo `RunAsync`, mesmo streaming, mesmo gerenciamento de sessões:

```csharp
// Descoberta via URI well-known
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Configuração direta
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// O streaming funciona da mesma forma
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Expor Seu Agente como Endpoint A2A

Qualquer `AIAgent` que você construiu — no Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic ou AWS Bedrock — pode ser exposto como endpoint A2A com duas linhas no ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

O cartão do agente é servido automaticamente em `/.well-known/agent-card.json`.

## O que Isso Significa na Prática

O protocolo estável v1 significa que você pode conectar seus agentes .NET com agentes construídos em Python, Java ou qualquer outra linguagem sem se preocupar com mudanças que quebrem compatibilidade. A identidade criptográfica nas Agent Cards assinadas também fornece uma base para verificação de confiança entre agentes.

Veja o [post completo](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) para o changelog completo e notas de migração do v0.3.
