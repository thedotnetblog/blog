---
title: "Agentic Platform Engineering Gerçeğe Dönüşüyor — Git-APE Nasıl Yapıldığını Gösteriyor"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft'in Git-APE projesi agentic platform engineering'i pratiğe taşıyor — GitHub Copilot ajanları ve Azure MCP kullanarak doğal dil isteklerini doğrulanmış bulut altyapısına dönüştürüyor."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform engineering, konferanslarda harika söylemesi ama genellikle "dahili bir portal ve Terraform sarmalayıcısı oluşturduk" anlamına gelen terimlerden biri. Gerçek söz — gerçekten güvenli, yönetilen ve hızlı self-service altyapı — her zaman birkaç adım uzakta kaldı.

Azure ekibi az önce [agentic platform engineering serisinin 2. Bölümünü](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) yayımladı. Buna **Git-APE** diyorlar — GitHub Copilot ajanlarını ve Azure MCP sunucularını kullanarak doğal dil isteklerini doğrulanmış, dağıtılmış altyapıya dönüştüren açık kaynaklı bir proje.

## Git-APE gerçekte ne yapıyor

Temel fikir: geliştiriciler Terraform modüllerini öğrenmek yerine bir Copilot ajanıyla konuşur. Ajan amacı yorumlar, Infrastructure-as-Code üretir, politikalara göre doğrular ve dağıtır — hepsi VS Code'da.

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Çalışma alanını VS Code'da açın; ajan yapılandırma dosyaları GitHub Copilot tarafından otomatik keşfedilir:

```
@git-ape deploy a function app with storage in West Europe
```

Temizleme de aynı derecede kolay:

```
@git-ape destroy my-resource-group
```

## Neden önemli

Azure üzerine inşa edenler için bu, platform engineering konuşmasını "portal nasıl inşa ederiz"den "guardraillerimizi API olarak nasıl tanımlarız"a taşıyor.

.NET geliştiricisi olarak: Azure MCP Server ve GitHub Copilot ajanları herhangi bir Azure iş yüküyle çalışır — ASP.NET Core API'niz, .NET Aspire yığınınız — hepsi ajentic dağıtım akışının hedefi olabilir.

## Sonuç

Git-APE, pratikte agentic platform engineering'in erken ama somut bir görünümü. [Repoyu](https://github.com/Azure/git-ape) klonlayın ve [tam yazıyı](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) okuyun.
