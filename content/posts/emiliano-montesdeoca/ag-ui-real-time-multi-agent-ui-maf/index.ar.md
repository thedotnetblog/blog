---
title: "بناء واجهات مستخدم للوكلاء المتعددة في الوقت الفعلي لا تبدو كصندوق أسود"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "يتحد AG-UI وإطار عمل Microsoft Agent لمنح سير العمل متعدد الوكلاء واجهة أمامية حقيقية — مع بث فوري، وموافقات بشرية، ورؤية كاملة لما يفعله وكلاؤك."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

إليك الحقيقة عن أنظمة الوكلاء المتعددين: تبدو رائعة في العروض التوضيحية. ثلاثة وكلاء يتبادلون العمل، يحلون المشكلات، يتخذون القرارات. ثم تحاول وضعها أمام المستخدمين الحقيقيين... صمت. مؤشر دوار. لا أحد يعرف أي وكيل يفعل ماذا أو لماذا توقف النظام. هذا ليس منتجًا — هذه مشكلة ثقة.

نشر فريق Microsoft Agent Framework للتو [دليلًا رائعًا](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) حول دمج سير عمل MAF مع [AG-UI](https://github.com/ag-ui-protocol/ag-ui)، وهو بروتوكول مفتوح لبث أحداث تنفيذ الوكلاء إلى الواجهة الأمامية عبر Server-Sent Events. وبصراحة؟ هذا هو الجسر الذي كنا بحاجة إليه.

## لماذا يهم هذا لمطوري .NET

إذا كنت تبني تطبيقات مدعومة بالذكاء الاصطناعي، فمن المحتمل أنك واجهت هذا الجدار. تنسيق الخلفية يعمل بشكل رائع — الوكلاء يحيلون العمل لبعضهم البعض، تعمل الأدوات، تُتخذ القرارات. لكن الواجهة الأمامية لا تعرف شيئًا عما يجري خلف الكواليس. يحل AG-UI هذا بتعريف بروتوكول قياسي لبث أحداث الوكلاء (`RUN_STARTED`، `STEP_STARTED`، `TOOL_CALL_*`، `TEXT_MESSAGE_*`) مباشرةً إلى طبقة واجهة المستخدم عبر SSE.

العرض التوضيحي الذي بنوه هو سير عمل دعم العملاء مع ثلاثة وكلاء: وكيل الفرز الذي يوجه الطلبات، ووكيل الاسترداد الذي يتعامل مع شؤون المال، ووكيل الطلبات الذي يدير عمليات الاستبدال. كل وكيل لديه أدواته الخاصة، وتوبولوجيا الإحالة محددة بوضوح — لا "استنتج من التعليمات".

## توبولوجيا الإحالة هي النجم الحقيقي

ما لفت انتباهي هو كيف يتيح `HandoffBuilder` الإعلان عن رسم بياني موجّه للتوجيه بين الوكلاء:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

كل `add_handoff` يُنشئ حافة موجّهة مع وصف باللغة الطبيعية. يُولّد الإطار أدوات الإحالة لكل وكيل بناءً على هذه التوبولوجيا. وبذلك تستند قرارات التوجيه إلى بنية التنسيق لديك، لا إلى ما يريد نموذج اللغة الكبير فعله. هذا أمر بالغ الأهمية لموثوقية الإنتاج.

## Human-in-the-loop الذي يعمل فعلًا

يعرض العرض التوضيحي نمطين للمقاطعة تحتاجهما أي تطبيق وكيل في العالم الحقيقي:

**مقاطعات موافقة الأدوات** — عندما يستدعي وكيل أداة محددة بـ `approval_mode="always_require"`، يتوقف سير العمل ويُصدر حدثًا. تعرض الواجهة الأمامية نافذة موافقة تحتوي على اسم الأداة والوسائط. لا حلقات إعادة المحاولة التي تستهلك الرموز — مجرد تدفق نظيف من التوقف والموافقة والاستئناف.

**مقاطعات طلب المعلومات** — عندما يحتاج وكيل إلى سياق إضافي من المستخدم (مثل معرف الطلب)، يتوقف ويسأل. تعرض الواجهة الأمامية السؤال، يُجيب المستخدم، ويستأنف التنفيذ من حيث توقف تمامًا.

يُبث كلا النمطين كأحداث AG-UI قياسية، لذلك لا تحتاج الواجهة الأمامية إلى منطق مخصص لكل وكيل — فهي تعرض فقط أي حدث يصل عبر اتصال SSE.

## التوصيل بسيط بشكل مفاجئ

التكامل بين MAF وAG-UI هو استدعاء وظيفة واحدة:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

يُنشئ `workflow_factory` سير عمل جديد لكل خيط، لذا تحصل كل محادثة على حالة معزولة. يتعامل endpoint مع كل أعمال SSE تلقائيًا. إذا كنت تستخدم FastAPI بالفعل (أو يمكنك إضافته كطبقة خفيفة)، فهذا يكاد لا يتطلب أي جهد.

## رأيي

بالنسبة لنا كمطوري .NET، السؤال الفوري هو: "هل يمكنني فعل هذا بـ C#؟" إطار عمل Agent Framework متاح لـ .NET وPython، وبروتوكول AG-UI مستقل عن اللغة (إنه مجرد SSE). لذا، على الرغم من أن هذا العرض التوضيحي يستخدم Python وFastAPI، فإن النمط ينتقل مباشرةً. يمكنك توصيل ASP.NET Core minimal API بنقاط نهاية SSE وفق نفس مخطط أحداث AG-UI.

الاستنتاج الأكبر هو أن واجهات المستخدم متعددة الوكلاء أصبحت اهتمامًا من الدرجة الأولى، وليست فكرة لاحقة. إذا كنت تبني أي شيء يتفاعل فيه الوكلاء مع البشر — دعم العملاء، سير عمل الموافقة، معالجة المستندات — فإن هذا الجمع بين تنسيق MAF وشفافية AG-UI هو النمط الواجب اتباعه.

## خلاصة

AG-UI + Microsoft Agent Framework يمنحك أفضل ما في العالمين: تنسيق قوي متعدد الوكلاء في الخلفية ورؤية فورية في الواجهة الأمامية. لا مزيد من تفاعلات الوكيل كصندوق أسود.

اطلع على [الدليل الكامل](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) و[مستودع بروتوكول AG-UI](https://github.com/ag-ui-protocol/ag-ui) للتعمق أكثر.
