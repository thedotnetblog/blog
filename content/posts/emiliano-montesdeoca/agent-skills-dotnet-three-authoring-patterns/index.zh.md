---
title: ".NET的Agent Skills变得真正灵活了"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework现在支持三种创建技能的方式——文件、类和内联代码——全部通过单一provider组合。这篇文章解释为什么这很重要以及如何使用每种方式。"
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}})。*

如果你一直在用Microsoft Agent Framework构建代理，那你已经熟悉流程了：定义技能，连接到provider，让代理决定调用哪个。新的是你*如何*创建这些技能——灵活性的提升非常显著。

最新更新引入了三种agent skill编写模式：**基于文件的**、**基于类的**和**内联代码定义的**。三种都连接到单一的 `AgentSkillsProviderBuilder`，意味着你可以自由混搭，无需路由逻辑或特殊粘合代码。让我带你了解每种模式以及何时使用。

## 基于文件的技能：起点

基于文件的技能顾名思义——磁盘上的一个目录，包含 `SKILL.md` 文件、可选脚本和参考文档。给代理添加新能力最直接的方式：

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md` 的frontmatter声明技能名称和描述，指令部分告诉代理如何使用脚本和参考：

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

然后用 `SubprocessScriptRunner.RunAsync` 连接脚本执行：

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

代理自动发现技能并在需要检查账户状态时调用配置脚本。干净简单。

## 基于类的技能：通过NuGet分发

这里对团队来说变得有趣了。基于类的技能继承自 `AgentClassSkill<T>` 并使用 `[AgentSkillResource]` 和 `[AgentSkillScript]` 等属性，让框架通过反射发现一切：

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

妙处在于团队可以将其打包为NuGet包。你添加到项目中，放入builder，它就能和基于文件的技能一起工作，无需协调：

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

两个技能都出现在代理的系统提示中。代理根据对话决定使用哪个——不需要路由代码。

## 内联技能：快速桥接

你知道那个时刻吗，另一个团队正在构建你需要的技能，但要到下个sprint才能完成？`AgentInlineSkill` 就是你的桥梁：

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

和其他技能一样添加到builder：

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

当NuGet包最终发布时，你只需将内联技能替换为基于类的版本。代理不会注意到区别。

但内联技能不仅仅用于桥接。当你需要在运行时动态生成技能——想想从配置加载的每个业务单元一个技能——或者当脚本需要捕获不属于DI容器的本地状态时，它们也是正确的选择。

## 脚本审批：人在回路中

对我们构建生产代理的.NET开发者来说，这是真正打开部署讨论的部分。有些脚本有实际后果——给某人注册福利、查询生产基础设施。开启 `UseScriptApproval`，代理在执行任何脚本前会暂停：

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

当代理想执行脚本时，它会返回一个审批请求。你的应用收集决定——批准或拒绝——代理相应继续。在受监管的环境中，这就是"我们可以部署这个"和"法务说不行"之间的区别。

## 为什么这种组合很重要

真正的力量不在于任何单一模式——而在于组合。你可以：

- 用基于文件的技能**从小处开始**，迭代指令，不写C#就能发布
- 将**可复用的技能**作为NuGet包分发，其他团队一行代码就能添加
- 当*现在*需要某样东西时，用内联技能**填补空白**
- 用谓词**过滤共享目录**，让代理只加载应该加载的
- 为触及生产系统的脚本**添加人工监督**

这一切都通过 `AgentSkillsProviderBuilder` 组合。没有特殊路由，没有条件逻辑，没有技能类型检查。

## 总结

.NET中的agent skills现在拥有了真正灵活的编写模型。无论你是用基于文件的技能做原型的独立开发者，还是通过NuGet分发打包能力的企业团队，这些模式都能适配。脚本审批机制使其在需要人工检查点的环境中也能投入生产。

查看[原始公告](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/)、Microsoft Learn上的[Agent Skills文档](https://learn.microsoft.com/en-us/agent-framework/agents/skills)和GitHub上的[.NET示例](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills)开始动手吧。
