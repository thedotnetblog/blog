---
title: "Hemen yama yapın: ASP.NET Core Data Protection için .NET 10.0.7 OOB güvenlik güncellemesi"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7, Microsoft.AspNetCore.DataProtection içindeki bir güvenlik açığını düzelten bir out-of-band sürümdür — yönetilen kimliği doğrulanmış şifreleyici HMAC'i yanlış baytlar üzerinde hesaplıyordu, bu da ayrıcalık yükselmesine yol açabilirdi. Hemen güncelleyin."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Bu güncelleme isteğe bağlı değil. Uygulamanız `Microsoft.AspNetCore.DataProtection` kullanıyorsa, 10.0.7'ye yükseltmeniz gerekir.

## Ne Oldu

`.NET 10.0.6` Patch Tuesday sürümünden sonra bazı kullanıcılar uygulamalarında şifre çözmenin başarısız olduğunu bildirmeye başladı. Ekip bu gerilemeyi incelerken bir güvenlik açığı da keşfetti: **CVE-2026-40372**.

`Microsoft.AspNetCore.DataProtection`'ın `10.0.0` ile `10.0.6` arasındaki sürümlerinde, yönetilen kimliği doğrulanmış şifreleyici HMAC doğrulama etiketini yükün **yanlış baytları** üzerinde hesaplıyor ve ardından hesaplanan hash'i atıyordu. Bu, ayrıcalık yükselmesine yol açabilirdi.

Basitçe söylemek gerekirse: bütünlük denetimi yapması gereken şeyi yapmıyordu. Data Protection, kurcalamayı önlemek için kimliği doğrulanmış şifreleme kullanır — HMAC, "bu değiştirildi mi?" kontrolüdür. HMAC yanlış veri üzerinde hesaplanırsa bu güvenceyi kaybedersiniz.

## Kimler Etkileniyor

`Microsoft.AspNetCore.DataProtection` kullanan her .NET 10 uygulaması — 10.0.0 ile 10.0.6 arasındaki sürümler. İyi haber şu ki bu paket yalnızca .NET 10'a özeldir. Hâlâ .NET 8 veya 9 kullanıyorsanız, bu özel CVE'den etkilenmiyorsunuz.

Data Protection için yaygın kullanım alanları: çerez şifreleme, antiforgery token'ları, MVC'de temp data ve uygulamanızdaki `IDataProtector` kullanımlarının tamamı.

## Nasıl Düzeltilir

`Microsoft.AspNetCore.DataProtection` NuGet paketini **10.0.7**'ye güncelleyin:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Ya da SDK/runtime'ınızı güncelleyin: [ .NET 10.0.7 indir ](https://dotnet.microsoft.com/download/dotnet/10.0).

Doğru sürümde olduğunuzu doğrulayın:

```bash
dotnet --info
```

Ardından uygulamanızı **yeniden derleyip yeniden dağıtın**. Düzeltme, güncellenmiş paketi çalıştırmaya başlayana kadar etkin olmaz.

## Daha Büyük Resim

Out-of-band güvenlik sürümleri nadirdir — yalnızca bir açığın bir sonraki Patch Tuesday'i bekleyemeyecek kadar ciddi olduğu durumlarda gelirler. Bu olay, 10.0.6'daki bir gerilemenin doğrudan sonucuydu ve bir güvenlik açığı oluşturdu. Sorunun hata raporları sayesinde bulunması iyi bir işaret: süreç çalıştı. Düzeltme hızlı ve kapsam dar.

.NET 10'u üretimde herhangi bir web uygulama çatısıyla kullanıyorsanız, bu aynı gün yapılacak bir güncellemedir.

Rahul Bhandari'nin orijinal duyurusu: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).