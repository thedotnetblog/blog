---
title: "Microsoft Agent Framework'te Dayanıklı İş Akışları: In-Memory'den Azure Functions'a"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAF'ın iş akışı programlama modeli artık Durable Task tarafından desteklenen dayanıklı çalıştırmayı destekliyor — işte süreç yeniden başlatmalarından sağ çıkan ve Azure Functions üzerinde ölçeklenen kompozit ajan iş akışları nasıl oluşturulur."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Erken AI ajan iş akışlarının sorunlarından biri: kırılgandırlar. Tek bir sürece bağlı uzun süreli çok adımlı bir iş akışı, süreç yeniden başlatması = durum kaybı anlamına gelir. Basit demolar için bu sorun değil. Üretim iş yükleri için değil.

Microsoft Agent Framework'ün iş akışı programlama modeli artık Azure Functions barındırma ile Durable Task çerçevesi tarafından desteklenen **dayanıklı çalıştırmayı** destekliyor. Programlama modelinin nasıl çalıştığını ve dayanıklılık hikayesinin neden önemli olduğunu açıklıyoruz.

## Temel Yapı Taşları

**Executor'lar** temel iş birimidir. Her biri türlendirilmiştir — belirli bir girdi alır ve belirli bir çıktı üretir:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // siparişi ara, geri döndür
        return new Order(Id: message.OrderId, ...);
    }
}
```

**İş akışları** fluent builder kullanarak executor'ları yönlendirilmiş grafiklere bağlar. Çerçeve çalıştırmayı, adımlar arasındaki veri akışını ve hata yayılımını yönetir.

Modelleyebilecekleriniz:
- Sıralı zincirler (adım A → adım B → adım C)
- Paralel fan-out/fan-in (ajan A, B, C'yi paralel çalıştır, sonuçları topla)
- Koşullu dallanma
- Human-in-the-loop onayları (iş akışını duraklat, dış sinyal bekle)

## Yerel Geliştirme için In-Memory Runner

Başlamak hızlıdır:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Temel paket, hafif bir süreç içi runner içerir. Harici bağımlılık yok, veritabanı yok, Azure kaynakları yok. Yerel geliştirme ve birim testi için mükemmel çalışır.

## Durable Task ile Dayanıklılık Ekleme

Bir iş akışının süreç yeniden başlatmalarından sağ çıkması gerektiğinde — uzun süreli olduğu için, human-in-the-loop adımları olduğu için, birçok paralel ajan çağrısına dağıldığı için — in-memory runner yeterli değildir.

MAF'ın Durable Task entegrasyonu iş akışı durumunu Azure Storage'da saklar. Süreç yeniden başlarsa, iş akışı kaldığı yerden devam eder. Programlama modeli aynı kalır; sadece runner'ı değiştirirsiniz.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Aynı executor'lar, aynı iş akışı grafiği — dayanıklı durum tarafından desteklenir.

## Azure Functions Barındırma

Üçüncü katman Azure Functions barındırmadır. İş akışınız bir Function uygulaması olur: HTTP endpoint aracılığıyla iş akışını tetikleyin ve dayanıklı runtime ölçekleme, durum ve güvenilirliği yönetir.

Bu, paralel çağrılar, koşullu dallar ve insan onayları içeren çok ajanlı bir iş akışının özel durum yönetimi olmadan sunucusuz Functions ortamında ölçeklenebileceği anlamına gelir.

## Bu Neden Önemli

Bu kombinasyon gerçek AI sistemleri için önemlidir:

- **Paralel ajan çağrıları** — bloklamadan birden fazla uzmanlaşmış ajana aynı anda dağıtın, tümü tamamlandığında sonuçları toplayın
- **Uzun süreli süreçler** — insan onayı veya harici olaylar içeren iş akışları saatler veya günler boyunca duraklatıp devam edebilir
- **Ölçekleme** — Azure Functions çalıştırmayı yatay olarak ölçekler; Durable Task çerçevesi paralel durum koordinasyonunu yönetir

Basit yerel demolar ötesinde MAF iş akışları oluşturuyorsanız, üretim kalitesinde çalıştırmanın yolu budur.

Orijinal yazı: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
