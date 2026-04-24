---
title: "Foundry Toolboxes: نقطة نهاية واحدة لجميع أدوات وكلاء الذكاء الاصطناعي"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "أطلقت Microsoft Foundry ميزة Toolboxes في معاينة عامة — طريقة لإدارة أدوات وكلاء الذكاء الاصطناعي وعرضها عبر نقطة نهاية واحدة متوافقة مع MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

ثمة مشكلة تبدو عادية حتى تواجهها بنفسك: تبني المؤسسة وكلاء ذكاء اصطناعي متعددة، كل منها يحتاج أدوات، وكل فريق يُهيؤها من الصفر. نفس تكامل البحث على الويب، نفس إعداد Azure AI Search، نفس اتصال خادم GitHub MCP — لكن في مستودع مختلف، من فريق مختلف، ببيانات اعتماد مختلفة، ودون أي حوكمة مشتركة.

أطلقت Microsoft Foundry للتو [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) في معاينة عامة، وهو إجابة مباشرة على هذه المشكلة.

## ما هو Toolbox؟

Toolbox هو حزمة أدوات مُسمّاة وقابلة لإعادة الاستخدام، تُعرَّف مرة واحدة في Foundry وتُعرض عبر نقطة نهاية واحدة متوافقة مع MCP. أي بيئة تشغيل وكيل تتحدث MCP يمكنها استهلاكه — دون قيد على Foundry Agents.

الوعد بسيط: **build once, consume anywhere**. عرِّف الأدوات، هيِّئ المصادقة مركزيًا (OAuth passthrough، الهوية المُدارة في Entra)، انشر نقطة النهاية. كل وكيل يحتاج تلك الأدوات يتصل بنقطة النهاية ويحصل عليها جميعًا.

## الأركان الأربعة (اثنان متاحان اليوم)

| الركن | الحالة | ما يفعله |
|-------|--------|---------|
| **Discover** | قريبًا | إيجاد الأدوات المعتمدة دون بحث يدوي |
| **Build** | متاح | تجميع الأدوات في حزمة قابلة لإعادة الاستخدام |
| **Consume** | متاح | نقطة نهاية MCP واحدة تعرض جميع الأدوات |
| **Govern** | قريبًا | مصادقة مركزية + إمكانية مراقبة جميع استدعاءات الأدوات |

## مثال عملي

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="البحث في الوثائق والرد على issues في GitHub",
    tools=[
        {"type": "web_search", "description": "البحث في الوثائق العامة"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

بعد النشر، تُوفر Foundry نقطة نهاية موحدة. اتصال واحد، جميع الأدوات.

## لا قيد على Foundry Agents

تُنشأ Toolboxes وتُدار في Foundry، لكن سطح الاستهلاك هو بروتوكول MCP المفتوح. يمكن استخدامها من وكلاء مخصصة (Microsoft Agent Framework، LangGraph)، وGitHub Copilot وبيئات IDE الأخرى المتوافقة مع MCP.

## لماذا يهم هذا الآن

موجة الوكلاء المتعددة تصل إلى الإنتاج. كل وكيل جديد هو سطح جديد للإعداد المكرر والبيانات الاعتمادية القديمة والسلوك غير المتسق. أساس Build + Consume كافٍ للبدء في المركزة. حين يصل ركن Govern، ستتوفر طبقة أدوات قابلة للمراقبة الكاملة ومُتحكَّم بها مركزيًا لكامل أسطول الوكلاء.

## خلاصة

لا يزال مبكرًا — معاينة عامة، Python SDK أولًا، مع Discover وGovern في الطريق. لكن النموذج راسخ والتصميم الأصيل لـ MCP يعني أنه يعمل مع الأدوات التي تُبنى بالفعل. جميع التفاصيل في [الإعلان الرسمي](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/).
