---
title: "Ajanlı Platform Mühendisliği Gerçek Oluyor — Git-APE Bunu Nasıl Yapıyor"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft'un Git-APE projesi, ajanlı platform mühendisliğini pratiğe döküyor — GitHub Copilot agentları ve Azure MCP kullanarak doğal dil isteklerini doğrulanmış bulut altyapısına dönüştürüyor."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform mühendisliği, konferans konuşmalarında harika duyulan ama genellikle "dahili bir portal ve bir Terraform sarmalayıcı geliştirdik" anlamına gelen terimlerden biridir. Gerçek vaat — gerçekten güvenli, yönetişimli ve hızlı self-servis altyapı — her zaman birkaç adım uzakta olmuştur.

Azure ekibi, [ajanlı platform mühendisliği serisinin 2. Bölümünü](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) yayımladı ve bu bölüm tamamen uygulamalı implementasyona odaklanıyor. Buna **Git-APE** (evet, kısaltma kasıtlı) diyorlar; GitHub Copilot agentları ile Azure MCP sunucularını kullanarak doğal dil isteklerini doğrulanmış, dağıtılmış altyapıya dönüştüren açık kaynak bir proje.

## Git-APE gerçekte ne yapıyor

Temel fikir şu: geliştiricilerin Terraform modüllerini öğrenmesi, portal arayüzlerinde gezinmesi veya platform ekibine bilet açması yerine, bir Copilot agentıyla konuşması. Agent niyeti yorumlar, Infrastructure-as-Code üretir, politikalara göre doğrular ve dağıtır — tümü VS Code içinde.

İşte kurulum:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Çalışma alanını VS Code'da açın; agent yapılandırma dosyaları GitHub Copilot tarafından otomatik olarak keşfedilir. Agent ile doğrudan etkileşime geçersiniz:

```
@git-ape deploy a function app with storage in West Europe
```

Agent, Azure servisleriyle etkileşim kurmak için arka planda Azure MCP Server'ı kullanır. VS Code ayarlarındaki MCP yapılandırması belirli yetenekleri etkinleştirir:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Neden önemli

Azure üzerine geliştirme yapanlar için bu, platform mühendisliği konuşmasını "nasıl bir portal inşa ederiz" yerine "kısıtlamalarımızı API'ler olarak nasıl tanımlarız" sorusuna kaydırıyor. Platformunuzun arayüzü bir AI agentı olduğunda, kısıtlamalarınızın ve politikalarınızın kalitesi ürün haline geliyor.

1. Bölüm teorisi ortaya koydu: iyi tanımlanmış API'ler, kontrol şemaları ve açık koruyucular platformları agent-hazır kılar. 2. Bölüm gerçek araçları yayımlayarak bunun işe yaradığını kanıtlıyor. Agent kaynakları körü körüne üretmez — en iyi uygulamalara karşı doğrular, adlandırma kurallarına saygı gösterir ve kuruluşunuzun politikalarını uygular.

Temizlik de aynı derecede kolaydır:

```
@git-ape destroy my-resource-group
```

## Benim görüşüm

Dürüst olacağım — bu, belirli araçtan çok desen hakkında. Git-APE'nin kendisi bir demo/referans mimarisidir. Ama temel fikir — platformunuza arayüz olarak agentlar, protokol olarak MCP, host olarak GitHub Copilot — kurumsal geliştirici deneyiminin nereye gittiğidir.

Dahili araçlarını agent-dostu hale getirmeye bakan bir platform ekibiyseniz, daha iyi bir başlangıç noktası yok. .NET geliştiricisi olarak bunun dünyanzla nasıl bağlantılı olduğunu merak ediyorsanız: Azure MCP Server ve GitHub Copilot agentları herhangi bir Azure iş yüküyle çalışır. ASP.NET Core API'niz, .NET Aspire yığınınız, konteynerize mikro servisleriniz — hepsi ajanlı bir dağıtım akışının hedefi olabilir.

## Sonuç

Git-APE, ajanlı platform mühendisliğine pratikte erken ama somut bir bakış. [Repo'yu](https://github.com/Azure/git-ape) klonlayın, demoyu deneyin ve platformunuzun API'lerinin ve politikalarının bir agentın bunları güvenle kullanması için nasıl görünmesi gerektiğini düşünmeye başlayın.

Rehber ve video demolar için [tam yazıyı](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) okuyun.
