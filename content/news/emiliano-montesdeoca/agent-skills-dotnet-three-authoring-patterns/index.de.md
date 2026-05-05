---
title: "Agent Skills in .NET sind jetzt richtig flexibel"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Das Microsoft Agent Framework unterstützt jetzt drei Wege Skills zu erstellen — Dateien, Klassen und Inline-Code — alle über einen einzigen Provider zusammengesetzt. Hier erfahrt ihr warum das wichtig ist und wie ihr jeden Ansatz nutzt."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [hier klicken]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}}).*

Wenn ihr Agenten mit dem Microsoft Agent Framework baut, kennt ihr den Ablauf: Skills definieren, in einen Provider einbinden und den Agenten entscheiden lassen, welchen er aufruft. Neu ist *wie* ihr diese Skills erstellt — und der Flexibilitätssprung ist erheblich.

Das neueste Update führt drei verschiedene Authoring-Patterns für Agent Skills ein: **dateibasiert**, **klassenbasiert** und **inline-codedefiniert**. Alle drei werden über einen einzigen `AgentSkillsProviderBuilder` verbunden, sodass ihr sie ohne Routing-Logik oder speziellen Glue-Code mischen könnt. Ich zeige euch jedes Pattern und wann ihr es einsetzen solltet.

## Dateibasierte Skills: der Einstiegspunkt

Dateibasierte Skills sind genau das, wonach sie klingen — ein Verzeichnis auf der Festplatte mit einer `SKILL.md`-Datei, optionalen Scripts und Referenzdokumenten. Die einfachste Art, eurem Agenten neue Fähigkeiten zu geben:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

Das `SKILL.md`-Frontmatter deklariert den Skill-Namen und die Beschreibung, und der Instruktionsabschnitt sagt dem Agenten, wie er Scripts und Referenzen nutzen soll:

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

Dann verbindet ihr es mit `SubprocessScriptRunner.RunAsync` für die Script-Ausführung:

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

Der Agent entdeckt den Skill automatisch und ruft das Provisioning-Script auf, wenn er den Kontostatus prüfen muss. Sauber und einfach.

## Klassenbasierte Skills: per NuGet ausliefern

Hier wird es für Teams interessant. Klassenbasierte Skills leiten von `AgentClassSkill<T>` ab und verwenden Attribute wie `[AgentSkillResource]` und `[AgentSkillScript]`, damit das Framework alles per Reflection entdeckt:

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

Das Schöne daran: Ein Team kann das als NuGet-Paket verpacken. Ihr fügt es eurem Projekt hinzu, steckt es in den Builder und es funktioniert neben euren dateibasierten Skills ohne Koordination:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Beide Skills erscheinen im System-Prompt des Agenten. Der Agent entscheidet basierend auf dem Gespräch, welchen er nutzt — kein Routing-Code nötig.

## Inline Skills: die schnelle Brücke

Kennt ihr das, wenn ein anderes Team genau den Skill baut, den ihr braucht, aber erst im nächsten Sprint fertig wird? `AgentInlineSkill` ist eure Brücke:

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

Fügt ihn genauso wie die anderen zum Builder hinzu:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Wenn das NuGet-Paket irgendwann erscheint, tauscht ihr den Inline-Skill gegen die klassenbasierte Version aus. Der Agent merkt den Unterschied nicht.

Inline Skills sind aber nicht nur für Brücken. Sie sind auch die richtige Wahl, wenn ihr Skills dynamisch zur Laufzeit generieren müsst — denkt an einen Skill pro Geschäftsbereich aus einer Konfiguration geladen — oder wenn ein Script lokalen State erfassen muss, der nicht in einen DI-Container gehört.

## Script-Genehmigung: Mensch in der Schleife

Für uns .NET-Entwickler, die Produktionsagenten bauen, ist das der Teil, der Deployment-Gespräche wirklich freischaltet. Manche Scripts haben echte Konsequenzen — jemanden in Benefits einschreiben, Produktionsinfrastruktur abfragen. Aktiviert `UseScriptApproval` und der Agent pausiert vor jeder Script-Ausführung:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Wenn der Agent ein Script ausführen will, gibt er stattdessen eine Genehmigungsanfrage zurück. Eure App sammelt die Entscheidung — genehmigen oder ablehnen — und der Agent fährt entsprechend fort. In regulierten Umgebungen ist das der Unterschied zwischen "wir können das deployen" und "die Rechtsabteilung sagt nein."

## Warum diese Kombination wichtig ist

Die echte Stärke liegt nicht in einem einzelnen Authoring-Pattern — sondern in der Komposition. Ihr könnt:

- **Klein anfangen** mit einem dateibasierten Skill, die Instruktionen iterieren und ohne C# veröffentlichen
- **Wiederverwendbare Skills** als NuGet-Pakete ausliefern, die andere Teams mit einer Zeile hinzufügen können
- **Lücken überbrücken** mit Inline Skills, wenn ihr etwas *jetzt* braucht
- **Gemeinsame Skill-Verzeichnisse filtern** mit Predicates, damit euer Agent nur das lädt, was er soll
- **Menschliche Aufsicht hinzufügen** für Scripts, die Produktionssysteme berühren

All das wird über `AgentSkillsProviderBuilder` zusammengesetzt. Kein spezielles Routing, keine bedingte Logik, keine Skill-Typ-Prüfungen.

## Zum Abschluss

Agent Skills in .NET haben jetzt ein wirklich flexibles Authoring-Modell. Ob ihr ein Solo-Entwickler seid, der mit dateibasierten Skills einen Prototyp skizziert, oder ein Enterprise-Team, das verpackte Fähigkeiten per NuGet ausliefert — die Patterns passen. Und der Script-Genehmigungsmechanismus macht es produktionsreif für Umgebungen, in denen ihr diesen menschlichen Checkpoint braucht.

Schaut euch die [Original-Ankündigung](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) an, die [Agent Skills Dokumentation](https://learn.microsoft.com/en-us/agent-framework/agents/skills) auf Microsoft Learn und die [.NET-Beispiele auf GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) zum Loslegen.
