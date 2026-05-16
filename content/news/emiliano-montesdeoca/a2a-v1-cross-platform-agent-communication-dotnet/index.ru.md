---
title: "A2A v1 Здесь: Кросс-Платформенная Коммуникация Агентов в Microsoft Agent Framework для .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Протокол A2A v1.0 выпущен, и пакеты Microsoft Agent Framework для .NET обновлены — стабильный стандарт совместимости для подключения и раскрытия AI-агентов между провайдерами."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Этот пост был переведён автоматически. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

[A2A v1 Здесь: Кросс-Платформенная Коммуникация Агентов в Microsoft Agent Framework для .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — Протокол A2A только что достиг v1.0, и оба пакета A2A Agent (клиент) и A2A Hosting (сервер) для .NET обновлены.

## Что такое A2A v1 на самом деле

A2A — это открытый протокол совместимости для AI-агентов, поддерживаемый техническим руководящим комитетом с представителями AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP и ServiceNow. Метка v1 означает, что это теперь стабильный, готовый к производству стандарт. Пакеты SDK и Agent Framework, реализующие его, всё ещё находятся в предварительной версии, но сам протокол зафиксирован.

v1 улучшает v0.3 с поддержкой мультиарендности, подписанными Agent Cards для криптографической идентификации, улучшенными потоками безопасности и веб-ориентированной архитектурой.

## Подключение к удалённому агенту A2A

Удалённый агент A2A — это просто `AIAgent` в вашем коде — тот же `RunAsync`, то же потоковое воспроизведение, то же управление сессиями:

```csharp
// Обнаружение через well-known URI
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Прямая конфигурация
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Потоковое воспроизведение работает так же
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Раскрытие вашего агента как конечной точки A2A

Любой `AIAgent`, который вы уже создали — на Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic или AWS Bedrock — можно раскрыть как конечную точку A2A двумя строками в ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

Карточка агента автоматически обслуживается по адресу `/.well-known/agent-card.json`.

## Что это означает на практике

Стабильный протокол v1 означает, что вы можете соединять своих .NET-агентов с агентами, созданными на Python, Java или любом другом языке, не беспокоясь о критических изменениях. Криптографическая идентичность в подписанных Agent Cards также обеспечивает основу для проверки доверия между агентами.

Полный журнал изменений и заметки о миграции с v0.3 см. в [полном посте](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/).
