---
title: "Windows App Dev CLI v0.3: Terminalden F5 Hata Ayıklama ve Ajanlar için UI Otomasyonu"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3, terminalden hata ayıklama başlatmak için winapp run, UI otomasyonu için winapp ui ve paketlenmiş uygulamalarla dotnet run'ı çalıştıran yeni bir NuGet paketi getiriyor."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "index.md" >}}).*

Visual Studio'nun F5 deneyimi harika. Ama yalnızca paketlenmiş bir Windows uygulamasını başlatıp hata ayıklamak için VS'yi açmak — bir CI boru hattında, otomatik bir iş akışında veya bir yapay zeka ajanı testleri çalıştırırken — fazla ağır bir yük.

Windows App Development CLI v0.3 [yayınlandı](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) ve bunu iki temel özellikle doğrudan ele alıyor: `winapp run` ve `winapp ui`.

## winapp run: Her yerden F5

`winapp run` paketlenmemiş bir uygulama klasörü ve manifest alır; VS'nin hata ayıklama başlatmasında yaptığı her şeyi yapar: loose paket kaydeder, uygulamayı başlatır ve yeniden dağıtımlar arasında `LocalState`'i korur.

```bash
# Uygulamayı derleyin, ardından paketlenmiş uygulama olarak çalıştırın
winapp run ./bin/Debug
```

WinUI, WPF, WinForms, Console, Avalonia ve daha fazlası için çalışır. Modlar hem geliştiriciler hem de otomatik iş akışları için tasarlanmıştır:

- **`--detach`**: Başlatır ve hemen terminale kontrolü geri döndürür. CI için ideal.
- **`--unregister-on-exit`**: Uygulama kapatıldığında kayıtlı paketi temizler.
- **`--debug-output`**: `OutputDebugString` mesajlarını ve istisnaları gerçek zamanlı yakalar.

## Yeni NuGet Paketi: Paketlenmiş uygulamalar için dotnet run

.NET geliştiricileri için yeni bir NuGet paketi var: `Microsoft.Windows.SDK.BuildTools.WinApp`. Kurulumdan sonra `dotnet run` tüm iç döngüyü yönetir: derleme, loose-layout paketi hazırlama, Windows'ta kayıt ve başlatma — tek adımda.

```bash
winapp init
# veya
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: Komut satırından UI Otomasyonu

Bu, ajan senaryolarını açan özellik. `winapp ui`, terminalden çalışan herhangi bir Windows uygulamasına (WPF, WinForms, Win32, Electron, WinUI3) tam UI Automation erişimi sağlar.

Yapılabilecekler:

- Tüm üst düzey pencereleri listele
- Herhangi bir pencerenin tam UI Automation ağacında gezin
- Ad, tür veya otomasyon kimliğine göre öğe ara
- Tıkla, çağır ve değer ayarla
- Ekran görüntüsü al
- Öğelerin görünmesini bekle — test senkronizasyonu için ideal

`winapp ui` ile `winapp run`'ı birleştirmek, terminalden eksiksiz bir derleme → başlatma → doğrulama iş akışı sağlar. Bir ajan uygulamayı çalıştırabilir, UI durumunu inceleyebilir, programatik olarak etkileşime girebilir ve sonucu doğrulayabilir.

## Diğer yenilikler

- **`winapp unregister`**: Tamamlandığında yandan yüklenmiş paketi kaldırır.
- **`winapp manifest add-alias`**: Terminalden adıyla uygulama başlatmak için takma ad ekler.
- **Sekme tamamlama**: PowerShell tamamlamayı tek komutla yapılandırın.

## Nasıl edinilir

```bash
winget install Microsoft.WinAppCli
# veya
npm install -g @microsoft/winappcli
```

CLI genel önizleme aşamasında. Tam belgeleme için [GitHub deposuna](https://github.com/microsoft/WinAppCli), tüm ayrıntılar için [orijinal duyuruya](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) bakın.
