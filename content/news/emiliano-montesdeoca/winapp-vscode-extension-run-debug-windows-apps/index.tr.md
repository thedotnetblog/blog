---
title: "WinApp VS Code Uzantısı: Editörü Terk Etmeden Windows Uygulamalarını Çalıştır, Hata Ayıkla ve Paketle"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "WinApp VS Code uzantısı, Windows Uygulama Geliştirme CLI'sının tamamını doğrudan VS Code'a getiriyor — Visual Studio'ya gerek kalmadan WPF, WinUI, .NET, C++ uygulamalarını paket kimliğiyle çalıştırın, hata ayıklayın, paketleyin ve imzalayın."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Bu yazı otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

VS Code'da bir Windows uygulaması geliştirmeye çalıştıysanız, o anı bilirsiniz. Favori editörünüzde kod yazarken akıştasınızdır ve birden bir Windows API için paket kimliğine ihtiyaç duyarsınız. Ya da MSIX oluşturmanız gerekir. Ya da bir paketi imzalamanız. Ve kendinizi Visual Studio'yu açarken ya da gece 11'de "msix packaging without visual studio" ararken bulursunuz.

O sürtünme artık yok. [WinApp VS Code uzantısı](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) genel önizlemeye girdi — ve bu, [Windows Uygulama Geliştirme CLI](https://github.com/microsoft/WinAppCli)'sının tamamını doğrudan VS Code'a entegre ediyor. Ayrı kurulum yok, Visual Studio gerektirmiyor.

## F5 ile Paket Kimliği

Windows API'leri ile ilgili sorun şu — bildirimler, arka plan görevleri, cihaz üzerinde yapay zeka özellikleri, paylaşım hedefleri — bunların çoğu, uygulamanızın **paket kimliğine** sahip olmasını gerektirir. Olmadan, bu API'ler çalışmaz.

Geleneksel olarak paket kimliği almak, tam bir MSIX yükleyicisi oluşturmak veya Visual Studio'dan çalıştırmak anlamına geliyordu. WinApp uzantısı, özel bir `winapp` hata ayıklama türüyle bunu tamamen değiştiriyor.

`launch.json` dosyanıza bunu ekleyin:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

F5'e basın. Uzantı, derleme çıktınızı ve manifestinizi bulur, `winapp run` aracılığıyla uygulamanıza paket kimliği verir ve hata ayıklayıcıyı ekler. .NET uygulamaları için `coreclr` (C# Dev Kit gerektirir), C/C++ için `cppvsdbg`, Node/Electron için yerleşik hata ayıklayıcı.

Her F5'e basmadan önce projenin otomatik olarak derlenmesi için `preLaunchTask` yapılandırabilirsiniz — Visual Studio'nun derleme ve başlatma akışıyla aynı, ancak VS Code'da.

## Komut Paletinde Her Şey

`Ctrl+Shift+P` açın, `WinApp` yazın — tam araç setini elde edersiniz:

- **Initialize Project** — projeyi Windows SDK ve/veya Windows App SDK ile yapılandır
- **Run Application** — paket kimliğiyle gevşek düzenli paketlenmiş uygulama olarak başlat
- **Create MSIX Package** — sertifika ve çalışma zamanı seçenekleriyle uygulamayı paketle
- **Update Manifest Assets** — tek bir kaynak görüntüden gerekli tüm uygulama simgelerini otomatik oluştur
- **Generate / Install Certificate** — geliştirme sertifikası yönetimi
- **Sign Package** — MSIX veya yürütülebilir dosyayı imzala
- **Run SDK Tool** — `makeappx`, `signtool`, `mt` veya `makepri`'yi doğrudan çalıştır

WinApp CLI'yi kurmanıza da gerek yok. Uzantıyla birlikte geliyor.

## Birden Fazla Framework ile Çalışır

Bu yalnızca .NET WPF/WinUI aracı değil. Uzantı şunlarla çalışır:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Bu genişlik kasıtlı. VS Code, web ve çapraz platform geliştiricilerinin yaşadığı yer. Windows paketlemesine ihtiyaç duyan bir Tauri veya Electron uygulaması geliştiriyorsanız, bu uzantı sizi Visual Studio benimsemek zorunda kalmadan karşılıyor.

## .NET Geliştiricileri İçin Neden Önemli

VS Code'da çok çalışıyorum — Markdown yazdığım, yapılandırmaları yönettiğim, küçük projeleri düzenlediğim ve terminalleri çalıştırdığım yer orası. Ama .NET Windows masaüstü geliştirmede, paketlemeyle ilgili bir şeye ihtiyaç duyulduğu anda Visual Studio tek gerçek seçenekti.

Bu uzantı o boşluğu kapatıyor. Artık VS Code'dan çıkmadan tam bir .NET Windows masaüstü geliştirme döngüsüne sahip olabilirsiniz — düzenleme, derleme, paket kimliğiyle çalıştırma, hata ayıklama, paketleme, imzalama. Bu gerçek bir yaşam kalitesi iyileştirmesi.

## Başlarken

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Ya da Extensions görünümünde (`Ctrl+Shift+X`) **WinApp** arayın.

Gereksinimler:
- Windows 10 veya üzeri
- VS Code 1.109.0 veya üzeri
- Uygulamanızın dili için hata ayıklayıcı uzantısı

Daha fazla ayrıntı için [Chiara Mooney'nin tam duyurusunu](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) okuyun.

## Sonuç

WinApp VS Code uzantısı, VS Code'da yaşayan ancak paketleme çalışmaları için Visual Studio'ya geçmek zorunda kalan .NET Windows masaüstü geliştiricileri için hoş bir ekleme. F5 ile paket kimliği, komut paletinden MSIX paketleme, yerleşik sertifika yönetimi — bu doğru özellik seti.

Bir sonraki WPF veya WinUI projenizde deneyin. Etrafından dolaştığınız sürtünme az önce çok daha küçük hale geldi.
