---
title: "Pull request'leri Visual Studio içinde incelemek tam da sevdiğim türden bir friksiyon azaltma"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio artık IDE'den çıkmadan pull request'leri baştan sona review edebiliyor. Bu küçük bir adım gibi görünebilir, ama gün boyu Visual Studio içinde yaşayan ekipler için gereksiz context switching'i ciddi şekilde azaltıyor."
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinalini [buradan]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}}) okuyabilirsiniz.*

Browser code review workflow'ünün çok büyük bir kısmını çok uzun süredir alıp götürüyor.

Bu yüzden Visual Studio'nun **IDE içinde uçtan uca pull request review** tarafına daha da ilerlediğini görmek beni çok mutlu ediyor.

Bu, büyük manşetler üretmeyebilecek ama günlük development'ı gerçekten iyileştirebilecek özelliklerden biri.

## Ana değer basit: daha az context switching

Review loop'unuzun bir kısmı IDE'de, bir kısmı browser'da yaşıyorsa friction birikir:

- PR'ı başka yerde aç
- değişiklikleri bir tool'da incele
- daha derin inceleme için solution'a geri dön
- comment ya da approve için tekrar geçiş yap

Bu katastrofik değil. Sadece verimsiz.

Visual Studio size aynı çalışma ortamından PR açma, inceleme, yorum yapma, onaylama ve merge etme imkânı verirse, bu gerçek bir productivity win olur.

## "checkout yapmadan review" seçeneği özellikle güzel

Özellikle hoşuma giden bir şey, PR branch'ini checkout etmeden review yapabilmek.

Küçük görünebilir ama şunlar için mükemmel:

- hızlı review pass'leri
- interrupt-driven feedback istekleri
- mevcut branch ve local state'i olduğu gibi korumak

Bu, iyi code review araçlarının tam olarak ihtiyaç duyduğu esneklik.

## Benim görüşüm

Bu devrimsel bir özellik değil.

Daha iyisi: pratik bir özellik.

Günün büyük kısmını Visual Studio'da geçiren ekipler için PR review desteğini sıkılaştırmak, workflow breaks'i azaltır ve incelemeden aksiyona giden yolu yumuşatır.

Bana göre bu, değerli bir iyileştirme.

Orijinal yazı: [Visual Studio'dan çıkmadan pull request review yapın](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)