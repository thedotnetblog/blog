---
title: "تجميع الدبابيس أخيراً يصل إلى .NET MAUI Maps — خاصية واحدة، لا ألم"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 يضيف تجميع الدبابيس الأصلي إلى عنصر التحكم Map. خاصية واحدة، مجموعات تجميع منفصلة، ومعالجة النقر — كلها مدمجة."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "maui-maps-pin-clustering-finally" >}}).*

تعرف تلك اللحظة عندما تحمّل خريطة بمئة دبوس ويتحول كل شيء إلى كتلة غير قابلة للقراءة؟ هذا كان تجربة .NET MAUI Maps — حتى الآن.

David Ortinau [أعلن للتو](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) أن .NET MAUI 11 Preview 3 يشحن تجميع الدبابيس جاهزاً للاستخدام.

## خاصية واحدة لحكمهم جميعاً

```xml
<maps:Map IsClusteringEnabled="True" />
```

هذا كل شيء. تُجمَّع الدبابيس القريبة في مجموعات مع شارة العدد.

## مجموعات تجميع مستقلة

خاصية `ClusteringIdentifier` تتيح فصل الدبابيس إلى مجموعات مستقلة:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});
```

## معالجة النقر على المجموعة

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("
", e.Pins.Select(p => p.Label));
    await DisplayAlert($"Cluster ({e.Pins.Count} pins)", names, "OK");
};
```

## ابدأ الآن

ثبّت [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) وحدّث حمل عمل .NET MAUI.
