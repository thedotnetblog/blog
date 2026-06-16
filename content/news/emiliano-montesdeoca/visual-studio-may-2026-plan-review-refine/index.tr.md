---
title: "Visual Studio'nun Mayıs güncellemesi aslında fikir ile değişiklik arasında daha iyi kontrolle ilgili"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "Visual Studio'nun Mayıs güncellemesi Plan agent, daha iyi skill yönetimi, context window görünürlüğü ve daha güçlü multi-file diff deneyimleri ekliyor. Ortak tema, AI-assisted inner loop üzerinde daha iyi kontrol."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinalini [buradan]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}}) okuyabilirsiniz.*

Visual Studio'nun Mayıs güncellemesindeki en ilginç şey tek bir izole özellik değil.

Ortak yön.

Bu sürüm, şu alanın arasını geliştirmeye devam ediyor:

- bir fikir
- bir plan
- üretilen bir değişiklik
- bir review
- rafine edilmiş bir sonuç

AI-assisted development'ın güvenilir mi yoksa kaotik mi hissedileceğine karar veren kısım tam da burası.

## Özellik listesi çeşitlidir ama niyet tutarlıdır

Kâğıt üzerinde bu sürüm bir sürü şey içeriyor:

- yeni Plan agent
- skill yönetimi iyileştirmeleri
- context window görünürlüğü
- multi-file summary diff
- Copilot ile ilgili workflow temizliği
- C++ tarafında MSVC güncellemeleri

Bu bir karma torba gibi görünebilir.

Bence öyle değil.

Ana çizgi oldukça açık: **Visual Studio, geliştiricilere AI-assisted işler üzerinde daha fazla control vermeye çalışıyor ama onları yavaşlatmak istemiyor.**

Bu, hedeflenmesi gereken tam doğru trade-off.

## Plan agent bu sürümün felsefi merkezidir

Diğer özellikler önemli olsa da, Plan agent'ın bu güncellemenin en açıklayıcı kısmı olduğunu düşünüyorum.

Bu, coding agent kullananların çoğunun hissettiği bir şeyi açık hale getiriyor:

hızlı başlamak, her zaman etkili ilerlemek demek değildir.

Sürüm, planning, review ve controlled implementation'ı daha doğal bir sıra haline getirerek bunu güçlendiriyor.

Bu sağlıklı.

## multi-file diff çalışması sessizce büyük bir iyileştirme

Multi-file summary diff'in de muhtemelen hak ettiğinden daha az kredi alacağını düşünüyorum.

Agent'ler aynı anda birden fazla file değiştirdiğinde, review experience aslında ürünün kendisi olur.

Değişiklikleri review etmek dağınık hissediyorsa, developer'lar workflow'a daha az güvenir.

Değişiklikleri review etmek tutarlı hissediyorsa, developer'lar aracı kullanmaya devam etme olasılığı daha yüksek olur.

Bu yüzden unified summary view çok önemlidir. Üretilen işe evet mi hayır mı diye karar vermenin cognitive cost'unu azaltır.

## context window indicator kulağa geldiğinden daha akıllı bir ekleme

Context kullanım göstergesini de seviyorum.

Küçük bir ayrıntı gibi gelebilir ama çok gerçek bir AI workflow problemine çözüm getiriyor: aracın konuşmanın önceki kısmını ne zaman unutmaya başlayacağını bilmemek.

Bunu görünür hale getirmek iyi bir design choice.

Model context'ini sihirli biçimde genişletmez. Ama sınırı gözlemlenebilir kılar; çoğu zaman bir sonraki en iyi şey budur.

## Benim görüşüm

Bu güncelleme aslında geliştiricilere AI-assisted loop üzerinde daha fazla görünürlük ve control vermekle ilgili.

Daha fazla novelty değil.
Daha fazla kaos değil.
Daha fazla control.

AI tools'u ciddi bir IDE workflow'u içinde daha güvenilir hissettirmek istiyorsanız, yatırım yapılacak doğru yer tam burasıdır.

Orijinal yazı: [Visual Studio'nun Mayıs güncellemesi — Plan, Review, Refine](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)