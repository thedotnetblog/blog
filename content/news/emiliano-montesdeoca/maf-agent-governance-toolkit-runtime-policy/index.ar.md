---
title: "بناء الوكلاء هو الجزء السهل — تشغيلهم بأمان هو الجزء الصعب"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "يتعاون Microsoft Agent Framework وAgent Governance Toolkit لتطبيق سياسات وقت التشغيل والتحكم في استدعاءات الأدوات وتوفير سجلات تدقيق مرتبطة بـ Merkle — دون المساس بمطالبات الوكيل."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

هناك نمط في تطوير وكلاء الذكاء الاصطناعي بدأت أسميه "ندم العرض التوضيحي". يعمل الوكيل بشكل رائع في العروض. ثم يسأل أحدهم: ماذا يحدث إذا استدعى الأداة الخاطئة؟ ماذا لو وصل إلى بيانات لا ينبغي له ذلك؟ من قام بمراجعة ذلك؟

يدعمك Microsoft Agent Framework في البناء والتنسيق. Agent Governance Toolkit (AGT) يغطي الجزء بعد ذلك — الحوكمة وتطبيق السياسات وقابلية التدقيق في وقت التشغيل.

## ما يفعله كل مشروع فعلياً

**Microsoft Agent Framework (MAF)** يوفر نموذج البرمجة: سير عمل متعدد الوكلاء، وإمكانية التشغيل البيني لبروتوكول A2A، وخطافات الوسيط، والذاكرة، والاستضافة المُدارة عبر Foundry Agent Service. يتعامل مع أمان المحتوى على مستوى إدخال/إخراج النموذج.

**Agent Governance Toolkit (AGT)** يتصل بنفس خط أنابيب الوسيط لإدارة *الإجراءات*. كل استدعاء أداة والوصول إلى الموارد والرسالة بين الوكلاء يتم تقييمها مقابل السياسة قبل التنفيذ. تكلفة إضافية أقل من ميلي ثانية. لا سيدكار، لا وكلاء، لا مطالبات معدلة.

```
إجراء الوكيل --> فحص السياسة --> سماح / رفض --> سجل التدقيق    (< 0.1 ms)
```

طبقات مختلفة، تغطية كاملة، خط أنابيب واحد.

## الاتصال مجرد إضافة وسيط

في Python، يضيف AGT إلى نفس معامل `middleware` الذي تستخدمه للتسجيل أو مرشحات المحتوى:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

في .NET، نفس النمط عبر `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

نفس الوكيل، نفس التنسيق، نفس الأدوات. يضيف AGT قدرات الحوكمة دون المساس بمنطق الوكيل.

## ما ستحصل عليه

- **GovernancePolicyMiddleware** — يقيّم كل إجراء مقابل قواعد السياسة التصريحية
- **CapabilityGuardMiddleware** — قائمة مسموح بها تحدد الأدوات التي يُسمح للوكيل باستدعائها (أداة `approve_small_loan` ليست في القائمة المسموح بها أعلاه — عن عمد)
- **RogueDetectionMiddleware** — يكتشف أنماط السلوك الشاذة في وقت التشغيل
- **AuditTrailMiddleware** — سجل تدقيق مرتبط بـ Merkle بحيث يكون كل إجراء محمياً تشفيرياً من التلاعب

الأخير مهم للامتثال. سلسلة Merkle تعني أنه إذا قام أحدهم بتعديل السجل، تنكسر السلسلة. التدقيق هو الدليل.

## خمسة سيناريوهات صناعية

يحتوي مستودع AGT على خمسة سيناريوهات كاملة من البداية إلى النهاية: الخدمات المالية (موظف القروض)، الرعاية الصحية (بيانات المرضى)، القانوني (مراجعة العقود)، الحكومة (خدمات المواطنين)، والتصنيع (مراقبة الجودة). كل منها يقرن وكلاء MAF الحقيقيين مع وسيط حوكمة AGT الحقيقي.

هذه ليست عروضاً تجريبية. هذه هي أنواع السيناريوهات التي ستحتاج فيها فعلاً إلى الحوكمة في الإنتاج.

## الخلاصة

إذا كنت تبني وكلاء يتعاملون مع بيانات حقيقية، ويتخذون قرارات ذات عواقب، أو يعملون دون مراقبة في الإنتاج — الحوكمة ليست اختيارية. مزيج MAF + AGT يمنحك المجموعة الكاملة: ابنه بـ Agent Framework، وحكمه بـ AGT.

كلا المشروعين مفتوحا المصدر. المقال الأصلي يحتوي على روابط لأمثلة الكود الكاملة.

المنشور الأصلي: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
