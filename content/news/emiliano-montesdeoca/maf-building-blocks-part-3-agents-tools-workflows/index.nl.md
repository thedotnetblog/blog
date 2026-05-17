---
title: "Microsoft Agent Framework Deel 3: Van tools naar workflows — de bouwstenen vallen op hun plek"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Deel 3 van de Building Blocks for AI in .NET-serie behandelt het Microsoft Agent Framework — van enkelvoudige agents met tools tot multi-agent workflows met geheugen. Hier is wat er echt toe doet."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

Als je de Building Blocks for AI in .NET-serie hebt gevolgd, weet je: Deel 1 gaf ons `IChatClient` (de universele modelinterface) en Deel 2 gaf ons `Microsoft.Extensions.VectorData` (semantisch zoeken en RAG). Beide zijn fundamenteel en elk voor zich nuttig. Maar hier begint alles met elkaar te verbinden.

Deel 3 gaat over het [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — en eerlijk gezegd is dit het stuk waar ik op wachtte in .NET. Versie 1.0 verscheen in april. De API is stabiel. Het is tijd om echte agents te bouwen.

## Wat een agent eigenlijk is (vs. een chatbot)

Voordat we in de code duiken, verduidelijken we dit onderscheid. Een chatbot ontvangt input, roept een model aan, retourneert output. Eenvoudige lus.

Een agent heeft *autonomie*. Hij kan redeneren over een taak, beslissen welke tools te gebruiken, ze aanroepen, resultaten evalueren en beslissen wat daarna te doen — dit alles zonder dat je voor elk scenario expliciete stap-voor-stap-logica schrijft. Je geeft hem tools en instructies, en hij regelt de orkestratie.

Denk er zo over: `IChatClient` is als een gesprek voeren. Een agent is als een takenlijst delegeren aan iemand.

## Je eerste agent in 10 regels

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

De uitbreidingsmethode `.AsAIAgent()` is de brug. Hetzelfde patroon als `.AsIChatClient()` van MEAI — het omhult de SDK van de provider in een stabiele abstractie. Werkt met Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry of lokale modellen.

Streaming werkt ook:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## De agent tools geven

Hier houden agents op geavanceerde chatbots te zijn. Tools zijn functies die het model kan beslissen aan te roepen op basis van wat de gebruiker vraagt. Geen routeringslogica van jouw kant — het model lost het zelf op.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Twee dingen om op te merken. Ten eerste: `AIFunctionFactory` komt van MEAI — dezelfde tool factory die je zou gebruiken met een gewone `IChatClient`. Als je al tools hebt gedefinieerd voor chatscenario's, werken ze hier ook.

Ten tweede: de `Description`-attributen zijn heel belangrijk. Dit is hoe het model begrijpt wat een tool doet en wanneer het te gebruiken. Behandel ze als documentatie voor je AI, niet voor mensen.

## Sessies: Gesprekken die echt onthouden

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Zonder sessie is elke `RunAsync`-aanroep stateloos. Met een sessie weet de agent welke grap je bedoelt. `AgentSession` behoudt de gespreksgeschiedenis tussen beurten.

Voor stateless productiediensten serialiseren sessies netjes:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... sla het ergens op ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Dit is cruciaal als je agent draait in een serverloze of horizontaal geschaalde omgeving.

## AIContextProvider: Persistent geheugen over sessies heen

Sessies bewaren de gespreksgeschiedenis *binnen* een sessie. Maar hoe zit het met het kennen van dingen over een gebruiker over sessies heen? `AIContextProvider` regelt dat.

Het heeft twee hooks:
- **`ProvideAIContextAsync`** — wordt uitgevoerd *vóór* elke interactie, injecteert context in de agent
- **`StoreAIContextAsync`** — wordt uitgevoerd *na* elke interactie, maakt leren en persisteren mogelijk

Het patroon is elegant: je kunt meerdere providers stapelen — één voor gebruikersvoorkeuren, één voor recente interacties, één die je VectorData-store bevraagt voor relevante documenten. Die laatste is precies het RAG-patroon uit Deel 2, nu automatisch uitgevoerd als onderdeel van elke agent-aanroep.

## Multi-agent workflows

Hier verdient het framework zijn naam. Het bevat een graafgebaseerd workflowsysteem waarbij executors (agents, functies, wat dan ook) via kanten verbonden worden.

Enkele native ondersteunde patronen:

- **Sequentieel**: De output van Agent A voedt Agent B
- **Gelijktijdig (fan-out/fan-in)**: Dispatcht parallel naar meerdere agents, verzamelt resultaten
- **Voorwaardelijke routering**: Routeert werk naar verschillende agents op basis van output
- **Schrijver-criticus-lussen**: Eén agent schrijft, een andere evalueert, lus tot goedkeuring
- **Sub-workflows**: Hiërarchisch samenstellen van workflows

Een schrijver-criticus-voorbeeld:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Netjes, leesbaar, en de voorwaardegebaseerde routering betekent dat je de luslogica niet zelf schrijft.

## Human-in-the-Loop

Niet alles moet volledig autonoom lopen. Voor gevoelige operaties — databaseschrijvingen, financiële transacties, het verzenden van communicatie — wil je dat een mens goedkeurt voordat de agent uitvoert.

Het framework heeft ingebouwde ondersteuning hiervoor via `FunctionApprovalRequestContent` en `FunctionApprovalResponseContent`. De agent stelt de tool-aanroep voor, je applicatiecode presenteert die aan de gebruiker, en de reactie bepaalt of de uitvoering doorgaat.

Dit is de juiste manier om te denken over agents in enterprise-omgevingen: niet volledig autonoom, maar *autonomie met vangrails*.

## Het volledige beeld

Als je een stap terugzet:

- **MEAI** geeft je een universele interface naar elk model
- **VectorData** geeft je agents toegang tot de kennis van je organisatie via semantisch zoeken
- **Agent Framework** orkestreert alles — gebruikt `IChatClient` onder de motorkap, componeert met context providers, en coördineert via workflows

Elk stuk is ontworpen om met de andere te componeren. Bekijk de [originele post van Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) en het [Agent Framework GitHub-repository](https://github.com/microsoft/agent-framework/tree/main/dotnet) voor de volledige voorbeelden.

## Conclusie

De Deel 3-post van het Microsoft Agent Framework sluit de lus van de Building Blocks-serie. Voor .NET-ontwikkelaars die AI-agents willen bouwen — geen chatbots, maar echte agents die tools gebruiken, dingen onthouden en coördineren — dit is je weg vooruit.

De stabiele release 1.0 betekent dat je hier productie op kunt bouwen. Als je wachtte om in agent-development in .NET te springen, is het moment nu.
