---
title: "KubeCon Europe 2026: ما يجب أن يهتم به مطورو .NET فعلاً"
date: 2026-03-29
author: "Emiliano Montesdeoca"
description: "أطلق Microsoft جداراً من إعلانات Kubernetes في KubeCon Europe 2026. إليك النسخة المفلترة — فقط تحديثات AKS والسحابة الأصلية المهمة إذا كنت تشحن تطبيقات .NET."
tags:
  - kubernetes
  - aks
  - azure
  - dotnet
  - cloud-native
  - ai
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "kubecon-2026-aks-updates-dotnet-developers" >}}).*

نشر Microsoft [ملخصه الكامل لـ KubeCon Europe 2026](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/).

## mTLS بدون ضريبة service mesh

[Azure Kubernetes Application Network](https://aka.ms/aks/application-network) يمنحك TLS المتبادل والتفويض الواعي بالتطبيق وبيانات تتبع حركة المرور — دون نشر شبكة كاملة ثقيلة بالحاويات الجانبية. واجهات برمجة ASP.NET Core تتحدث إلى العمال الخلفيين — كل شيء مشفر على مستوى الشبكة، بدون تغييرات في كود التطبيق.

## إمكانية مراقبة GPU

[AKS يعرض الآن مقاييس GPU بشكل أصلي](https://aka.ms/aks/managed-gpu-metrics) إلى Prometheus وGrafana المُدارَين. بدون مصدّرين مخصصين.

## شبكة متعددة العناقيد

Azure Kubernetes Fleet Manager يشحن الآن [شبكة متعددة العناقيد](https://aka.ms/kubernetes-fleet/networking/cross-cluster) — اتصال موحد وسجل خدمات عالمي.

## ترقيات أكثر أماناً

**ترقيات pool العوامل باللون الأزرق-الأخضر** تُنشئ pool عقد موازياً. **التراجع عن pool العوامل** يتيح العودة للإصدار السابق.

## من أين أبدأ

1. **إمكانية المراقبة أولاً** — فعّل مقاييس GPU وسجلات تدفق الشبكة
2. **جرّب ترقيات الأزرق-الأخضر** — اختبر سير عمل التراجع
3. **اختبر الشبكة الواعية بالهوية** — فعّل mTLS لمسار خدمة واحد
