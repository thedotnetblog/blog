---
title: "¿Dónde Recuerda las Cosas tu Agente? Guía Práctica sobre el Almacenamiento del Historial de Chat"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "¿Gestionado por el servicio o por el cliente? ¿Lineal o con bifurcaciones? La decisión arquitectónica que define lo que tu agente IA puede hacer realmente, con ejemplos de código en C# y Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Cuando construyes un agente IA, dedicas la mayor parte de tu energía al modelo, las herramientas y los prompts. La pregunta de *dónde vive el historial de conversación* parece un detalle de implementación — pero es una de las decisiones arquitectónicas más importantes que tomarás.

Determina si los usuarios pueden bifurcar conversaciones, deshacer respuestas, reanudar sesiones después de un reinicio, y si tus datos salen alguna vez de tu infraestructura. El [equipo de Agent Framework publicó un análisis en profundidad](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) y vale la pena entender el panorama completo.

## Dos patrones fundamentales

**Gestionado por el servicio**: el servicio de IA almacena el estado de la conversación. Tu app mantiene una referencia (un ID de hilo, un ID de respuesta) y el servicio incluye automáticamente el historial relevante en cada solicitud. Más simple de configurar. Menos control.

**Gestionado por el cliente**: tu app mantiene el historial completo y envía mensajes relevantes con cada solicitud. El servicio no tiene estado. Controlas todo.

## Gestionado por servicio: lineal vs bifurcación

**Lineal (hilo único)**: los mensajes forman una secuencia ordenada. Puedes añadir pero no bifurcar. Ideal para chatbots y flujos simples. Malo para "inténtalo de nuevo" o exploración paralela.

**Con capacidad de bifurcación**: cada respuesta tiene un ID único, y las nuevas solicitudes pueden referenciar cualquier respuesta anterior como punto de continuación. Esto es lo que soporta la API de Responses (Microsoft Foundry, Azure OpenAI, OpenAI). Permite bifurcar conversaciones y construir flujos de "deshacer".

## Cómo Agent Framework abstrae esto

```csharp
// C# — funciona igual independientemente del proveedor
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Me llamo Alice.", session);
var second = await agent.RunAsync("¿Cuál es mi nombre?", session);
```

```python
# Python
session = agent.create_session()
first = await agent.run("Me llamo Alice.", session=session)
second = await agent.run("¿Cuál es mi nombre?", session=session)
```

La sesión maneja las diferencias subyacentes. Este desacoplamiento es valioso para experimentar con diferentes proveedores sin reescribir tu código.

## Referencia rápida de proveedores

| Proveedor | Almacenamiento | Modelo | Compactación |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Cliente | N/A | Tú |
| Foundry Agent Service | Servicio | Lineal | Servicio |
| Responses API (por defecto) | Servicio | Bifurcación | Servicio |
| Responses API (`store=false`) | Cliente | N/A | Tú |
| Anthropic Claude, Ollama | Cliente | N/A | Tú |

## Cómo elegir

1. **¿Necesitas bifurcación o "deshacer"?** → Responses API gestionado por servicio
2. **¿Necesitas soberanía total de datos?** → Gestionado por cliente con proveedor respaldado por base de datos
3. **¿Es un chatbot sencillo?** → Lineal gestionado por servicio está bien
4. **¿Necesitas portabilidad entre proveedores?** → Gestionado por cliente da portabilidad

Lee el [post completo](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) para el árbol de decisión completo y los detalles de la API de Conversations.
