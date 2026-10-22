---
title: ".NET 11 Preview 5: Gerçekte İlk Önce Neyi Denerdim"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5, SDK, runtime, C#, ASP.NET Core ve EF Core'da iyileştirmeler sunuyor. İşte gerçek .NET uygulamaları oluşturuyorsanız erken test etmeye en değer olduğunu düşündüğüm güncellemeler."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

.NET önizleme yazıları her zaman doludur.

Bu platform için iyi haber, ancak aynı zamanda pratik sorunun gömülmesi anlamına gelir: **gerçekte önce neyi test etmelisiniz?**

.NET 11 Preview 5, SDK, runtime, kütüphaneler, ASP.NET Core, C#, MAUI ve EF Core'da çok şey getiriyor. Bunu dev bir değişiklik günlüğü özetine dönüştürmek yerine, şu anda gerçek geliştirici ilgisini hak eden kısımlara odaklanmak istiyorum.

## MCP sunucu şablonunun `dotnet new` içinde olması bir sinyaldir

Bu muhtemelen SDK bölümündeki en stratejik öğedir.

Bir proje şablonu doğrudan SDK'ya indiğinde, platformun artık senaryoyu niş olarak görmediği anlamına gelir. `dotnet new` içine yerleşik bir **MCP Sunucu şablonuna** sahip olmak, modeli deneme maliyetini düşürür ve ekosistemin nereye gittiği hakkında net bir mesaj gönderir.

.NET'te ajan araçları, dahili asistanlar veya AI entegre geliştirici yardımcı programları oluşturuyorsanız, test edeceğim ilk şeylerden biri budur.

## Derleme zamanı güvenlik açığı ve kullanım ömrü sonu kontrolleri tam sevdiğim türden varsayılanlardır

Güvenlik ve yaşam döngüsü farkındalığı, platform size ayrı bir raporda kimsanın okumadığı sonradan bildirmek yerine **derleme sırasında** yardımcı olduğunda çok daha iyidir.

Derleme sırasında güvenlik açıkları ve kullanım ömrü sonu paketler için yeni SDK kontrolleri, daha iyi davranışı varsayılan haline getirdikleri için sevdiğim türden özelliklerdir.

Bunlar gösterişli değil, ancak gerçekten iyi yaşlanan türden iyileştirmelerdir.

## C# doğru yerlerde daha anlamlı olmaya devam ediyor

Preview 5 C# öğeleri ilginç, özellikle:

- kapalı sınıf hiyerarşileri
- birleşim bildirimleri ve birleşim desenleri
- devam eden unsafe evrim çalışmaları

Henüz tüm bunları üretim kodunda körü körüne benimsemem, çünkü önizleme dil özellikleri her zaman ayık bir test döngüsünü hak eder. Ancak yön iyi. C#, kimliğini kaybetmeden daha zengin modellemeye doğru ilerlemeye devam ediyor.

## ASP.NET Core ve EF Core'un erken test edilmeye değer pratik güncellemeleri var

Kesinlikle bir keşif yapacağım iki alan:

### Blazor iyileştirmeleri

Blazor SSR için istemci tarafı doğrulama ve etkileşimsiz QuickGrid iyileştirmeleri, gerçek uygulamaları basitleştirebilecek türden yaşam kalitesi özellikleridir.

### EF Core varsayılanları ve uyarıları

EF Core'un SQL Server 2022 uyumluluğunu varsayılana taşıması ve eşzamansız EF sorgularının eşzamanlı çalışması için uyarılar eklemesi, gerçek kod tabanlarında gizli sorunları ortaya çıkarabilecek türden değişikliklerdir.

Bu, er ya da geç test etmeye değer olduğu anlamına gelir.

## İlk geçiş için kısa listem

Preview 5'i keşfetmek için yarım günüm olsaydı, şunu yapardım:

1. MCP sunucu şablonunu denerdim
2. derlemeleri çalıştırır ve yeni güvenlik açığı/EOL kontrollerini incelerdim
3. yeni C# modelleme özelliklerinden faydalanabilecek herhangi bir kod tabanını test ederdim
4. o yığınsanız Blazor SSR senaryolarını doğrular
5. EF Core ağırlıklı yolları çalıştırır ve uyarı değişikliklerini veya SQL farklılıklarını izlerdim

Erken değerin olduğu yer burasıdır.

## Benim görüşüm

.NET 11 Preview 5, platformun aynı anda iki yönde itmeye devam ettiği sürümlerden biri gibi hissediyor:

- daha iddialı geliştirici yetenekleri
- üretim odaklı ekipler için daha iyi varsayılanlar

Bu kombinasyon, bir önizleme döngüsünden istediğim şeydir.

Deneyin, ancak amaçla deneyin.

Orijinal yazı: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)