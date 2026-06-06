---
title: "VS Code 1.120: Güvenli Parola İstemleri, Bağlam Boyutu Seçici, Agent Host'ta GitHub Meta Verileri"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120, Copilot kullanıcılarına odaklanan bir sürüm: güvenli parola istemi yönetimi, model bağlam boyutu seçici, ajan oturumlarında GitHub PR meta verileri ve oturum arşiv yönetimi."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120, tek tek küçük ama günlük kullanımda belirgin biçimde daha iyi olan Copilot ajan iyileştirmeleri setiyle gönderildi.

## Ajan Terminallerinde Güvenli Parola İstemi Algılama

Bir Copilot ajanı parola veya parola ifadesi istemi tetikleyen bir terminal komutu çalıştırdığında, VS Code artık bunu algılar ve bir onay iletişim kutusu gösterir. İletişim kutusu terminale odaklanır, böylece sırrı doğrudan yazabilirsiniz — ve kritik olarak, sırlar hiçbir zaman model üzerinden yönlendirilmez.

Bu önemli bir güvenlik geliştirmesidir. Önceden, kimlik doğrulama istemleri tetikleyen komutları çalıştıran ajanlar, kullanıcıların yanlışlıkla kimlik bilgilerini ifşa edebileceği durumlar oluşturabiliyordu. Ekran okuyucu duyurusu, erişilebilirlik kullanıcılarının da bildirimi alacağı anlamına gelir.

## Model Seçicide Bağlam Boyutu Seçici

Yeni bir bağlam boyutu seçici, modelin bir oturum için ne kadar bağlam kullandığını seçmenize olanak tanır. Farklı modellerin farklı bağlam penceresi boyutları vardır ve bazı iş akışları onu kısıtlamaktan (daha düşük gecikme, daha düşük maliyet) veya maksimize etmekten (karmaşık kod tabanları, uzun süreli oturumlar) yararlanır.

## Agent Host Oturumlarında GitHub PR Meta Verileri

Bir GitHub deposu tarafından desteklenen oturumlar için VS Code artık ajan host kullanıcı arabiriminde GitHub meta verilerini — bir çekme isteği düğmesi dahil — görüntüler. Bir PR üzerinde çalışırken tarayıcıya veya GitHub uzantısına daha az bağlam geçişi.

## Sohbet Oturumu Arşiv Yönetimi

Oturumlar Quick Pick için iki iyileştirme:
- Arşivlenen oturumlar varsayılan olarak gizlidir (daha az görsel karmaşa)
- Arama hâlâ arşivlenen oturumlarla eşleşir, böylece başlıkla birini canlandırabilirsiniz

Oturumlar ayrıca varsayılan olarak yeniliğe göre gruplandırılır, son çalışmanın bulunmasını kolaylaştırır.

## Copilot CLI Eklenti Keşfi

VS Code artık `~/.copilot/installed-plugins/` konumundan kullanıcı tarafından yüklenen Copilot CLI eklentilerini otomatik olarak keşfeder. WinUI veya diğer etki alanına özgü ajan becerilerini kurduysanız, manuel yapılandırma olmadan algılanırlar.

## Özel Diff Düzenleyici API (Önizleme)

Uzantı yazarları için: yeni önerilen bir API `customDiffEditorProvider`, uzantıların iki yan yana özel düzenleyici görünümü yerine hem orijinal hem de değiştirilmiş belgelere erişimle birleşik bir farkı tek bir webview'da oluşturmasına olanak tanır.

Orijinal gönderi: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
