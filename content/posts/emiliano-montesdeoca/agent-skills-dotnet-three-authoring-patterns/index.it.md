---
title: "Le Agent Skills in .NET sono diventate davvero flessibili"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Il Microsoft Agent Framework ora supporta tre modi per creare skill — file, classi e codice inline — tutte composte attraverso un singolo provider. Ecco perché è importante e come usare ciascun approccio."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}}).*

Se avete costruito agenti con il Microsoft Agent Framework, conoscete il processo: definite le skill, le collegate a un provider e lasciate che l'agente decida quale invocare. La novità è *come* create queste skill — e il salto in flessibilità è significativo.

L'ultimo aggiornamento introduce tre pattern di authoring per le agent skill: **basate su file**, **basate su classi** e **definite in codice inline**. Tutte e tre si collegano a un unico `AgentSkillsProviderBuilder`, il che significa che potete mescolarle senza logica di routing o codice speciale. Vi mostro ciascuna e quando usarla.

## Skill basate su file: il punto di partenza

Le skill basate su file sono esattamente quello che sembrano — una directory su disco con un file `SKILL.md`, script opzionali e documenti di riferimento. Il modo più diretto per dare nuove capacità al vostro agente:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

Il frontmatter di `SKILL.md` dichiara il nome e la descrizione, e la sezione istruzioni dice all'agente come usare script e riferimenti:

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

Poi lo collegate con `SubprocessScriptRunner.RunAsync` per l'esecuzione degli script:

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

L'agente scopre la skill automaticamente e invoca lo script di provisioning quando deve verificare lo stato degli account. Pulito e semplice.

## Skill basate su classi: distribuire via NuGet

Qui diventa interessante per i team. Le skill basate su classi derivano da `AgentClassSkill<T>` e usano attributi come `[AgentSkillResource]` e `[AgentSkillScript]` perché il framework scopra tutto tramite reflection:

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

Il bello è che un team può impacchettarlo come pacchetto NuGet. Lo aggiungete al progetto, lo inserite nel builder e funziona accanto alle vostre skill basate su file senza coordinazione:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Entrambe le skill appaiono nel system prompt dell'agente. L'agente decide quale usare in base alla conversazione — nessun codice di routing necessario.

## Skill inline: il ponte rapido

Conoscete quel momento in cui un altro team sta costruendo esattamente la skill di cui avete bisogno, ma non sarà pronta fino al prossimo sprint? `AgentInlineSkill` è il vostro ponte:

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

Aggiungetela al builder come le altre:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Quando il pacchetto NuGet esce finalmente, sostituite la skill inline con la versione basata su classe. L'agente non nota la differenza.

Ma le skill inline non sono solo per i ponti. Sono anche la scelta giusta quando dovete generare skill dinamicamente a runtime — pensate a una skill per unità di business caricata dalla configurazione — o quando uno script deve catturare stato locale che non appartiene a un container DI.

## Approvazione degli script: umano nel loop

Per noi sviluppatori .NET che costruiamo agenti di produzione, questa è la parte che sblocca davvero le discussioni sul deployment. Alcuni script hanno conseguenze reali — iscrivere qualcuno ai benefit, interrogare l'infrastruttura di produzione. Attivate `UseScriptApproval` e l'agente si ferma prima di eseguire qualsiasi script:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Quando l'agente vuole eseguire uno script, restituisce una richiesta di approvazione. La vostra app raccoglie la decisione — approvare o rifiutare — e l'agente continua di conseguenza. Negli ambienti regolamentati, questa è la differenza tra "possiamo fare il deploy" e "l'ufficio legale dice no."

## Perché questa combinazione conta

Il vero potere non è in nessun pattern individuale — è nella composizione. Potete:

- **Iniziare in piccolo** con una skill basata su file, iterare sulle istruzioni e pubblicarla senza scrivere C#
- **Distribuire skill riutilizzabili** come pacchetti NuGet che altri team aggiungono con una riga
- **Colmare lacune** con skill inline quando avete bisogno di qualcosa *adesso*
- **Filtrare directory condivise** con predicati perché il vostro agente carichi solo quello che deve
- **Aggiungere supervisione umana** per gli script che toccano sistemi di produzione

Tutto questo si compone tramite `AgentSkillsProviderBuilder`. Nessun routing speciale, nessuna logica condizionale, nessun controllo del tipo di skill.

## Per concludere

Le agent skill in .NET ora hanno un modello di authoring genuinamente flessibile. Che siate uno sviluppatore solo che prototipa con skill basate su file o un team enterprise che distribuisce capacità impacchettate via NuGet, i pattern si adattano. E il meccanismo di approvazione degli script lo rende pronto per la produzione negli ambienti dove serve quel checkpoint umano.

Date un'occhiata all'[annuncio originale](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), alla [documentazione Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) su Microsoft Learn e agli [esempi .NET su GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) per iniziare.
