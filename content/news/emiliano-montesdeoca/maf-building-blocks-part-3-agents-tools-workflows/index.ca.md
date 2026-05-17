---
title: "Microsoft Agent Framework Part 3: De les Eines als Workflows — Les Peces Encaixen"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "La tercera part de la sèrie de blocs de construcció d'IA en .NET cobreix el Microsoft Agent Framework — des d'agents únics amb eines fins a workflows multi-agent amb memòria. Això és el que realment importa."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Si has seguit la sèrie Building Blocks for AI en .NET, saps que la Part 1 ens va donar `IChatClient` (la interfície universal de models) i la Part 2 ens va donar `Microsoft.Extensions.VectorData` (cerca semàntica i RAG). Ambdues són fonamentals i útils per si soles. Però aquí és on tot comença a connectar-se.

La Part 3 tracta del [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — i sincerament, és la peça que estava esperant veure arribar a .NET. La versió 1.0 es va publicar a l'abril. L'API és estable. És hora de construir agents de veritat.

## Què és un Agent (vs. un Chatbot)

Abans d'entrar al codi, aclarim aquesta distinció. Un chatbot rep input, crida un model, retorna output. Bucle simple.

Un agent té *autonomia*. Pot raonar sobre una tasca, decidir quines eines usar, cridar-les, avaluar resultats i decidir què fer a continuació — tot sense que tu escriguis lògica pas a pas per a cada escenari. Li dónes eines i instruccions, i s'encarrega de l'orquestració.

Pensa-hi així: `IChatClient` és com tenir una conversa. Un agent és com delegar una llista de tasques a algú.

## El Teu Primer Agent en 10 Línies

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

El mètode d'extensió `.AsAIAgent()` és el pont. Mateix patró que `.AsIChatClient()` de MEAI — embolica el SDK del proveïdor en una abstracció estable. Funciona amb Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry o models locals.

L'streaming també funciona:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Donant Eines a l'Agent

Aquí és on els agents deixen de ser chatbots sofisticats. Les eines són funcions que el model pot decidir cridar segons el que l'usuari demani. No necessites lògica d'enrutament — el model ho descobreix sol.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Dues coses a tenir en compte. Primer, `AIFunctionFactory` és de MEAI — la mateixa fàbrica d'eines que usaries amb un `IChatClient` normal. Si ja tens eines definides per a escenaris de xat, funcionen aquí també.

Segon, els atributs `Description` importen molt. Són com el model entén què fa una eina i quan usar-la. Tracta'ls com a documentació per a la teva IA, no per a humans.

## Sessions: Converses amb Memòria Real

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Sense sessió, cada crida a `RunAsync` és sense estat. Amb sessió, l'agent sap a quin acudit et refereixes. `AgentSession` preserva l'historial de conversa entre torns.

Per a serveis sense estat en producció, les sessions es serialitzen de forma neta:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... guarda-ho en algun lloc ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Això és crític si el teu agent s'executa en entorns serverless o amb escalat horitzontal.

## AIContextProvider: Memòria Persistent Entre Sessions

Les sessions preserven l'historial *dins* d'una sessió. Però què passa amb conèixer coses d'un usuari entre sessions? `AIContextProvider` s'encarrega d'això.

Té dos ganxos:
- **`ProvideAIContextAsync`** — s'executa *abans* de cada interacció, injecta context a l'agent
- **`StoreAIContextAsync`** — s'executa *després* de cada interacció, permet aprendre i persistir

El patró és elegant: pots apillar múltiples proveïdors — un per a preferències d'usuari, un per a interaccions recents, un que consulta el teu magatzem de VectorData per a documents rellevants. Aquest últim és exactament el patró RAG de la Part 2, ara executant-se automàticament a cada crida de l'agent.

## Workflows Multi-Agent

Aquí és on el framework es guanya el seu nom. Inclou un sistema de workflows basat en grafs on els executors (agents, funcions, el que sigui) es connecten mitjançant arestes.

Alguns patrons suportats nativament:

- **Seqüencial**: La sortida de l'Agent A alimenta l'Agent B
- **Concurrent (fan-out/fan-in)**: Despacha a múltiples agents en paral·lel, recull resultats
- **Enrutament condicional**: Enruta feina a agents diferents segons la sortida
- **Bucles escriptor-crític**: Un agent escriu, un altre avalua, bucle fins a aprovació
- **Sub-workflows**: Compon workflows jeràrquicament

Un exemple escriptor-crític:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Net, llegible, i l'enrutament basat en condicions significa que no escrius la lògica del bucle tu mateix.

## Human-in-the-Loop

No tot hauria d'executar-se de forma completament autònoma. Per a operacions sensibles — escriptures a bases de dades, transaccions financeres, enviament de comunicacions — vols que un humà aprovi abans que l'agent executi.

El framework té suport integrat per a això mitjançant `FunctionApprovalRequestContent` i `FunctionApprovalResponseContent`. L'agent proposa la crida a l'eina, el teu codi la presenta a l'usuari, i la resposta determina si l'execució continua.

Aquesta és la forma correcta de pensar en agents en entorns empresarials: no completament autònoms, sinó *autonomia amb barreres*.

## El Quadre Complet

Si fas un pas enrere:

- **MEAI** et dóna una interfície universal per a qualsevol model
- **VectorData** dóna als teus agents accés al coneixement de la teva organització mitjançant cerca semàntica
- **Agent Framework** orquestra tot — usa `IChatClient` internament, es compon amb proveïdors de context i coordina mitjançant workflows

Cada peça va ser dissenyada per compondre's amb les altres. Consulta el [post original de Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) i el [repositori de GitHub del Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) per als exemples complets.

## Conclusió

El post de la Part 3 del Microsoft Agent Framework tanca el bucle de la sèrie de blocs de construcció. Per als desenvolupadors .NET que volen construir agents AI — no sols chatbots, sinó agents reals que usen eines, recorden coses i coordinen — aquest és el camí.

La versió estable 1.0 significa que pots construir amb això en producció. Si has estat esperant per saltar al desenvolupament d'agents en .NET, el moment és ara.
