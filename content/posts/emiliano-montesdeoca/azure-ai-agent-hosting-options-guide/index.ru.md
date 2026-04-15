---
title: "Где размещать AI-агентов в Azure? Практическое руководство по выбору"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure предлагает шесть способов размещения AI-агентов — от контейнеров до полностью управляемых Foundry Hosted Agents. Вот как выбрать подходящий вариант для вашей .NET нагрузки."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Этот пост был переведён автоматически. Оригинальная версия доступна [здесь]({{< ref "azure-ai-agent-hosting-options-guide.md" >}}).*

Если вы сейчас создаёте AI-агентов с .NET, вы наверняка заметили: способов разместить их в Azure *очень много*. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — и все звучат разумно, пока вам не нужно действительно выбрать один. Microsoft только что опубликовала [полное руководство по размещению AI-агентов в Azure](https://devblogs.microsoft.com/all-things-azure/hostedagent/), и я хочу разобрать его с практической точки зрения .NET-разработчика.

## Шесть вариантов с первого взгляда

| Вариант | Лучше всего для | Вы управляете |
|---------|----------------|---------------|
| **Container Apps** | Полный контроль контейнеров без сложности K8s | Наблюдаемость, состояние, жизненный цикл |
| **AKS** | Корпоративный комплаенс, мультикластер, пользовательские сети | Всем (в этом и суть) |
| **Azure Functions** | Событийные краткосрочные задачи агентов | Почти ничем — настоящий serverless |
| **App Service** | Простые HTTP-агенты, предсказуемый трафик | Развёртывание, настройка масштабирования |
| **Foundry Agents** | Агенты без кода через портал/SDK | Почти ничем |
| **Foundry Hosted Agents** | Агенты с пользовательским фреймворком на управляемой инфраструктуре | Только ваш код агента |

Первые четыре — это вычисления общего назначения: вы *можете* запускать на них агентов, но они не были для этого спроектированы. Последние два — нативные для агентов: они понимают разговоры, вызовы инструментов и жизненные циклы агентов как первоклассные концепции.

## Foundry Hosted Agents — оптимальный выбор для .NET-разработчиков агентов

Вот что привлекло моё внимание. Foundry Hosted Agents находятся точно посередине: вы получаете гибкость запуска собственного кода (Semantic Kernel, Agent Framework, LangGraph — что угодно), а платформа управляет инфраструктурой, наблюдаемостью и управлением разговорами.

Ключевой элемент — **Hosting Adapter** — тонкий слой абстракции, который соединяет ваш фреймворк агентов с платформой Foundry. Для Microsoft Agent Framework это выглядит так:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Это вся ваша история хостинга. Адаптер обрабатывает трансляцию протоколов, стриминг через server-sent events, историю разговоров и трассировку OpenTelemetry — всё автоматически. Никакого пользовательского middleware, никакой ручной прокладки.

## Развёртывание действительно простое

Я раньше развёртывал агентов в Container Apps, и это работает, но в итоге вы пишете много связующего кода для управления состоянием и наблюдаемости. С Hosted Agents и `azd` развёртывание — это:

```bash
# Установить расширение AI-агента
azd ext install azure.ai.agents

# Инициализировать из шаблона
azd ai agent init

# Собрать, отправить, развернуть — готово
azd up
```

Эта единственная команда `azd up` собирает ваш контейнер, отправляет его в ACR, создаёт проект Foundry, развёртывает endpoints моделей и запускает вашего агента. Пять шагов сжаты в одну команду.

## Встроенное управление разговорами

Это та часть, которая экономит больше всего времени в продакшене. Вместо создания собственного хранилища состояния разговоров, Hosted Agents обрабатывают это нативно:

```python
# Создать постоянный разговор
conversation = openai_client.conversations.create()

# Первый ход
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Второй ход — контекст сохранён
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Никакого Redis. Никакого хранилища сессий Cosmos DB. Никакого middleware для сериализации сообщений. Платформа просто справляется.

## Мой фреймворк принятия решений

Пройдя все шесть вариантов, вот моя быстрая ментальная модель:

1. **Нужен нулевой уровень инфраструктуры?** → Foundry Agents (портал/SDK, без контейнеров)
2. **Есть пользовательский код агента, но нужен управляемый хостинг?** → Foundry Hosted Agents
3. **Нужны событийные краткосрочные задачи агентов?** → Azure Functions
4. **Нужен максимальный контроль контейнеров без K8s?** → Container Apps
5. **Нужен строгий комплаенс и мультикластер?** → AKS
6. **Простой HTTP-агент с предсказуемым трафиком?** → App Service

Для большинства .NET-разработчиков, работающих с Semantic Kernel или Microsoft Agent Framework, Hosted Agents — вероятно правильная отправная точка. Вы получаете scale-to-zero, встроенный OpenTelemetry, управление разговорами и гибкость фреймворка — без управления Kubernetes или создания собственного стека наблюдаемости.

## Подводя итог

Ландшафт хостинга агентов в Azure быстро зреет. Если вы начинаете новый проект AI-агента сегодня, я бы серьёзно рассмотрел Foundry Hosted Agents, прежде чем по привычке тянуться к Container Apps или AKS. Управляемая инфраструктура экономит реальное время, а паттерн hosting adapter позволяет сохранить ваш выбор фреймворка.

Ознакомьтесь с [полным руководством Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) и [репозиторием Foundry Samples](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) для рабочих примеров.
