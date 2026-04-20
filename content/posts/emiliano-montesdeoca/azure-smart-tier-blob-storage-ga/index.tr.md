---
title: "Azure Smart Tier GA Oldu — Yaşam Döngüsü Kuralları Olmadan Otomatik Blob Storage Maliyet Optimizasyonu"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Blob Storage smart tier artık genel kullanıma açık, gerçek erişim düzenlerine göre nesneleri otomatik olarak hot, cool ve cold katmanları arasında taşıyor."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-smart-tier-blob-storage-ga" >}}).*

Azure Blob Storage yaşam döngüsü politikalarını ayarlamak için zaman harcadıysanız ve bunların erişim kalıpları değiştiğinde çöktüğünü izlediyseniz, bu sizin için. Microsoft, Azure Blob ve Data Lake Storage için [smart tier'ın genel kullanılabilirliğini](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) duyurdu.

## Smart tier ne yapıyor?

Smart tier, depolama hesabınızdaki her nesnenin son erişim zamanını sürekli değerlendirir. Sık erişilen veriler hot'ta kalır, etkin olmayan veriler 30 gün sonra cool'a, ardından 60 gün sonra cold'a taşınır. Veriye yeniden erişildiğinde, hemen hot'a geri alınır.

Yapılandırılacak yaşam döngüsü kuralı yok. Manuel ayarlama yok.

Önizleme sırasında Microsoft, **smart tier tarafından yönetilen kapasitenin %50'sinden fazlasının otomatik olarak daha soğuk katmanlara geçtiğini** bildirdi.

## .NET geliştiricileri için neden önemli

Pratik senaryolar:
- **Uygulama telemetrisi ve logları** — hata ayıklarken hot, birkaç hafta sonra nadiren erişilir
- **Veri pipeline'ları ve ETL çıktıları** — işleme sırasında yoğun erişim, sonra çoğunlukla cold
- **Kullanıcı tarafından oluşturulan içerik** — yeni yüklemeler hot, eski içerik yavaşça soğur

## Bilinmesi gereken takas

Smart tier'ın katmanlama kuralları statiktir (30 gün → cool, 90 gün → cold). Özel eşiklere ihtiyaç duyuyorsanız, yaşam döngüsü kuralları hâlâ geçerli. Smart tier tarafından yönetilen nesnelere yaşam döngüsü kuralları uygulamaktan kaçının.
