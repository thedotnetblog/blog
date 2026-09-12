---
title: "Azure Functions Skills, Agentic Fonksiyonları Doğru Yola Sokmanın En Hızlı Yolu Olabilir"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Yeni azure-functions-skills önizlemesi ilginç çünkü kod iskeleti oluşturmaktan fazlasını yapıyor. Kod yazan ajanlara güncel desenler, yönetilen kimlik ve dağıtım farkında varsayılanlarla Azure Functions inşa etmeyi öğretiyor."
tags:
  - Azure Functions
  - AI
  - MCP
  - GitHub Copilot
  - Azure
---

Yapay zeka tarafından üretilen bulut kodundaki en yaygın sorunlardan biri, gerçeklikten hafifçe geride kalırken bile makul görünmesi.

Kod derleniyor. Fonksiyon dağıtılıyor. Örnek iyi görünüyor.

Sonra detayları fark ediyorsunuz:

- eski programlama modelleri
- projede sabit kodlanmış gizli diziler
- kötü ölçeklendirme seçimleri
- kimlik öncelikli olmayan tasarım
- dağıtım öncesi eksik doğrulama

**azure-functions-skills**'in bana yararlı görünmesinin tam nedeni bu.

Önizleme yalnızca başka bir iskelet oluşturma yardımcısı değil. Çok daha önemli bir sorunu çözmeye çalışıyor: kod yazan ajanların, iyi görünen ama operasyonel olarak eski ilk taslaklar yerine **güncel, varsayılan olarak güvenli Azure Functions çözümleri** üretmesini sağlamak.

## Kaynak yazı, başarısızlık modu konusunda ferahlatıcı derecede dürüst

Orijinal makalenin çok beğendiğim bir kısmı, sorun hakkında ne kadar doğrudan olması.

Genel ajanların genellikle "**sabit kodlanmış anahtarları, bağlantı dizelerini ve diğer gizli dizileri fonksiyonunuzda sizin daha sonra temizlemeniz için bıraktığını**" söylüyor.

Bu, böyle bir yazıda istediğim tam olarak türden bir cümle.

Çünkü boşluğun küçük olduğunu numara yapmak yerine gerçek sorunu adlandırıyor.

Bu, ajanların hiç kod yazıp yazamayacağıyla ilgili değil. Yazabiliyorlar.

Bu, **üretime uygun Azure kodu** yazıp yazamamalarıyla ilgili.

Bu farklı bir çıta.

## Gerçek değer, ajana daha iyi alışkanlıklar öğretmek

Beni etkileyen şey yalnızca kurulum komutu veya skill kataloğu değil.

Eklentinin ajana şunları vermesi fikri:

- güncel Azure Functions desenleri
- yönetilen kimlik varsayılanları
- Flex Consumption rehberliği
- Azure MCP şablon entegrasyonu
- dağıtım ve doğrulama skill'leri
- gönderim öncesi bir "doctor" geçişi

Bu önemli, çünkü birçok yapay zeka kod yazma başarısızlığı **genel kod üretimi** ile **platforma özgü doğruluk** arasındaki boşlukta gerçekleşiyor.

Ve ekiplerin zaman kaybettiği yer o boşluk.

## Bu neden zamanında görünüyor

Daha fazla ekip GitHub Copilot CLI, Claude Code, VS Code ve benzer akışları bulut uygulamaları inşa etmek için kullandıkça, eksik parça genellikle ham kod üretimi değil.

Bağlam.

Daha spesifik olarak:

- güncel barındırma modeli nedir?
- tercih edilen kimlik doğrulama hikâyesi nedir?
- bu platformda hangi desenler ölçeklenir?
- dağıtımdan önce ne doğrulanmalı?

Bu tam olarak "ajan skill'lerinin" soruna sadece daha büyük bir model atmaktan daha mantıklı hale gelmeye başladığı alanlar.

## `doctor` fikri özellikle akıllıca

Duyurudan seçmem gereken bir şey varsa, ekiplerin en çok takdir edeceğini düşündüğüm şey muhtemelen `doctor` komutu.

Kaynak yazı, kod kusurlarının ve yanlış yapılandırmanın dahili analizlerinde Azure Functions destek olaylarının "**yaklaşık %53**"ünü oluşturduğunu söylüyor.

Bu sayı önemli.

Çünkü platform ekibinin sadece acının nerede olduğunu tahmin etmediği anlamına geliyor. Çok somut bir başarısızlık deseni etrafında inşa ediyorlar.

Ve dürüst olmak gerekirse, bu daha çok güvendiğim türden bir ürün düşüncesi:

- en pahalı tekrarlayan hataları belirle
- dağıtımdan önce onları yakala
- iyi yolu kötü yoldan daha kolay hale getir

Geliştirici deneyimini anlamlı şekilde iyileştirmenin yolu bu.

## Hâlâ dikkatli olacağım şey

Yönü çok beğensem de, bunu hâlâ mühendislik muhakemesinin yerine geçen bir şey değil, bir üretkenlik katmanı olarak ele alırdım.

Ekiplerin kesinlikle şunları gözden geçirmesini isterdim:

- üretilen kimlik kurulumu
- herhangi bir altyapı varsayımı
- bağlama (binding) seçimleri
- depolama, kuyruklar ve gizli diziler etrafındaki güvenlik modeli
- `--deep` tarzı doğrulamanın CI kullanımı

İyi haber, aracın bu gerçekliği düşünerek tasarlanmış gibi görünmesi. Doğrulamayı gizlemiyor veya ajanın her şeyi bildiğini iddia etmiyor. Daha güvenli, rehberli bir şerit oluşturmaya çalışıyor.

Bu daha iyi bir başlangıç noktası.

## Görüşüm

Bu tam olarak daha yaygın hale gelmesini beklediğim türden araç katmanı.

Ajanların daha fazla heyecana ihtiyacı olduğu için değil, Azure Functions gibi gerçek platformları hedeflerken **daha iyi raylara** ihtiyaç duydukları için.

Bu önizlemenin en akıllı kısmı, ajanların yalnızca kod yazmasına yardımcı olmaması. Onların **güncel, Azure farkında, kimlik farkında, dağıtım farkında** kod yazmasına yardımcı olması.

Bu çok daha yararlı bir hırs.

Ve Azure üzerinde sunucusuz veya ajan destekli iş yükleri inşa eden ekipler için, bu önizlemeyi çok yakından izlemeye değer kılıyor.

Orijinal yazı: [Introducing azure-functions-skills: An AI-Era Workspace for Azure Functions (Preview)](https://devblogs.microsoft.com/azure-sdk/introducing-azure-functions-skills-ai-era-workspace/)
