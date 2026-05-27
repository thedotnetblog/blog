---
title: "dotnet new WinUI: Visual Studio'ya Dokunmadan Windows Uygulamaları Oluşturun"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI proje şablonları artık dotnet new ile çalışıyor — boş uygulamalar, NavigationView desenleri ve daha fazlası. VS Code desteği, Visual Studio gerekmez, Fluent Design varsayılanları yerleşik olarak geliyor."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI geliştirme eskiden Visual Studio gerektiriyordu. Bu değişiyor: Microsoft, `dotnet new` ile çalışan WinUI için açık kaynaklı proje ve öğe şablonları yayımladı; Windows uygulama geliştirmeyi standart CLI iş akışına entegre etti.

## Üç Komutla Başlayın

```shell
# Şablonları yükle
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# NavigationView uygulaması oluştur
dotnet new winui-navview -n MyApp

# Çalıştır
cd MyApp
dotnet run
```

Visual Studio yok, manuel proje kurulumu yok. Uygulama `dotnet run` ile çalışıyor.

## Neler Dahil

**Boş şablon** (`dotnet new winui`) — zaten bağlanmış Fluent başlık çubuğu, `.ico` varlıklı güncellenmiş varsayılan uygulama simgesi ve açık/koyu mod için doğru varsayılanlarla modern bir başlangıç noktası. Temel bilgileri kendiniz yapılandırmanızı gerektiren eski boş şablondan daha iyi.

**NavigationView şablonu** (`dotnet new winui-navview`) — NavigationView, modern başlık çubuğu ve çok sayfalı gezinme yapısıyla tamamen bağlanmış ana-ayrıntı gezinme deseni. Gezinme tabanlı uygulamalar için standart Windows uygulama siluetini takip eder. Yan gezinmeli bir şey oluşturuyorsanız buradan başlayın.

Her iki şablon da [Windows uygulama siluetlerini](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — düzen, gezinme ve görsel yapı için modern Fluent Design desenleri — hemen kutunun içinden takip eder.

## Visual Studio Dışındaki Geliştiriciler İçin Neden Önemli

VS Code, Rider veya komut satırı araçları kullanan WinUI geliştiricileri iyi hizmet görmemişti. Mevcut Visual Studio şablonları VS dışında kullanılamıyordu — proje yapısını manuel olarak yeniden oluşturmak ve temel unsurları bağlamak gerekiyordu.

Bu şablonlar açık kaynaklıdır ([WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)'e bakın), [topluluk geri bildirimlerinden](https://github.com/microsoft/microsoft-ui-xaml/issues/10388) geliştirildi ve şu anda kullanılabilir. Visual Studio desteği üzerinde çalışılıyor — bu şablonlar eninde sonunda orada da çalışacak.

WinUI proje kurulumlarını betik haline getirmek, CI'ye entegre etmek veya sadece Visual Studio dışında bir editör kullanmak isteyen ekipler için bu anlamlı bir gelişme.

Orijinal gönderi: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
