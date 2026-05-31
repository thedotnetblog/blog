---
title: "Flujos de Trabajo Duraderos en Microsoft Agent Framework: De In-Memory a Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "El modelo de programación de flujos de trabajo de MAF ahora soporta ejecución duradera respaldada por Durable Task — aquí te mostramos cómo construir flujos de trabajo de agentes componibles que sobreviven a reinicios de procesos y escalan a través de Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Uno de los puntos débiles de los primeros flujos de trabajo de agentes de IA: son frágiles. Un flujo de trabajo de múltiples pasos de larga duración vinculado a un único proceso significa que el reinicio del proceso = estado perdido. Para demos simples está bien. Para cargas de trabajo en producción, no.

El modelo de programación de flujos de trabajo de Microsoft Agent Framework ahora soporta **ejecución duradera**, respaldada por el framework Durable Task, con hospedaje en Azure Functions. Aquí te explicamos cómo funciona el modelo de programación y por qué importa la historia de durabilidad.

## Los Bloques de Construcción Básicos

Los **Executors** son la unidad fundamental de trabajo. Cada uno tiene tipo — toma una entrada específica y produce una salida específica:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // buscar el pedido, devolverlo
        return new Order(Id: message.OrderId, ...);
    }
}
```

Los **Workflows** conectan ejecutores en grafos dirigidos usando un constructor fluido. El framework gestiona la ejecución, el flujo de datos entre pasos y la propagación de errores.

Puedes modelar:
- Cadenas secuenciales (paso A → paso B → paso C)
- Fan-out/fan-in paralelo (ejecutar agentes A, B, C en paralelo, agregar resultados)
- Ramificación condicional
- Aprobaciones de humano en el bucle (pausar flujo de trabajo, esperar señal externa)

## El Corredor In-Memory para Desarrollo Local

Empezar es rápido:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

El paquete principal incluye un corredor ligero en proceso. Sin dependencias externas, sin base de datos, sin recursos Azure. Funciona perfectamente para desarrollo local y pruebas unitarias.

## Agregar Durabilidad con Durable Task

Cuando un flujo de trabajo necesita sobrevivir a reinicios de proceso — porque es de larga duración, porque tiene pasos de humano en el bucle, porque se dispersa a través de muchas llamadas de agente en paralelo — el corredor in-memory no es suficiente.

La integración de Durable Task de MAF almacena el estado del flujo de trabajo en Azure Storage. Si el proceso se reinicia, el flujo de trabajo se reanuda desde donde lo dejó. El modelo de programación permanece igual; solo cambias el corredor.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Los mismos ejecutores, el mismo grafo de flujo de trabajo — respaldado por estado duradero.

## Hospedaje en Azure Functions

La tercera capa es el hospedaje en Azure Functions. Tu flujo de trabajo se convierte en una aplicación Function: activa el flujo de trabajo a través de un endpoint HTTP, y el runtime duradero gestiona el escalado, el estado y la fiabilidad.

Esto significa que un flujo de trabajo multi-agente con llamadas paralelas, ramas condicionales y aprobaciones humanas puede escalar a través de un entorno de Functions sin servidor sin gestión de estado personalizada.

## Por Qué Importa Esto

La combinación es significativa para sistemas de IA reales:

- **Llamadas de agente en paralelo** — dispersar a múltiples agentes especializados simultáneamente sin bloquear, agregar resultados cuando todos completen
- **Procesos de larga duración** — los flujos de trabajo que implican aprobación humana o eventos externos pueden pausar y reanudar durante horas o días
- **Escalado** — Azure Functions escala la ejecución horizontalmente; el framework Durable Task gestiona la coordinación del estado paralelo

Si estás construyendo flujos de trabajo MAF más allá de demos locales simples, este es el camino hacia la ejecución de grado producción.

Publicación original: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
