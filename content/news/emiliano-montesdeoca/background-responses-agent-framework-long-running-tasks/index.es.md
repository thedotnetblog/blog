---
title: "Respuestas en segundo plano en Microsoft Agent Framework: Se acabó la ansiedad por timeouts"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework ahora te permite descargar tareas de IA de larga duración con tokens de continuación. Así es cómo funcionan las respuestas en segundo plano y por qué importan para tus agentes .NET."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Si has construido algo con modelos de razonamiento como o3 o GPT-5.2, conoces el dolor. Tu agente empieza a pensar en una tarea compleja, el cliente se queda esperando, y en algún punto entre "todo está bien" y "¿se habrá colgado?" tu conexión se corta por timeout. ¿Todo ese trabajo? Perdido.

Microsoft Agent Framework acaba de lanzar [respuestas en segundo plano](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — y honestamente, esta es una de esas funcionalidades que deberían haber existido desde el primer día.

## El problema con las llamadas bloqueantes

En un patrón tradicional de petición-respuesta, tu cliente se bloquea hasta que el agente termine. Eso funciona bien para tareas rápidas. Pero cuando le pides a un modelo de razonamiento que haga investigación profunda, análisis de múltiples pasos, o genere un informe de 20 páginas? Estás mirando minutos de tiempo real. Durante esa ventana:

- Las conexiones HTTP pueden expirar
- Los cortes de red matan toda la operación
- Tu usuario se queda mirando un spinner preguntándose si algo está pasando

Las respuestas en segundo plano le dan la vuelta a esto.

## Cómo funcionan los tokens de continuación

En lugar de bloquear, lanzas la tarea del agente y recibes un **token de continuación**. Piénsalo como un ticket de recogida en un taller de reparaciones — no te quedas parado en el mostrador esperando, vuelves cuando está listo.

El flujo es directo:

1. Envía tu petición con `AllowBackgroundResponses = true`
2. Si el agente soporta procesamiento en segundo plano, recibes un token de continuación
3. Consulta a tu ritmo hasta que el token vuelva `null` — eso significa que el resultado está listo

Aquí está la versión .NET:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Consultar hasta completar
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Si el agente completa inmediatamente (tareas simples, modelos que no necesitan procesamiento en segundo plano), no se devuelve ningún token de continuación. Tu código simplemente funciona — sin manejo especial necesario.

## Streaming con reanudación: la verdadera magia

El polling está bien para escenarios de disparar y olvidar, pero ¿qué pasa cuando quieres progreso en tiempo real? Las respuestas en segundo plano también soportan streaming con reanudación incorporada.

Cada actualización del stream lleva su propio token de continuación. Si tu conexión se cae a mitad del stream, retomas exactamente donde lo dejaste:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Simular una interrupción de red
}

// Reanudar desde exactamente donde lo dejamos
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

El agente sigue procesando en el servidor independientemente de lo que pase con tu cliente. Eso es tolerancia a fallos incorporada sin que tú escribas lógica de reintentos o circuit breakers.

## Cuándo usar esto realmente

No toda llamada al agente necesita respuestas en segundo plano. Para completaciones rápidas, estás añadiendo complejidad sin razón. Pero aquí es donde brillan:

- **Tareas de razonamiento complejo** — análisis de múltiples pasos, investigación profunda, cualquier cosa que haga a un modelo de razonamiento realmente pensar
- **Generación de contenido largo** — informes detallados, documentos de múltiples partes, análisis extenso
- **Redes poco fiables** — clientes móviles, despliegues en el edge, VPNs corporativas inestables
- **Patrones UX asíncronos** — envía una tarea, ve a hacer otra cosa, vuelve por los resultados

Para nosotros los desarrolladores .NET construyendo apps empresariales, ese último es particularmente interesante. Piensa en una app Blazor donde un usuario solicita un informe complejo — lanzas la tarea del agente, les muestras un indicador de progreso, y les dejas seguir trabajando. Sin gimnasia con WebSockets, sin infraestructura de colas personalizada, solo un token y un bucle de polling.

## Para cerrar

Las respuestas en segundo plano están disponibles ahora tanto en .NET como en Python a través de Microsoft Agent Framework. Si estás construyendo agentes que hacen algo más complejo que simple Q&A, vale la pena añadir esto a tu toolkit. El patrón de token de continuación mantiene las cosas simples mientras resuelve un problema de producción muy real.

Revisa la [documentación completa](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) para la referencia completa de la API y más ejemplos.
