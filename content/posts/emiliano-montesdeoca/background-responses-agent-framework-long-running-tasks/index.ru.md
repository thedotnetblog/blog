---
title: "Фоновые ответы в Microsoft Agent Framework: больше никакой тревоги из-за таймаутов"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework теперь позволяет выносить длительные ИИ-задачи с помощью continuation-токенов. Вот как работают фоновые ответы и почему они важны для ваших .NET-агентов."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Если вы создавали что-либо с моделями рассуждения, такими как o3 или GPT-5.2, вы знаете эту боль. Ваш агент начинает обдумывать сложную задачу, клиент сидит и ждёт, и где-то между «всё нормально» и «он завис?» ваше соединение падает по таймауту. Вся работа? Потеряна.

Microsoft Agent Framework только что выпустил [фоновые ответы](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — и честно говоря, это одна из тех функций, которая должна была существовать с первого дня.

## Проблема с блокирующими вызовами

В традиционной модели запрос-ответ ваш клиент блокируется до завершения работы агента. Это нормально для быстрых задач. Но когда вы просите модель рассуждения провести глубокое исследование, многоэтапный анализ или сгенерировать 20-страничный отчёт? Вы смотрите на минуты реального времени. В течение этого окна:

- HTTP-соединения могут упасть по таймауту
- Сетевые сбои убивают всю операцию
- Ваш пользователь смотрит на спиннер, гадая, происходит ли что-нибудь

Фоновые ответы переворачивают этот подход.

## Как работают continuation-токены

Вместо блокировки вы запускаете задачу агента и получаете обратно **continuation-токен**. Представьте его как квитанцию в ремонтной мастерской — вы не стоите у стойки и ждёте, а приходите, когда всё готово.

Процесс прост:

1. Отправьте запрос с `AllowBackgroundResponses = true`
2. Если агент поддерживает фоновую обработку, вы получаете continuation-токен
3. Опрашивайте по своему расписанию, пока токен не вернёт `null` — это значит, результат готов

Вот версия на .NET:

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

// Опрашиваем до завершения
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Если агент завершает немедленно (простые задачи, модели, не требующие фоновой обработки), continuation-токен не возвращается. Ваш код просто работает — никакой специальной обработки не нужно.

## Стриминг с возобновлением: настоящая магия

Опрос подходит для сценариев «запустил и забыл», но что если вы хотите видеть прогресс в реальном времени? Фоновые ответы также поддерживают стриминг со встроенным возобновлением.

Каждое потоковое обновление несёт свой continuation-токен. Если соединение прерывается посреди потока, вы продолжаете ровно с того места, где остановились:

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
    break; // Симулируем разрыв сети
}

// Возобновляем ровно с того места, где остановились
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

Агент продолжает обработку на стороне сервера независимо от того, что происходит с вашим клиентом. Это встроенная отказоустойчивость без написания логики повторных попыток или circuit breaker'ов.

## Когда это действительно использовать

Не каждый вызов агента нуждается в фоновых ответах. Для быстрых завершений вы добавляете сложность без причины. Но вот где они реально полезны:

- **Сложные задачи рассуждения** — многоэтапный анализ, глубокие исследования, всё, что заставляет модель рассуждения действительно думать
- **Генерация длинного контента** — детальные отчёты, многочастные документы, обширный анализ
- **Ненадёжные сети** — мобильные клиенты, периферийные развёртывания, нестабильные корпоративные VPN
- **Асинхронные UX-паттерны** — отправьте задачу, займитесь другим делом, вернитесь за результатами

Для .NET-разработчиков, создающих корпоративные приложения, последний пункт особенно интересен. Представьте Blazor-приложение, где пользователь запрашивает сложный отчёт — вы запускаете задачу агента, показываете индикатор прогресса и позволяете ему продолжить работу. Никакой WebSocket-гимнастики, никакой пользовательской инфраструктуры очередей, просто токен и цикл опроса.

## Итог

Фоновые ответы уже доступны в .NET и Python через Microsoft Agent Framework. Если вы создаёте агентов, которые делают что-то сложнее простых вопросов-ответов, это стоит добавить в свой инструментарий. Паттерн с continuation-токенами сохраняет простоту, решая очень реальную продакшен-проблему.

Ознакомьтесь с [полной документацией](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) для полного справочника API и дополнительных примеров.
