---
title: "Foundry RFT Daha Ucuz ve Daha Akıllı Oldu — İşte Ne Değişti"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry bu ay üç RFT güncellemesi gönderdi: o4-mini için global eğitim, yeni GPT-4.1 model değerlendiriciler ve en iyi uygulamalar kılavuzu."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

İnce ayarlı modellere dayanan .NET uygulamaları geliştiriyorsanız, bu ayki Foundry güncellemeleri dikkat etmeye değer.

Tüm ayrıntılar [resmi duyuruda](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/) bulunabilir.

## o4-mini için Global Eğitim

o4-mini, ağır akıl yürütme ve ajantik iş yükleri için tercih edilen modeldir. Artık 13+ Azure bölgesinden ince ayar işleri başlatabilirsiniz.

```bash
"trainingType": "globalstandard"
```

## Yeni Model Değerlendiriciler: GPT-4.1 Ailesi

Üç yeni seçenek: GPT-4.1, GPT-4.1-mini ve GPT-4.1-nano.

Katmanlama stratejisi:
- **GPT-4.1-nano** ilk iterasyonlar için. Düşük maliyet, hızlı geri bildirim.
- **GPT-4.1-mini** değerlendirme rubrığı stabil olduğunda.
- **GPT-4.1** üretim değerlendirmesi için.

## RFT Veri Formatı Tuzağı

RFT veri formatı SFT'den farklı. Her satırdaki son mesaj User veya Developer rolünde olmalı — Assistant değil.

## .NET Geliştiricileri için Neden Önemli

Daha ucuz eğitim daha agresif iterasyon yapabileceğiniz anlamına geliyor. [GitHub'daki](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) en iyi uygulamalar kılavuzu gerçek hata ayıklama zamanı kazandıracak.
