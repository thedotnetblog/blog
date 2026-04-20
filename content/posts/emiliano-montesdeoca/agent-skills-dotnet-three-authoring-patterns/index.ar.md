---
title: "مهارات الوكلاء في .NET أصبحت مرنة بشكل حقيقي"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "يدعم Microsoft Agent Framework الآن ثلاث طرق لكتابة المهارات — الملفات والفئات والكود المضمّن — كلها مُجمَّعة عبر مزوّد واحد. إليك لماذا يهم هذا وكيف تستخدم كل نهج."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

إذا كنت تبني وكلاء مع Microsoft Agent Framework، فأنت تعرف الطريقة: تعرّف المهارات، توصّلها بمزوّد، وتترك الوكيل يقرر أيها يستدعي. الجديد هو *كيف* تؤلّف تلك المهارات — والقفزة في المرونة كبيرة.

يُقدّم التحديث الأخير ثلاثة أنماط مختلفة لتأليف مهارات الوكيل: **قائمة على الملفات**، **قائمة على الفئات**، و**محددة بالكود المضمّن**. تتوصل الثلاثة جميعاً بـ`AgentSkillsProviderBuilder` واحد، مما يعني أنك تستطيع المزج والمطابقة بدون منطق توجيه.

## المهارات القائمة على الملفات: نقطة البداية

المهارات القائمة على الملفات هي تماماً ما تبدو عليه — دليل على القرص مع ملف `SKILL.md` ونصوص برمجية اختيارية ومستندات مرجعية:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

يُعلن الـ frontmatter في `SKILL.md` اسم المهارة ووصفها، وقسم التعليمات يخبر الوكيل كيف يستخدم النصوص والمراجع.

تتوصل به عبر `SubprocessScriptRunner.RunAsync`:

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);
```

## المهارات القائمة على الفئات: الشحن عبر NuGet

هنا يصبح الأمر مثيراً للاهتمام بالنسبة للفرق. المهارات القائمة على الفئات تشتق من `AgentClassSkill<T>` وتستخدم سمات مثل `[AgentSkillResource]` و`[AgentSkillScript]`:

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

يمكن لفريق تعبئة هذا كحزمة NuGet. تضيفه إلى مشروعك، وتضعه في المنشئ، ويعمل جنباً إلى جنب مع مهاراتك القائمة على الملفات.

## المهارات المضمّنة: الجسر السريع

تلك اللحظة عندما يبني فريق آخر المهارة التي تحتاجها بالضبط لكنها لن تُشحن قبل sprint؟ `AgentInlineSkill` هو جسرك:

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: "1. اطلب معرف الموظف. 2. استخدم calculate-balance. 3. اعرض النتائج.")
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int remaining = HrDatabase.GetAnnualAllowance(employeeId, leaveType)
                      - HrDatabase.GetDaysUsed(employeeId, leaveType);
        return JsonSerializer.Serialize(new { employeeId, leaveType, remaining });
    });
```

عند شحن حزمة NuGet، تستبدل المهارة المضمّنة بالقائمة على الفئة. الوكيل لا يلاحظ الفرق.

## موافقة النصوص: human-in-the-loop

لمطوري .NET الذين يبنون وكلاء للإنتاج، هذا هو الجزء الذي يفتح محادثات النشر فعلاً. شغّل `UseScriptApproval` ليتوقف الوكيل قبل تنفيذ أي نص:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

## خلاصة

مهارات الوكلاء في .NET لديها الآن نموذج تأليف مرن حقاً. سواء كنت تبني نموذجاً أولياً بمهارات قائمة على الملفات أو ترسل إمكانات مُعبّأة عبر NuGet، تتكامل جميع الأنماط عبر `AgentSkillsProviderBuilder`.

اطلع على [الإعلان الأصلي](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) و[نماذج GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills).
