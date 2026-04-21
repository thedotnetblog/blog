---
title: "azd + GitHub Copilot: Yapay Zeka Destekli Proje Kurulumu ve Akıllı Hata Çözümü"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI artık GitHub Copilot ile entegre olarak proje altyapısını oluşturuyor ve dağıtım hatalarını çözüyor — terminal'den çıkmadan."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Bu makale otomatik olarak çevrilmiştir. Orijinal İngilizce sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Mevcut bir uygulamayı Azure'a dağıtmak isteyip boş bir `azure.yaml` dosyasına bakarak Express API'nizin Container Apps mı yoksa App Service mi kullanması gerektiğini hatırlamaya çalıştığınız o anı biliyor musunuz? O an artık çok daha kısa.

Azure Developer CLI (`azd`) artık GitHub Copilot ile iki somut şekilde entegre: `azd init` sırasında AI destekli proje iskele kurma ve dağıtımlar başarısız olduğunda akıllı hata giderme. Her iki özellik de tamamen terminalde kalıyor.

## azd init Sırasında Copilot ile Kurulum

`azd init` çalıştırıldığında artık "Set up with GitHub Copilot (Preview)" seçeneği görünüyor. Seçin ve Copilot, gerçek kodunuzu temel alarak `azure.yaml`, altyapı şablonları ve Bicep modülleri oluşturmak için kod tabanınızı analiz eder.

```
azd init
# Seçin: "Set up with GitHub Copilot (Preview)"
```

Gereksinimler:

- **azd 1.23.11 veya üzeri** — `azd version` ile kontrol edin veya `azd update` ile güncelleyin
- **Aktif GitHub Copilot aboneliği** (Bireysel, İş veya Kurumsal)
- **GitHub CLI (`gh`)** — gerekirse `azd` oturum açmanızı isteyecek

Gerçekten faydalı bulduğum şey: her iki yönde de çalışıyor. Sıfırdan mı inşa ediyorsunuz? Copilot doğru Azure hizmetlerini başından itibaren yapılandırmanıza yardımcı olur. Dağıtmak istediğiniz mevcut bir uygulamanız mı var? Copilot'u ona yöneltin — kodu yeniden yapılandırmadan konfigürasyon oluşturulur.

### Gerçekte Ne Yapar

PostgreSQL bağımlılığına sahip bir Node.js Express API'niz olduğunu varsayalım. Container Apps ile App Service arasında manuel seçim yapmak ve ardından sıfırdan Bicep yazmak yerine, Copilot yığınınızı algılar ve şunları oluşturur:

- Doğru `language`, `host` ve `build` ayarlarına sahip `azure.yaml`
- Azure Container Apps için Bicep modülü
- Azure Database for PostgreSQL için Bicep modülü

Ve herhangi bir şeyi değiştirmeden önce ön kontroller yapar — git çalışma dizininin temiz olduğunu doğrular, MCP sunucu araç iznini önceden sorar. Her şey bilginiz dahilinde gerçekleşir.

## Copilot ile Hata Giderme

Dağıtım hataları kaçınılmazdır. Eksik parametreler, izin sorunları, SKU kullanılabilirlik sorunları — ve hata mesajı nadiren gerçekten bilmeniz gereken tek şeyi söyler: *nasıl düzeltilir*.

Copilot olmadan döngü şöyle görünür: hatayı kopyala → belgelerden ara → ilgisiz üç Stack Overflow cevabı oku → birkaç `az` CLI komutu çalıştır → tekrar dene ve umut et. `azd`'de Copilot ile bu döngü çöküyor. Herhangi bir `azd` komutu başarısız olduğunda anında dört seçenek sunuluyor:

- **Explain** — ne yanlış gittiğinin anlaşılır dilde açıklaması
- **Guidance** — sorunu gidermek için adım adım talimatlar
- **Diagnose and Guide** — tam analiz + Copilot düzeltmeyi uygular (onayınızla) + isteğe bağlı yeniden deneme
- **Skip** — kendiniz halledin

Kritik nokta: Copilot'un projeniz, başarısız olan komut ve hata detayları hakkında zaten bağlamı var. Önerileri *sizin durumunuza* özeldir.

### Varsayılan Davranışı Ayarlama

Her zaman aynı seçeneği seçiyorsanız etkileşimli istemi atlayın:

```
azd config set copilot.errorHandling.category troubleshoot
```

Değerler: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Otomatik düzeltme ve yeniden denemeyi de etkinleştirebilirsiniz:

```
azd config set copilot.errorHandling.fix allow
```

İstediğiniz zaman etkileşimli moda geri dönün:

```
azd config unset copilot.errorHandling.category
```

## Sonuç

En son sürümü edinmek için `azd update` çalıştırın ve bir sonraki projenizde `azd init` deneyin.

[Orijinal duyuruyu buradan okuyun](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
