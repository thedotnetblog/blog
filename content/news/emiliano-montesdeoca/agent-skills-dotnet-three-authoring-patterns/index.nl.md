---
title: "Agent Skills in .NET Zijn Nu Serieus Flexibel"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework ondersteunt nu drie manieren om skills te schrijven — bestanden, klassen en inline code — allemaal samengesteld via één provider. Dit is waarom het belangrijk is en hoe je ze gebruikt."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

Als je agents bouwt met Microsoft Agent Framework, ken je de werkwijze: je definieert skills, koppelt ze aan een provider en laat de agent bepalen welke hij aanroept. Nieuw is *hoe* je die skills schrijft — en de sprong in flexibiliteit is aanzienlijk.

De nieuwste update introduceert drie verschillende patronen voor het schrijven van agent skills: **bestand-gebaseerd**, **klasse-gebaseerd** en **inline code-gedefinieerd**. Alle drie koppelen aan één `AgentSkillsProviderBuilder`, wat betekent dat je ze kunt mixen zonder routeringslogica.

## Bestand-gebaseerde skills: het startpunt

Bestand-gebaseerde skills zijn precies wat ze klinken — een map op schijf met een `SKILL.md`-bestand, optionele scripts en referentiedocumenten:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

De frontmatter van `SKILL.md` declareert de skillnaam en beschrijving, en de instructiesectie vertelt de agent hoe scripts en referenties te gebruiken.

Je koppelt het met `SubprocessScriptRunner.RunAsync`:

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);
```

## Klasse-gebaseerde skills: leveren via NuGet

Hier wordt het interessant voor teams. Klasse-gebaseerde skills leiden af van `AgentClassSkill<T>` en gebruiken attributen zoals `[AgentSkillResource]` en `[AgentSkillScript]`:

```csharp
public sealed class BenefitsEnrollmentSkill : AgentClassSkill<BenefitsEnrollmentSkill>
{
    public override AgentSkillFrontmatter Frontmatter { get; } = new(
        "benefits-enrollment",
        "Enroll an employee in health, dental, or vision plans.");

    [AgentSkillScript("enroll")]
    private static string Enroll(string employeeId, string planCode)
    {
        bool success = HrClient.EnrollInPlan(employeeId, planCode);
        return JsonSerializer.Serialize(new { success, employeeId, planCode });
    }
}
```

Een team kan dit als NuGet-pakket verpakken. Voeg het toe aan je project, stop het in de builder en het werkt naast je bestand-gebaseerde skills.

## Inline skills: de snelle brug

Dat moment wanneer een ander team precies de skill bouwt die je nodig hebt, maar deze pas over een sprint beschikbaar is? `AgentInlineSkill` is je brug:

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: "1. Vraag om medewerker-ID. 2. Gebruik calculate-balance. 3. Presenteer resultaten.")
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int remaining = HrDatabase.GetAnnualAllowance(employeeId, leaveType)
                      - HrDatabase.GetDaysUsed(employeeId, leaveType);
        return JsonSerializer.Serialize(new { employeeId, leaveType, remaining });
    });
```

Wanneer het NuGet-pakket verschijnt, vervang je de inline skill door de klasse-gebaseerde. De agent merkt het verschil niet.

## Scriptgoedkeuring: human-in-the-loop

Voor .NET-ontwikkelaars die productie-agents bouwen, is dit het deel dat implementatiegesprekken daadwerkelijk deblokkert. Zet `UseScriptApproval` aan en de agent pauzeert voor het uitvoeren van elk script:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

## Samenvatting

Agent skills in .NET hebben nu een echt flexibel schrijfmodel. Of je nu een prototype bouwt met bestand-gebaseerde skills of verpakte mogelijkheden via NuGet levert — alle patronen stellen samen via `AgentSkillsProviderBuilder`.

Bekijk de [originele aankondiging](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) en [GitHub-voorbeelden](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills).
