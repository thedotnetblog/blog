---
title: "خدمة Foundry Agent متاحة للعموم: ما يهمّ فعلاً لبنّائي وكلاء .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "أصبحت خدمة Foundry Agent من Microsoft متاحة للعموم مع دعم الشبكات الخاصة، وVoice Live، وتقييمات الإنتاج، وبيئة تشغيل متعددة النماذج ومفتوحة. إليك ما تحتاج إلى معرفته."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

لنكن صريحين — بناء نموذج أولي لوكيل ذكاء اصطناعي هو الجزء السهل. الجزء الصعب هو كل ما يأتي بعده: نقله إلى بيئة الإنتاج مع عزل الشبكة المناسب، وتشغيل تقييمات ذات معنى حقيقي، ومعالجة متطلبات الامتثال، وتجنّب الأعطال في الساعة الثانية صباحاً.

[خدمة Foundry Agent أصبحت الآن متاحة للعموم](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)، وهذا الإصدار مركّز تماماً على سدّ تلك الفجوة في "كل ما يأتي بعده".

## مبنية على Responses API

هذا هو العنوان الرئيسي: خدمة Foundry Agent من الجيل التالي مبنية على OpenAI Responses API. إذا كنت تبني بالفعل باستخدام هذا البروتوكول، فإن الهجرة إلى Foundry تستلزم تغييرات طفيفة في الكود. ما ستكسبه: أمان المؤسسات، والشبكات الخاصة، وEntra RBAC، والتتبع الكامل، والتقييم — فوق منطق وكيلك الحالي.

البنية مفتوحة عن قصد. لست مقيّداً بمزوّد نماذج واحد أو إطار تنسيق واحد. استخدم DeepSeek للتخطيط، وOpenAI للتوليد، وLangGraph للتنسيق — بيئة التشغيل تتولى طبقة الاتساق.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> إذا كنت قادماً من حزمة `azure-ai-agents`، فإن الوكلاء أصبحوا الآن عمليات من الدرجة الأولى على `AIProjectClient` في `azure-ai-projects`. أزل التبعية المنفصلة واستخدم `get_openai_client()` لتشغيل الاستجابات.

## الشبكات الخاصة: العقبة المؤسسية أُزيلت

هذه هي الميزة التي تفتح الطريق أمام تبنّي المؤسسات. تدعم Foundry الآن الشبكات الخاصة الكاملة من طرف إلى طرف مع BYO VNet:

- **لا خروج عام** — لا تلمس حركة مرور الوكيل شبكة الإنترنت العامة أبداً
- **حقن الحاوية/الشبكة الفرعية** في شبكتك للاتصال المحلي
- **اتصال الأدوات مشمول** — خوادم MCP، وAzure AI Search، ووكلاء بيانات Fabric تعمل جميعها عبر مسارات خاصة

هذه النقطة الأخيرة بالغة الأهمية. لا تبقى طلبات الاستدلال فحسب خاصة — كل استدعاء لأداة وكل طلب استرجاع يبقى داخل حدود شبكتك أيضاً. للفرق العاملة في ظل سياسات تصنيف البيانات التي تحظر التوجيه الخارجي، هذا هو ما كان مفقوداً.

## مصادقة MCP بالطريقة الصحيحة

تدعم اتصالات خادم MCP الآن الطيف الكامل من أنماط المصادقة:

| طريقة المصادقة | متى تستخدمها |
|----------------|--------------|
| مبنية على المفتاح | وصول مشترك بسيط للأدوات الداخلية على مستوى المؤسسة |
| Entra Agent Identity | من خدمة إلى خدمة؛ الوكيل يُصادق بهويته الخاصة |
| Entra Managed Identity | عزل على مستوى المشروع؛ لا إدارة لبيانات الاعتماد |
| OAuth Identity Passthrough | وصول مُفوَّض من المستخدم؛ الوكيل يعمل نيابةً عن المستخدمين |

OAuth Identity Passthrough هو الأكثر إثارةً للاهتمام. عندما يحتاج المستخدمون إلى منح وكيل حق الوصول إلى بياناتهم الشخصية — OneDrive الخاص بهم، أو مؤسسة Salesforce الخاصة بهم، أو واجهة برمجية SaaS مقيّدة بالمستخدم — يعمل الوكيل نيابةً عنهم من خلال تدفقات OAuth القياسية. لا هوية نظام مشتركة تتظاهر بأنها الجميع.

## Voice Live: الكلام إلى الكلام دون التعقيدات

كان إضافة الصوت إلى وكيل يعني سابقاً تجميع STT وLLM وTTS معاً — ثلاث خدمات، وثلاث نقاط تأخير، وثلاثة أسطح للفوترة، كلها متزامنة يدوياً. **Voice Live** يدمج ذلك كله في واجهة برمجية موحّدة مُدارة مع:

- الكشف الدلالي عن نشاط الصوت ونهاية الدور (يفهم المعنى، لا الصمت فحسب)
- قمع الضوضاء وإلغاء الصدى من جانب الخادم
- دعم المقاطعة (يمكن للمستخدمين المقاطعة في منتصف الاستجابة)

تمرّ تفاعلات الصوت عبر نفس بيئة تشغيل الوكيل كالنص. نفس المُقيِّمات، ونفس التتبعات، ونفس رؤية التكاليف. لسيناريوهات دعم العملاء، والخدمة الميدانية، أو إمكانية الوصول، يستبدل هذا ما كان يستلزم سابقاً خط أنابيب صوتياً مخصصاً.

## التقييمات: من مربّع اختيار إلى مراقبة مستمرة

هنا تأخذ Foundry جودة الإنتاج بجدية. يمتلك نظام التقييم الآن ثلاث طبقات:

1. **مُقيِّمات جاهزة للاستخدام** — التماسك، والصلة، والتأريض، وجودة الاسترجاع، والسلامة. اربطها بمجموعة بيانات أو حركة المرور الحية واحصل على النتائج.

2. **مُقيِّمات مخصصة** — شفّر منطقك التجاري الخاص، ومعايير النبرة، وقواعد الامتثال الخاصة بمجالك.

3. **التقييم المستمر** — تأخذ Foundry عيّنات من حركة مرور الإنتاج الحية، وتشغّل مجموعة مُقيِّماتك، وتعرض النتائج عبر لوحات المعلومات. اضبط تنبيهات Azure Monitor لحالات انخفاض التأريض أو خرق عتبات السلامة.

كل شيء يُنشر إلى Azure Monitor Application Insights. جودة الوكيل، وصحة البنية التحتية، والتكلفة، وتتبع التطبيق — كل ذلك في مكان واحد.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## ستة مناطق جديدة للوكلاء المستضافين

الوكلاء المستضافون متاحون الآن في East US وNorth Central US وSweden Central وSoutheast Asia وJapan East وغيرها. هذا مهم لمتطلبات إقامة البيانات ولضغط زمن الاستجابة عندما يعمل وكيلك قريباً من مصادر بياناته.

## لماذا يهمّ هذا مطوّري .NET

على الرغم من أن نماذج الكود في إعلان الإتاحة للعموم تُقدَّم بـ Python أولاً، فإن البنية التحتية الأساسية مستقلة عن اللغة — وحزمة .NET SDK الخاصة بـ `azure-ai-projects` تتبع نفس الأنماط. واجهة Responses API، وإطار التقييم، والشبكات الخاصة، ومصادقة MCP — كل هذا متاح من .NET.

إذا كنت تنتظر أن تنتقل وكلاء الذكاء الاصطناعي من "عرض توضيحي رائع" إلى "يمكنني فعلاً شحن هذا في العمل"، فإن إصدار الإتاحة للعموم هذا هو الإشارة. الشبكات الخاصة، والمصادقة المناسبة، والتقييم المستمر، ومراقبة الإنتاج — هذه هي القطع التي كانت مفقودة.

## خلاصة

خدمة Foundry Agent متاحة الآن. ثبّت حزمة SDK، وافتح [البوابة](https://ai.azure.com)، وابدأ البناء. [دليل البدء السريع](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) يأخذك من الصفر إلى وكيل عامل في دقائق.

للتعمق التقني الكامل مع جميع نماذج الكود، راجع [إعلان الإتاحة للعموم](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
