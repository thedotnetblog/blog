---
title: "Umiejętności agentów w .NET stały się naprawdę elastyczne"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework obsługuje teraz trzy sposoby tworzenia umiejętności — na podstawie plików, klas i kodu inline — wszystkie komponowane przez jeden dostawca. Oto dlaczego to ważne i jak używać każdego z nich."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

Jeśli budujesz agenty z Microsoft Agent Framework, znasz schemat: definiujesz umiejętności, podłączasz je do dostawcy i pozwalasz agentowi zdecydować, którą wywołać. Co nowego to *sposób* tworzenia tych umiejętności — a skok elastyczności jest znaczący.

Najnowsza aktualizacja wprowadza trzy odmienne wzorce tworzenia umiejętności agentów: **oparty na plikach**, **oparty na klasach** i **zdefiniowany w kodzie inline**. Wszystkie trzy podłączają się do jednego `AgentSkillsProviderBuilder`, co oznacza, że możesz je mieszać i dopasowywać bez żadnej logiki routingu ani specjalnego kodu spinającego. Przeprowadzę cię przez każdy z nich i kiedy po który sięgać.

## Umiejętności oparte na plikach: punkt startowy

Umiejętności oparte na plikach to dokładnie to, na co wskazuje nazwa — katalog na dysku z plikiem `SKILL.md`, opcjonalnymi skryptami i dokumentami referencyjnymi. Pomyśl o tym jako o najprostszym sposobie na danie agentowi nowych możliwości:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

Metadane w `SKILL.md` deklarują nazwę i opis umiejętności, a sekcja instrukcji mówi agentowi, jak używać skryptów i referencji:

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

Następnie podłączasz to za pomocą `SubprocessScriptRunner.RunAsync` do wykonania skryptów:

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

Agent automatycznie wykrywa umiejętność i wywołuje skrypt sprawdzania uprawnień, gdy jest to potrzebne. Czyste i proste.

## Umiejętności oparte na klasach: dostarcz przez NuGet

Tu robi się interesująco dla zespołów. Umiejętności oparte na klasach dziedziczą z `AgentClassSkill<T>` i używają atrybutów takich jak `[AgentSkillResource]` i `[AgentSkillScript]`, dzięki czemu framework odkrywa wszystko przez refleksję:

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

Piękno polega na tym, że zespół może spakować to jako pakiet NuGet. Dodajesz go do projektu, wrzucasz do buildera i działa obok umiejętności opartych na plikach bez żadnej koordynacji:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Obie umiejętności pojawiają się w prompcie systemowym agenta. Agent decyduje, którą użyć na podstawie rozmowy — bez kodu routingu.

## Umiejętności inline: szybki pomost

Znasz ten moment, gdy inny zespół buduje dokładnie tę umiejętność, której potrzebujesz, ale nie wyda jej przez sprint? `AgentInlineSkill` to twój pomost:

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

Dodajesz ją do buildera tak samo jak pozostałe:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Gdy pakiet NuGet w końcu się pojawi, wymieniasz umiejętność inline na opartą na klasach. Agent nie zna różnicy.

Ale umiejętności inline nie są tylko dla pomostów. Są też właściwym wyborem, gdy musisz dynamicznie generować umiejętności w czasie działania — pomyśl jedna umiejętność na jednostkę biznesową ładowaną z konfiguracji — albo gdy skrypt musi zamykać się na lokalnym stanie, który nie należy do kontenera DI.

## Zatwierdzanie skryptów: człowiek w pętli

Dla nas, programistów .NET, budujących agenty produkcyjne, to jest część, która naprawdę odblokowuje rozmowy o wdrożeniu. Niektóre skrypty mają realne konsekwencje — rejestrowanie kogoś w świadczeniach, zapytania do infrastruktury produkcyjnej. Włącz `UseScriptApproval` i agent wstrzymuje się przed wykonaniem jakiegokolwiek skryptu:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Gdy agent chce uruchomić skrypt, zamiast tego zwraca żądanie zatwierdzenia. Twoja aplikacja zbiera decyzję — zatwierdź lub odrzuć — i agent kontynuuje odpowiednio. W regulowanych środowiskach to jest różnica między "możemy to wdrożyć" a "dział prawny mówi nie".

## Dlaczego ta kombinacja ma znaczenie

Prawdziwa moc nie leży w żadnym pojedynczym wzorcu tworzenia — to w kompozycji. Możesz:

- **Zacząć mało** z umiejętnością opartą na plikach, iterować instrukcje i dostarczyć bez pisania C#
- **Dostarczać umiejętności wielokrotnego użytku** jako pakiety NuGet, które inne zespoły mogą dodać jedną linijką
- **Pomost luk** z umiejętnościami inline, gdy potrzebujesz czegoś *teraz*
- **Filtrować współdzielone katalogi umiejętności** za pomocą predykatów, by agent ładował tylko to, co powinien
- **Dodawać nadzór ludzki** dla skryptów dotykających systemów produkcyjnych

Wszystko to komponuje się przez `AgentSkillsProviderBuilder`. Żadnego specjalnego routingu, żadnej logiki warunkowej, żadnych sprawdzeń typów umiejętności.

## Podsumowanie

Umiejętności agentów w .NET mają teraz naprawdę elastyczny model tworzenia. Czy jesteś samotnym programistą szkicującym prototyp z umiejętnościami opartymi na plikach, czy zespołem enterprise dostarczającym spakowane możliwości przez NuGet — wzorce się dopasowują. A mechanizm zatwierdzania skryptów sprawia, że jest gotowe do produkcji dla środowisk, gdzie potrzebujesz tego ludzkiego punktu kontrolnego.

Sprawdź [oryginalne ogłoszenie](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) po pełny przewodnik, [dokumentację Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) na Microsoft Learn i [przykłady .NET na GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills), by zacząć pracę.
