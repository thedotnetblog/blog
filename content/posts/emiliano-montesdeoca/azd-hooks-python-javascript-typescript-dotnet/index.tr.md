---
title: "Python, TypeScript ve .NET ile azd Hook Yazma: Shell Script'lere Veda"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI artık Python, JavaScript, TypeScript veya .NET ile hook yazmayı destekliyor. Sadece bir migrasyon scripti çalıştırmak için Bash'e geçmek zorunda kalmayacaksınız."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Tamamen .NET ile yazılmış bir projeniz olmasına rağmen azd hook'ları için Bash scriptleri yazmak zorunda kaldıysanız, bu acıyı iyi biliyorsunuzdur. Projenin geri kalanı C# iken, neden bir pre-provisioning adımı için shell sözdizimine geçiş yapmak zorunda kalınsın?

Bu hayal kırıklığı artık resmi bir çözüme kavuştu. Azure Developer CLI [hook'lar için çok dilli destek yayımladı](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) ve tam olarak duyulduğu kadar iyi.

## Hook nedir?

Hook'lar, `azd` yaşam döngüsünün kritik noktalarında çalışan scriptlerdir — provisioning öncesi, deployment sonrası vb. `azure.yaml` içinde tanımlanır ve CLI'yi değiştirmeden özel mantık eklemenizi sağlar.

Önceden yalnızca Bash ve PowerShell destekleniyordu. Artık **Python, JavaScript, TypeScript veya .NET** kullanılabilir — `azd` geri kalanını otomatik olarak halleder.

## Algılama nasıl çalışır

Yalnızca hook'u bir dosyaya yönlendirin; `azd` uzantıdan dili çıkarır:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Ek yapılandırma gerekmez. Uzantı belirsizse `kind: python` (veya ilgili dil) ile açıkça belirtebilirsiniz.

## Dile göre önemli ayrıntılar

### Python

Scriptin yanına (veya herhangi bir üst dizine) `requirements.txt` ya da `pyproject.toml` koyun. `azd` otomatik olarak sanal ortam oluşturur, bağımlılıkları kurar ve scripti çalıştırır.

### JavaScript ve TypeScript

Aynı desen — script yakınına `package.json` koyun ve `azd` önce `npm install` çalıştırır. TypeScript için derleme adımı ve `tsconfig.json` gerekmeden `npx tsx` kullanılır.

### .NET

İki mod mevcuttur:

- **Proje modu**: Script yanında `.csproj` varsa `azd` otomatik olarak `dotnet restore` ve `dotnet build` çalıştırır.
- **Tek dosya modu**: .NET 10+ sürümünde bağımsız `.cs` dosyaları `dotnet run script.cs` ile doğrudan çalıştırılabilir. Proje dosyası gerekmez.

## Executor'a özgü yapılandırma

Her dil isteğe bağlı bir `config` bloğunu destekler:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## .NET geliştiricileri için önemi

Hook'lar, azd tabanlı bir projede dil değiştirmeyi zorunlu kılan son yerdi. Artık uygulama kodu, altyapı scriptleri ve yaşam döngüsü hook'ları dahil tüm deployment pipeline'ı tek bir dilde yaşayabilir. Mevcut .NET yardımcı programlarını hook'larda yeniden kullanabilir, paylaşılan kütüphanelere referans verebilir ve shell script bakımından kurtulabilirsiniz.

## Sonuç

Küçük görünse de azd günlük iş akışından çok fazla sürtünme kaldıran değişikliklerden biri. Hook'lar için çok dilli destek şu anda kullanılabilir — [resmi gönderi](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)nde tam belgelere ulaşabilirsiniz.
