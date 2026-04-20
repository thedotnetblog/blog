---
title: "Aspire'ın Isolated Modu Paralel Geliştirmedeki Port Çakışma Kabusu'nu Çözüyor"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2, --isolated modunu tanıtıyor: rastgele port ataması, ayrı secret'lar ve aynı AppHost'un birden fazla örneğini çalıştırırken sıfır çakışma. AI ajanları, worktree'ler ve paralel iş akışları için mükemmel."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Aynı projenin iki örneğini aynı anda çalıştırmayı hiç denediniz mi? O acıyı bilirsiniz. Port 8080 zaten kullanımda. Port 17370 alınmış. Bir şeyleri kapatın, yeniden başlatın, ortam değişkenlerini dengeleyin — bu, üretkenliği mahveden bir durum.

Bu sorun daha da kötüleşiyor, iyileşmiyor. AI ajanlar bağımsız çalışmak için git worktree'ler oluşturuyor. Background agent'lar ayrı ortamlar başlatıyor. Geliştiriciler özellik dalları için aynı repoyu iki kez checkout yapıyor. Bu senaryoların her biri aynı engelle karşılaşıyor: aynı uygulamanın iki örneği aynı portlar için çarpışıyor.

Aspire 13.2 bunu tek bir bayrakla çözüyor. Aspire ekibinden James Newton-King [tüm ayrıntıları yazdı](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) ve bu, "bunu neden daha önce yoktu?" diye düşündüren özelliklerden biri.

## Çözüm: `--isolated`

```bash
aspire run --isolated
```

Hepsi bu. Her çalıştırma şunları alıyor:

- **Rastgele portlar** — örnekler arasında artık çakışma yok
- **İzole user secret'lar** — bağlantı dizeleri ve API anahtarları örnek başına ayrı kalıyor

Manuel port yeniden ataması yok. Ortam değişkeni dengeleme yok. Her çalıştırma otomatik olarak taze, çakışmasız bir ortam alıyor.

## Bunun parladığı gerçek senaryolar

**Çoklu checkout'lar.** Bir dizinde özellik dalı, başka bir dizinde hata düzeltmesi var:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Her ikisi de çakışma olmadan çalışıyor. Dashboard neyin nerede çalıştığını gösteriyor.

**VS Code'daki background agent'lar.** Copilot Chat'in background agent'ı kodunuz üzerinde bağımsız çalışmak için bir git worktree oluşturduğunda, Aspire AppHost'unuzu çalıştırması gerekebilir. `--isolated` olmadan, bu birincil worktree'nizle port çakışmasına yol açar. Bununla birlikte her iki örnek de çalışır.

`aspire agent init` ile birlikte gelen Aspire skill'i, worktree'lerde çalışırken ajanlara otomatik olarak `--isolated` kullanmalarını talimatlandırıyor. Dolayısıyla Copilot'un background agent'ı bunu kutudan çıkar çıkmaz halledebilmeli.

**Geliştirmeyle eş zamanlı entegrasyon testleri.** Özellik geliştirmeye devam ederken canlı bir AppHost'a karşı test çalıştırmanız mı gerekiyor? Isolated mod, her bağlama kendi portlarını ve yapılandırmasını veriyor.

## Arka planda nasıl çalışıyor

`--isolated` geçirdiğinizde, CLI çalıştırma için benzersiz bir örnek kimliği oluşturuyor. Bu iki davranışı yönlendiriyor:

1. **Port rastgeleleştirmesi** — AppHost yapılandırmanızda tanımlanan öngörülebilir portlara bağlanmak yerine, isolated mod her şey için — dashboard, servis endpoint'leri, hepsi — rastgele uygun portlar seçiyor. Servis keşfi otomatik olarak ayarlanıyor, bu nedenle servisler hangi portlara düşerlerse düşsünler birbirlerini buluyor.

2. **Secret izolasyonu** — Her izole çalıştırma, örnek kimliğiyle anahtarlanan kendi user secret deposunu alıyor. Bir çalıştırmadan bağlantı dizeleri ve API anahtarları diğerine sızmıyor.

Kodunuzun değiştirilmesi gerekmiyor. Aspire'ın servis keşfi, endpoint'leri çalışma zamanında çözümlüyor, bu nedenle port atamasından bağımsız olarak her şey doğru şekilde bağlanıyor.

## Ne zaman kullanmalı

Aynı AppHost'un birden fazla örneğini aynı anda çalıştırırken `--isolated` kullanın — ister paralel geliştirme, ister otomatik testler, ister AI ajanları, ister git worktree'ler olsun. Tahmin edilebilir portları tercih ettiğiniz tek örnekli geliştirme için, normal `aspire run` hâlâ gayet iyi çalışıyor.

## Özet

Isolated mod, gerçek ve giderek yaygınlaşan bir sorunu çözen küçük bir özellik. AI destekli geliştirme bizi daha fazla paralel iş akışına — birden fazla ajan, birden fazla worktree, birden fazla bağlam — doğru iterken, portlar için çakışmadan yeni bir örnek başlatabilme yeteneği vazgeçilmez hale geliyor.

Tüm teknik ayrıntılar için [tam yazıyı](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) okuyun ve 13.2'yi almak için `aspire update --self` ile deneyin.
