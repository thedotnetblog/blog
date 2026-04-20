---
title: "O Visual Studio Kayan Pencere Ayarını Hiç Duydunuz mu? (Duymanız Gerekiyor)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Gizli bir Visual Studio ayarı, kayan pencereler üzerinde tam kontrol sağlıyor — bağımsız görev çubuğu girişleri, düzgün çoklu monitör davranışı ve mükemmel FancyZones entegrasyonu. Tek bir açılır menü her şeyi değiştiriyor."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "visual-studio-floating-windows-powertoys" >}}).*

Birden fazla monitörle Visual Studio kullanıyorsanız (ve dürüstçe söylemek gerekirse, günümüzde kim kullanmıyor ki), muhtemelen o can sıkıcı durumu yaşamışsınızdır: ana IDE'yi küçülttüğünüzde kayan araç pencereleri kayboluyor, her zaman her şeyin üstünde kalıyor ve ayrı görev çubuğu butonları olarak görünmüyorlar. Bazı iş akışları için işe yarayabilir, ancak çoklu monitör kurulumlarında oldukça sinir bozucu.

Visual Studio ekibinden Mads Kristensen, kayan pencerelerin davranışını kökten değiştiren [az bilinen bir ayarı paylaştı](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/). Tek bir açılır menü. Hepsi bu kadar.

## Ayar nerede?

**Tools > Options > Environment > Windows > Floating Windows**

"These floating windows are owned by the main window" açılır menüsünde üç seçenek bulunuyor:

- **None** — tam bağımsızlık. Her kayan pencere kendi görev çubuğu girişini alır ve normal bir Windows penceresi gibi davranır.
- **Tool Windows** (varsayılan) — belgeler serbestçe kalar, araç pencereleri IDE'ye bağlı kalır.
- **Documents and Tool Windows** — klasik Visual Studio davranışı, her şey ana pencereye bağlı.

## Çoklu monitör kurulumlarında neden "None" doğru seçim?

**None** olarak ayarlayın ve aniden tüm kayan araç pencereleriniz ve belgeleriniz gerçek Windows uygulamaları gibi davranmaya başlar. Görev çubuğunda görünürler, ana Visual Studio penceresini küçülttüğünüzde görünür kalmaya devam ederler ve artık her şeyin önüne zorla gelmiyor.

Bunu **PowerToys FancyZones** ile birleştirirseniz oyun değiştirucu bir deneyim elde edersiniz. Monitörlerinizde özel düzenler oluşturun, Solution Explorer'ınızı bir bölgeye, hata ayıklayıcıyı bir diğerine ve kod dosyalarını istediğiniz yere yerleştirin. Her şey yerinde kalır, her şeye bağımsız olarak erişilebilir ve çalışma alanınız kaotik yerine düzenli hissedilir.

## Hızlı öneriler

- **Çoklu monitör güç kullanıcıları**: **None** olarak ayarlayın, FancyZones ile birleştirin
- **Ara sıra kayan pencere kullananlar**: **Tool Windows** (varsayılan) sağlam bir orta yol
- **Geleneksel iş akışı**: **Documents and Tool Windows** her şeyi klasik tutar

İpucu: Herhangi bir araç penceresi başlık çubuğuna **Ctrl + çift tıklayarak** anında kayan veya yerleşik hale getirebilirsiniz. Ayarı değiştirdikten sonra yeniden başlatmaya gerek yok.

## Sonuç

Bu, "bunu neden daha önce bilmiyordum" dedirten ayarlardan biri. Visual Studio'daki kayan pencereler sizi hiç rahatsız ettiyse şu anda gidip bunu değiştirin.

Ayrıntılar ve ekran görüntüleri için [tam yazıyı](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) okuyun.
