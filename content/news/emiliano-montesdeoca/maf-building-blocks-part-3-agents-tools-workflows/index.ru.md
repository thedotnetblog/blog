---
title: "Microsoft Agent Framework Часть 3: От инструментов к воркфлоу — строительные блоки встают на место"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Третья часть серии Building Blocks for AI в .NET посвящена Microsoft Agent Framework — от одиночных агентов с инструментами до мультиагентных воркфлоу с памятью. Вот что действительно важно."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Этот пост переведён автоматически. Чтобы прочитать оригинал, [нажмите здесь]({{< ref "index.md" >}}).*

Если вы следили за серией Building Blocks for AI в .NET, вы знаете: Часть 1 дала нам `IChatClient` (универсальный интерфейс модели), а Часть 2 — `Microsoft.Extensions.VectorData` (семантический поиск и RAG). Оба — фундаментальные, оба полезны сами по себе. Но здесь всё начинает соединяться.

Часть 3 — о [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). Честно говоря, это именно тот кусочек, которого я ждал в .NET. Версия 1.0 вышла в апреле. API стабильный. Пора строить настоящих агентов.

## Что такое агент (vs. чат-бот)

Прежде чем нырять в код, разберёмся с этим различием. Чат-бот получает ввод, вызывает модель, возвращает вывод. Простой цикл.

Агент имеет *автономию*. Он может рассуждать о задаче, решать, какие инструменты использовать, вызывать их, оценивать результаты и решать, что делать дальше — всё это без написания явной пошаговой логики для каждого сценария. Вы даёте ему инструменты и инструкции, а он сам занимается оркестрацией.

Думайте об этом так: `IChatClient` — как вести разговор. Агент — как поручить кому-то список задач.

## Первый агент в 10 строках

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

Метод расширения `.AsAIAgent()` — это мост. Тот же паттерн, что и `.AsIChatClient()` из MEAI — оборачивает SDK провайдера в стабильную абстракцию. Работает с Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry или локальными моделями.

Стриминг тоже работает:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Даём агенту инструменты

Здесь агенты перестают быть продвинутыми чат-ботами. Инструменты — это функции, которые модель может решить вызвать в зависимости от запроса пользователя. Логика маршрутизации не нужна — модель разберётся сама.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Два момента. Первый: `AIFunctionFactory` из MEAI — та же фабрика инструментов, что используется с обычным `IChatClient`. Если вы уже определили инструменты для сценариев чата, здесь они тоже работают.

Второй: атрибуты `Description` имеют большое значение. Именно через них модель понимает, что делает инструмент и когда его применять. Относитесь к ним как к документации для ИИ, а не для людей.

## Сессии: разговоры с настоящей памятью

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Без сессии каждый вызов `RunAsync` — безсостоянческий. С сессией агент знает, о каком анекдоте вы говорите. `AgentSession` сохраняет историю разговора между ходами.

Для stateless-сервисов в продакшне сессии сериализуются чисто:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... сохраните куда-нибудь ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Это критично, если ваш агент работает в serverless или горизонтально масштабируемой среде.

## AIContextProvider: постоянная память между сессиями

Сессии сохраняют историю разговора *внутри* сессии. Но что насчёт знания о пользователе между сессиями? Этим занимается `AIContextProvider`.

У него два хука:
- **`ProvideAIContextAsync`** — выполняется *перед* каждым взаимодействием, внедряет контекст в агента
- **`StoreAIContextAsync`** — выполняется *после* каждого взаимодействия, позволяет учиться и сохранять

Паттерн элегантный: можно складывать несколько провайдеров — один для предпочтений пользователя, один для недавних взаимодействий, один который запрашивает VectorData-хранилище на предмет релевантных документов. Последний — это именно RAG-паттерн из Части 2, теперь автоматически выполняющийся при каждом вызове агента.

## Мультиагентные воркфлоу

Здесь фреймворк оправдывает своё название. Он включает графовую систему воркфлоу, где исполнители (агенты, функции, что угодно) соединяются рёбрами.

Некоторые поддерживаемые паттерны:

- **Последовательный**: вывод Агента A поступает в Агент B
- **Параллельный (fan-out/fan-in)**: диспетчеризация нескольким агентам параллельно, сбор результатов
- **Условная маршрутизация**: направление работы разным агентам в зависимости от вывода
- **Циклы писатель-критик**: один агент пишет, другой оценивает, цикл до одобрения
- **Подворкфлоу**: иерархическая композиция воркфлоу

Пример писатель-критик:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Чисто, читаемо, и маршрутизация на основе условий означает, что логику цикла писать самому не нужно.

## Human-in-the-Loop

Не всё должно выполняться полностью автономно. Для чувствительных операций — записи в БД, финансовых транзакций, отправки сообщений — нужно человеческое одобрение перед выполнением агентом.

Фреймворк имеет встроенную поддержку через `FunctionApprovalRequestContent` и `FunctionApprovalResponseContent`. Агент предлагает вызов инструмента, ваш код приложения показывает его пользователю, и ответ определяет, будет ли выполнение продолжено.

Это правильный способ думать об агентах в корпоративной среде: не полная автономия, а *автономия с ограничителями*.

## Общая картина

Если сделать шаг назад:

- **MEAI** даёт универсальный интерфейс к любой модели
- **VectorData** открывает агентам доступ к знаниям организации через семантический поиск
- **Agent Framework** оркестрирует всё — использует `IChatClient` под капотом, компонуется с провайдерами контекста, координирует через воркфлоу

Каждая часть разработана для компоновки с другими. Смотрите [оригинальный пост Джереми Ликнесса](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) и [GitHub-репозиторий Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) для полных примеров.

## Итог

Пост Часть 3 Microsoft Agent Framework закрывает цикл серии строительных блоков. Для .NET-разработчиков, которые хотят строить агентов ИИ — не просто чат-ботов, а настоящих агентов, использующих инструменты, помнящих и координирующих — это ваш путь вперёд.

Стабильный релиз 1.0 означает, что это можно использовать в продакшне. Если вы ждали момента, чтобы войти в разработку агентов в .NET, этот момент — сейчас.
