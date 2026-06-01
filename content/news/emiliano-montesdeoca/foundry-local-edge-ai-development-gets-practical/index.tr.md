---
title: "Foundry Local, edge AI geliştirmeyi pratik hissettirmeye başlıyor"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "En son Foundry Local güncellemeleri dil desteğini, Linux ARM64 desteğini, iptal akışlarını ve Windows hızlandırmasını genişletiyor. Daha büyük hikâye ise yerel ve edge AI geliştirmeyi operasyonelleştirmenin giderek kolaylaşması."
tags:
  - Microsoft Foundry
  - Local AI
  - Edge AI
  - AI
  - Developer Tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Edge AI, onu paketlemek, çalıştırmak, optimize etmek ve gerçek donanımda desteklemek zorunda kalana kadar heyecan verici görünür.

Bu yüzden en yeni **Foundry Local** güncellemesi öne çıkıyor.

Sürüm, bir demoyu gerçekten dağıtılabilir bir şeye dönüştüren tam noktalarda desteği genişletiyor:

- çok dilli transcription
- Linux ARM64 desteği
- iptal desteği
- Windows ML iyileştirmeleri
- daha geniş donanım taşınabilirliği

## Kaynak makale doğru yerden başlıyor

Orijinal makalenin, geliştiricilerin zaten bildiği bir gerçeği kabul ederek başlamasını seviyorum:

> "**AI artık cloud deneyleriyle sınırlı değil.**"

Bu açık gibi görünebilir ama önemlidir, çünkü gereksinimleri değiştirir.

AI uygulamalara, edge sistemlerine, AI PC'lere ve düzenlenmiş ortamlara taşındığında, platform yalnızca inference erişiminden çok daha fazlasını çözmek zorunda kalır.

Şunları çözmek zorundadır:

- paketleme
- runtime farklılıkları
- donanım desteği
- iptal ve kontrol akışları
- deployment tutarlılığı
- gizlilik ve yerel yürütme kısıtları

İşte yerel AI ya gerçek mühendislik olur, ya da sadece hoş bir keynote fikri olarak kalır.

## Bu sürüm neden aspirational yerine pratik hissettiriyor

Burada takdir ettiğim şey, duyurunun beni büyük ve soyut bir vaatle etkilemeye çalışmaması.

Yerel AI'ı pratikte zor yapan parçaları tam da olması gerektiği gibi iyileştiriyor:

- canlı transcription'da daha fazla dil
- Linux ARM64 desteği
- SDK'lar genelinde iptal desteği
- WinML 2.0 ile daha basit Windows hızlandırması
- daha güçlü cihaz taşınabilirliği

Bu gösterişli değil.

Ama faydalı.

Ve faydalı olan şey, ekipleri deneyden ürüne gerçekten taşıyan şeydir.

## GitHub Copilot CLI ses örneği akıllı bir kanıt noktası

Özellikle hoşuma giden kısım, GitHub Copilot CLI voice input'unun Foundry Local üzerine kurulu olduğuna dair somut açıklamaydı.

Bu, "bakın neler mümkün" türü belirsiz bir demodan çok daha iyi.

Şunları gösteriyor:

- gerçek bir workflow
- gerçek bir ürün yüzeyi
- gerçek performans soruları
- yerel çalıştırmanın gerçek değeri

Bu, platform hikâyesini çok daha sağlam hissettiriyor.

## Gizlilik ve taşınabilirlik asıl uzun vadeli temalardır

En yakından takip edeceğim kısım tek bir API eklemesi değil.

Şu kombinasyon:

- gizlilik öncelikli yürütme
- donanım taşınabilirliği
- hibrit/yerel deployment desteği
- enterprise'a hazır kontrol

Bu kombinasyon, yerel AI'ı niş deneylerin ötesinde uygulanabilir kılıyor.

Çünkü pek çok workload için yerel hikâye sadece gecikme ile ilgili değildir. Kontrol ile ilgilidir.

## Benim görüşüm

Buradaki önemli değişim, yerel AI'ın artık özel bir durum gibi değil, gerçek bir mühendislik hedefi gibi görünmeye başlaması.

Bu, gizlilik, tepki süresi, donanım çeşitliliği ve cihaza daha yakın çalışan AI'ı önemseyen geliştiriciler için iyi bir haber.

Ve bu yüzden Foundry Local, genellikle "AI at the edge" duyurularının çoğundan daha fazla dikkat etmeyi hak ediyor.

Orijinal makale: [Accelerate Edge AI Development with Foundry Local](https://devblogs.microsoft.com/foundry/accelerate-edge-ai-development-with-foundry-local/)