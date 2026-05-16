---
title: "A2A v1 Ha Llegado: Comunicación Entre Agentes Cross-Platform en Microsoft Agent Framework para .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "El Protocolo A2A v1.0 ha sido lanzado y los paquetes de Microsoft Agent Framework para .NET están actualizados — interoperabilidad estable para conectar y exponer agentes de IA entre proveedores."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[A2A v1 Ha Llegado: Comunicación Entre Agentes Cross-Platform en Microsoft Agent Framework para .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — el Protocolo A2A acaba de alcanzar v1.0, y tanto el paquete A2A Agent (cliente) como A2A Hosting (servidor) para .NET han sido actualizados.

## Qué es A2A v1 realmente

A2A es un protocolo de interoperabilidad abierto para agentes de IA respaldado por un comité directivo técnico con representantes de AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP y ServiceNow. La etiqueta v1 significa que ahora es un estándar estable y listo para producción. Los paquetes SDK y Agent Framework que lo implementan aún están en preview, pero el protocolo en sí está bloqueado.

v1 mejora v0.3 con soporte multi-tenant, Agent Cards firmadas para identidad criptográfica, flujos de seguridad mejorados y una arquitectura alineada con la web.

## Conectarse a un agente A2A remoto

Un agente A2A remoto es simplemente un `AIAgent` en tu código — el mismo `RunAsync`, el mismo streaming, el mismo manejo de sesiones:

```csharp
// Descubrimiento via URI conocida
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Configuración directa
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// El streaming funciona igual
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

El enfoque `A2ACardResolver` hace el descubrimiento automático via el endpoint `/.well-known/agent-card.json`. El camino directo con `A2AClient` te da control explícito sobre el nombre y descripción.

## Exponer tu agente como endpoint A2A

Cualquier `AIAgent` que hayas construido — en Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic o AWS Bedrock — puede exponerse como endpoint A2A con dos líneas en ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

La tarjeta del agente se sirve automáticamente en `/.well-known/agent-card.json`.

## Lo que esto significa en la práctica

El protocolo estable v1 significa que puedes conectar tus agentes .NET con agentes construidos en Python, Java o cualquier otro lenguaje sin preocuparte por cambios que rompan compatibilidad. La identidad criptográfica en las Agent Cards firmadas también te da una base para la verificación de confianza entre agentes.

Consulta el [post completo](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) para el registro de cambios completo y las notas de migración desde v0.3.
