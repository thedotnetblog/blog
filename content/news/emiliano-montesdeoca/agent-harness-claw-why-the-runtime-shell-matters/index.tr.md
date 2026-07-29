---
title: "Ajan Kabukları Önemlidir Çünkü Prompt'lar Yeterli Değildir"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "Yeni Microsoft Agent Framework claw ve harness anlatımı, gerçek ajanların model etrafında bir çalışma zamanı kabuğuna ihtiyaç duyduğunun faydalı bir hatırlatıcısı: araçlar, planlama, bellek, oturumlar ve pratik bir yürütme döngüsü."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Ajan geliştirmedeki en kolay hatalardan biri, prompt'un ürün olduğunu düşünmektir.

Değil.

Microsoft Agent Framework ekibinin yeni **agent harness ve claw** anlatımı değerli, çünkü odağı gerçekten bir ajanın kullanılabilir hissettirip hissettirmediğini belirleyen kısımda tutuyor: modelin etrafındaki çalışma zamanı kabuğu.

Buna şunlar dahil:

- araçlar
- planlama
- oturum durumu
- bellek
- yürütme modları
- yineleme için kullanılabilir bir konsol veya arayüz

Ajanların akıllı demolar olmaktan çıkıp yazılım gibi hissettirmeye başladığı yer burası.

## Harness deseni pratik bir desen

Burada beğendiğim şey, fikrin ne kadar yaklaşılabilir olduğu.

Bir sohbet istemcisiyle başlıyorsunuz.

Sonra onu talimatlar ve araçlarla bir harness'e sarıyorsunuz.

Ardından planlama, yapılacaklar listeleri, oturumlar ve akış (streaming) etkileşimi destekleyen bir kabuk üzerinden çalıştırıyorsunuz.

Bu sağlıklı bir desen çünkü sorumlulukları açıkça ayırıyor:

- model muhakemeyi yönetir
- harness çalışma zamanı davranışını yönetir
- uygulama hangi araçların ve deneyimlerin önemli olduğuna karar verir

## Bu, .NET geliştiricilerinin sistem kurma biçimiyle çok iyi örtüşüyor

Harness fikri, .NET zihniyetine de güzel şekilde denk düşüyor.

Çalışma zamanı davranışı açık ve birleştirilebilir olduğunda genellikle daha iyisini yapıyoruz. Ara katman yazılımları (middleware), boru hatları, seçenekler, sağlayıcılar ve adaptörler bu dünyada doğal hissettiriyor.

Bu yüzden Agent Framework'ün .NET geliştiricileriyle iyi bir uyum yakalama şansı yüksek diye düşünüyorum. Herkesi tek bir sihirli soyutlamaya zorlamıyor. Size birlikte bağlayabileceğiniz yapılandırılmış çalışma zamanı parçaları veriyor.

## Görüşüm

Bu yazının en yararlı kısmı, ajanların iyi bir model ve akıllı bir talimat dizesinden daha fazlasına ihtiyaç duyduğu hatırlatması.

Onlara yapı, bellek, araç erişimi, planlama ve kullanılabilir bir geliştirici döngüsü veren bir çalışma zamanı kabuğuna ihtiyaçları var.

Harness'in size verdiği tam olarak bu.

Ve dürüst olmak gerekirse, bu deseni takip etmeye değer olmasının nedeni de bu.

Orijinal yazı: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)
