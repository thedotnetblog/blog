---
title: ".NET 11 Sonunda Süreç API'sini Düzeltiyor"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process yıllar içindeki en büyük güncellemesini alıyor. RunAndCaptureTextAsync, KillOnParentExit, SafeProcessHandle API'leri ve standart tanıtıcı yönlendirme üzerinde tam kontrol — artık deadlock kalıp kodu yok."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Hiç bir süreç başlatıp çıktısını yakalamak zorunda kalan her .NET geliştiricisi, aynı tehlikeli kalıp kodun bir varyasyonunu yazmıştır: stdout'tan asenkron okuma, stderr'den asenkron okuma, `WaitForExitAsync`, her iki akışı da boşaltmayı unutmayın yoksa deadlock olur. Bu yıllardır bilinen bir tuzaktır.

.NET 11 bunu sonunda düzgün bir şekilde düzeltiyor.

## RunAndCaptureTextAsync

Temel eklenti: bir süreci başlatan, stdout ve stderr'i yakalayan ve deadlock olmaksızın çıkışı bekleyen tek bir statik metod.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Tek çağrı. Manuel akış boşaltma yok. Özenle yerleştirilmiş `WaitForExit` yok. Sadece bir şey çalıştırmanız ve çıktısını almanız gerekiyorsa, istediğiniz API budur.

Çıktıyı yakalamadan çıkışı beklemek istediğiniz durum için `Process.RunAsync` da var.

## KillOnParentExit

Başlatılan süreçlerle ilgili yaygın bir sorun: üst süreç çöküyor veya sonlandırılıyorsa, alt süreçler yetim olarak çalışmaya devam eder. `KillOnParentExit`, süreç başlangıcında alt sürecin üst süreç çıktığında sonlandırılması gerektiğini bildirmenizi sağlar.

Bu, platforma özgü şekillerde var olan bir özelliktir (Windows'ta iş nesneleri, Linux'ta prctl) ancak .NET'ten kullanmak için p/invoke veya üçüncü taraf kütüphaneler gerektiriyordu. Artık `ProcessStartInfo` üzerinde birinci sınıf bir özellik haline geldi.

## SafeProcessHandle Tabanlı API'ler

Yeni hafif API yüzeyi, tam `Process` sınıfı yerine `SafeProcessHandle` etrafında inşa edilmiştir. Tam `Process` sınıfı çok fazla durum taşır ve kırpılması zordur — `SafeProcessHandle` yolu, çıktı boyutunu en aza indirmesi gereken uygulamalar (WASM, yerel AOT) için daha kırpıcı dostu.

## Tanıtıcı Kalıtımı Üzerinde Tam Kontrol

Güncellemede ayrıca bir alt sürecin hangi tanıtıcıları miras alacağı ve standart tanıtıcıların nasıl yönlendirileceği üzerinde ayrıntılı kontrol ekleniyor. Daha önce stdin/stdout/stderr'i yönlendirebiliyordunuz ancak OS düzeyinde tam olarak hangi tanıtıcıların miras alınacağını belirleyemiyordunuz. Yeni API'ler bu kontrolü açığa çıkarıyor.

## Bu Neden Önemli

`Process` sınıfı araçlarda, derleme sistemlerinde, test koşucularında ve diğer yürütülebilir dosyaları çağıran her uygulamada kullanılıyor. Eski API yüzeyi .NET Framework döneminden kalmaydı ve yaşını gösteriyordu. Bu bir kırıcı değişiklik değil — eski API'ler hâlâ çalışıyor — ancak yeni kodların yeni yüzeyi tercih etmesi gerekiyor.

Kırpılmış uygulamalar veya AOT derleme senaryoları için `SafeProcessHandle` yolu özellikle memnuniyetle karşılanıyor. Eski `Process` sınıfı, kırpmayı karmaşık hale getiren çok sayıda yansıma ağır kodu beraberinde getiriyordu.

Orijinal gönderi: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
