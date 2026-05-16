---
title: "Agentic Platform Engineering ile Göç'ün Tekrarlayan İşlerini Ortadan Kaldırma"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape, gerçek bir AWS Terraform dağıtımını Azure Bicep'e taşıma sürecini gösterir — 1:1 sözdizimi dönüşümü yapmak yerine dağıtım amacını çıkararak ve mimariyi yeniden eşleyerek."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — Git-Ape'nin (git agentik platform mühendisliği aracı) gerçek bir AWS Terraform deposunu Azure'a taşıdığı, satır satır dönüştürme yerine dağıtım amacı çıkarmaya odaklanan bir rehber.

## Girdi: contoso-migration

Kaynak, AWS'de bir Next.js uygulaması dağıtan gerçek bir Terraform projesidir (`contoso-migration`) — işlem için EC2, yük dengeleme için ALB, artefaktlar için S3 ve kimlik için IAM anahtarları. Maliyet: Aylık ~34 $. Amaç, Azure'da aynı altyapıyı yeniden oluşturmak değil; dağıtımın gerçekte ne yapmaya çalıştığını anlamak ve bunu Azure-native hizmetler üzerinde yeniden inşa etmektir.

## Adım 1: Doğrulama ve kimlik doğrulama

Git-Ape, herhangi bir şeye dokunmadan önce tüm gerekli CLI araçlarını — `az`, `aws`, `gh`, `jq`, `git` — doğrulayarak ve aktif kimlik doğrulama oturumlarını onaylayarak başlar. Kısmi çalıştırma yoktur.

## Adım 2: Niyet çıkarma

Ajan, kaynak depoyu GitHub API aracılığıyla okur ve dağıtım amacını çıkarır: çalışma zamanı (Node.js), işlem türü, ingress deseni, artefakt işleme, kimlik modeli, ağ ve izleme. Bu kritik adımdır — hangi Terraform anahtar kelimelerini kullandığını değil, dağıtımın ne yaptığının semantik modelini oluşturuyor.

## Adım 3: Hizmet eşleme

AWS hizmetleri Azure eşdeğerlerine eşlenir:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → App Service yerleşik yük dengeleme
- IAM rolleri/anahtarları → Managed Identity
- Terraform → Bicep + GitHub Actions

## Adım 4: Eleştiri ajanı

Çıktı oluşturmadan önce bir eleştiri ajanı çalışır ve iki engelleyici sorunu tespit eder:

1. **Başlatmada build anti-deseni** — orijinal Terraform, EC2'de başlangıçta `npm install && npm run build` çalıştırıyordu. Düzeltme: CI'da derle, hazır bir artefakt dağıt.
2. **Gereksiz Blob Storage** — S3, uygun CI/CD ile ortadan kaldırılabilecek artefakt hazırlama için kullanılıyordu. Eleştiri ajanı bunu tamamen kaldırdı.

## Adım 5: Oluşturulan çıktı

Sonuç, orijinal 200+ satır Terraform yerine ~80 satır Bicep'tir. Ajan, `infra/main.bicep` ve `.github/workflows/deploy.yml` içeren yeni bir GitHub deposu oluşturdu ve tüm AWS'ye özgü dosyaları kaldırdı.

## Güvenlik durumu karşılaştırması

Göç aynı zamanda anlamlı bir güvenlik iyileştirmesi de sağladı:

| AWS orijinal | Azure çıktı |
|---|---|
| Yalnızca HTTP | Yalnızca HTTPS, TLS 1.2 |
| SSH 0.0.0.0/0'a açık | SSH açığı yok |
| IAM erişim anahtarları | OIDC + Managed Identity |
| İzleme yok | Application Insights |

Maliyet: Orijinal 34 $/ayın aksine ~13 $/ay.

## Bunu sözdizimi dönüştürücüden farklı kılan nedir

Eleştiri ajanı adımı, bunu mekanik bir çeviriden ayıran şeydir. AWS'de işe yarayan ancak Azure'da yanlış olacak desenleri yakaladı — ve onları kopyalamak yerine düzeltti. Çıktı "Azure sözdiziminde AWS" değil; aynı hedefi daha temiz bir şekilde başaran Azure-native bir dağıtımdır.

Tam ajan izlemesi ve oluşturulan dosyalar için [tam rehbere](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) bakın.
