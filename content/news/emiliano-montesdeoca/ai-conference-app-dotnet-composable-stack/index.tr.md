---
title: ".NET'in Birleştirilebilir Stack'i ile Yapay Zeka Destekli Konferans Uygulaması Oluşturma"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft, ConferencePulse'u oluşturdu — Microsoft.Extensions.AI, DataIngestion, VectorData, MCP ve Agent Framework'ü bir araya getirerek canlı konferans Blazor uygulaması. Parçaların nasıl bir araya geldiğini açıklıyoruz."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[.NET'in Birleştirilebilir Stack'i ile Yapay Zeka Destekli Konferans Uygulaması Oluşturma](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft, beş .NET uzantı kütüphanesini bir araya getirerek canlı konferans oturumları için bir Blazor Server uygulaması olan ConferencePulse'u oluşturdu. MVP Summit'te kullanıldı.

## ConferencePulse ne yapar

ConferencePulse canlı oturumlar sırasında çalışır ve şunları sağlar: oturum içeriğinden AI tarafından oluşturulan anketler, canlı bir bilgi tabanından RAG pipeline'ı ile dinleyici Soru-Cevap, otomatik oluşturulan içgörüler ve birden fazla eş zamanlı AI ajanı tarafından üretilen oturum özetleri. Stack .NET 10, Blazor Server, Aspire'dan oluşur ve beş projeye bölünmüştür: Web, Core, Ingestion, Agents, Mcp ve AppHost.

## Microsoft.Extensions.AI: her şey için tek soyutlama

`IChatClient` birleşik soyutlamadır — bir kez yapılandırılır ve aynı arayüz Azure OpenAI, OpenAI, Anthropic veya diğer sağlayıcılar için çalışır. Fonksiyon çağırma, OpenTelemetry izleme ve loglama middleware'i ile tam yapılandırılmış bir istemci için altı satır:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

Aynı `IChatClient` daha sonra veri alımı zenginleştirme adımı için yeniden kullanılır — bunun için ayrı bir istemciye gerek yoktur.

## DataIngestion pipeline'ı

Oturum içeriği bir pipeline'dan geçer: `MarkdownReader` → `HeaderChunker` (500 token, 50 token örtüşme) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Zenginleştiriciler, indeksleme öncesinde özet oluşturmak ve anahtar kelimeleri çıkarmak için aynı `IChatClient`'ı kullanır. Dinleyici soruları, Soru-Cevap çiftleri ve anket sonuçları oturum ilerledikçe gerçek zamanlı olarak alınır — bilgi tabanı konuşma sırasında büyür.

## VectorData: sağlayıcıdan bağımsız arama

`VectorStoreCollection.SearchAsync()`, destekleyici depo Qdrant veya Azure AI Search olsun, aynı şekilde çalışır. Hibrit arama (vektör + tam metin) desteklenmektedir. Dinleyici Soru-Cevap için RAG pipeline'ı bu koleksiyonu sorgular ve sohbet istemcisine bağlam olarak iletmek üzere ilgili parçaları geri alır.

## MCP: araç olarak oturum içeriği

Oturum içeriği, MCP uyumlu herhangi bir istemcinin erişebilmesi için MCP aracılığıyla açığa çıkarılır. Hem sunucu hem de istemci uygulanmıştır — sunucu, oturum bilgisini MCP araçları olarak açığa çıkarır ve istemci, ajan pipeline'ı içinden bu araçların çağrılmasına olanak tanır.

## Agent Framework: paralel çoklu ajan özeti

Oturum özeti, eş zamanlı olarak çalışan üç ajan tarafından oluşturulur — `PollSummaryAgent`, `QuestionSummaryAgent` ve `InsightSummaryAgent` — ardından birleştirilir. Bu, Microsoft Agent Framework'ün grup sohbeti veya paralel yürütme modelini kullanır. Her ajan bir konuyu ele alır; orkestratör çıktıları birleştirir.

## Tasarım ilkesi

Yazı, akılda tutmaya değer bir nokta vurguluyor: en basit uygun aracı kullanın. Basit üretim görevleri için doğrudan `IChatClient` çağrıları. Yapılandırılmış veri çıkarma için araç/fonksiyon çağrısı. Yalnızca özerk çok adımlı akıl yürütmeye ihtiyaç duyulduğunda tam ajanlar. Kütüphane katmanlama bunu zorunlu kılar — tam Agent Framework'ü dahil etmeden `Microsoft.Extensions.AI`'yi kullanabilirsiniz.

Tam proje yapısı ve kaynak bağlantıları için [tam yazıya](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) bakın.
