---
title: "Создать Агентов — Это Лёгкая Часть. Безопасно Их Запустить — Вот Что Сложно"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework и Agent Governance Toolkit объединяются для применения политик времени выполнения, управления вызовами инструментов и создания журналов аудита с Merkle-цепочкой — без изменения промптов агента."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

В разработке ИИ-агентов есть паттерн, который я начал называть «сожалением о демо». Агент отлично работает на демонстрациях. Потом кто-то спрашивает: что произойдёт, если он вызовет не тот инструмент? А если получит доступ к данным, к которым не должен? Кто это проверял?

Microsoft Agent Framework поддерживает вас в построении и оркестрации. Agent Governance Toolkit (AGT) покрывает то, что идёт после — управление, применение политик и аудитируемость во время выполнения.

## Что На Самом Деле Делает Каждый Проект

**Microsoft Agent Framework (MAF)** предоставляет модель программирования: мульти-агентные рабочие процессы, совместимость протокола A2A, хуки middleware, память и управляемый хостинг через Foundry Agent Service. Обрабатывает безопасность контента на уровне ввода/вывода модели.

**Agent Governance Toolkit (AGT)** подключается к тому же pipeline middleware для управления *действиями*. Каждый вызов инструмента, обращение к ресурсам и сообщение между агентами оценивается относительно политики до выполнения. Накладные расходы менее миллисекунды. Нет сайдкаров, нет прокси, нет изменённых промптов.

```
Действие Агента --> Проверка Политики --> Разрешить / Запретить --> Журнал Аудита    (< 0.1 мс)
```

Разные слои, полное покрытие, один pipeline.

## Подключение — Это Просто Добавление Middleware

В Python AGT добавляется к тому же параметру `middleware`, который вы использовали бы для логирования или фильтров контента:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

В .NET тот же паттерн через `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Тот же агент, та же оркестрация, те же инструменты. AGT добавляет возможности управления, не затрагивая логику агента.

## Что Вы Получаете

- **GovernancePolicyMiddleware** — оценивает каждое действие по декларативным правилам политики
- **CapabilityGuardMiddleware** — whitelist инструментов, которые агент имеет право вызывать (инструмент `approve_small_loan` намеренно не включён в список выше)
- **RogueDetectionMiddleware** — обнаруживает аномальные паттерны поведения во время выполнения
- **AuditTrailMiddleware** — журнал аудита с Merkle-цепочкой, чтобы каждое действие было криптографически защищено от подделки

Последнее важно для соответствия требованиям. Merkle-цепочка означает: если кто-то изменит журнал, цепочка нарушится. Аудит является доказательством.

## Пять Отраслевых Сценариев

Репозиторий AGT содержит пять полных сквозных сценариев: финансовые услуги (кредитный сотрудник), здравоохранение (данные пациентов), юридический (проверка контрактов), государственные органы (гражданские услуги) и производство (контроль качества). Каждый сочетает настоящие агенты MAF с настоящим middleware управления AGT.

Это не игрушечные демо. Это именно те сценарии, где в продакшне действительно нужно управление.

## Подводя Итоги

Если вы создаёте агентов, которые работают с реальными данными, принимают решения с последствиями или работают без наблюдения в продакшне — управление не опционально. Комбинация MAF + AGT даёт вам полный стек: стройте с Agent Framework, управляйте с AGT.

Оба проекта с открытым исходным кодом. Оригинальная статья содержит ссылки на полные примеры кода.

Оригинальная публикация: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
