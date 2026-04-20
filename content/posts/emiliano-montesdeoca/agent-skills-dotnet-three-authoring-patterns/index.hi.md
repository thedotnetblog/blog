---
title: ".NET में Agent Skills अब काफी लचीली हो गई हैं"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework अब skills बनाने के तीन तरीके support करता है — files, classes, और inline code — सभी एक single provider के ज़रिए compose होते हैं। यह क्यों मायने रखता है और हर एक को कैसे use करें।"
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

अगर आप Microsoft Agent Framework के साथ agents बना रहे हैं, तो आप यह drill जानते हैं: skills define करें, उन्हें provider में wire करें, और agent को decide करने दें कि कौन-सी invoke करनी है। नया यह है कि आप उन skills को *कैसे* बनाते हैं — और flexibility में जो उछाल आई है वह काफी बड़ी है।

ताज़ा update agent skills के लिए तीन अलग authoring patterns introduce करता है: **file-based**, **class-based**, और **inline code-defined**। तीनों एक single `AgentSkillsProviderBuilder` में plug होते हैं, यानी आप बिना किसी routing logic या special glue code के mix और match कर सकते हैं। चलिए हर एक को walk through करते हैं और देखते हैं कि आप उसे कब choose करेंगे।

## File-based skills: शुरुआती बिंदु

File-based skills बिल्कुल वैसी ही हैं जैसी सुनाई देती हैं — disk पर एक directory जिसमें `SKILL.md` file, optional scripts, और reference documents हों। अपने agent को नई capabilities देने का यह सबसे सीधा तरीका है:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md` frontmatter skill का name और description declare करता है, और instructions section agent को बताता है कि scripts और references कैसे use करें:

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

फिर script execution के लिए `SubprocessScriptRunner.RunAsync` के साथ wire up करें:

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

Agent skill को automatically discover करता है और account status check करने की ज़रूरत पड़ने पर provisioning script invoke करता है। साफ और सरल।

## Class-based skills: NuGet के ज़रिए ship करें

Teams के लिए यहाँ दिलचस्प बात है। Class-based skills `AgentClassSkill<T>` से derive होती हैं और `[AgentSkillResource]` और `[AgentSkillScript]` जैसे attributes use करती हैं ताकि framework reflection के ज़रिए सब कुछ discover कर सके:

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

यहाँ खूबसूरती यह है कि एक team इसे NuGet package के रूप में package कर सकती है। आप इसे अपने project में add करें, builder में drop करें, और यह आपकी file-based skills के साथ बिना किसी coordination के काम करता है:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

दोनों skills agent के system prompt में दिखाई देती हैं। Agent conversation के आधार पर decide करता है कि कौन-सी use करनी है — कोई routing code नहीं चाहिए।

## Inline skills: त्वरित bridge

वह पल जब आप जानते हैं कि दूसरी team ठीक वही skill बना रही है जो आपको चाहिए, लेकिन वह एक sprint के लिए ship नहीं होगी? `AgentInlineSkill` आपका bridge है:

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

इसे दूसरों की तरह ही builder में add करें:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

जब NuGet package आखिरकार ship होगा, तो आप inline skill को class-based से swap कर देते हैं। Agent को फ़र्क नहीं पड़ता।

लेकिन inline skills सिर्फ bridge के लिए नहीं हैं। ये तब भी सही choice हैं जब आपको runtime पर dynamically skills generate करनी हों — config से load की गई हर business unit के लिए एक skill सोचें — या जब किसी script को local state पर close करना हो जो किसी DI container में नहीं जाती।

## Script approval: human-in-the-loop

Production agents बनाने वाले हम .NET developers के लिए, यह वह हिस्सा है जो deployment conversations को actually unblock करता है। कुछ scripts के real consequences होते हैं — किसी को benefits में enroll करना, production infra query करना। `UseScriptApproval` on करें और agent किसी भी script execute करने से पहले रुक जाता है:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

जब agent कोई script run करना चाहता है, तो वह approval request return करता है। आपकी app decision collect करती है — approve या reject — और agent उसी के अनुसार continue करता है। Regulated environments में, यही फ़र्क है "हम इसे deploy कर सकते हैं" और "legal ने मना कर दिया" के बीच।

## यह combination क्यों मायने रखता है

असली power कोई एक authoring pattern नहीं है — यह composition है। आप:

- **छोटे से शुरू कर सकते हैं** file-based skill से, instructions पर iterate करें, और बिना C# लिखे ship करें
- **Reusable skills ship कर सकते हैं** NuGet packages के रूप में जिन्हें दूसरी teams एक line से add कर सकती हैं
- **Gaps को bridge कर सकते हैं** inline skills से जब आपको *अभी* कुछ चाहिए
- **Shared skill directories को filter कर सकते हैं** predicates से ताकि आपका agent सिर्फ वही load करे जो उसे चाहिए
- **Human oversight add कर सकते हैं** उन scripts के लिए जो production systems को touch करती हैं

ये सभी `AgentSkillsProviderBuilder` के ज़रिए compose होते हैं। कोई special routing नहीं, कोई conditional logic नहीं, कोई skill type checks नहीं।

## Wrapping up

.NET में Agent skills के पास अब एक genuinely flexible authoring model है। चाहे आप file-based skills से prototype sketch करने वाले solo developer हों या NuGet के ज़रिए packaged capabilities ship करने वाली enterprise team, patterns fit हैं। और script approval mechanism इसे उन environments के लिए production-ready बनाता है जहाँ आपको वह human checkpoint चाहिए।

पूरे walkthrough के लिए [original announcement](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), Microsoft Learn पर [Agent Skills documentation](https://learn.microsoft.com/en-us/agent-framework/agents/skills), और hands-on होने के लिए [.NET samples on GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) देखें।
