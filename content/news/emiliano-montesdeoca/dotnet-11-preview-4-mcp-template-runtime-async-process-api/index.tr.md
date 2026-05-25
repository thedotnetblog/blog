---
title: ".NET 11 Preview 4: MCP Sunucu Şablonu, Runtime-Async Kütüphaneleri, Süreç API'si"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 yayınlandı. Öne çıkanlar: SDK'daki MCP sunucu şablonu, runtime-async ile derlenen çalışma zamanı kütüphaneleri, mobil için dotnet watch ve Süreç API'sinin önemli genişlemesi."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 kullanıma sunuldu. Her büyük .NET önizleme sürümü, çalışma zamanı, SDK, kütüphaneler, ASP.NET Core, MAUI, C# ve Entity Framework genelinde uzun bir değişiklik listesi ekler. Listenin tamamını tekrarlamak yerine, dikkatimi çeken şeyler bunlar.

## .NET SDK'ya MCP Sunucu Şablonu Geliyor

En ilginç öğe: SDK'ya artık bir MCP sunucu proje şablonu dahil edildi. Bu, `dotnet new mcp-server` (ya da komutun ne olacağı) kutudan çıktığı gibi çalışıyor demektir. .NET'te MCP araçları geliştiren herkes için bu, başlangıç sürtünmesini önemli ölçüde azaltır. Platform toolchain'e MCP entegrasyonu, ekosistemin hangi yöne gittiğinin sinyalini vermektedir.

## Runtime-Async ile Derlenen Çalışma Zamanı Kütüphaneleri

Çalışma zamanının kendisi artık standart kütüphanelerini runtime-async özelliğini kullanarak derliyor. Bu, performansı etkileyen dahili bir değişikliktir — çalışma zamanındaki async durum makineleri daha verimli hale geliyor. Buradaki önem kullanıcıya görünür API değişikliklerinde değil; runtime-async'in BCL'nin kendisi için kullanılabilecek kadar olgunlaşmış olmasında, bu da özelliğin hazırlık durumu hakkında anlamlı bir sinyaldir.

## JIT Optimizasyonları ve Donanım İç Fonksiyonları

Preview 4, JIT çalışmalarını sürdürüyor. Donanım iç fonksiyonları ve kod üretimi iyileştirmeleri burada yayınlanıyor — ayrıntılar çalışma zamanı sürüm notlarında. Bu tür değişiklikler genellikle kodunuzda herhangi bir değişiklik yapılmadan yoğun hesaplama döngülerinde verimliliği artırır.

## Süreç API'sinin Genişlemesi

Preview 4'te `System.Diagnostics.Process`'e büyük bir güncelleme geliyor:

- `Process.RunAndCaptureTextAsync` — bir süreci başlat, stdout/stderr'i yakala, çıkışı bekle, hepsini deadlock riski olmadan tek bir çağrıda
- `KillOnParentExit` — üst ve alt süreçler arasında hafif yaşam döngüsü eşleştirmesi
- Daha trimmer dostu `SafeProcessHandle` tabanlı API'ler

Eğer hiç deadlock'a yol açmadan süreç çıktısını yakalamak için ortak kod yazdıysanız (aynı anda stdout *ve* stderr'den async okuma), `RunAndCaptureTextAsync` tam da ihtiyacınız olan API'dir.

## Android ve iOS için dotnet watch

`dotnet watch` artık .NET MAUI Android ve iOS projeleri için cihaz seçimini destekliyor. Build döngüsünde cihaz bağlantılarını elle yönetmeden mobilde daha hızlı iterasyon.

## Span Tabanlı Sıkıştırma API'leri

Kütüphanelere yeni span tabanlı Deflate, ZLib ve GZip encoder/decoder API'leri geliyor. Sıkıştırılmış verilerle çalışırken daha az tahsis — yüksek verimli veri işleme yapıyorsanız alakalı.

## Deneyin

[.NET 11 Preview 4'ü İndirin](https://dotnet.microsoft.com/download/dotnet/11.0) — bu bir önizleme, production'a hazır değil, ancak RC döngüsünden önce sorunları erken yakalamak için projelerinizde çalıştırmaya değer.

Orijinal gönderi: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
