---
title: "Azure SDK أبريل 2026: AI Foundry 2.0 وما يجب أن يعرفه مطورو .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "إصدار Azure SDK لأبريل 2026 يشحن Azure.AI.Projects 2.0.0 المستقر مع تغييرات جوهرية كبيرة، وإصلاحات أمان حاسمة لـ Cosmos DB، وموجة من مكتبات Provisioning الجديدة لـ .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

غالبًا ما يمر إصدارات SDK الشهرية دون اهتمام. لكن هذا الإصدار يحتوي على بعض الأشياء التي تستحق الانتباه — خاصة إذا كنت تبني باستخدام AI Foundry أو Cosmos DB في Java أو تقوم بتوفير البنية التحتية من كود .NET.

## Azure.AI.Projects 2.0.0 — تغييرات جوهرية منطقية

حزمة NuGet `Azure.AI.Projects` تصل إلى الإصدار المستقر 2.0.0 مع بعض التغييرات المعمارية الهامة. إذا كنت تستخدم المعاينة بالفعل، إليك ما تغير:

- **تقسيم مساحات الأسماء**: Evaluations انتقلت إلى `Azure.AI.Projects.Evaluation`، وعمليات الذاكرة انتقلت إلى `Azure.AI.Projects.Memory`. عبارات using الخاصة بك ستحتاج إلى تحديث.
- **أنواع معاد تسميتها**: `Insights` ← `ProjectInsights`، `Schedules` ← `ProjectSchedules`، `Evaluators` ← `ProjectEvaluators`، `Trigger` ← `ScheduleTrigger`
- **اتفاقيات التسمية**: خصائص Boolean تتبع الآن اتفاقية `Is*` بشكل متناسق

هذه هي أنواع التغييرات الجوهرية التي تؤلم مرة واحدة ثم تبدو صحيحة إلى الأبد. إذا كنت تبني على المعاينة، حدث الاستيرادات الخاصة بك ودع المترجم يوجهك للباقي.

الخبر السار: إنه مستقر. يمكنك بالفعل الاعتماد على هذه API الآن.

## Cosmos DB Java: إصلاح أمان حاسم (RCE)

هذا جدي. مكتبة Java Cosmos DB (`azure-cosmos`) الإصدار 4.79.0 تتضمن إصلاح أمان حاسم لثغرة **تنفيذ تعليمات برمجية عن بعد (CWE-502)**.

المشكلة كانت إلغاء تسلسل Java في `CosmosClientMetadataCachesSnapshot` و `AsyncCache` و `DocumentCollection`. الإصلاح يستبدل إلغاء تسلسل Java بالتسلسل المستند إلى JSON، مما يلغي فئة كاملة من هجمات إلغاء التسلسل.

إذا كان لديك أي خدمات Java تستخدم Azure Cosmos DB، حدث إلى 4.79.0 فورًا. هذا ليس اختياريًا.

## مكتبات Provisioning جديدة لـ .NET

موجة من مكتبات Provisioning المستقرة وصلت إلى 1.0.0 هذا الشهر — هذه هي المكتبات التي تتيح لك تعريف البنية التحتية لـ Azure في كود C# بدلاً من قوالب ARM أو Bicep:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

العديد غيرها في beta.1، تغطي API Management و Batch و Compute و Monitor و MySQL و Security Center. إذا كنت تقوم بالبنية التحتية ككود من .NET — خاصة مع عمليات نشر Aspire — هذه المكتبات هي نقطة الدخول الخاصة بك.

## Azure AI Agents Java: 2.0.0 GA

مكتبة Java Azure AI Agents تصل أيضًا إلى التوفر العام هذا الشهر. التغييرات الجوهرية الرئيسية:

- عدة أنواع enum تم تحويلها إلى فئات قائمة على `ExpandableStringEnum` (أكثر مرونة للقيم الجديدة)
- فئات نموذج `*Param` أعيدت تسميتها إلى `*Parameter`
- `MCPToolConnectorId` ← `McpToolConnectorId` (حروف متسقة)
- تحميل زائد جديد مناسب لـ `beginUpdateMemories`

## خلاصة

العنوان الرئيسي لمطوري .NET هذا الشهر هو وصول `Azure.AI.Projects 2.0.0` إلى الاستقرار — إذا كنت تبني باستخدام AI Foundry، الآن هو الوقت لتثبيت الإصدار المستقر وتحديث الاستيرادات الخاصة بك. لمتاجر Java التي تستخدم Cosmos DB، التحديث الأمني عاجل.

ملاحظات الإصدار الكاملة في [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases). المقال الأصلي: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).