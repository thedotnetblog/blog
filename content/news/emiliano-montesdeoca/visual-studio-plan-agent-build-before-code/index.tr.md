---
title: "Visual Studio'daki yeni Plan agent, çok gerçek bir AI iş akışı sorununu çözüyor"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "Visual Studio'nun yeni Plan agent'ı önemlidir çünkü uygulamadan önce yapılandırılmış bir planlama aşaması oluşturur; büyük özellikler ve refactor'lar genellikle tam da buna ihtiyaç duyar."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinalini [buradan]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}) okuyabilirsiniz.*

AI coding workflow'ündeki en sinir bozucu şeylerden biri, implementasyonun fazla hızlı başlamasıdır.

Kod teknik olarak gayet iyi bile olabilir, ama kafanızdaki problemin yanlış versiyonunu çözüyor olabilir.

Siz bir refactor istediniz. O bir rewrite başlattı.
Siz kapsamı dar bir iyileştirme istediniz. Projenin yarısına dokundu.
Siz seçenekleri konuşmak istediniz. Doğrudan file changes'a geçti.

İşte bu yüzden Visual Studio'daki yeni **Plan agent** çok kullanışlı bir ek.

## Bu, sadece kozmetik değil, gerçek bir workflow sorununu çözüyor

Orijinal yazı çok tanıdık bir durumu şöyle anlatıyor: "**Kod yanlış değil... sadece istediğiniz şey değil.**"

Bu cümle tam yerinde.

Çünkü AI-assisted development'daki zayıf nokta modelin kod üretip üretememesi değil. Asıl soru, workflow'un implementasyon başlamadan önce işin hedeflenen şekli üzerinde uzlaşmak için yeterli alan yaratıp yaratmadığıdır.

Bu özellikle şunlar için önemlidir:

- büyük features
- unfamiliar codebase'ler
- trivial olmayan refactor'lar
- architecture-sensitive değişiklikler
- editlere başlamadan önce team review gerektiren işler

Böyle durumlarda doğrudan implementasyona atlamak çoğu zaman yanlış harekettir.

## Görev gerçekse planlama overhead değildir

Takımların, implementasyona çok erken başlayarak ne kadar zaman kaybettiklerini bazen küçümsediğini düşünüyorum.

Eğer agent:

- yanlış file'lara dokunursa
- yanlış approach'u seçerse
- önemli bir constraint'i kaçırırsa
- gerekli bir edge case'i gözden kaçırırsa

"hızlı" başlangıç sonuçta daha yavaş bir workflow'a dönüşür.

Bu yüzden bu feature'ı seviyorum.

Şunlar için alan açıyor:

- açıklayıcı sorular
- plan taslağı hazırlama
- planı doğrudan düzenleme
- kod değişiklikleri başlamadan önce planı paylaşma

Bu bureaucracy değil. Çoğu zaman sadece iyi engineering'dir.

## Markdown plan file akıllıca bir tercih

Özellikle hoşuma giden bir detay, her planın `.copilot/plans/plan-{title}.md` içine kaydedilmesidir.

Bu, planning adımını somut hale getirir.

Plan chat transcript içinde sıkışıp kalmaz. Şunlara dönüşür:

- review etmek
- düzenlemek
- zihinsel olarak version'lamak
- takım arkadaşlarıyla tartışmak
- implementasyona daha bilinçli şekilde devretmek

Bu da feature'ı, code generation öncesindeki geçici bir önsözden çok daha ciddi hissettirir.

## AI workflow'leri burada takım sürecine saygı duymaya başlıyor

Bence bu, bu tool'ların olgunlaştığının daha güçlü işaretlerinden biri.

En iyi AI developer workflow'leri tüm ara adımları kaldıranlar değildir. Doğru ara adımları iyileştirenlerdir.

Planning de bu adımlardan biridir.

Plan güçlüyse implementasyon kolaylaşır.
Plan zayıfsa implementasyon gürültülü hale gelir.

Bu feature bunu doğrudan kabul ediyor.

## Benim görüşüm

Bu sadece bir AI nicety değil.

Bir workflow iyileştirmesi.

Ve gerçek features ile gerçek refactor'lar için, tam da gereksiz churn'ü, review noise'u ve "ben onu öyle demek istemedim" türü rework'ü azaltabilecek türden bir iyileştirme.

Giderek daha fazla agent experience'in eninde sonunda buna benzer bir şeye ihtiyaç duyacağını düşünüyorum.

Visual Studio buna daha erken ve kullanışlı bir şekilde ulaştı.

Orijinal yazı: [Yapmadan önce planlayın: Visual Studio'da Plan agent'ı tanıtıyoruz](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)