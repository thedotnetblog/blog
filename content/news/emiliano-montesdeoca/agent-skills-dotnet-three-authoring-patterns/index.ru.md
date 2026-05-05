---
title: "Agent Skills в .NET стали по-настоящему гибкими"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework теперь поддерживает три способа создания навыков — файлы, классы и инлайн-код — все компонуются через единый provider. Рассказываю почему это важно и как использовать каждый из них."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Эта статья была переведена автоматически. Оригинал доступен [здесь]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}}).*

Если вы строили агентов с Microsoft Agent Framework, вам знаком процесс: определяете навыки, подключаете их к provider и позволяете агенту решать, какой вызвать. Новое — это *как* вы создаёте эти навыки, и скачок в гибкости значительный.

Последнее обновление вводит три паттерна создания agent skills: **файловые**, **классовые** и **определённые инлайн-кодом**. Все три подключаются к единому `AgentSkillsProviderBuilder`, что означает свободное комбинирование без логики маршрутизации или специального связующего кода. Расскажу о каждом и когда его использовать.

## Файловые навыки: отправная точка

Файловые навыки — это именно то, что звучит: директория на диске с файлом `SKILL.md`, опциональными скриптами и справочными документами. Самый прямой способ дать агенту новые возможности:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

Фронтматтер `SKILL.md` объявляет имя и описание навыка, а секция инструкций говорит агенту, как использовать скрипты и ссылки:

```markdown
---
name: onboarding-guide
description: >-
  Walk new hires through their first-week setup checklist.
---

## Instructions

1. Ask for the employee's name and start date.
2. Run `scripts/check-provisioning.py` to verify accounts.
3. Walk through `references/onboarding-checklist.md`.
4. Follow up on incomplete items.
```

Затем подключаете `SubprocessScriptRunner.RunAsync` для выполнения скриптов:

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);

AIAgent agent = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential())
    .GetResponsesClient()
    .AsAIAgent(new ChatClientAgentOptions
    {
        Name = "HRAgent",
        ChatOptions = new() { Instructions = "You are a helpful HR assistant." },
        AIContextProviders = [skillsProvider],
    },
    model: deploymentName);
```

Агент автоматически обнаруживает навык и вызывает скрипт провизионирования, когда нужно проверить статус аккаунтов. Чисто и просто.

## Классовые навыки: распространяем через NuGet

Здесь для команд становится интересно. Классовые навыки наследуют от `AgentClassSkill<T>` и используют атрибуты `[AgentSkillResource]` и `[AgentSkillScript]`, чтобы фреймворк обнаружил всё через рефлексию:

```csharp
public sealed class BenefitsEnrollmentSkill : AgentClassSkill<BenefitsEnrollmentSkill>
{
    public override AgentSkillFrontmatter Frontmatter { get; } = new(
        "benefits-enrollment",
        "Enroll an employee in health, dental, or vision plans.");

    protected override string Instructions => """
        1. Read the available-plans resource.
        2. Confirm the plan the employee wants.
        3. Use the enroll script to complete enrollment.
        """;

    [AgentSkillResource("available-plans")]
    [Description("Plan options with monthly pricing.")]
    public string AvailablePlans => """
        ## Available Plans (2026)
        - Health: Basic HMO ($0/month), Premium PPO ($45/month)
        - Dental: Standard ($12/month), Enhanced ($25/month)
        - Vision: Basic ($8/month)
        """;

    [AgentSkillScript("enroll")]
    [Description("Enrolls employee in the specified benefit plan.")]
    private static string Enroll(string employeeId, string planCode)
    {
        bool success = HrClient.EnrollInPlan(employeeId, planCode);
        return JsonSerializer.Serialize(new { success, employeeId, planCode });
    }
}
```

Красота в том, что команда может упаковать это как NuGet-пакет. Добавляете в проект, помещаете в builder, и оно работает рядом с файловыми навыками без координации:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Оба навыка появляются в системном промпте агента. Агент решает, какой использовать, на основе разговора — никакого кода маршрутизации.

## Инлайн-навыки: быстрый мост

Знаете тот момент, когда другая команда строит именно тот навык, который вам нужен, но он будет готов только к следующему спринту? `AgentInlineSkill` — ваш мост:

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: """
        1. Ask for the employee ID if not provided.
        2. Use calculate-balance to get the remaining balance.
        3. Present used and remaining days clearly.
        """)
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int totalDays = HrDatabase.GetAnnualAllowance(employeeId, leaveType);
        int daysUsed = HrDatabase.GetDaysUsed(employeeId, leaveType);
        int remaining = totalDays - daysUsed;
        return JsonSerializer.Serialize(new { employeeId, leaveType, totalDays, daysUsed, remaining });
    });
```

Добавьте в builder так же, как и остальные:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Когда NuGet-пакет наконец выйдет, замените инлайн-навык на классовую версию. Агент не заметит разницы.

Но инлайн-навыки не только для мостов. Они также правильный выбор, когда нужно генерировать навыки динамически в рантайме — представьте навык для каждого бизнес-подразделения, загруженный из конфигурации — или когда скрипту нужно захватить локальное состояние, которое не принадлежит DI-контейнеру.

## Одобрение скриптов: человек в цикле

Для нас, .NET-разработчиков, строящих продакшен-агентов, это та часть, которая по-настоящему разблокирует разговоры о деплое. Некоторые скрипты имеют реальные последствия — записать кого-то на бенефиты, запросить продакшен-инфраструктуру. Включите `UseScriptApproval`, и агент делает паузу перед выполнением любого скрипта:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Когда агент хочет выполнить скрипт, он возвращает запрос на одобрение. Ваше приложение собирает решение — одобрить или отклонить — и агент продолжает соответственно. В регулируемых средах это разница между «мы можем это задеплоить» и «юристы сказали нет».

## Почему эта комбинация важна

Настоящая сила не в каком-то отдельном паттерне — а в композиции. Вы можете:

- **Начать с малого** с файловым навыком, итерировать инструкции и опубликовать без написания C#
- **Распространять переиспользуемые навыки** как NuGet-пакеты, которые другие команды добавляют одной строкой
- **Закрывать пробелы** инлайн-навыками, когда что-то нужно *прямо сейчас*
- **Фильтровать общие директории** предикатами, чтобы агент загружал только то, что нужно
- **Добавить человеческий контроль** для скриптов, затрагивающих продакшен-системы

Всё это компонуется через `AgentSkillsProviderBuilder`. Никакой специальной маршрутизации, никакой условной логики, никаких проверок типа навыка.

## Подводя итог

Agent skills в .NET теперь имеют по-настоящему гибкую модель создания. Будь вы соло-разработчик, прототипирующий с файловыми навыками, или корпоративная команда, распространяющая упакованные возможности через NuGet — паттерны подходят. А механизм одобрения скриптов делает решение готовым к продакшену в средах, где нужен человеческий чекпоинт.

Ознакомьтесь с [оригинальным объявлением](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), [документацией Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) на Microsoft Learn и [примерами .NET на GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills), чтобы начать.
