---
title: ".NET 10'da NuGet package pruning, her yerde hissedilen türden bir iyileştirme"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10'daki yeni NuGet package pruning, false-positive vulnerability reports sayısını azaltır, restore graph'ı sadeleştirir ve restore performansını iyileştirir. Bu, günlük işi sessizce daha iyi yapan platform değişikliklerinden biridir."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *Bu makale otomatik olarak çevrildi. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Bazı platform iyileştirmeleri yeni senaryolar açtıkları için heyecan vericidir.

Diğerleri ise mevcut workflows'ları daha az gürültülü, daha az kırılgan ve daha az sinir bozucu hale getirdikleri için heyecan vericidir.

**.NET 10'daki NuGet package pruning** açıkça ikinci kategoriye giriyor ve bunu bir övgü olarak söylüyorum.

## Neden önemli

Eğer daha önce transitive vulnerability noise, gereksiz büyük restore graph'lar veya teknik olarak mevcut olup da uygulamanızın kullandığı runtime için aslında önemli olmayan package'larla uğraştıysanız, bu değişiklik gerçek bir pain point'e dokunuyor.

Pruning, runtime zaten sağlıyorsa platform-provided packages'i effective dependency graph'tan kaldırarak yardımcı olur.

Bu da şunları sağlar:

- daha az false-positive vulnerability reports
- daha temiz transitive dependency graphs
- daha az restore overhead
- daha actionable audit sonuçları

## Görüşüm

İşte tam da bu tür .NET iyileştirmelerini seviyorum.

Defaults'u iyileştirir, mental overhead'i azaltır ve hem security signal quality'yi hem de günlük tooling davranışını geliştirir.

Bu bir kazançtır, keynote slide'ına hiç çıkmasa bile.

Orijinal yazı: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
