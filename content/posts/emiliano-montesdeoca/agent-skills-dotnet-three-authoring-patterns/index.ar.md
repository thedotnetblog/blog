---
title: "مهارات الوكيل في .NET أصبحت أكثر مرونة من أي وقت مضى"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "يدعم Microsoft Agent Framework الآن ثلاث طرق لتأليف المهارات — ملفات، وفئات، وكود مضمّن — وكلها تُركَّب عبر مزوّد واحد. إليك لماذا يهمّ هذا وكيف تستخدم كل طريقة."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

إذا كنت تبني وكلاء باستخدام Microsoft Agent Framework، فأنت تعرف القاعدة: تعرّف المهارات، واربطها بمزوّد، واترك الوكيل يقرر أيّها يستدعي. الجديد هو *كيفية* تأليف تلك المهارات — وقفزة المرونة ملموسة.

يُقدّم التحديث الأحدث ثلاثة أنماط تأليف مميزة لمهارات الوكيل: **مستندة إلى الملفات**، و**مستندة إلى الفئات**، و**محدّدة بكود مضمّن**. الثلاثة تتوصّل بـ `AgentSkillsProviderBuilder` واحد، أي يمكنك المزج والتوفيق دون أي منطق توجيه أو كود ربط خاص. دعني أرشدك عبر كل واحدة ومتى تلجأ إليها.

## المهارات المستندة إلى الملفات: نقطة البداية

المهارات المستندة إلى الملفات هي بالضبط ما يوحي به اسمها — دليل على القرص بملف `SKILL.md`، وسكريبتات اختيارية، ومستندات مرجعية. فكّر في الأمر كأبسط طريقة لمنح وكيلك قدرات جديدة:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

تُعلن البيانات الأولية في `SKILL.md` اسم المهارة ووصفها، ويخبر قسم التعليمات الوكيلَ كيف يستخدم السكريبتات والمراجع:

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

ثم تربطها مع `SubprocessScriptRunner.RunAsync` لتنفيذ السكريبت:

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

يكتشف الوكيل المهارة تلقائياً ويستدعي سكريبت التزويد عند الحاجة إلى التحقق من حالة الحساب. نظيف وبسيط.

## المهارات المستندة إلى الفئات: الشحن عبر NuGet

هنا تصبح الأمور مثيرة للاهتمام للفرق. المهارات المستندة إلى الفئات تشتق من `AgentClassSkill<T>` وتستخدم سمات مثل `[AgentSkillResource]` و`[AgentSkillScript]` لكي يكتشف الإطار كل شيء عبر الانعكاس:

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

الجمال هنا أن فريقاً ما يمكنه تعبئة هذا كحزمة NuGet. تضيفها إلى مشروعك، وتُسقطها في المُنشئ، وتعمل جنباً إلى جنب مع مهاراتك المستندة إلى الملفات دون أي تنسيق:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

تظهر كلتا المهارتين في النص التوجيهي للنظام للوكيل. يقرر الوكيل أيّهما يستخدم بناءً على المحادثة — لا حاجة لكود توجيه.

## المهارات المضمّنة: الجسر السريع

تعرف تلك اللحظة حين يبني فريق آخر بالضبط المهارة التي تحتاجها، لكنها لن تُشحن لدورة تطوير كاملة؟ `AgentInlineSkill` هو جسرك:

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

أضفها إلى المُنشئ تماماً كالأخريات:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

حين تُشحن حزمة NuGet أخيراً، تستبدل المهارة المضمّنة بالمستندة إلى الفئات. الوكيل لا يلاحظ الفرق.

لكن المهارات المضمّنة ليست مجرد جسور. إنها أيضاً الخيار الصحيح حين تحتاج إلى توليد مهارات ديناميكياً في وقت التشغيل — فكّر في مهارة واحدة لكل وحدة عمل محمّلة من الإعداد — أو حين يحتاج سكريبت إلى الإغلاق على حالة محلية لا تنتمي إلى حاوية حقن التبعيات.

## موافقة السكريبت: الإنسان في الحلقة

لنا نحن مطوّري .NET الذين يبنون وكلاء في الإنتاج، هذا هو الجزء الذي يفتح محادثات النشر فعلاً. بعض السكريبتات لها عواقب حقيقية — تسجيل شخص ما في المزايا، أو الاستعلام عن البنية التحتية للإنتاج. فعّل `UseScriptApproval` ويتوقف الوكيل قبل تنفيذ أي سكريبت:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

حين يريد الوكيل تشغيل سكريبت، يُعيد طلب موافقة بدلاً من ذلك. تجمع تطبيقك القرار — موافقة أو رفض — ويستمر الوكيل وفقاً لذلك. في البيئات الخاضعة للتنظيم، هذا هو الفرق بين "يمكننا نشر هذا" و"الفريق القانوني يقول لا."

## لماذا يهمّ هذا التوليف

القوة الحقيقية ليست في أي نمط تأليف منفرد — بل في التركيب. يمكنك:

- **البدء صغيراً** بمهارة مستندة إلى ملفات، والتكرار على التعليمات، وشحنها دون كتابة C#
- **شحن مهارات قابلة لإعادة الاستخدام** كحزم NuGet تضيفها فرق أخرى بسطر واحد
- **سد الفجوات** بمهارات مضمّنة حين تحتاج شيئاً *الآن*
- **تصفية أدلة المهارات المشتركة** بمسندات حتى يحمّل وكيلك فقط ما ينبغي
- **إضافة رقابة بشرية** للسكريبتات التي تلمس أنظمة الإنتاج

كل هذه تتركّب عبر `AgentSkillsProviderBuilder`. لا توجيه خاص، ولا منطق شرطي، ولا فحوصات نوع المهارة.

## خلاصة القول

مهارات الوكيل في .NET أصبحت الآن تمتلك نموذج تأليف مرناً حقاً. سواء كنت مطوراً فردياً ترسم نموذجاً أولياً بمهارات مستندة إلى الملفات، أو فريق مؤسسة يشحن قدرات مُعبّأة عبر NuGet، فإن الأنماط تناسب الجميع. وآلية موافقة السكريبت تجعلها جاهزة للإنتاج في البيئات التي تحتاج فيها إلى تلك نقطة التفتيش البشرية.

اطّلع على [الإعلان الأصلي](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) للشرح الكامل، و[وثائق Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) على Microsoft Learn، و[أمثلة .NET على GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) للتطبيق العملي.
