---
title: "Foundry'nin RFT'si Daha Ucuz ve Daha Akıllı Hale Geldi — İşte Neler Değişti"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry bu ay üç RFT güncellemesi gönderdi: o4-mini için global eğitim, yeni GPT-4.1 model grader'ları ve saatlerince hata ayıklamadan tasarruf etmenizi sağlayacak en iyi pratikler kılavuzu."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Fine-tune edilmiş modellere dayanan .NET uygulamaları geliştiriyorsanız, bu ayki Foundry güncellemeleri dikkat etmeye değer. Reinforcement Fine-Tuning daha erişilebilir ve önemli ölçüde daha ucuz hale geldi.

Tüm ayrıntılar [resmi duyuruda](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/) mevcut, ancak işte pratik özet.

## o4-mini için Global Eğitim

o4-mini, akıl yürütme ağırlıklı ve agentic iş yükleri için tercih edilen modeldir. Büyük haber: artık 13+ Azure bölgesinden fine-tuning işleri başlatabilirsiniz; Standart eğitime kıyasla daha düşük token başına eğitim maliyetiyle. Aynı altyapı, aynı kalite, daha geniş erişim.

Ekibiniz coğrafi olarak dağıtılmışsa bu önemlidir. Artık eğitim yapabilmek için birkaç bölgeyle sınırlı değilsiniz.

Global bir eğitim işi başlatmak için REST API çağrısı:

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

`trainingType: globalstandard` bayrağı temel farktır.

## Yeni Model Grader'lar: GPT-4.1 Ailesi

Grader'lar, modelinizin optimize ettiği ödül sinyalini tanımlar. Şimdiye kadar model tabanlı grader'lar daha küçük bir model setiyle sınırlıydı. Artık üç yeni seçenek var: GPT-4.1, GPT-4.1-mini ve GPT-4.1-nano.

Deterministik grader'lar yerine model grader'larına ne zaman başvurmalısınız? Görev çıktınız açık uçluysa, birden fazla boyutta kısmi puan almanız gerekiyorsa veya araç çağrısının doğruluğunun semantik bağlama bağlı olduğu agentic iş akışları oluşturuyorsanız.

Kademeli strateji pratik:

- İlk iterasyonlar için **GPT-4.1-nano**. Düşük maliyet, hızlı geri bildirim döngüleri.
- Grading rubric'iniz stabil olduğunda ve daha yüksek doğruluğa ihtiyaç duyduğunuzda **GPT-4.1-mini**.
- Üretim grading'i veya her puanlama kararının önemli olduğu karmaşık rubric'ler için **GPT-4.1**.

Tek bir RFT işinde grader türlerini bile karıştırabilirsiniz. "Doğru cevap" boyutu için string eşleşmesi ve akıl yürütme kalitesini değerlendirmek için model grader kullanın. Bu esneklik, gerçek iş yükleri için kullanışlı kılan şey.

## RFT Veri Formatı Tuzağı

Bu insanları tökezletiyor. RFT veri formatı SFT'den farklıdır. Her satırdaki son mesaj User veya Developer rolünde olmalıdır — Assistant değil. Beklenen cevap, grader'ın doğrudan referans aldığı `reference_answer` gibi üst düzey bir anahtara gider.

Denetimli fine-tuning yapıyorsanız ve RFT'ye geçmek istiyorsanız, eğitim verilerinizi yeniden yapılandırmanız gerekir. Bu adımı atlarsanız işleriniz sessizce başarısız olur.

## .NET Geliştiricileri İçin Neden Önemli?

Azure OpenAI SDK üzerinden fine-tune edilmiş modelleri .NET uygulamalarınızdan çağırıyorsanız, daha ucuz eğitim daha agresif iterasyon yapabileceğiniz anlamına gelir. Model grader seçenekleri, nüanslı görevler için fine-tuning yapabileceğiniz anlamına gelir — yalnızca tam eşleşme senaryoları için değil. [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md)'daki en iyi pratikler kılavuzu size gerçek hata ayıklama süresi kazandıracak.

Küçük başlayın. On ila yüz örnek. Basit grader. Döngüyü doğrulayın. Sonra ölçeklendirin.
