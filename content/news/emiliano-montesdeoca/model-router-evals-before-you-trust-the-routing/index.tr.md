---
title: "Model router evals, pek çok ekibin atladığı adımdır"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Foundry'deki yeni model router evaluation repo'su önemlidir çünkü routing kararlarının, otomatik model seçimini sihir gibi görmeden önce kalite, gecikme ve maliyet açısından ölçülmesi gerekir."
tags:
  - Microsoft Foundry
  - AI
  - Evaluations
  - Model Router
  - Cost Optimization
---

> *Bu makale otomatik olarak çevrildi. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Otomatik model routing kulağa harika gelir; ta ki bunun workload'unuz için doğru seçim olduğunu yine de kanıtlamanız gerektiğini fark edene kadar.

İşte bu yüzden yeni **model router evaluation repo** faydalıdır.

Ekiplerin gerçekten önemli olan sorulara daha somut cevaplar vermesini sağlar:

- routing kaliteyi koruyor mu?
- maliyeti iyileştiriyor mu?
- gecikmeye etkisi ne?
- model subset'i kısıtlarsam ne değişir?

## Kaynak makale doğru soruları soruyor

Orijinal yazıda en sevdiğim şeylerden biri, model router'ı kendiliğinden iyi kabul etmemesi.

Bunun yerine rahatsız edici ama doğru soruları soruyor:

- "**Prompt'larımda, model router'ın otomatik seçtiği model, aksi halde benim seçeceğim tek modelle eşleşiyor mu ya da onu geçiyor mu?**"
- "**Gerçekten uçtan uca para mı tasarruf ediyorum, yoksa sadece harcamayı bir yerden başka bir yere mi kaydırıyorum?**"

Bu tam olarak doğru tutum.

Çünkü otomatik routing çekici olsa da bu hâlâ bir system decision. Ve system decision'lar beğenilmemeli, ölçülmelidir.

## Bu repo ilk bakışta göründüğünden neden daha önemli

Bir düzeyde bu sadece bir evaluation repo'su.

Başka bir düzeyde ise olgunluk işaretidir.

Şunu söylüyor: otomatik routing'i benimsemek istiyorsanız, işte test etmek için daha disiplinli bir yol:

- kalite
- maliyet
- gecikme
- subset trade-off'ları
- model dağılım davranışı

Bu, routing'i iyi markalanmış bir black box gibi ele almaktan çok daha iyidir.

## Benim görüşüm

Bu, AI platform'ların daha fazlasına ihtiyaç duyduğu tooling türüne iyi bir örnek: daha fazla sihir değil, güvenmeden önce sihri doğrulamanın daha fazla yolu.

Ekiplerin test edilmemiş varsayımlar üzerinde pahalı güven inşa etmesini böyle önlersiniz.

Orijinal makale: [How to run evals for the model router](https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/)
