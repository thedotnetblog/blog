---
title: "أين تستضيف وكلاء الذكاء الاصطناعي على Azure؟ دليل قرار عملي"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "يوفر Azure ستة طرق لاستضافة وكلاء الذكاء الاصطناعي — من الحاويات الخام إلى Foundry Hosted Agents المُدارة بالكامل. إليك كيف تختار المناسب لحمل عمل .NET الخاص بك."
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

إذا كنت تبني وكلاء ذكاء اصطناعي مع .NET الآن، ربما لاحظت شيئاً: هناك *الكثير* من طرق استضافتها على Azure. Container Apps وAKS وFunctions وApp Service وFoundry Agents وFoundry Hosted Agents.

نشرت Microsoft [دليلاً شاملاً لاستضافة وكيل Azure AI](https://devblogs.microsoft.com/all-things-azure/hostedagent/).

## نظرة سريعة على الخيارات الستة

| الخيار | الأفضل لـ | تُدير |
|--------|----------|-------|
| **Container Apps** | تحكم كامل بالحاوية دون تعقيدات K8s | المراقبة والحالة ودورة الحياة |
| **AKS** | امتثال المؤسسات، متعدد الكتل | كل شيء |
| **Azure Functions** | المهام القصيرة المدفوعة بالأحداث | شيء قليل جداً |
| **App Service** | وكلاء HTTP البسيطة | النشر والتوسع |
| **Foundry Agents** | وكلاء اختيارية الكود | لا شيء تقريباً |
| **Foundry Hosted Agents** | وكلاء بأطر مخصصة | كود وكيلك فقط |

## Foundry Hosted Agents — النقطة المثلى لمطوري وكلاء .NET

النشر بسيط فعلاً:

```bash
azd ext install azure.ai.agents
azd ai agent init
azd up
```

ذلك الأمر الواحد `azd up` يبني حاويتك، يدفعها إلى ACR، يهيئ مشروع Foundry، ويشغّل وكيلك.

## إطار قراري

1. **تريد صفر بنية تحتية?** → Foundry Agents
2. **لديك كود وكيل مخصص لكن تريد استضافة مُدارة?** → Foundry Hosted Agents
3. **مهام قصيرة مدفوعة بالأحداث?** → Azure Functions
4. **أقصى تحكم بالحاوية?** → Container Apps
5. **امتثال صارم ومتعدد الكتل?** → AKS

## خلاصة

لمعظم مطوري .NET الذين يبنون مع Semantic Kernel أو Microsoft Agent Framework، Hosted Agents هو على الأرجح نقطة البداية الصحيحة. تحقق من [الدليل الكامل من Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/).
