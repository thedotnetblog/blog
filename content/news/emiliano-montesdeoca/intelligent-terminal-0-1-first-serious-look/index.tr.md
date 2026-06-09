---
title: "Intelligent Terminal 0.1, yapay zekâya özgü bir shell deneyimine dair ciddi bir ilk deneme"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Intelligent Terminal 0.1, yerleşik bir agent paneli, hataları fark eden yardım, arka plan görevleri ve command palette üzerinden başlatılan agent akışları ekliyor. Hâlâ deneysel, ama yönü çok etkileyici."
tags:
  - Terminal
  - AI
  - GitHub Copilot
  - Developer Tools
  - Windows Terminal
---

> *Bu yazı otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

Terminalin, AI destekli geliştirmenin gerçekten faydalı hale gelmesi için en doğal yerlerden biri olduğunu düşünmeye devam ediyorum.

Bu yüzden **Intelligent Terminal 0.1**, deneysel haliyle bile ciddi bir duyuru gibi geliyor.

İlginç olan şey sadece "terminalde sohbet etmek" değil. Yerleşik entegrasyon şu unsurlardan oluşuyor:

- agent paneli
- hata algılama
- oturum yönetimi
- arka plan görevleri
- command palette üzerinden başlatılan agent aksiyonları

Bu, yan tarafa eklenmiş bir eklenti gibi değil, gerçek bir shell deneyimi gibi hissettirmeye başlıyor.

## Orijinal makale gerçek acı noktasını anlıyor

Orijinal gönderinin en iyi taraflarından biri, soyut bir AI iddiasıyla başlamaması.

Çok sıradan bir geliştirici deneyimiyle başlıyor:

> "**Hiç PowerShell komutu girip hata aldınız mı, sonra bunu kopyalayıp tarayıcıyı açıp yapıştırdınız mı ve düzeltmek için birkaç forum yazısı arasında mı gezindiniz?**"

Bu soru işe yarıyor çünkü acı verici derecede tanıdık.

Terminal bu tür küçük kesintilerle dolu.

Dolayısıyla AI bir yere girecekse, tam da bu kesintilerin yanına girmeli.

## Neden bu, çoğu terminal AI demosundan daha güçlü hissediliyor

Bunu ilginç yapan şey sadece bir agent olması değil.

Terminal deneyiminin, geliştiricilerin gerçekten nasıl çalıştığını merkeze alarak yeniden düşünülmesi:

- kalıcı bir agent yüzeyi
- shell çıktısından gelen context
- hata oluştuğunda hızlı yardım
- arka planda görev başlatma
- oturumları sürdürme
- giriş noktası olarak command palette

Bu, shell penceresine eklenmiş yüzen bir chatbot'tan çok daha kullanışlı bir workflow'a yakın.

## Buradaki asıl ürün agent paneli

Tasarımda en önemli kısmı seçmem gerekseydi, muhtemelen agent paneli olurdu.

Neden? Çünkü iki rahatsız edici mod arasında bir orta yol oluşturuyor:

- terminali tamamen terk etmek
- ya da tüm etkileşimi inline shell text içine sıkıştırmak

Bu iyi bir tasarım kararı.

Terminali bir çalışma yüzeyi olarak saygıyla ele alıyor ve aynı zamanda agent'a autocomplete'ten daha fazlası olabilmesi için yeterli alan veriyor.

## Hata algılama, değerin görünür hale gelmeye başladığı yer

Otomatik hata algılama da burada tam yerinde duran bir özellik.

Terminalin zaten context'i var.
Hata zaten olmuş durumda.
Ve geliştirici hâlâ flow'un içinde.

Bu da shell'i şu işler için en iyi yerlerden biri haline getiriyor:

- anında teşhis
- düzeltme önerileri
- hızlı yineleme
- mevcut ortamı terk etmeden devam eden akıl yürütme

Bu sihir değil. Sadece workflow'u doğru yere koymak.

## Benim görüşüm

Henüz erken, ama terminalde AI için şimdiye kadar gördüğüm en ikna edici yönlerden biri.

Sihir vaat ettiği için değil.
Geliştiricilerin shell içinde zaten nasıl çalıştığına yakın kaldığı için.

Ve bu yönde gelişmeye devam ederse, Microsoft araç portföyündeki en ilginç AI-native developer experience'lerden biri olabilir.

Orijinal gönderi: [Announcing Intelligent Terminal 0.1](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/)
