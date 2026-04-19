---
title: "Les habilitats d'agent a.NET s'acaben de ser molt flexibles"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "El Microsoft Agent Framework ara admet tres maneres de crear habilitats: fitxers, classes i codi en línia, totes compostes a través d'un sol proveïdor. Heus aquí per què és important i com utilitzar-los."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

Si heu estat creant agents amb Microsoft Agent Framework, coneixeu l'exercici: definiu les habilitats, les connecteu a un proveïdor i deixeu que l'agent esbringui quina invocar. El que és nou és *com* autors d'aquestes habilitats, i el salt de flexibilitat és important.

L'última actualització introdueix tres patrons de creació personalitzats per a les habilitats d'agent: **basat en fitxers**, **basat en classes** i **definit en codi en línia**. Els tres es connecten a un únic `AgentSkillsProviderBuilder`, el que significa que podeu barrejar i combinar sense cap lògica d'encaminament ni codi de cola especial. Permeteu-me que us acompanyi a través de cadascuna i quan ho aconseguiu.

## Habilitats basades en fitxers: el punt de partida

Les habilitats basades en fitxers són exactament el que sonen: un directori al disc amb un fitxer `SKILL.md`, scripts opcionals i documents de referència. Penseu en això com la manera més senzilla de donar noves capacitats al vostre agent:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

El frontmatter `SKILL.md` declara el nom i la descripció de l'habilitat, i la secció d'instruccions indica a l'agent com utilitzar els scripts i les referències:

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

A continuació, connecteu-lo amb `SubprocessScriptRunner.RunAsync` per a l'execució de l'script:

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

L'agent descobreix l'habilitat automàticament i invoca l'script de subministrament quan necessita comprovar l'estat del compte. Net i senzill.

## Habilitats basades en classe: enviament mitjançant NuGet

Aquí és on es posa interessant per als equips. Les habilitats basades en classe es deriven de `AgentClassSkill<T>` i utilitzen atributs com `[AgentSkillResource]` i `[AgentSkillScript]` perquè el marc ho descobreixi tot mitjançant la reflexió:

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

La bellesa aquí és que un equip pot empaquetar-ho com a paquet NuGet. L'afegiu al vostre projecte, el deixeu anar al constructor i funciona juntament amb les vostres habilitats basades en fitxers amb una coordinació zero:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Les dues habilitats es mostren a l'indicador del sistema de l'agent. L'agent decideix quin utilitzar en funció de la conversa, no cal cap codi d'encaminament.

## Habilitats en línia: el pont ràpid

Coneixeu aquell moment en què un altre equip està construint exactament l'habilitat que necessiteu, però no s'enviarà per a un sprint? `AgentInlineSkill` és el teu pont:

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

Afegiu-lo al constructor igual que els altres:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Quan finalment s'envia el paquet NuGet, canvieu l'habilitat en línia per la basada en classe. L'agent no sap la diferència.

Però les habilitats en línia no són només per als ponts. També són l'opció correcta quan necessiteu generar habilitats de manera dinàmica en temps d'execució (penseu en una habilitat per unitat de negoci carregada des de la configuració) o quan un script s'ha de tancar a l'estat local que no pertany a un contenidor DI.

## Aprovació de l'script: human-in-the-loop

Per als desenvolupadors de.NET que creem agents de producció, aquesta és la part que realment desbloqueja les converses de desplegament. Alguns scripts tenen conseqüències reals: inscriure algú als beneficis, consultar la producció infra. Gireu `UseScriptApproval` i l'agent s'aturarà abans d'executar qualsevol script:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Quan l'agent vol executar un script, torna una sol·licitud d'aprovació. La vostra aplicació recull la decisió (aprovar o rebutjar) i l'agent continua en conseqüència. En entorns regulats, aquesta és la diferència entre "podem desplegar això" i "legal diu que no".

## Per què és important aquesta combinació

El poder real no és cap patró d'autor, sinó la composició. Pots:

- **Comença petit** amb una habilitat basada en fitxers, itera les instruccions i envia'l sense escriure C#
- **Envia habilitats reutilitzables** com a paquets NuGet que altres equips poden afegir amb una línia
- **Rebre els buits** amb habilitats en línia quan necessiteu alguna cosa *ara*
- **Filtreu els directoris d'habilitats compartits** amb predicats perquè el vostre agent només carregui el que hauria de fer
- **Afegiu supervisió humana** per als scripts que toquen els sistemes de producció

Tots ells es componen mitjançant `AgentSkillsProviderBuilder`. Sense encaminament especial, sense lògica condicional, sense comprovacions de tipus d'habilitat.

## Tancant

Les habilitats d'agent a.NET ara tenen un model d'autoria realment flexible. Tant si sou un desenvolupador en solitari que dibuixa un prototip amb habilitats basades en fitxers com si un equip empresarial envia capacitats empaquetades mitjançant NuGet, els patrons s'ajusten. I el mecanisme d'aprovació de l'script fa que estigui llest per a la producció per a entorns on necessiteu aquest punt de control humà.

Consulteu l'[anunci original](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) per a la guia completa, la [documentació d'habilitats de l'agent](https://learn.microsoft.com/en-us/agent-framework/agents/skills) a Microsoft Learn i les [mostres.NET a GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) per fer-ho pràctica.
