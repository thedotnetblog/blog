---
title: "Azure Smart Tier Genel Kullanıma Açıldı — Yaşam Döngüsü Kuralları Olmadan Otomatik Blob Depolama Maliyet Optimizasyonu"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Blob Storage smart tier artık genel kullanıma açık; nesneleri gerçek erişim kalıplarına göre hot, cool ve cold katmanları arasında otomatik olarak taşıyor — yaşam döngüsü kurallarına gerek yok."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-smart-tier-blob-storage-ga" >}}).*

Azure Blob Storage yaşam döngüsü politikalarını ayarlamak için zaman harcadınız ve ardından erişim kalıpları değişince bunların çöktüğünü izlediyseniz, bu yazı sizin için. Microsoft, Azure Blob ve Data Lake Storage için [smart tier'ın genel kullanıma açıldığını](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) duyurdu — nesneleri gerçek kullanıma göre hot, cool ve cold katmanları arasında otomatik olarak taşıyan, tam yönetimli bir katmanlama özelliği.

## Smart tier aslında ne yapıyor

Konsept basit: smart tier, depolama hesabınızdaki her nesnenin son erişim zamanını sürekli değerlendiriyor. Sık erişilen veriler hot'ta kalıyor, etkin olmayan veriler 30 gün sonra cool'a geçiyor ve ardından 60 gün sonra cold'a iniyor. Verilere tekrar erişildiğinde hemen hot'a geri yükseltiliyor. Döngü yeniden başlıyor.

Yapılandırılacak yaşam döngüsü kuralı yok. Erişim kalıbı tahmini yok. Manuel ayarlama yok.

Önizleme sürecinde Microsoft, **smart tier tarafından yönetilen kapasitenin %50'sinden fazlasının gerçek erişim kalıplarına göre otomatik olarak daha soğuk katmanlara geçtiğini** bildirdi. Büyük depolama hesapları için bu anlamlı bir maliyet azalması.

## Bu .NET geliştiricileri için neden önemli

Günlük, telemetri, analitik veri veya büyüyen herhangi bir veri kümesi üreten uygulamalar geliştiriyorsanız — ki dürüst olmak gerekirse kim üretmiyor — depolama maliyetleri hızla artıyor. Geleneksel yaklaşım, yaşam döngüsü yönetim politikaları yazmak, bunları test etmek ve uygulamanızın erişim kalıpları değiştiğinde yeniden ayarlamaktı. Smart tier bu iş akışının tamamını ortadan kaldırıyor.

Bunun işe yaradığı pratik senaryolar:

- **Uygulama telemetrisi ve günlükleri** — hata ayıklama sırasında hot, birkaç hafta sonra nadiren erişilen
- **Veri pipeline'ları ve ETL çıktıları** — işleme sırasında yoğun erişim, ardından çoğunlukla cold
- **Kullanıcı tarafından oluşturulan içerik** — son yüklemeler hot, eski içerik zamanla soğuyor
- **Yedekleme ve arşiv verileri** — uyumluluk için ara sıra erişilen, çoğunlukla atıl

## Kurulum

Smart tier'ı etkinleştirmek tek seferlik bir yapılandırma:

- **Yeni hesaplar**: Depolama hesabı oluşturma sırasında varsayılan erişim katmanı olarak smart tier'ı seçin (bölgesel yedeklilik gereklidir)
- **Mevcut hesaplar**: Blob erişim katmanını mevcut varsayılandan smart tier'a geçirin

128 KiB'den küçük nesneler hot'ta kalır ve izleme ücretine tabi değildir. Diğer her şey için katman geçiş ücreti, erken silme ücreti ve veri alma maliyeti olmaksızın standart hot/cool/cold kapasite ücretleri ödüyorsunuz. Nesne başına aylık bir izleme ücreti orkestrasyon maliyetini karşılıyor.

## Bilmeniz gereken takas

Smart tier'ın katmanlama kuralları sabit (30 gün → cool, 90 gün → cold). Belirli bir iş yükü için 7 günde cool'a geçmek gibi özel eşikler ihtiyacınız varsa, yaşam döngüsü kuralları hâlâ doğru seçenek. İkisini de karıştırmayın: smart tier tarafından yönetilen nesnelerde yaşam döngüsü kurallarından kaçının, çünkü çakışabilirler.

## Sonuç

Bu devrim niteliğinde değil, ama gerçek bir operasyonel baş ağrısını çözüyor. Büyüyen blob depolama hesaplarını yönetiyorsanız ve yaşam döngüsü politikalarını korumaktan bıktıysanız, [smart tier'ı etkinleştirin](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-smart) ve Azure'un üstlenmesine izin verin. Neredeyse tüm bölgesel genel bulut bölgelerinde bugün itibariyle kullanılabilir.
