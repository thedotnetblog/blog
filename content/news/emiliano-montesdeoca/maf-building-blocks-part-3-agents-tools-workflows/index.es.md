---
title: "Microsoft Agent Framework Parte 3: De las Herramientas a los Workflows — Las Piezas Encajan"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "La tercera parte de la serie de bloques de construcción de .NET AI cubre el Microsoft Agent Framework — desde agentes simples con herramientas hasta workflows multiagente con memoria. Esto es lo que realmente importa."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Si has seguido la serie Building Blocks for AI en .NET, sabes que la Parte 1 nos dio `IChatClient` (la interfaz universal de modelos) y la Parte 2 nos dio `Microsoft.Extensions.VectorData` (búsqueda semántica y RAG). Ambas son fundamentales y útiles por sí solas. Pero aquí es donde todo empieza a conectarse.

La Parte 3 trata del [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — y sinceramente, es la pieza que estaba esperando ver en .NET. La versión 1.0 se publicó en abril. La API es estable. Es hora de construir agentes de verdad.

## Qué es un Agente (vs. un Chatbot)

Antes de entrar en el código, dejemos esto claro. Un chatbot recibe input, llama a un modelo, devuelve output. Bucle simple.

Un agente tiene *autonomía*. Puede razonar sobre una tarea, decidir qué herramientas usar, llamarlas, evaluar resultados y decidir qué hacer a continuación — todo sin que tú escribas lógica paso a paso para cada escenario. Le das herramientas e instrucciones, y él se encarga de la orquestación.

Piénsalo así: `IChatClient` es como tener una conversación. Un agente es como delegarle una lista de tareas a alguien.

## Tu Primer Agente en 10 Líneas

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

El método de extensión `.AsAIAgent()` es el puente. Mismo patrón que `.AsIChatClient()` de MEAI — envuelve el SDK del proveedor en una abstracción estable. Funciona con Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry o modelos locales.

El streaming también funciona:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Dando Herramientas al Agente

Aquí es donde los agentes dejan de ser chatbots sofisticados. Las herramientas son funciones que el modelo puede decidir llamar según lo que el usuario pida. No necesitas lógica de enrutamiento — el modelo lo descifra solo.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Dos cosas a notar. Primero, `AIFunctionFactory` es de MEAI — la misma fábrica de herramientas que usarías con un `IChatClient` normal. Si ya tienes herramientas definidas para escenarios de chat, funcionan aquí también.

Segundo, los atributos `Description` importan mucho. Son cómo el modelo entiende qué hace una herramienta y cuándo usarla. Trátalos como documentación para tu IA, no para humanos.

## Sesiones: Conversaciones con Memoria Real

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Sin sesión, cada llamada a `RunAsync` es sin estado. Con sesión, el agente sabe a qué chiste te refieres. `AgentSession` preserva el historial de conversación entre turnos.

Para servicios sin estado en producción, las sesiones se serializan de forma limpia:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... guárdalo en algún lugar ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Esto es crítico si tu agente se ejecuta en entornos serverless o con escalado horizontal.

## AIContextProvider: Memoria Persistente Entre Sesiones

Las sesiones preservan el historial *dentro* de una sesión. Pero ¿qué hay de conocer cosas sobre un usuario entre sesiones? `AIContextProvider` maneja eso.

Tiene dos ganchos:
- **`ProvideAIContextAsync`** — se ejecuta *antes* de cada interacción, inyecta contexto en el agente
- **`StoreAIContextAsync`** — se ejecuta *después* de cada interacción, permite aprender y persistir

El patrón es elegante: puedes apilar múltiples proveedores — uno para preferencias del usuario, uno para interacciones recientes, uno que consulta tu almacén de VectorData para documentos relevantes. Ese último es exactamente el patrón RAG de la Parte 2, ahora ejecutándose automáticamente en cada llamada al agente.

## Workflows Multiagente

Aquí es donde el framework se gana su nombre. Incluye un sistema de workflows basado en grafos donde los ejecutores (agentes, funciones, lo que sea) se conectan mediante aristas.

Algunos patrones soportados nativamente:

- **Secuencial**: La salida del Agente A alimenta al Agente B
- **Concurrente (fan-out/fan-in)**: Despacha a múltiples agentes en paralelo, recoge resultados
- **Enrutamiento condicional**: Enruta trabajo a diferentes agentes según el output
- **Bucles escritor-crítico**: Un agente escribe, otro evalúa, bucle hasta aprobación
- **Sub-workflows**: Compone workflows jerárquicamente

Un ejemplo de escritor-crítico:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Limpio, legible, y el enrutamiento basado en condiciones significa que no escribes la lógica del bucle tú mismo.

## Human-in-the-Loop

No todo debería ejecutarse de forma completamente autónoma. Para operaciones sensibles — escrituras en bases de datos, transacciones financieras, envío de comunicaciones — quieres que un humano apruebe antes de que el agente ejecute.

El framework tiene soporte integrado para esto mediante `FunctionApprovalRequestContent` y `FunctionApprovalResponseContent`. El agente propone la llamada a la herramienta, tu código la presenta al usuario, y la respuesta determina si la ejecución procede.

Esta es la forma correcta de pensar en agentes en entornos empresariales: no completamente autónomos, sino *autonomía con barandillas*.

## El Cuadro Completo

Si das un paso atrás:

- **MEAI** te da una interfaz universal para cualquier modelo
- **VectorData** da a tus agentes acceso al conocimiento de tu organización mediante búsqueda semántica
- **Agent Framework** orquesta todo — usa `IChatClient` internamente, se compone con proveedores de contexto y coordina mediante workflows

Cada pieza fue diseñada para componerse con las otras. Consulta el [post original de Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) y el [repositorio de GitHub del Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) para los ejemplos completos.

## Conclusión

El post de la Parte 3 del Microsoft Agent Framework cierra el bucle de la serie de bloques de construcción. Para los desarrolladores .NET que quieren construir agentes AI — no solo chatbots, sino agentes reales que usan herramientas, recuerdan cosas y coordinan — este es el camino.

La versión estable 1.0 significa que puedes construir con esto en producción. Si has estado esperando para saltar al desarrollo de agentes en .NET, el momento es ahora.
