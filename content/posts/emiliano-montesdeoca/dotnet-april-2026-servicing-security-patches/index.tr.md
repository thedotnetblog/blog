---
title: ".NET Nisan 2026 Servis Güncellemesi — Bugün Uygulamanız Gereken Güvenlik Yamaları"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Nisan 2026 servis sürümü, .NET 10, .NET 9, .NET 8 ve .NET Framework'teki 6 CVE'yi yamalar — iki uzaktan kod yürütme güvenlik açığı dahil."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

.NET ve .NET Framework için [Nisan 2026 servis güncellemeleri](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) yayımlandı, ve bu sürüm yakında uygulamak isteyeceğiniz güvenlik düzeltmelerini içeriyor. İki uzaktan kod yürütme (RCE) güvenlik açığı dahil altı CVE yamalandı.

## Neler yamalandı

| CVE | Tür | Etkiler |
|-----|-----|---------|
| CVE-2026-26171 | Güvenlik Özelliği Atlatma | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Uzaktan Kod Yürütme** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Uzaktan Kod Yürütme** | .NET 10, 9, 8 |
| CVE-2026-32203 | Hizmet Engeli | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Hizmet Engeli | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Hizmet Engeli | .NET Framework 2.0–4.8.1 |

## Güncellenen sürümler

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

## Ne yapmalı

Projelerinizi ve CI/CD pipeline'larınızı en son yama sürümlerine güncelleyin. İki RCE güvenlik açığı ertelenecek bir şey değil.
