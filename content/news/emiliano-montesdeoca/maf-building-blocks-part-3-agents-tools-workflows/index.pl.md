---
title: "Microsoft Agent Framework Część 3: Od narzędzi do przepływów pracy — klocki zatrzaskują się na miejscu"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Trzecia część serii Building Blocks for AI w .NET omawia Microsoft Agent Framework — od pojedynczych agentów z narzędziami po przepływy multiagentowe z pamięcią. Oto co naprawdę ważne."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Ten post został przetłumaczony automatycznie. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Jeśli śledzisz serię Building Blocks for AI w .NET, wiesz: Część 1 dała nam `IChatClient` (uniwersalny interfejs modelu), a Część 2 — `Microsoft.Extensions.VectorData` (wyszukiwanie semantyczne i RAG). Oba są podstawowe i przydatne same w sobie. Ale tutaj wszystko zaczyna się łączyć.

Część 3 dotyczy [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — i szczerze, to właśnie ten kawałek czekałem, żeby zobaczyć w .NET. Wersja 1.0 wyszła w kwietniu. API jest stabilne. Czas budować prawdziwych agentów.

## Czym tak naprawdę jest agent (vs. chatbot)

Zanim wejdziemy w kod, wyjaśnijmy to rozróżnienie. Chatbot odbiera input, wywołuje model, zwraca output. Prosta pętla.

Agent ma *autonomię*. Może rozumować nad zadaniem, zdecydować, które narzędzia użyć, wywołać je, ocenić wyniki i zdecydować, co zrobić dalej — wszystko bez pisania eksplicitnej logiki krok po kroku dla każdego scenariusza. Dajesz mu narzędzia i instrukcje, a on sam zajmuje się orkiestracją.

Pomyśl tak: `IChatClient` to jak prowadzenie rozmowy. Agent to jak delegowanie listy zadań komuś.

## Twój pierwszy agent w 10 liniach

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

Metoda rozszerzająca `.AsAIAgent()` jest mostem. Ten sam wzorzec co `.AsIChatClient()` z MEAI — opakowuje SDK dostawcy w stabilną abstrakcję. Działa z Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry lub lokalnymi modelami.

Streaming też działa:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Dawanie narzędzi agentowi

Tu agenci przestają być wyszukanymi chatbotami. Narzędzia to funkcje, które model może zdecydować się wywołać na podstawie tego, o co prosi użytkownik. Nie potrzebujesz logiki routingu — model sam to rozgryzie.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Dwie rzeczy do zanotowania. Po pierwsze, `AIFunctionFactory` pochodzi z MEAI — ta sama fabryka narzędzi, której używałbyś z normalnym `IChatClient`. Jeśli masz już zdefiniowane narzędzia dla scenariuszy czatowych, działają tu też.

Po drugie, atrybuty `Description` mają ogromne znaczenie. To dzięki nim model rozumie, co narzędzie robi i kiedy go użyć. Traktuj je jako dokumentację dla twojej AI, nie dla ludzi.

## Sesje: Rozmowy, które naprawdę pamiętają

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Bez sesji każde wywołanie `RunAsync` jest bezstanowe. Z sesją agent wie, o którym żarcie mówisz. `AgentSession` zachowuje historię rozmowy między turami.

Dla bezstanowych usług produkcyjnych sesje serializują się czysto:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... przechowaj gdzieś ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

To kluczowe, jeśli twój agent działa w środowisku serverless lub poziomo skalowanym.

## AIContextProvider: Trwała pamięć między sesjami

Sesje zachowują historię rozmowy *wewnątrz* sesji. Ale co z wiedzą o użytkowniku między sesjami? `AIContextProvider` to obsługuje.

Ma dwa haki:
- **`ProvideAIContextAsync`** — wykonuje się *przed* każdą interakcją, wstrzykuje kontekst do agenta
- **`StoreAIContextAsync`** — wykonuje się *po* każdej interakcji, pozwala na uczenie i utrwalanie

Wzorzec jest elegancki: możesz układać wiele dostawców w stos — jeden dla preferencji użytkownika, jeden dla ostatnich interakcji, jeden który odpytuje twój store VectorData o odpowiednie dokumenty. Ten ostatni to dokładnie wzorzec RAG z Części 2, teraz wykonywany automatycznie przy każdym wywołaniu agenta.

## Przepływy multiagentowe

Tutaj framework zasługuje na swoją nazwę. Zawiera oparty na grafach system przepływów pracy, gdzie egzekutory (agenci, funkcje, cokolwiek) łączą się przez krawędzie.

Kilka natywnie obsługiwanych wzorców:

- **Sekwencyjny**: Wyjście Agenta A zasila Agenta B
- **Współbieżny (fan-out/fan-in)**: Dyspatchuje do wielu agentów równolegle, zbiera wyniki
- **Warunkowe routowanie**: Kieruje pracę do różnych agentów w zależności od wyjścia
- **Pętle pisarz-krytyk**: Jeden agent pisze, drugi ocenia, pętla do zatwierdzenia
- **Pod-przepływy**: Hierarchiczne komponowanie przepływów

Przykład pisarz-krytyk:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Czyste, czytelne, i routowanie oparte na warunkach oznacza, że logiki pętli nie piszesz sam.

## Human-in-the-Loop

Nie wszystko powinno działać w pełni autonomicznie. Dla wrażliwych operacji — zapisów do bazy danych, transakcji finansowych, wysyłania komunikatów — chcesz, żeby człowiek zatwierdził przed wykonaniem przez agenta.

Framework ma wbudowane wsparcie dla tego poprzez `FunctionApprovalRequestContent` i `FunctionApprovalResponseContent`. Agent proponuje wywołanie narzędzia, twój kod aplikacji przedstawia je użytkownikowi, a odpowiedź decyduje, czy wykonanie postępuje.

To właściwy sposób myślenia o agentach w środowiskach korporacyjnych: nie w pełni autonomiczni, ale *autonomia z barierkami*.

## Pełny obraz

Jeśli cofniesz się o krok:

- **MEAI** daje ci uniwersalny interfejs do dowolnego modelu
- **VectorData** daje twoim agentom dostęp do wiedzy organizacji przez wyszukiwanie semantyczne
- **Agent Framework** orkiestruje wszystko — używa `IChatClient` pod spodem, komponuje się z dostawcami kontekstu, koordynuje przez przepływy

Każda część została zaprojektowana, by komponować się z innymi. Sprawdź [oryginalny post Jeremy'ego Liknessa](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) i [repozytorium GitHub Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) dla pełnych przykładów.

## Podsumowanie

Post Część 3 Microsoft Agent Framework zamyka pętlę serii Building Blocks. Dla deweloperów .NET chcących budować agentów AI — nie tylko chatboty, ale prawdziwych agentów używających narzędzi, pamiętających rzeczy i koordynujących — to jest twoja droga naprzód.

Stabilny release 1.0 oznacza, że możesz budować na tym w produkcji. Jeśli czekałeś, żeby wskoczyć w tworzenie agentów w .NET, ten moment jest teraz.
