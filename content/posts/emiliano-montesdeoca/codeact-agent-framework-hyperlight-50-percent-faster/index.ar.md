---
title: "CodeAct في Agent Framework: كيف تخفض زمن استجابة وكيلك إلى النصف"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "يضغط CodeAct سلاسل الأدوات متعددة الخطوات في كتلة كود واحدة معزولة — يقلل زمن الاستجابة بنسبة 52% واستخدام الرموز بنسبة 64%."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائياً. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

في كل مشروع وكلاء، تأتي لحظة تنظر فيها إلى التتبع وتفكر: "لماذا يستغرق هذا كل هذا الوقت؟" النموذج جيد. الأدوات تعمل. لكن هناك سبع جولات ذهاباً وإياباً للحصول على نتيجة يمكن حسابها في مرة واحدة.

هذا بالضبط ما يحله CodeAct — و[فريق Agent Framework أصدر للتو دعماً تجريبياً](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) عبر حزمة `agent-framework-hyperlight` الجديدة.

## ما هو CodeAct؟

[نمط CodeAct](https://arxiv.org/abs/2402.01030) بسيط بأناقة: بدلاً من إعطاء النموذج قائمة من الأدوات لاستدعائها واحدة تلو الأخرى، تعطيه أداة `execute_code` واحدة وتتيح له التعبير عن *الخطة بأكملها* كبرنامج Python قصير.

| الأسلوب | الوقت | الرموز |
|--------|------|--------|
| التقليدي | 27.81 ث | 6,890 |
| CodeAct | 13.23 ث | 2,489 |
| **التحسن** | **52.4%** | **63.9%** |

## الأمان: الأجهزة الافتراضية الصغيرة Hyperlight

تستخدم حزمة `agent-framework-hyperlight` الأجهزة الافتراضية الصغيرة [Hyperlight](https://github.com/hyperlight-dev/hyperlight). كل استدعاء `execute_code` يحصل على جهاز افتراضي صغير خاص به تم إنشاؤه حديثاً. بدء التشغيل يُقاس بالمللي ثانية. العزل عملياً مجاني.

تستمر أدواتك في التشغيل على المضيف. الكود التوصيلي الذي يولده النموذج يعمل في بيئة مُعزلة. هذا هو التقسيم الصحيح.

## الإعداد الأدنى

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## متى تستخدم CodeAct (ومتى لا تستخدمه)

**استخدم CodeAct عندما:**
- تتضمن المهمة سلسلة من استدعاءات الأدوات الصغيرة (بحث، دمج، حسابات)
- زمن الاستجابة وتكلفة الرموز مهمان
- تريد عزلاً قوياً للكود الذي يولده النموذج

**ابقَ مع استدعاء الأدوات التقليدي عندما:**
- يُجري الوكيل استدعاءً أو اثنين فقط في كل دور
- لكل استدعاء آثار جانبية تستوجب موافقة فردية

## جرّبه الآن

```bash
pip install agent-framework-hyperlight --pre
```

اقرأ [المنشور الكامل في مدونة Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/).
