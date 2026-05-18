---
title: "Aspire 13.3: Kubernetes Desteği, Tarayıcı Günlükleri ve Aspireify Becerisi"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "13.2'den beş hafta sonra Aspire 13.3, ilk sınıf AKS dağıtımı, yapay zeka destekli ekleme becerisi, tarayıcı günlüğü yakalama ve yapılandırılmış komut sonuçlarını içeren 45 yeni özellikle geliyor."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Beş hafta bir sürüm için uzun bir süre değil, ancak Aspire 13.3 öyle hissettirmiyor. Ana öğeler önemli: Helm ile Kubernetes ve AKS birinci sınıf dağıtımı, Aspireify adlı ajan destekli ekleme becerisi, doğrudan panoda tarayıcı günlüğü yakalama ve yapılandırılmış komut sonuçları. Ayrıca 45 yeni özellik, 134 iyileştirme ve 93 hata düzeltmesi.

Öne çıkanlara geçelim.

## Aspireify: Ajan Destekli Ekleme

Mevcut bir projeye Aspire eklemek basit görünüyor — bir AppHost ekleyin, bitti. Pratikte çok fazla araştırma gerektirir: hangi portların önemli olduğu, hangi ortam değişkenlerinin gerçek bağımlılıklar olduğu, hangi Docker Compose hizmetlerinin Aspire entegrasyonlarıyla eşleştirilmesi gerektiği.

Yeni **Aspireify becerisi** kodlama ajanınıza tam da bunun için yönlendirilmiş bir iş akışı sağlar. `aspire init` bir iskelet AppHost oluşturduğunda, Aspireify becerisi ajanın depoyu incelemesine, nasıl çalıştığını anlamasına ve AppHost'u uygulamaya uyacak şekilde bağlamasına yardımcı olur — bunun tersi değil.

Varsayılan tutum "kodunuzdaki değişiklikleri en aza indirmek"tir. Uygulamanız zaten `DATABASE_URL` okuyorsa, ajan yapılandırmanızı yeniden yazmanızı istemek yerine bunu `WithEnvironment()` ile eşler. Bir port sabit kodlanmışsa, beceri ajana ne zaman koruması gerektiğini söyler.

Bu, inceleme için daha fazla iş oluşturmak yerine gerçekten zaman kazandıran yapay zeka araçlarının türüdür.

## Birinci Sınıf Kubernetes ve AKS Dağıtımı

Bu bir süredir istek listesindeydi. Aspire 13.3, **Helm ile Kubernetes ve AKS birinci sınıf dağıtım desteği** sunuyor. Artık Aspire araçlarından doğrudan AKS'i dağıtım hedefi olarak seçebilirsiniz.

AKS'de üretim iş yüklerini zaten çalıştıran ekipler için bu önemli bir boşluğu kapatıyor. Aspire uygulama modeliniz artık Helm grafikleri yazmak zorunda kalmadan yerel geliştirmeden Kubernetes'e temiz bir yola sahip.

## Panoda Tarayıcı Günlükleri

Bu, bir ön yüz sorununu hata ayıklayana kadar küçük görünen özelliklerden biri.

Yeni `WithBrowserLogs()` API'si herhangi bir endpoint özelliğine sahip kaynağa izlenen bir tarayıcı kaynağı ekler. Aspire, özel bir CDP borusu kullanarak Chromium'u başlatır ve konsol günlüklerini, ağ isteklerini ve hataları doğrudan kaynağın günlük akışına akıtır:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

TypeScript AppHost da aynısını destekler:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Konsol hataları, başarısız ağ istekleri, istemci tarafı istisnalar — hepsi zaten izleme ve metrikleri izlediğiniz aynı panoda görünür. Temel şeyler için tarayıcı DevTools'a sekme değiştirmeye artık gerek yok.

## Yapılandırılmış Komut Sonuçları

Kaynak komutları önemli bir yükseltme aldı. Şimdiye kadar komutlar başarı/başarısızlık döndürüyordu. Artık yapılandırılmış sonuçlar döndürüyorlar: model, pano kullanıcı arayüzü, CLI ve MCP araçları arasında akan metin, JSON veya Markdown.

Pano bunu başlıktaki yeni bir bildirim merkezi ile birbirine bağlar. Komut sonuçları, Markdown oluşturma ve "Yanıtı görüntüle" eylemiyle zaman damgalı bildirimler olarak görünür.

Bu, kaynak komutlarını gerçekten birleştirilebilir yapar. Bir entegrasyon artık yalnızca bir yerde durumu değiştirmek yerine — tünel URL'si gibi — anlamlı bir çıktı döndüren bir komut sunabilir.

## Sonuç

Aspire 13.3, yalnızca Kubernetes desteği için bile güncellemeye değer. Tarayıcı günlükleri ve yapılandırılmış komut sonuçları, günlük geliştirme iş akışında hızla biriken yaşam kalitesi iyileştirmeleri gibi hissettiriyor.

Tam sürüm notları: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
