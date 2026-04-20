---
title: "تجميع الدبابيس يصل أخيراً إلى خرائط .NET MAUI — خاصية واحدة، لا ألم"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 يضيف تجميع الدبابيس الأصيلي إلى عنصر التحكم Map. خاصية واحدة، ومجموعات تجميع منفصلة، ومعالجة النقر — كل ذلك مدمج."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "maui-maps-pin-clustering-finally" >}}).*

تعرف تلك اللحظة حين تحمّل خريطة بمئة دبوس ويتحول كل شيء إلى كتلة غير قابلة للقراءة؟ نعم، هذا كان تجربة .NET MAUI Maps — حتى الآن. لا مزيد من ذلك.

David Ortinau [أعلن للتو](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) أن .NET MAUI 11 Preview 3 يشحن تجميع الدبابيس جاهزاً للاستخدام على Android وiOS/Mac Catalyst. والجزء الأفضل — تفعيله سهل بشكل مدهش.

## خاصية واحدة لحكمهم جميعاً

```xml
<maps:Map IsClusteringEnabled="True" />
```

هذا كل شيء. تُجمَّع الدبابيس القريبة في مجموعات مع شارة العدد. قرّب الخريطة وتتمدد. ابتعد وتنضمّ. هذا النوع من السلوك الذي يتوقعه المستخدمون من أي خريطة حديثة — والآن تحصل عليه بخاصية واحدة.

## مجموعات تجميع مستقلة

هنا تصبح الأمور مثيرة للاهتمام. ليس كل الدبابيس يجب أن تتجمع معاً. المقاهي والحدائق أشياء مختلفة، ويجب أن تعرف خريطتك ذلك.

خاصية `ClusteringIdentifier` تتيح لك فصل الدبابيس إلى مجموعات مستقلة:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});

map.Pins.Add(new Pin
{
    Label = "Occidental Square",
    Location = new Location(47.6064, -122.3325),
    ClusteringIdentifier = "parks"
});
```

الدبابيس ذات المعرّف نفسه تتجمع معاً. المعرّفات المختلفة تُشكّل مجموعات مستقلة حتى عند التقارب الجغرافي. لا معرّف؟ المجموعة الافتراضية. واضح ومتوقع.

## معالجة النقر على المجموعة

حين ينقر مستخدم على مجموعة، تحصل على حدث `ClusterClicked` بكل ما تحتاجه:

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("\n", e.Pins.Select(p => p.Label));
    await DisplayAlert(
        $"Cluster ({e.Pins.Count} pins)",
        names,
        "OK");

    // Suppress default zoom-to-cluster behavior:
    // e.Handled = true;
};
```

تمنحك وسيطات الحدث `Pins` (الدبابيس في المجموعة)، و`Location` (المركز الجغرافي)، و`Handled` (اضبطها على `true` إذا أردت تجاوز التكبير الافتراضي). بسيط، عملي، تماماً ما تتوقعه.

## تفاصيل المنصة تستحق المعرفة

على Android، يستخدم التجميع خوارزمية شبكية مخصصة تُعيد الحساب عند تغيّر مستوى التكبير — دون تبعيات خارجية. على iOS وMac Catalyst، يستفيد من دعم `MKClusterAnnotation` الأصيل في MapKit، مما يعني حركات انتقال سلسة وأصيلة للمنصة.

هذه إحدى الحالات التي اتخذ فيها فريق MAUI القرار الصحيح — الاتكاء على المنصة حيث يكون ذلك منطقياً.

## لماذا يهمّ هذا

تجميع الدبابيس كان أحد أكثر الميزات المطلوبة في .NET MAUI ([المشكلة #11811](https://github.com/dotnet/maui/issues/11811))، ولسبب وجيه. كل تطبيق يعرض مواقع على خريطة — تتبع التوصيل، ومحدّدات المتاجر، والعقارات — يحتاج إلى هذا. سابقاً كان عليك بناؤه بنفسك أو استيراد مكتبة من جهة خارجية. الآن هو مدمج.

لنا نحن مطوّري .NET الذين نبني تطبيقات جوالة متعددة المنصات، هذا هو نوع تحسينات جودة الحياة الذي يجعل MAUI خياراً عملياً حقيقياً للسيناريوهات المكثفة باستخدام الخرائط.

## ابدأ الآن

ثبّت [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) وحدّث حمل عمل .NET MAUI. [نموذج Maps](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) يتضمن صفحة Clustering جديدة يمكنك تجربتها مباشرةً.

ابنِ شيئاً به — واترح خرائطك أخيراً.
