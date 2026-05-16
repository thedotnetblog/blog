---
title: "Crear una app de conferencias con IA usando la pila componible de .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft creó ConferencePulse — una app Blazor para conferencias en vivo — combinando Microsoft.Extensions.AI, DataIngestion, VectorData, MCP y Agent Framework. Así encajan las piezas."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[Crear una app de conferencias con IA usando la pila componible de .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft creó ConferencePulse, una app Blazor Server para sesiones de conferencias en vivo, combinando cinco bibliotecas de extensión de .NET. La usaron en el MVP Summit.

## Qué hace ConferencePulse

ConferencePulse se ejecuta durante las sesiones en vivo y proporciona: encuestas generadas por IA a partir del contenido de la sesión, preguntas y respuestas del público con un pipeline RAG que extrae de una base de conocimiento en vivo, insights generados automáticamente y resúmenes de sesiones producidos por múltiples agentes de IA concurrentes. La pila es .NET 10, Blazor Server, Aspire, dividida en cinco proyectos: Web, Core, Ingestion, Agents, Mcp y AppHost.

## Microsoft.Extensions.AI: una abstracción para todo

`IChatClient` es la abstracción unificada — se configura una vez y la misma interfaz funciona para Azure OpenAI, OpenAI, Anthropic o cualquier otro proveedor. Seis líneas para obtener un cliente totalmente configurado con invocación de funciones, rastreo OpenTelemetry y middleware de registro:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

El mismo `IChatClient` se reutiliza más adelante para el paso de enriquecimiento de la ingesta de datos — no se necesita un cliente separado para eso.

## Pipeline de DataIngestion

El contenido de la sesión fluye a través de un pipeline: `MarkdownReader` → `HeaderChunker` (500 tokens, 50 tokens de solapamiento) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Los enriquecedores usan el mismo `IChatClient` para generar resúmenes y extraer palabras clave antes de la indexación. Las preguntas del público, los pares de preguntas y respuestas y los resultados de las encuestas se ingieren en tiempo real a medida que avanza la sesión — la base de conocimiento crece durante la charla.

## VectorData: búsqueda independiente del proveedor

`VectorStoreCollection.SearchAsync()` funciona igual tanto si el almacén subyacente es Qdrant como Azure AI Search. La búsqueda híbrida (vector + texto completo) es compatible. El pipeline RAG para preguntas y respuestas del público consulta esta colección y obtiene fragmentos relevantes para pasar como contexto al cliente de chat.

## MCP: contenido de la sesión como herramientas

El contenido de la sesión se expone a través de MCP para que cualquier cliente compatible con MCP pueda acceder a él. Tanto el servidor como el cliente están implementados — el servidor expone el conocimiento de la sesión como herramientas MCP, y el cliente permite llamar a esas herramientas desde dentro del pipeline del agente.

## Agent Framework: resumen multi-agente en paralelo

El resumen de la sesión es generado por tres agentes que se ejecutan de forma concurrente — `PollSummaryAgent`, `QuestionSummaryAgent` e `InsightSummaryAgent` — y luego se fusionan. Esto utiliza el patrón de chat en grupo o ejecución paralela de Microsoft Agent Framework. Cada agente maneja una preocupación; el orquestador fusiona las salidas.

## El principio de diseño

El post hace un punto que vale la pena recordar: usa la herramienta más simple que se adapte. Llamadas directas a `IChatClient` para tareas de generación simples. Llamada de herramienta/función para la extracción de datos estructurados. Agentes completos solo cuando necesitas razonamiento autónomo de múltiples pasos. La superposición de bibliotecas lo enforza — puedes usar `Microsoft.Extensions.AI` sin incluir el Agent Framework completo.

Consulta el [post completo](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) para la estructura completa del proyecto y los enlaces al código fuente.
