---
title: "Azure SDK Nisan 2026: AI Foundry 2.0 ve .NET Geliştiricilerinin Bilmesi Gerekenler"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Nisan 2026 Azure SDK sürümü, önemli breaking changes'lerle Azure.AI.Projects 2.0.0 stable, Cosmos DB için kritik güvenlik düzeltmeleri ve .NET için yeni Provisioning kütüphaneleri dalgası getiriyor."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "index.md" >}}).*

Aylık SDK sürümlerini atlamak kolaydır. Bu sürümde dikkat etmeye değer birkaç şey var — özellikle AI Foundry ile, Java'da Cosmos DB ile veya .NET kodundan altyapı provisioning yapıyorsanız.

## Azure.AI.Projects 2.0.0 — Mantıklı breaking changes

`Azure.AI.Projects` NuGet paketi bazı önemli mimari değişikliklerle stable 2.0.0'a ulaşıyor. Preview kullanıyorsanız, değişenler şunlar:

- **Namespace ayrımı**: Evaluations `Azure.AI.Projects.Evaluation` altına taşındı, memory operations ise `Azure.AI.Projects.Memory` altına. `using` ifadelerinizi güncellemeniz gerekecek.
- **Yeniden adlandırılan tipler**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Adlandırma kuralları**: boolean property'ler artık tutarlı şekilde `Is*` kuralını izliyor

Bunlar, bir kez can acıtan ve sonra sonsuza kadar doğru hissettiren breaking changes türü. Preview üzerinde build aldıysanız importları güncelleyin ve gerisini compiler'ın işaretlemesine izin verin.

İyi haber: artık stable. Bu API'ye gerçekten güvenebilirsiniz.

## Cosmos DB Java: kritik güvenlik düzeltmesi (RCE)

Bu ciddi. Java Cosmos DB kütüphanesi (`azure-cosmos`) 4.79.0 sürümü, **Remote Code Execution vulnerability (CWE-502)** için kritik bir güvenlik düzeltmesi içeriyor.

Sorun, `CosmosClientMetadataCachesSnapshot`, `AsyncCache` ve `DocumentCollection` içinde Java deserialization'dı. Düzeltme, Java deserialization'ı JSON tabanlı serialization ile değiştirerek deserialization saldırılarının tüm sınıfını ortadan kaldırıyor.

Azure Cosmos DB kullanan Java servisleriniz varsa, hemen 4.79.0'a güncelleyin. Bu isteğe bağlı değil.

## .NET için yeni Provisioning kütüphaneleri

Bu ay birkaç stable Provisioning kütüphanesi 1.0.0'a geldi — bunlar Azure altyapısını ARM template'leri veya Bicep yerine C# koduyla tanımlamanızı sağlayan kütüphaneler:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

Beta.1'de birkaç tane daha var; API Management, Batch, Compute, Monitor, MySQL ve Security Center'ı kapsıyor. .NET'ten infrastructure-as-code yapıyorsanız — özellikle Aspire dağıtımlarıyla — bu kütüphaneler giriş noktanızdır.

## Azure AI Agents Java: 2.0.0 GA

Java Azure AI Agents kütüphanesi de bu ay general availability'ye ulaşıyor. Başlıca breaking changes:

- Birkaç enum tipi `ExpandableStringEnum` tabanlı sınıflara dönüştürüldü (yeni değerler için daha esnek)
- `*Param` model sınıfları `*Parameter` olarak yeniden adlandırıldı
- `MCPToolConnectorId` → `McpToolConnectorId` (tutarlı büyük/küçük harf kullanımı)
- `beginUpdateMemories` için yeni convenience overload

## Kapanış

Bu ay .NET geliştiricileri için başlık net: `Azure.AI.Projects 2.0.0` stable oluyor — AI Foundry ile geliştiriyorsanız, şimdi stable sürüme pin'leyip importları güncelleme zamanı. Cosmos DB kullanan Java ekipleri içinse güvenlik güncellemesi acil.

Tam sürüm notları [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases) adresinde. Orijinal yazı: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).