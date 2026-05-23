---
title: "Copilot Studio .NET 10 WebAssembly'ye Nasıl Geçti ve %20 Daha Hızlı Oldu"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10 WASM iyileştirmeleri sadece yeni projeler için değil. Copilot Studio'nun .NET 8'den yükseltme sonrası ölçtükleri: otomatik parmak izi, varsayılan WasmStripILAfterAOT ve gerçek yürütme performans sayıları."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Copilot Studio ekibi, tüm Blazor WASM geliştiricilerinin merak ettiği şeyi yaptı: bir üretim uygulamasını gerçekten .NET 8'den .NET 10'a yükseltti ve sonuçları ölçtü. Gönderi, nadir ve gerçekten yararlı olan belirli sayılar paylaşıyor.

## Yükseltme Sıkıcıydı (Bu İyi Bir Şey)

Hedef çerçeveyi güncellemek, paket referanslarını yenilemek, son değişiklikleri düzeltmek. Hepsi bu. .NET 10 derlemesi artık üretimde çalışıyor. Geçişin kendisi ilginç kısım değildi — .NET 10'daki değişiklikler ilginç.

## Otomatik Varlık Parmak İzi

Önceden, bir WASM uygulaması dağıtmak, önbellek temizleme için yayınlanan varlıkları SHA256 karmaları ile yeniden adlandırmak üzere özel komut dosyaları yazmak anlamına geliyordu. Copilot Studio'nun tam olarak bunu yapan bir PowerShell betiği vardı — dosyaları yeniden adlandırma, JavaScript yükleyicisine `integrity` özelliklerini enjekte etme, her şeyi manuel olarak yönetme.

.NET 10'da tüm bunlar yerleşiktir. Yayınlanan varlıklar otomatik olarak parmak izi alınır, doğrudan `dotnet.js`'den içe aktarılır ve manuel müdahale olmadan bütünlük doğrulaması yapılır. Ekip yeniden adlandırma betiğini sildi.

Kapsamda küçük değişiklik, karmaşıklıkta önemli azalma.

## WasmStripILAfterAOT Artık Varsayılan Olarak Açık

.NET 8'de, AOT derlenmiş derlemelerden IL kaldırmak isteğe bağlıydı. .NET 10'da bu varsayılan. AOT derlemesinden sonra, orijinal IL bayt kodu çıktıdan kaldırılır — çalışma zamanında gerekli değildir ve onu korumak paket boyutunu gereksiz yere şişiriyordu.

Copilot Studio belirli bir optimizasyon kullanır: hem JIT motoru (hızlı başlangıç) hem de AOT motorunu (maksimum kararlı durum performansı) dağıtır, her ikisini paralel olarak yükler ve hazır olduğunda JIT'ten AOT'a geçiş yapar. Ayrıca iki motor arasında özdeş dosyaları tekilleştirir.

Yeni IL sıyırma davranışı, AOT derlemelerinin artık JIT karşılıklarıyla bit bit eşleşmediği anlamına gelir, bu nedenle daha az dosya tekilleştirilir:
- .NET 8: 59 paylaşılan dosya
- .NET 10: 22 paylaşılan dosya

Net sonuç: AOT motoru için yaklaşık %15 daha büyük paket boyutu. AOT indirme hızlı LAN'da ~%6 daha yavaş, 4G'de ~%17 daha yavaş. Ancak tüm bunlar uygulama zaten etkileşimli olduktan sonra arka planda gerçekleşir.

## Performans Sayıları

Önemli olan kısım bu:

- İlk çağrıda **~%20 daha hızlı** (soğuk yol)
- Sonraki çağrılarda **~%5 daha hızlı** (sıcak yol)

İyileştirmeler, AOT derlenmiş kodun hakim olduğu büyük, karmaşık aracılarda — "büyük botlar"da en görünür. Daha basit iş akışları için kazanım daha küçüktür.

## Hâlâ .NET 8'deyseniz

Geçiş hikayesi gerçekten basit: `<TargetFramework>`'ü güncelleyin, paket referanslarını yenileyin, özel parmak izi komut dosyalarını kaldırın ve otomatik olarak `WasmStripILAfterAOT`'tan yararlanacaksınız. AOT derliyorsanız, benzer performans kazanımları bekleyin.

Gönderiden bir not: .NET WASM çalışma zamanını bir `WebWorker` içinde yüklüyorsanız, başlatırken `dotnetSidecar = true` ayarlayın.

Orijinal gönderi: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
