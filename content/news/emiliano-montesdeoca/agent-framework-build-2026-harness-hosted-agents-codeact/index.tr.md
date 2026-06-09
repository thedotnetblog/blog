---
title: "Agent Harness, Hosted Agents ve CodeAct: benim odaklanacağım Agent Framework güncellemesi bu"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Build 2026’deki Agent Framework duyurusu oldukça yoğun, ama en önemli başlıklar harness modeli, Foundry’de barındırılan hosted agents ve orkestrasyon yükünü azaltan CodeAct."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Build’deki büyük Agent Framework duyurusu çok şeyi kapsıyor, ama üç tema benim için hemen öne çıkıyor:

- **harness'in daha birinci sınıf bir runtime parçası haline gelmesi**
- **Foundry hosted agents'in production'a giden bir yol sunması**
- **CodeAct'in çok adımlı orkestrasyon yükünü azaltması**

Benim yakından izleyeceğim noktalar bunlar.

## Harness gerçek ağırlık merkezi haline geliyor

Kaynak yazı, harness'i modelin muhakemesinin gerçek yürütmeyle buluştuğu katman olarak tanımlıyor.

Bu doğru bir tanım ve bu yüzden bu kısmın birçok tekil özellik maddesinden daha önemli olduğunu düşünüyorum.

Bir ajan şunlara ihtiyaç duymaya başladığında:

- dosya erişimi
- shell çalıştırma
- planlama modları
- yapılacaklar
- oturum belleği
- onay iş akışları

artık sadece bir prompt ve modelden bahsetmiyorsunuz.

Runtime davranışından bahsediyorsunuz.

Framework'ler ya gerçekten faydalı hale gelir ya da oyuncak olarak kalır; fark tam da burada ortaya çıkar.

Ve Microsoft Agent Framework açıkça tam bu katmanda daha faydalı hale gelmeye çalışıyor.

## Hosted agents, yerelden production'a geçiş hikayesinin gerçekten önem kazandığı yer

Hosted agents kısmının da duyurunun stratejik olarak en önemli bölümlerinden biri olduğunu düşünüyorum.

Kaynak yazı, bunun o agent'a production için bir yuva vermenin en kolay yolu olduğunu açıkça söylüyor.

Bu ifade önemli, çünkü çoğu agent framework hâlâ operasyonel dağıtımdan çok yerel deneylerde daha güçlü.

Foundry hosted agents yerel geliştirmeden şunlara geçişi ciddi biçimde kolaylaştırırsa:

- scaling
- observability
- managed identity
- session handling
- versioning

mevcut agent ekosistemindeki en büyük boşluklardan birini kapatır.

Bu anlamlı bir iyileştirme olur.

## CodeAct, güncellemedeki en heyecan verici teknik fikir

Postta en ilginç teknik konsepti seçmem gerekseydi, muhtemelen CodeAct'i seçerdim.

Çözmeye çalıştığı problem çok gerçek: Çok sayıda çok adımlı agent workflow pahalı hale geliyor, çünkü orkestrasyon döngüsünün kendisi çok fazla model turu tüketiyor.

Bu yüzden kaynak yazı şöyle bir sonuç gösterdiğinde:

- 52.4% faster
- 63.9% fewer tokens

hemen dikkatimi çekiyor.

Elbette bunlar temsilî bir iş yüküne bağlı benchmark sayıları, evrensel bir yasa değil. Ama daha büyük fikir yine de oldukça ikna edici.

Model tool-calling zincirini daha verimli bir yürütme biçimine sıkıştırabilirse, agent sistemlerinin ekonomisi epey değişebilir.

## Bence geliştiricilerin bu güncellemeden gerçekten çıkarması gereken şey

Önemli ders, kaç özellik çıktığı değil.

Asıl önemli olan, framework'ün gerçek uygulamaların en çok ihtiyaç duyduğu yerlerde güçlenmesi:

- runtime shell
- dağıtım yolu
- yürütme verimliliği
- yerleşik operasyonel kalıplar

Bu tür bir olgunluk sinyali, bir başka yüzeysel AI özellik listesinden çok daha değerlidir.

## Benim görüşüm

Bu güncelleme, yalnızca daha fazla yüzey alanı eklediği için önemli değil.

Ajanlar etrafındaki runtime ve deployment hikayesini, gerçek uygulamalar için önemli olması gereken biçimlerde güçlendiriyor; özellikle de yerel deneylerden gerçekten çalıştırılıp sürdürülebilecek sistemlere geçmek isteyen ekipler için.

Framework'ün daha ikna edici hale geldiği yer tam da burası.

Bu sürümü yakından takip edecek olsaydım, harness, hosted agents ve CodeAct kesinlikle en çok dikkat edeceğim alanlar olurdu.

Orijinal gönderi: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
