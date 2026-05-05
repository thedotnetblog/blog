---
title: "Les Agent Skills en .NET deviennent vraiment flexibles"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Le Microsoft Agent Framework supporte désormais trois façons de créer des skills — fichiers, classes et code inline — toutes composées via un seul provider. Voici pourquoi c'est important et comment utiliser chacune."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}}).*

Si vous construisez des agents avec le Microsoft Agent Framework, vous connaissez le principe : vous définissez des skills, vous les connectez à un provider et vous laissez l'agent décider lequel invoquer. Ce qui est nouveau, c'est *comment* vous créez ces skills — et le gain en flexibilité est significatif.

La dernière mise à jour introduit trois patterns d'authoring pour les agent skills : **basées sur des fichiers**, **basées sur des classes** et **définies en code inline**. Les trois se branchent sur un seul `AgentSkillsProviderBuilder`, ce qui veut dire que vous pouvez les mixer sans logique de routage ni code spécial. Je vous présente chacune et quand l'utiliser.

## Skills basées sur des fichiers : le point de départ

Les skills basées sur des fichiers sont exactement ce que leur nom suggère — un répertoire sur disque avec un fichier `SKILL.md`, des scripts optionnels et des documents de référence. La façon la plus directe de donner de nouvelles capacités à votre agent :

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

Le frontmatter du `SKILL.md` déclare le nom et la description, et la section d'instructions dit à l'agent comment utiliser les scripts et les références :

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

Ensuite vous le connectez avec `SubprocessScriptRunner.RunAsync` pour l'exécution des scripts :

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

L'agent découvre la skill automatiquement et invoque le script de provisioning quand il doit vérifier le statut des comptes. Propre et simple.

## Skills basées sur des classes : distribuer via NuGet

C'est là que ça devient intéressant pour les équipes. Les skills basées sur des classes dérivent de `AgentClassSkill<T>` et utilisent des attributs comme `[AgentSkillResource]` et `[AgentSkillScript]` pour que le framework découvre tout par réflexion :

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

Le beau ici, c'est qu'une équipe peut packager ça en paquet NuGet. Vous l'ajoutez à votre projet, vous le mettez dans le builder, et ça fonctionne à côté de vos skills fichier sans coordination :

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Les deux skills apparaissent dans le system prompt de l'agent. L'agent décide laquelle utiliser en fonction de la conversation — pas de code de routage nécessaire.

## Skills inline : le pont rapide

Vous connaissez ce moment où une autre équipe construit exactement la skill dont vous avez besoin, mais elle ne sera pas prête avant le prochain sprint ? `AgentInlineSkill` est votre pont :

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

Ajoutez-la au builder comme les autres :

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Quand le paquet NuGet sort enfin, vous échangez la skill inline contre la version classe. L'agent ne voit pas la différence.

Les skills inline ne sont pas que pour les ponts. Elles sont aussi le bon choix quand vous devez générer des skills dynamiquement à l'exécution — pensez à une skill par unité métier chargée depuis la config — ou quand un script doit capturer un état local qui n'a pas sa place dans un conteneur DI.

## Approbation de scripts : l'humain dans la boucle

Pour nous développeurs .NET qui construisons des agents de production, c'est la partie qui débloque vraiment les discussions de déploiement. Certains scripts ont des conséquences réelles — inscrire quelqu'un à des avantages, interroger l'infrastructure de production. Activez `UseScriptApproval` et l'agent se met en pause avant d'exécuter tout script :

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Quand l'agent veut exécuter un script, il retourne une demande d'approbation à la place. Votre app collecte la décision — approuver ou rejeter — et l'agent continue en conséquence. Dans les environnements réglementés, c'est la différence entre "on peut déployer ça" et "le juridique dit non."

## Pourquoi cette combinaison compte

Le vrai pouvoir n'est pas dans un pattern individuel — c'est dans la composition. Vous pouvez :

- **Commencer petit** avec une skill fichier, itérer sur les instructions et la publier sans écrire de C#
- **Distribuer des skills réutilisables** comme paquets NuGet que d'autres équipes ajoutent en une ligne
- **Combler les lacunes** avec des skills inline quand vous avez besoin de quelque chose *maintenant*
- **Filtrer les répertoires partagés** avec des prédicats pour que votre agent ne charge que ce qu'il doit
- **Ajouter une supervision humaine** pour les scripts qui touchent les systèmes de production

Tout cela se compose via `AgentSkillsProviderBuilder`. Pas de routage spécial, pas de logique conditionnelle, pas de vérifications de type de skill.

## Pour conclure

Les agent skills en .NET ont maintenant un modèle d'authoring véritablement flexible. Que vous soyez un développeur solo qui prototype avec des skills fichier ou une équipe enterprise qui distribue des capacités packagées via NuGet, les patterns s'adaptent. Et le mécanisme d'approbation de scripts le rend prêt pour la production dans les environnements où vous avez besoin de ce checkpoint humain.

Consultez l'[annonce originale](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), la [documentation Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) sur Microsoft Learn et les [exemples .NET sur GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) pour vous lancer.
