---
title: "أين تستضيف وكلاء الذكاء الاصطناعي على Azure؟ دليل عملي للقرار"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "تُقدّم Azure ستة طرق لاستضافة وكلاء الذكاء الاصطناعي — من الحاويات الخام إلى Foundry Hosted Agents المُدارة بالكامل. إليك كيفية اختيار الخيار المناسب لعبء عمل .NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "azure-ai-agent-hosting-options-guide" >}}).*

إن كنت تبني وكلاء ذكاء اصطناعي بـ .NET في الوقت الراهن، ربما لاحظت شيئاً: ثمة *الكثير* من طرق استضافتها على Azure. Container Apps، وAKS، وFunctions، وApp Service، وFoundry Agents، وFoundry Hosted Agents — وكلها تبدو معقولة حتى تحتاج فعلاً إلى اختيار واحدة. نشرت Microsoft للتو [دليلاً شاملاً لاستضافة وكلاء Azure AI](https://devblogs.microsoft.com/all-things-azure/hostedagent/) يوضّح هذا الأمر، وأريد تحليله من منظور مطوّر .NET عملي.

## الخيارات الستة في لمحة

إليك كيف أُلخّص المشهد:

| الخيار | الأنسب لـ | أنت تُدير |
|--------|----------|------------|
| **Container Apps** | التحكم الكامل في الحاويات دون تعقيد K8s | إمكانية المراقبة، الحالة، دورة الحياة |
| **AKS** | الامتثال للمؤسسات، متعدد المجموعات، شبكات مخصصة | كل شيء (هذا هو الهدف) |
| **Azure Functions** | المهام الوكيلة قصيرة الأمد المدفوعة بالأحداث | شبه لا شيء — خادم حقيقي بلا خوادم |
| **App Service** | وكلاء HTTP البسيطة، حركة المرور المتوقعة | النشر، إعداد التوسّع |
| **Foundry Agents** | وكلاء بدون كود عبر البوابة/SDK | شبه لا شيء |
| **Foundry Hosted Agents** | وكلاء بأُطر مخصصة مع بنية تحتية مُدارة | كود وكيلك فقط |

الخيارات الأربعة الأولى هي حوسبة للأغراض العامة — *يمكنك* تشغيل وكلاء عليها، لكنها لم تُصمَّم لذلك. الخياران الأخيران وكيل-أصيل: يفهمان المحادثات ومكالمات الأدوات ودورات حياة الوكلاء كمفاهيم أولى.

## Foundry Hosted Agents — النقطة الأمثل لمطوّري وكلاء .NET

ها هو ما لفت انتباهي. تقع Foundry Hosted Agents في المنتصف تماماً: تحصل على مرونة تشغيل كودك الخاص (Semantic Kernel، Agent Framework، LangGraph — ما تشاء) لكن المنصة تتولى إدارة البنية التحتية وإمكانية المراقبة وإدارة المحادثات.

القطعة الرئيسية هي **Hosting Adapter** — طبقة تجريد رفيعة تربط إطار وكيلك بمنصة Foundry. بالنسبة لـ Microsoft Agent Framework يبدو هكذا:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

هذه هي قصة استضافتك بالكامل. يتولى المحوّل ترجمة البروتوكول، والبثّ عبر server-sent events، وسجل المحادثات، وتتبع OpenTelemetry — كل ذلك تلقائياً. لا middleware مخصص، لا سباكة يدوية.

## النشر بسيط بشكل حقيقي

نشرت وكلاء إلى Container Apps من قبل وتعمل، لكنك تنتهي بكتابة الكثير من كود الربط لإدارة الحالة وإمكانية المراقبة. مع Hosted Agents وـ`azd`، يكون النشر:

```bash
# تثبيت إضافة وكلاء AI
azd ext install azure.ai.agents

# التهيئة من قالب
azd ai agent init

# بناء، رفع، نشر — انتهى
azd up
```

ذلك الأمر الواحد `azd up` يبني حاويتك، ويرفعها إلى ACR، ويُوفّر مشروع Foundry، ويُنشئ نقاط نهاية النماذج، ويُشغّل وكيلك. خمس خطوات في أمر واحد.

## إدارة المحادثات المدمجة

هذا الجانب هو الذي يُوفّر أكثر الوقت في الإنتاج. بدلاً من بناء مخزن حالة محادثة خاص بك، تتولى Hosted Agents ذلك بشكل أصيل:

```python
# إنشاء محادثة دائمة
conversation = openai_client.conversations.create()

# الدور الأول
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# الدور الثاني — السياق محفوظ
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

لا Redis. لا مخزن جلسات Cosmos DB. لا middleware مخصص لتسلسل الرسائل. المنصة تتولى الأمر ببساطة.

## إطاري للقرار

بعد مراجعة الخيارات الستة جميعها، إليك نموذجي الذهني السريع:

1. **هل تحتاج إلى بنية تحتية صفرية؟** ← Foundry Agents (بوابة/SDK، بلا حاويات)
2. **هل لديك كود وكيل مخصص لكنك تريد استضافة مُدارة؟** ← Foundry Hosted Agents
3. **هل تحتاج مهاماً وكيلة مدفوعة بالأحداث قصيرة الأمد؟** ← Azure Functions
4. **هل تحتاج أقصى تحكم في الحاويات دون K8s؟** ← Container Apps
5. **هل تحتاج امتثالاً صارماً ومتعدد المجموعات؟** ← AKS
6. **هل لديك وكيل HTTP بسيط بحركة مرور متوقعة؟** ← App Service

لمعظم مطوّري .NET الذين يبنون بـ Semantic Kernel أو Microsoft Agent Framework، من المرجح أن تكون Hosted Agents نقطة البداية الصحيحة. تحصل على التوسّع إلى الصفر، وOpenTelemetry المدمج، وإدارة المحادثات، ومرونة الإطار — دون إدارة Kubernetes أو تمديد سلسلة إمكانية مراقبة خاصة بك.

## خلاصة القول

مشهد استضافة الوكلاء على Azure ينضج بسرعة. إن كنت تبدأ مشروع وكيل ذكاء اصطناعي جديداً اليوم، أُوصي بجدية بالنظر في Foundry Hosted Agents قبل الوصول إلى Container Apps أو AKS من عادة. البنية التحتية المُدارة توفّر وقتاً حقيقياً، ونمط Hosting Adapter يتيح لك الحفاظ على اختيار إطارك.

اطّلع على [الدليل الكامل من Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) ومستودع [Foundry Samples](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) للحصول على أمثلة عملية.
