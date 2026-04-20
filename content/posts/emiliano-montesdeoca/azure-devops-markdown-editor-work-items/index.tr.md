---
title: "Azure DevOps Sonunda Herkesin Şikayet Ettiği Markdown Editörü UX'ini Düzeltiyor"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure DevOps iş öğeleri için Markdown editörü, önizleme ile düzenleme modu arasında daha net bir ayrım alıyor. Bu küçük bir değişiklik gibi görünse de gerçekten can sıkıcı bir iş akışı sorununu çözüyor."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-devops-markdown-editor-work-items" >}}).*

Azure Boards kullanıyorsanız, muhtemelen bunu yaşamışsınızdır: bir iş öğesi açıklamasını okuyorsunuz, belki kabul kriterlerini gözden geçiriyorsunuz ve yanlışlıkla çift tıklıyorsunuz. Bum — düzenleme modundasınız. Hiçbir şeyi düzenlemek istemiyordunuz. Sadece okuyordunuz.

Dan Hellem [düzeltmeyi duyurdu](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), ve bu, küçük gibi görünse de günlük iş akışınızdan gerçek sürtüşmeyi kaldıran değişikliklerden biri.

## Ne değişti

İş öğesi metin alanları için Markdown editörü artık varsayılan olarak **önizleme modunda** açılıyor. İçerikle okuyabilir ve etkileşime girebilirsiniz — bağlantıları takip etmek, biçimlendirmeyi gözden geçirmek — yanlışlıkla düzenleme moduna girme endişesi olmadan.

Gerçekten düzenlemek istediğinizde, alanın üstündeki düzenleme simgesine tıklarsınız. Bitirdiğinizde, açıkça önizleme moduna geri çıkarsınız.

## Neden göründüğünden daha önemli

Bu konudaki [topluluk geri bildirim dizisi](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) uzundu. Çift tıklama-düzenleme davranışı Temmuz 2025'te Markdown editörüyle tanıtıldı ve şikayetler neredeyse hemen başladı.

## Yayılım durumu

Bu zaten bir müşteri alt kümesine yayılıyor ve önümüzdeki iki ila üç hafta içinde herkese genişleyecek.
