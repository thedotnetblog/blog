---
title: "Microsoft Agent Framework Teil 3: Von Tools zu Workflows — Die Bausteine fügen sich zusammen"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Teil 3 der .NET AI Building Blocks-Serie behandelt das Microsoft Agent Framework — von einzelnen Agenten mit Tools bis hin zu Multi-Agenten-Workflows mit Gedächtnis. Hier ist, was wirklich wichtig ist."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Dieser Beitrag wurde automatisch übersetzt. Die Originalversion findest du [hier]({{< ref "index.md" >}}).*

Wenn du der Building Blocks for AI in .NET-Serie gefolgt bist, weißt du: Teil 1 brachte uns `IChatClient` (die universelle Modellschnittstelle) und Teil 2 `Microsoft.Extensions.VectorData` (semantische Suche und RAG). Beides sind grundlegende Bausteine, jeder für sich nützlich. Aber hier beginnt alles, sich zu verbinden.

Teil 3 dreht sich um das [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — und ehrlich gesagt ist es genau das Stück, auf das ich in .NET gewartet habe. Version 1.0 erschien im April. Die API ist stabil. Es ist Zeit, echte Agenten zu bauen.

## Was ein Agent wirklich ist (vs. ein Chatbot)

Bevor wir in den Code einsteigen, klären wir diesen Unterschied. Ein Chatbot empfängt Input, ruft ein Modell auf, gibt Output zurück. Einfache Schleife.

Ein Agent hat *Autonomie*. Er kann über eine Aufgabe nachdenken, entscheiden, welche Tools er verwenden soll, diese aufrufen, Ergebnisse auswerten und entscheiden, was als nächstes zu tun ist — alles ohne explizite Schritt-für-Schritt-Logik von deiner Seite. Du gibst ihm Tools und Anweisungen, und er kümmert sich um die Orchestrierung.

Stell es dir so vor: `IChatClient` ist wie ein Gespräch. Ein Agent ist wie das Delegieren einer Aufgabenliste an jemanden.

## Dein erster Agent in 10 Zeilen

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

Die `.AsAIAgent()`-Erweiterungsmethode ist die Brücke. Dasselbe Muster wie `.AsIChatClient()` von MEAI — es verpackt das SDK des Anbieters in eine stabile Abstraktion. Funktioniert mit Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry oder lokalen Modellen.

Streaming funktioniert ebenfalls:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Dem Agenten Tools geben

Hier hören Agenten auf, ausgefeilte Chatbots zu sein. Tools sind Funktionen, die das Modell je nach Benutzeranfrage aufrufen kann. Du brauchst keine Routing-Logik — das Modell findet es selbst heraus.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Zwei Dinge zu beachten. Erstens: `AIFunctionFactory` kommt von MEAI — dieselbe Tool-Factory, die du mit einem normalen `IChatClient` verwenden würdest. Bereits definierte Tools für Chat-Szenarien funktionieren hier auch.

Zweitens: Die `Description`-Attribute sind sehr wichtig. So versteht das Modell, was ein Tool macht und wann es eingesetzt werden soll. Behandle sie als Dokumentation für deine KI, nicht für Menschen.

## Sessions: Gespräche mit echtem Gedächtnis

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Ohne Session ist jeder `RunAsync`-Aufruf zustandslos. Mit Session weiß der Agent, auf welchen Witz du dich beziehst. `AgentSession` bewahrt den Gesprächsverlauf zwischen den Turns.

Für zustandslose Produktionsdienste lassen sich Sessions sauber serialisieren:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... irgendwo speichern ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Das ist entscheidend, wenn dein Agent in einer serverlosen oder horizontal skalierten Umgebung läuft.

## AIContextProvider: Persistentes Gedächtnis über Sessions hinaus

Sessions bewahren den Gesprächsverlauf *innerhalb* einer Session. Aber was ist mit Wissen über einen Benutzer über mehrere Sessions hinweg? Dafür ist `AIContextProvider` zuständig.

Er hat zwei Hooks:
- **`ProvideAIContextAsync`** — läuft *vor* jeder Interaktion, injiziert Kontext in den Agenten
- **`StoreAIContextAsync`** — läuft *nach* jeder Interaktion, ermöglicht Lernen und Persistierung

Das Muster ist elegant: Du kannst mehrere Provider stapeln — einer für Benutzerpräferenzen, einer für kürzliche Interaktionen, einer der deinen VectorData-Store nach relevanten Dokumenten abfragt. Letzteres ist genau das RAG-Muster aus Teil 2, das jetzt automatisch bei jedem Agenten-Aufruf ausgeführt wird.

## Multi-Agenten-Workflows

Hier verdient das Framework seinen Namen. Es enthält ein graphenbasiertes Workflow-System, in dem Executors (Agenten, Funktionen, was auch immer) über Kanten verbunden werden.

Nativ unterstützte Muster:

- **Sequenziell**: Die Ausgabe von Agent A speist Agent B
- **Parallel (Fan-out/Fan-in)**: Dispatchiert parallel an mehrere Agenten, sammelt Ergebnisse
- **Bedingtes Routing**: Leitet Arbeit je nach Ausgabe an unterschiedliche Agenten weiter
- **Schreiber-Kritiker-Schleifen**: Ein Agent schreibt, ein anderer bewertet, Schleife bis zur Genehmigung
- **Sub-Workflows**: Hierarchisches Komponieren von Workflows

Ein Schreiber-Kritiker-Beispiel:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Sauber, lesbar, und das bedingungsbasierte Routing bedeutet, dass du die Schleifenlogik nicht selbst schreibst.

## Human-in-the-Loop

Nicht alles sollte vollständig autonom laufen. Für sensible Operationen — Datenbankschreibvorgänge, Finanztransaktionen, Kommunikationsversendungen — möchtest du, dass ein Mensch genehmigt, bevor der Agent ausführt.

Das Framework hat dafür eingebaute Unterstützung via `FunctionApprovalRequestContent` und `FunctionApprovalResponseContent`. Der Agent schlägt den Tool-Aufruf vor, dein Anwendungscode präsentiert ihn dem Benutzer, und die Antwort entscheidet, ob die Ausführung fortgesetzt wird.

Das ist die richtige Art, in Unternehmensumgebungen über Agenten nachzudenken: nicht vollständig autonom, sondern *Autonomie mit Leitplanken*.

## Das Gesamtbild

Wenn du einen Schritt zurückgehst:

- **MEAI** gibt dir eine universelle Schnittstelle zu jedem Modell
- **VectorData** gibt deinen Agenten Zugriff auf das Wissen deiner Organisation durch semantische Suche
- **Agent Framework** orchestriert alles — verwendet intern `IChatClient`, kombiniert sich mit Kontext-Providern und koordiniert durch Workflows

Jedes Teil wurde darauf ausgelegt, mit den anderen zu komponieren. Schau dir den [Originalbeitrag von Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) und das [Agent Framework GitHub-Repository](https://github.com/microsoft/agent-framework/tree/main/dotnet) für die vollständigen Beispiele an.

## Fazit

Der Microsoft Agent Framework Teil 3 schließt den Kreis der Building Blocks-Serie. Für .NET-Entwickler, die KI-Agenten bauen wollen — keine Chatbots, echte Agenten, die Tools verwenden, Dinge merken und koordinieren — das ist dein Weg nach vorne.

Der stabile 1.0-Release bedeutet, dass du damit in der Produktion bauen kannst. Wenn du darauf gewartet hast, in die Agentenentwicklung in .NET einzusteigen, ist jetzt der richtige Zeitpunkt.
