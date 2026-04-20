---
title: ".NET Nisan 2026 Bakım Güncellemesi — Bugün Uygulamanız Gereken Güvenlik Yamaları"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Nisan 2026 bakım sürümü, .NET 10, .NET 9, .NET 8 ve .NET Framework genelinde 6 CVE'yi yamalıyor — iki uzaktan kod yürütme açığı da dahil olmak üzere."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

.NET ve .NET Framework için [Nisan 2026 bakım güncellemeleri](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) yayımlandı ve bu sürüm yakında uygulamak isteyeceğiniz güvenlik düzeltmelerini içeriyor. İki uzaktan kod yürütme (RCE) açığı dahil olmak üzere altı CVE yamalandı.

## Neler yamalandı

İşte hızlı özet:

| CVE | Tür | Etkileyen |
|-----|------|---------|
| CVE-2026-26171 | Güvenlik Özelliği Atlatma | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Uzaktan Kod Yürütme** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Uzaktan Kod Yürütme** | .NET 10, 9, 8 |
| CVE-2026-32203 | Hizmet Reddi | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Hizmet Reddi | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Hizmet Reddi | .NET Framework 2.0–4.8.1 |

İki RCE CVE'si (CVE-2026-32178 ve CVE-2026-33116) en geniş .NET sürümü yelpazesini etkiliyor ve öncelikli olarak ele alınmalı.

## Güncellenen sürümler

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

Tümü olağan kanallar aracılığıyla mevcut — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), MCR'deki container imajları ve Linux paket yöneticileri.

## Ne yapmalısınız

Projelerinizi ve CI/CD pipeline'larınızı en son yama sürümlerine güncelleyin. Container çalıştırıyorsanız, en son imajları çekin. .NET Framework kullanıyorsanız, ilgili yamalar için [.NET Framework sürüm notlarına](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) bakın.

Üretimde .NET 10 çalıştıranlar için (şu an güncel sürüm), 10.0.6 zorunlu bir güncellemedir. Bu LTS sürümlerindeyseniz .NET 9.0.15 ve .NET 8.0.26 için de aynısı geçerli. İki RCE açığı ertelenerek geçiştirilebilecek bir şey değildir.
