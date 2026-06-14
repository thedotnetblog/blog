---
title: "Microsoft Agent Framework'ün katmanlı tasarımı neden gerçekten önemli"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework'ün yeni katmanlı SDK açıklaması, mimari sohbetinden çok daha fazlası. Microsoft'un geliştiricilerin basit loop'lardan production-grade orchestration'a, her şeyi çöpe atmadan nasıl geçmesini istediğini gösteriyor."
tags:
  - Agent Framework
  - AI
  - .NET
  - Architecture
  - Developer Tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "index.md" >}}).

Framework duyuruları genelde özelliklerle başlar.

Bu duyuru **tasarım felsefesi** ile başladı ve bence onu önemli yapan da tam olarak bu.

Microsoft Agent Framework'ün **agent loops**, **workflows** ve **harnesses** etrafında nasıl yapılandığını anlatan yeni açıklama, başka bir özellik listesinden çok daha güçlü bir sinyal veriyor. Ekip, gerçek uygulamaların nasıl büyümesini beklediğini gösteriyor.

Ve .NET üzerinde agent geliştiren herkes için değerli kısım da bu.

## Çoğu agent uygulaması ilk mimarisini çok hızlı aşar

Bir model çağrısıyla başlarsın.

Sonra tools eklersin.

Sonra memory.

Sonra bir planner.

Sonra retries, telemetry, approvals, uzman agent'lar ve biraz workflow mantığı gelir; çünkü tek bir loop artık yetmez.

Birçok AI uygulamasının dağıldığı yer burası. İlk sürüm çalışıyordu, ama her yeni yetenek farklı bir soyutlama katmanından ekleniyordu.

Agent Framework yazısında hoşuma giden şey, katmanları açıkça göstermesi:

- **loops** temel yürütme döngüsü için
- **workflows** yapılandırılmış orchestration için
- **harnesses** agent etrafındaki yeniden kullanılabilir runtime yetenekleri için

İlk bakışta akademik gelebilir, ama çok pratik bir sorunu çözüyor: **uygulama karmaşıklaştıkça zihinsel modeli her seferinde yeniden yazmadan onu geliştirebilirsin**.

## harness kavramı özellikle önemli

Bence giderek daha önemli olacak tek bir parça seçmem gerekse, **harness** fikrini seçerdim.

Harness, agent geliştirme sürecinin prompting'den engineering'e dönüştüğü yerdir.

Bu katmanda şunları düşünmeye başlarsın:

- tools ve middleware
- planlama davranışı
- memory entegrasyonu
- observability
- controls ve governance
- tekrarlanabilir runtime davranışı

Bu tasarımın Microsoft stack'inin geri kalanıyla iyi uyum sağlamasının nedeni de bu. Foundry, governance araçları, hosted agents, evaluations ve tool ekosistemleri, modelin etrafındaki runtime shell birinci sınıf bir şey olarak ele alındığında çok daha anlamlı hale geliyor.

## Bu, .NET geliştiricileri için iyi bir işaret

Bu tür ekosistemlerde her zaman baktığım bir şey var: framework ilk demodan sonra hâlâ kullanışlı mı?

Katmanlı yaklaşım, Microsoft'un tüm yolculuğu düşündüğünü gösteriyor:

1. basit bir agent loop oluşturmak
2. karmaşa yaratmadan yapılandırılmış yetenekler eklemek
3. uygulama ihtiyaç duyduğunda daha resmi workflows'a geçmek
4. runtime'ı kurumsal sistemlerle entegre olacak kadar composable tutmak

Bu, "işte monolitik bir soyutlama, bol şans" yaklaşımından çok daha sağlıklı bir büyüme yolu.

Ve bu, .NET geliştiricilerinin genelde nasıl çalışmayı sevdiğiyle de çok uyumlu: katmanlı sistemler, açık composition, test edilebilir sınırlar ve güçlü runtime kontrolü.

## Benim bakışım

Bu yazıyı küçümsemek kolay, çünkü göz alıcı bir ekran görüntüsü ya da devasa bir API dökümü sunmuyor.

Ama böyle mimari notlar, bir framework'ün altı ay sonra ayakta kalıp kalmayacağını tahmin etmekte çoğu zaman daha iyidir.

Microsoft Agent Framework, model çağrılarının üstüne kurulmuş oyuncak bir sarıcı olmaktan çok daha fazlası olmaya çalışıyor. Katmanlı SDK hikâyesi, ekibin zor orta bölge için inşa ettiğini söylüyor: agent'ların orchestration, tools, runtime services ve production discipline'a ihtiyaç duyduğu yer.

Tam olarak ilgilendiğim yer de bu.

Orijinal yazı: [ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK]({{< ref "index.md" >}})
