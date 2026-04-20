---
title: "Microsoft Foundry مارس 2026 — GPT-5.4 وإطلاق خدمة Agent وتحديث SDK الذي يغيّر كل شيء"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "تحديث Microsoft Foundry لمارس 2026 ضخم: خدمة Agent تصبح متاحة للعموم، GPT-5.4 يوفّر استدلالاً موثوقاً، حزمة azure-ai-projects SDK تصبح مستقرة عبر جميع اللغات، وFireworks AI تجلب النماذج المفتوحة إلى Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "microsoft-foundry-march-2026-whats-new" >}}).*

منشورات "ما الجديد في Microsoft Foundry" الشهرية عادةً مزيج من التحسينات التدريجية والميزة الرئيسية العَرَضية. [إصدار مارس 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)؟ إنه في الأساس كله ميزات رئيسية. خدمة Foundry Agent تصبح متاحة للعموم، وGPT-5.4 يُشحن للإنتاج، وSDK يحصل على إصدار مستقر رئيسي، وFireworks AI تجلب استدلال النماذج المفتوحة إلى Azure. دعني أُفصّل ما يهمّ مطوّري .NET.

## Foundry Agent Service جاهز للإنتاج

هذه هي الكبرى. بيئة تشغيل الوكلاء من الجيل التالي متاحة للعموم — مبنية على OpenAI Responses API، ومتوافقة مع وكلاء OpenAI على مستوى البروتوكول، ومفتوحة للنماذج من مزوّدين متعددين. إذا كنت تبني بواجهة Responses API اليوم، فإن الهجرة إلى Foundry تضيف أمان المؤسسات، والشبكات الخاصة، وEntra RBAC، والتتبع الكامل، والتقييم — فوق منطق وكيلك الحالي.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

الإضافات الرئيسية: شبكات خاصة شاملة من طرف إلى طرف، وتوسيع مصادقة MCP (بما في ذلك OAuth passthrough)، وVoice Live في مرحلة المعاينة للوكلاء الكلامية، ووكلاء مستضافون في 6 مناطق جديدة.

## GPT-5.4 — الموثوقية فوق الذكاء الخام

GPT-5.4 لا يتعلق بأن يكون أذكى. يتعلق بأن يكون أكثر موثوقية. استدلال أقوى عبر التفاعلات الطويلة، وامتثال أفضل للتعليمات، وإخفاقات أقل في منتصف سير العمل، وقدرات استخدام الحاسوب المدمجة. للوكلاء في الإنتاج، تلك الموثوقية أهم بكثير من نتائج المعايير المعيارية.

| النموذج | السعر (لكل مليون رمز) | الأفضل لـ |
|---------|----------------------|-----------|
| GPT-5.4 (≤272K) | $2.50 / $15 للمخرجات | وكلاء الإنتاج، البرمجة، سير عمل المستندات |
| GPT-5.4 Pro | $30 / $180 للمخرجات | التحليل المعمّق، الاستدلال العلمي |
| GPT-5.4 Mini | فعّال من حيث التكلفة | التصنيف، الاستخراج، استدعاءات الأدوات الخفيفة |

الحركة الذكية هي استراتيجية توجيه: GPT-5.4 Mini يتعامل مع العمل عالي الحجم ومنخفض الزمن بينما يتولى GPT-5.4 الطلبات المكثفة بالاستدلال.

## SDK مستقر أخيراً

حزمة `azure-ai-projects` SDK أصدرت إصدارات مستقرة عبر جميع اللغات — Python 2.0.0 وJS/TS 2.0.0 وJava 2.0.0 و.NET 2.0.0 (الأول من أبريل). تبعية `azure-ai-agents` اختفت — كل شيء يقع تحت `AIProjectClient`. ثبّت بـ `pip install azure-ai-projects` والحزمة تحزم `openai` و`azure-identity` كتبعيات مباشرة.

لمطوّري .NET، هذا يعني حزمة NuGet واحدة لكامل سطح Foundry. لا مزيد من إدارة حزم وكلاء منفصلة.

## Fireworks AI تجلب النماذج المفتوحة إلى Azure

ربما الإضافة الأكثر أهمية معمارياً: Fireworks AI تعالج أكثر من 13 تريليون رمز يومياً بـ ~180,000 طلب/ثانية، متاحة الآن عبر Foundry. DeepSeek V3.2 وgpt-oss-120b وKimi K2.5 وMiniMax M2.5 عند الإطلاق.

القصة الحقيقية هي **إحضار أوزانك الخاصة** — حمّل أوزاناً مُكمَّمة أو مضبوطة الضبط الدقيق من أي مكان دون تغيير منظومة التقديم. انشر عبر الدفع حسب الاستخدام أو الإنتاجية المخصصة.

## أبرز الإضافات الأخرى

- **Phi-4 Reasoning Vision 15B** — استدلال متعدد الوسائط للرسوم البيانية والمخططات وتخطيطات المستندات
- **Evaluations GA** — مُقيِّمات جاهزة للاستخدام مع مراقبة إنتاج مستمرة مُوصَلة إلى Azure Monitor
- **Priority Processing** (معاينة) — مسار حوسبة مخصص لأحمال العمل الحساسة لزمن الاستجابة
- **Voice Live** — بيئة تشغيل كلامية تتصل مباشرةً بوكلاء Foundry
- **Tracing GA** — فحص كامل لتتبعات الوكلاء مع الفرز والتصفية
- **إهمال PromptFlow** — الهجرة إلى Microsoft Framework Workflows بحلول يناير 2027

## خلاصة

مارس 2026 نقطة تحوّل لـ Foundry. إتاحة خدمة Agent للعموم، وحزم SDK مستقرة عبر جميع اللغات، وGPT-5.4 لوكلاء إنتاج موثوقين، واستدلال النماذج المفتوحة عبر Fireworks AI — المنصة جاهزة لأحمال العمل الجادة.

اقرأ [الملخص الكامل](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) و[ابنِ وكيلك الأول](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) للبدء.
