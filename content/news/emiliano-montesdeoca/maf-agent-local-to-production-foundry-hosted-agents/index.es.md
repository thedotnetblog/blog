---
title: "Tu Agente MAF Local Acaba de Tener un Hogar en Producción"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents le da a tu agente de Microsoft Agent Framework identidad, escalado, persistencia de sesión y observabilidad sin configuración adicional. Así es como se ve en la práctica."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Hacer que un agente funcione localmente es la parte divertida. La parte complicada es todo lo que viene después: desplegarlo sin perder la cordura, gestionar sesiones, configurar identidad, conectar la observabilidad. Normalmente eso significa mucha infraestructura personalizada de pegamento.

Foundry Hosted Agents acaba de eliminar la mayor parte de ese pegamento para los usuarios de Microsoft Agent Framework (MAF).

## Lo Que Foundry Hosted Agents Realmente Hace

Cuando despliegas un agente MAF en Foundry Hosted Agents, la plataforma gestiona una lista sorprendentemente larga de cosas que de otro modo tendrías que construir tú mismo:

- **Escalar a cero** — tu agente no cuesta nada cuando está inactivo y vuelve a arrancar automáticamente
- **Sandboxes aislados por VM por sesión** — cada sesión de usuario obtiene su propio sandbox con persistencia del sistema de archivos que sobrevive a eventos de reducción de escala
- **Entra ID integrado** — cada agente obtiene su propia identidad para llamar a modelos de Foundry, Toolbox y servicios Azure sin secretos dentro de la imagen
- **Despliegues versionados** — cada despliegue es una instantánea inmutable, con soporte de despliegue blue/green y canary
- **Observabilidad sin configuración** — `APPLICATIONINSIGHTS_CONNECTION_STRING` se inyecta en tiempo de ejecución para que las trazas OpenTelemetry de MAF fluyan automáticamente hacia App Insights

Ese último es genuinamente agradable. Sin cableado extra, sin configuración adicional. Las trazas simplemente aparecen.

## La Diferencia en el Código Es Mínima

Esto es lo que más aprecio de esta integración. No reescribes tu agente. Solo lo envuelves:

**En .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**En Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Eso es todo. La misma lógica que probaste localmente es lo que se ejecuta en producción. La plataforma la envuelve en la infraestructura de gestión de sesiones, identidad y escalado.

## Dos Protocolos, Un Agente

Los Hosted Agents soportan dos estilos de endpoints:

- **Responses** (`/responses`) — compatible con OpenAI, gestiona el historial de conversación y streaming. Buen valor predeterminado para agentes con forma de chat.
- **Invocations** (`/invocations`) — tú defines el esquema de petición/respuesta. Bueno para flujos de trabajo no conversacionales.

Si estás construyendo algo que parece una conversación, empieza con Responses. Si estás construyendo un agente con forma de API que toma entrada estructurada y devuelve salida estructurada, Invocations te da la flexibilidad.

## El Flujo de Despliegue con `azd`

Cuando ejecutas `azd up` con un agente MAF:

1. Opcionalmente crea un proyecto Foundry y despliega un modelo
2. Empaqueta tu código y empuja una imagen a Azure Container Registry
3. Aprovisiona cómputo desde la imagen ACR
4. Asigna un Entra ID dedicado al agente
5. Expone un endpoint estable (`https://{project_endpoint}/agents/{agent_name}`)
6. Gestiona todo lo demás desde ese punto en adelante

Las sesiones persisten hasta 30 días. El cómputo inactivo se desaprovisiona después de 15 minutos y se restaura transparentemente en la siguiente solicitud. Desde la perspectiva del agente, nada cambió.

## Conclusión

La distancia entre "funcionando localmente" y "ejecutándose en producción" ha sido históricamente larga y dolorosa para los agentes de IA. Foundry Hosted Agents + MAF cierra esa brecha significativamente. Si ya tienes un agente local construido con Agent Framework, vale la pena probarlo hoy.

El equipo dice que GA llega pronto — actualmente está en preview. Consulta los [docs de integración de MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) y los [ejemplos de .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) para empezar.

Artículo original: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
