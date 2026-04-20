---
title: "Agent Skills in .NET Just Got Seriously Flexible"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "The Microsoft Agent Framework now supports three ways to author skills — files, classes, and inline code — all composed through a single provider. Here's why that matters and how to use each one."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

If you've been building agents with the Microsoft Agent Framework, you know the drill: you define skills, wire them into a provider, and let the agent figure out which one to invoke. What's new is *how* you author those skills — and the flexibility jump is significant.

The latest update introduces three distinct authoring patterns for agent skills: **file-based**, **class-based**, and **inline code-defined**. All three plug into a single `AgentSkillsProviderBuilder`, meaning you can mix and match without any routing logic or special glue code. Let me walk you through each one and when you'd reach for it.

## File-based skills: the starting point

File-based skills are exactly what they sound like — a directory on disk with a `SKILL.md` file, optional scripts, and reference documents. Think of it as the most straightforward way to give your agent new capabilities:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

The `SKILL.md` frontmatter declares the skill name and description, and the instructions section tells the agent how to use the scripts and references:

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

Then you wire it up with `SubprocessScriptRunner.RunAsync` for script execution:

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

The agent discovers the skill automatically and invokes the provisioning script when it needs to check account status. Clean and simple.

## Class-based skills: ship via NuGet

Here's where it gets interesting for teams. Class-based skills derive from `AgentClassSkill<T>` and use attributes like `[AgentSkillResource]` and `[AgentSkillScript]` so the framework discovers everything via reflection:

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

The beauty here is that a team can package this as a NuGet package. You add it to your project, drop it into the builder, and it works alongside your file-based skills with zero coordination:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Both skills show up in the agent's system prompt. The agent decides which one to use based on the conversation — no routing code needed.

## Inline skills: the quick bridge

You know that moment when another team is building exactly the skill you need, but it won't ship for a sprint? `AgentInlineSkill` is your bridge:

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

Add it to the builder just like the others:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

When the NuGet package eventually ships, you swap out the inline skill for the class-based one. The agent doesn't know the difference.

But inline skills aren't just for bridges. They're also the right choice when you need to generate skills dynamically at runtime — think one skill per business unit loaded from config — or when a script needs to close over local state that doesn't belong in a DI container.

## Script approval: human-in-the-loop

For us .NET developers building production agents, this is the part that actually unblocks deployment conversations. Some scripts have real consequences — enrolling someone in benefits, querying production infra. Flip on `UseScriptApproval` and the agent pauses before executing any script:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

When the agent wants to run a script, it returns an approval request instead. Your app collects the decision — approve or reject — and the agent continues accordingly. In regulated environments, this is the difference between "we can deploy this" and "legal says no."

## Why this combination matters

The real power isn't any single authoring pattern — it's the composition. You can:

- **Start small** with a file-based skill, iterate on the instructions, and ship it without writing C#
- **Ship reusable skills** as NuGet packages that other teams can add with one line
- **Bridge gaps** with inline skills when you need something *now*
- **Filter shared skill directories** with predicates so your agent only loads what it should
- **Add human oversight** for scripts that touch production systems

All of these compose through `AgentSkillsProviderBuilder`. No special routing, no conditional logic, no skill type checks.

## Wrapping up

Agent skills in .NET now have a genuinely flexible authoring model. Whether you're a solo developer sketching out a prototype with file-based skills or an enterprise team shipping packaged capabilities via NuGet, the patterns fit. And the script approval mechanism makes it production-ready for environments where you need that human checkpoint.

Check out the [original announcement](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) for the full walkthrough, the [Agent Skills documentation](https://learn.microsoft.com/en-us/agent-framework/agents/skills) on Microsoft Learn, and the [.NET samples on GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) to get hands-on.
