---
title: "Microsoft Agent Framework 1.0 Çıktı — .NET Geliştiricileri İçin Gerçekten Önemli Olan"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0, kararlı API'ler, çok ajanlı orkestrasyon ve her büyük AI sağlayıcısı için bağlayıcılarla üretime hazır. .NET geliştiricisi olarak bilmeniz gerekenler."
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agent-framework-1-0-production-ready" >}}).*

Erken Semantic Kernel ve AutoGen günlerinden bu yana Agent Framework yolculuğunu takip ediyorsanız, bu önemli bir gelişme. Microsoft Agent Framework [1.0 sürümüne ulaştı](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) — üretime hazır, kararlı API'ler, uzun vadeli destek taahhüdü. .NET ve Python için mevcut ve gerçek iş yükleri için gerçekten hazır.

Duyuru gürültüsünü bir kenara bırakıp .NET ile AI destekli uygulamalar geliştiriyorsanız önemli olana odaklanalım.

## Kısa özet

Agent Framework 1.0, Semantic Kernel ve AutoGen olan şeyi tek bir açık kaynaklı SDK'da birleştiriyor. Tek ajan soyutlaması. Tek orkestrasyon motoru. Birden fazla AI sağlayıcısı. Enterprise kalıpları için Semantic Kernel ile araştırma düzeyinde çok ajanlı iş akışları için AutoGen arasında gidip geliyorsanız, artık durabilirsiniz. Bu artık tek SDK.

## Başlamak neredeyse haksız derecede basit

İşte .NET'te çalışan bir ajan:

```csharp
// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry;
using Azure.Identity;

var agent = new AIProjectClient(endpoint: "https://your-project.services.ai.azure.com")
    .GetResponsesClient("gpt-5.3")
    .AsAIAgent(
        name: "HaikuBot",
        instructions: "You are an upbeat assistant that writes beautifully."
    );

Console.WriteLine(await agent.RunAsync("Write a haiku about shipping 1.0."));
```

Hepsi bu. Birkaç satırla Azure Foundry üzerinde çalışan bir AI ajanınız var. Python'daki karşılığı da aynı derecede özlü. Fonksiyon araçları, çok turlu konuşmalar ve akışı ilerledikçe ekleyin — API yüzeyi tuhaflaşmadan ölçekleniyor.

## Çok ajanlı orkestrasyon — gerçek olan bu

Tekli ajanlar demo için iyidir, ancak üretim senaryoları genellikle koordinasyon gerektirir. Agent Framework 1.0, Microsoft Research ve AutoGen'den doğrudan savaşta test edilmiş orkestrasyon kalıpları içeriyor:

- **Sequential** — ajanlar sırayla işler (yazar → gözden geçiren → editör)
- **Concurrent** — birden fazla ajana paralel olarak yayılın, sonuçları birleştirin
- **Handoff** — bir ajan amaca göre diğerine devreder
- **Group chat** — birden fazla ajan tartışır ve çözümde birleşir
- **Magentic-One** — MSR'den araştırma sınıfı çok ajanlı kalıp

Hepsi akış, denetim noktası, human-in-the-loop onayları ve duraklatma/devam etmeyi destekliyor. Denetim noktası kısmı kritik — uzun süreli iş akışları işlem yeniden başlatmalarından kurtulur.

## En önemli özellikler

**Middleware kancaları.** ASP.NET Core'daki middleware pipeline'larını biliyor musunuz? Aynı konsept, ama ajan yürütmesi için. Her aşamayı kesin — içerik güvenliği, günlükleme, uyumluluk politikaları ekleyin — ajan istemlere dokunmadan.

**Takılabilir bellek.** Konuşma geçmişi, kalıcı anahtar-değer durumu, vektör tabanlı alma. Backend'inizi seçin: Foundry Agent Service, Mem0, Redis, Neo4j veya kendinizinkini yazın.

**Bildirimsel YAML ajanları.** Ajanınızın talimatlarını, araçlarını, belleğini ve orkestrasyon topolojisini sürüm kontrollü YAML dosyalarında tanımlayın. Tek bir API çağrısıyla yükleyin ve çalıştırın.

**A2A ve MCP desteği.** MCP (Model Context Protocol) ajanların harici araçları dinamik olarak keşfetmesine ve çağırmasına olanak tanır. A2A (Agent-to-Agent protocol) çalışma zamanları arası işbirliğini sağlar.

## İzlenmeye değer önizleme özellikleri

- **DevUI** — ajan yürütmeyi, mesaj akışlarını ve araç çağrılarını gerçek zamanlı olarak görselleştirmek için tarayıcı tabanlı yerel hata ayıklayıcı.
- **GitHub Copilot SDK ve Claude Code SDK** — Copilot veya Claude'u doğrudan orkestrasyon kodunuzdan ajan koşum takımı olarak kullanın.
- **Agent Harness** — ajanlara kabuk, dosya sistemi ve mesajlaşma döngülerine erişim sağlayan özelleştirilebilir yerel çalışma zamanı.
- **Skills** — tekrar kullanılabilir alan yeteneği paketleri.

## Semantic Kernel veya AutoGen'den geçiş

Mevcut Semantic Kernel veya AutoGen kodunuz varsa, kodunuzu analiz eden ve adım adım geçiş planları üreten özel geçiş yardımcıları mevcuttur.

## Sonuç

Agent Framework 1.0, enterprise ekiplerin beklediği üretim kilometre taşıdır. Kararlı API'ler, çoklu sağlayıcı desteği ve gerçekten ölçekte çalışan orkestrasyon kalıpları.

Framework [GitHub'da tamamen açık kaynak](https://github.com/microsoft/agent-framework). "Üretimde kullanmak güvenli" sinyalini bekliyorsanız — işte bu.
