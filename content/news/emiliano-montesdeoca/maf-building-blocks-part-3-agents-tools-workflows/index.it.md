---
title: "Microsoft Agent Framework Parte 3: Dagli Strumenti ai Workflow — I Mattoni si Incastrano"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "La terza parte della serie Building Blocks for AI in .NET copre il Microsoft Agent Framework — da agenti singoli con strumenti a workflow multi-agente con memoria. Ecco cosa conta davvero."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Se hai seguito la serie Building Blocks for AI in .NET, sai che la Parte 1 ci ha dato `IChatClient` (l'interfaccia universale dei modelli) e la Parte 2 `Microsoft.Extensions.VectorData` (ricerca semantica e RAG). Entrambi sono fondamentali e utili da soli. Ma è qui che tutto inizia a connettersi.

La Parte 3 riguarda il [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — e onestamente, è il pezzo che stavo aspettando di vedere arrivare in .NET. La versione 1.0 è uscita ad aprile. L'API è stabile. È ora di costruire agenti veri.

## Cos'è un Agente (vs. un Chatbot)

Prima di immergerci nel codice, chiariamo questa distinzione. Un chatbot riceve input, chiama un modello, restituisce output. Loop semplice.

Un agente ha *autonomia*. Può ragionare su un compito, decidere quali strumenti usare, chiamarli, valutare i risultati e decidere cosa fare dopo — tutto senza che tu scriva logica passo-passo per ogni scenario. Gli dai strumenti e istruzioni, e lui si occupa dell'orchestrazione.

Pensaci così: `IChatClient` è come avere una conversazione. Un agente è come delegare una lista di compiti a qualcuno.

## Il Tuo Primo Agente in 10 Righe

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

Il metodo di estensione `.AsAIAgent()` è il ponte. Stesso pattern di `.AsIChatClient()` da MEAI — avvolge l'SDK del provider in un'astrazione stabile. Funziona con Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry o modelli locali.

Lo streaming funziona anche:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Dare Strumenti all'Agente

È qui che gli agenti smettono di essere chatbot sofisticati. Gli strumenti sono funzioni che il modello può decidere di chiamare in base a ciò che l'utente chiede. Nessuna logica di routing da parte tua — il modello lo capisce da solo.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Due cose da notare. Primo, `AIFunctionFactory` viene da MEAI — la stessa tool factory che useresti con un `IChatClient` normale. Se hai già definito strumenti per scenari di chat, funzionano qui anche.

Secondo, gli attributi `Description` sono molto importanti. È così che il modello capisce cosa fa uno strumento e quando usarlo. Trattali come documentazione per la tua IA, non per gli umani.

## Sessioni: Conversazioni con Memoria Vera

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Senza sessione, ogni chiamata a `RunAsync` è stateless. Con una sessione, l'agente sa a quale barzelletta ti riferisci. `AgentSession` preserva la cronologia della conversazione tra i turni.

Per servizi stateless in produzione, le sessioni si serializzano in modo pulito:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... conservalo da qualche parte ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Questo è fondamentale se il tuo agente gira in un ambiente serverless o con scaling orizzontale.

## AIContextProvider: Memoria Persistente tra le Sessioni

Le sessioni preservano la cronologia *all'interno* di una sessione. Ma che dire del conoscere cose su un utente tra sessioni diverse? `AIContextProvider` gestisce questo.

Ha due hook:
- **`ProvideAIContextAsync`** — viene eseguito *prima* di ogni interazione, inietta contesto nell'agente
- **`StoreAIContextAsync`** — viene eseguito *dopo* ogni interazione, permette di apprendere e persistere

Il pattern è elegante: puoi impilare più provider — uno per le preferenze utente, uno per le interazioni recenti, uno che interroga il tuo store VectorData per documenti rilevanti. Quest'ultimo è esattamente il pattern RAG della Parte 2, ora eseguito automaticamente ad ogni chiamata all'agente.

## Workflow Multi-Agente

È qui che il framework guadagna il suo nome. Include un sistema di workflow basato su grafi dove gli executor (agenti, funzioni, qualsiasi cosa) si connettono tramite archi.

Alcuni pattern supportati nativamente:

- **Sequenziale**: L'output dell'Agente A alimenta l'Agente B
- **Concorrente (fan-out/fan-in)**: Dispatcha a più agenti in parallelo, raccoglie risultati
- **Routing condizionale**: Instrada il lavoro ad agenti diversi in base all'output
- **Loop scrittore-critico**: Un agente scrive, un altro valuta, loop fino all'approvazione
- **Sub-workflow**: Compone workflow gerarchicamente

Un esempio scrittore-critico:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Pulito, leggibile, e il routing basato su condizioni significa che non scrivi la logica del loop tu stesso.

## Human-in-the-Loop

Non tutto dovrebbe girare in modo completamente autonomo. Per operazioni sensibili — scritture su database, transazioni finanziarie, invio di comunicazioni — vuoi che un umano approvi prima che l'agente esegua.

Il framework ha supporto integrato per questo tramite `FunctionApprovalRequestContent` e `FunctionApprovalResponseContent`. L'agente propone la chiamata allo strumento, il tuo codice applicativo la presenta all'utente, e la risposta determina se l'esecuzione procede.

Questo è il modo giusto di pensare agli agenti in contesti aziendali: non completamente autonomi, ma *autonomia con guardrail*.

## Il Quadro Completo

Se fai un passo indietro:

- **MEAI** ti dà un'interfaccia universale per qualsiasi modello
- **VectorData** dà ai tuoi agenti accesso alla conoscenza della tua organizzazione tramite ricerca semantica
- **Agent Framework** orchestra tutto — usa `IChatClient` internamente, si compone con context provider, e coordina tramite workflow

Ogni pezzo è stato progettato per comporsi con gli altri. Consulta il [post originale di Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) e il [repository GitHub dell'Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) per gli esempi completi.

## Conclusione

Il post Parte 3 del Microsoft Agent Framework chiude il cerchio della serie Building Blocks. Per gli sviluppatori .NET che vogliono costruire agenti AI — non solo chatbot, ma agenti veri che usano strumenti, ricordano cose e coordinano — questo è il percorso.

La versione stabile 1.0 significa che puoi costruire con questo in produzione. Se stavi aspettando di tuffarti nello sviluppo di agenti in .NET, il momento è adesso.
