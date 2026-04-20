---
title: "RFT في Foundry أصبح أرخص وأذكى — إليك ما الذي تغير"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "أصدر Microsoft Foundry ثلاث تحديثات RFT هذا الشهر: التدريب العالمي لـ o4-mini وتقييمات النماذج الجديدة GPT-4.1 ودليل أفضل الممارسات."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

إذا كنت تبني تطبيقات .NET تعتمد على نماذج دقيقة الضبط، فتحديثات Foundry هذا الشهر تستحق الانتباه.

التفاصيل الكاملة في [الإعلان الرسمي](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/).

## التدريب العالمي لـ o4-mini

o4-mini هو النموذج المفضل لأحمال العمل المكثفة بالاستدلال. يمكنك الآن إطلاق وظائف الضبط الدقيق من 13+ منطقة Azure بأسعار تدريب أقل.

```bash
"trainingType": "globalstandard"
```

## تقييمات نماذج جديدة: عائلة GPT-4.1

ثلاثة خيارات جديدة: GPT-4.1 وGPT-4.1-mini وGPT-4.1-nano.

استراتيجية التدرج:
- **GPT-4.1-nano** للتكرارات الأولية. تكلفة منخفضة، تغذية راجعة سريعة.
- **GPT-4.1-mini** عندما تستقر قواعد التقييم.
- **GPT-4.1** للتقييم في الإنتاج.

## فخ تنسيق بيانات RFT

تنسيق بيانات RFT مختلف عن SFT. يجب أن تكون الرسالة الأخيرة في كل صف بدور User أو Developer — ليس Assistant.

## لماذا يهم مطوري .NET

التدريب الأرخص يعني إمكانية التكرار بشكل أكثر عدوانية. سيوفر [دليل أفضل الممارسات على GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) وقتاً حقيقياً في التصحيح.
