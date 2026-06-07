---
title: "VS Code 1.121: Favori Modelleri Sabitle, Terminal Çıktı Sıkıştırması, Ajan SSH"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 model favorileri, test çalıştırıcıları ve derleme araçları için genişletilmiş terminal çıktı sıkıştırması, arka plan terminalleri için boşta-sessizlik zamanlayıcısı ve agent host'ta klavye-etkileşimli SSH kimlik doğrulaması ekler."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121, 1.120'den Copilot ajan kalite iyileştirmelerini sürdürüyor; model yönetimi ve terminal davranışına odaklanıyor.

## Favori Modelleri Sabitle

Model seçici artık sabitlemeyi destekliyor. Her zaman aynı model ya da iki modele erişiyorsanız, bunları listenin en üstüne sabitleyin. Birden fazla sağlayıcıdan birçok modele erişiminiz olduğunda kaydırmayı azaltır.

## Genişletilmiş Terminal Çıktı Sıkıştırması

Ajan terminal aracı zaten ortak komutlar için çıktıyı sıkıştırıyordu. 1.121 bunu test çalıştırıcılarını ve derleme araçlarını kapsayacak şekilde genişletiyor:

- **Test çalıştırıcıları:** `pytest`, `jest`, `cargo test`
- **Derleme araçları:** `tsc`, `cargo build`, `make`
- **Linter'lar, Docker, paket yöneticileri**

Uzun derleme çıktıları ve test hata raporları modele iletilmeden önce ilgili alıntılara sıkıştırılır. Bu, ajan binlerce çıktı satırı üretebilecek derleme döngüleri veya test paketleri çalıştırdığında bağlam kullanımını yönetilebilir tutar.

## Arka Plan Terminalleri İçin Boşta-Sessizlik Zamanlayıcısı

`run_in_terminal` aracı için yeni bir boşta-sessizlik zamanlayıcısı: bir eşzamanlı komut yapılandırılabilir bir süre boyunca çıktı üretmezse, otomatik olarak arka plan yürütmesine yükseltilir. Bu, uzun süre çalışan komutların sessizce işlerken ajanı engellemesini önler. Daha sonra kontrol etmek için bir terminal ID'si alırsınız.

## VSCODE_AGENT Ortam Değişkeni

Copilot Chat terminalde komutlar çalıştırdığında, artık bir `VSCODE_AGENT` ortam değişkeni ayarlanır. Bir ajan oturumundan çağrıldığında ile etkileşimli olarak çağrıldığında farklı davranan komut dosyalarınız veya araçlarınız varsa kullanışlıdır.

## Tarayıcıdan Sohbete Ekle

Entegre tarayıcıda sağ tıklama artık "Sohbete Ekle" seçeneğini gösteriyor. Bir web sayfasından içerik seçin ve kopyala-yapıştır yapmadan doğrudan Copilot Chat bağlamınıza ekleyin.

## Düzeltildi: Agent Host'ta Çok Satırlı Kabuk Komutları

Uzun zamandır beklenen bir hata düzeltmesi: Agent Host terminal aracındaki çok satırlı kabuk komutları artık doğru çalışıyor. Daha önce bunlar başarısız olabilir veya yanlış davranış üretebilirdi.

## Klavye-Etkileşimli SSH Kimlik Doğrulaması

Agent Host SSH bağlantıları artık klavye-etkileşimli kimlik doğrulamayı destekliyor — bazı SSH sunucuları (bazı eski kurumsal yapılandırmalar dahil) tarafından kullanılan yedek kimlik doğrulama yöntemi. Uzak SSH ana bilgisayarlarında çalışan ajanların kimlik doğrulama hatalarıyla karşılaşma olasılığı daha düşük.

Orijinal gönderi: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
