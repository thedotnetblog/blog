---
title: "Microsoft Agent Framework 1.0 Yayımlandı — .NET Geliştiricileri İçin Gerçekten Önemli Olan Şeyler"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0, kararlı API'lar, çoklu-agent orkestrasyonu ve tüm büyük AI sağlayıcıları için bağlayıcılarla üretime hazır hale geldi. Bir .NET geliştiricisi olarak bilmeniz gerekenler."
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agent-framework-1-0-production-ready" >}}).*

Erken Semantic Kernel ve AutoGen günlerinden bu yana Agent Framework yolculuğunu takip ediyorsanız, bu gelişme önemli. Microsoft Agent Framework [1.0 sürümüne ulaştı](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) — üretime hazır, kararlı API'lar, uzun vadeli destek taahhüdü. Hem .NET hem de Python için mevcut ve gerçek iş yükleri için gerçekten hazır.

Duyuru gürültüsünü bir kenara bırakarak, .NET ile AI destekli uygulamalar geliştiriyorsanız önemli olan şeylere odaklanayım.

## Özet

Agent Framework 1.0, eski Semantic Kernel ve AutoGen'i tek, açık kaynaklı bir SDK'da birleştirir. Tek bir agent soyutlaması. Tek bir orkestrasyon motoru. Birden fazla AI sağlayıcısı. Kurumsal desenler için Semantic Kernel ile araştırma düzeyindeki çoklu-agent iş akışları için AutoGen arasında gidip geliyorsanız, buna son verebilirsiniz. Artık tek SDK bu.

## Başlamak neredeyse haksız derecede kolay

İşte .NET'te çalışan bir agent:

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

Bu kadar. Birkaç satırla Azure Foundry üzerinde çalışan bir AI agentınız var. Python karşılığı da aynı derecede özlü. İlerlediğinizde function araçları, çok turlu konuşmalar ve streaming ekleyin — API yüzeyi tuhaflaşmadan büyür.

## Çoklu-agent orkestrasyonu — işte asıl konu bu

Tek agentlar demolar için güzel, ama üretim senaryoları genellikle koordinasyon gerektirir. Agent Framework 1.0, Microsoft Research ve AutoGen'den gelen savaşta test edilmiş orkestrasyon desenlerini içerir:

- **Sequential (Sıralı)** — agentlar sırayla işler (yazar → gözden geçiren → editör)
- **Concurrent (Eş zamanlı)** — birden fazla agenta paralel olarak yayıl, sonuçları birleştir
- **Handoff (Devir teslim)** — bir agent, niyete göre başka birine devreder
- **Group chat (Grup sohbeti)** — birden fazla agent tartışır ve bir çözümde uzlaşır
- **Magentic-One** — MSR'den araştırma düzeyindeki çoklu-agent deseni

Tümü streaming, checkpointing, human-in-the-loop onayları ve duraklat/devam et özelliklerini destekler. Checkpointing kısmı kritik — uzun süreli iş akışları süreç yeniden başlatmalarını atlatır. Azure Functions ile dayanıklı iş akışları geliştirmiş .NET geliştiricileri için bu tanıdık hissettiriyor.

## En önemli özellikler

Bilmeye değer şeylerin kısa listesi:

**Middleware kancaları.** ASP.NET Core'un middleware pipeline'ları var ya? Aynı kavram, ama agent yürütmesi için. Her aşamayı yakalayın — içerik güvenliği, loglama, uyumluluk politikaları ekleyin — agent prompt'larına dokunmadan. Agentları kurumsal düzeyde hazır kılmanın yolu budur.

**Takılabilir bellek.** Konuşma geçmişi, kalıcı anahtar-değer durumu, vektör tabanlı erişim. Backend'inizi seçin: Foundry Agent Service, Mem0, Redis, Neo4j veya kendinizinkini yazın. Bellek, durumsuz bir LLM çağrısını gerçekten bağlamı hatırlayan bir agenta dönüştüren şeydir.

**Bildirimsel YAML agentları.** Agentınızın talimatlarını, araçlarını, belleğini ve orkestrasyon topolojisini sürüm kontrollü YAML dosyalarında tanımlayın. Tek bir API çağrısıyla yükleyin ve çalıştırın. Bu, kod yeniden dağıtmadan agent davranışını yinelemek isteyen ekipler için oyun değiştiricidir.

**A2A ve MCP desteği.** MCP (Model Context Protocol), agentların harici araçları dinamik olarak keşfetmesine ve çağırmasına izin verir. A2A (Agent-to-Agent protokolü), çalışma zamanları arası işbirliğini mümkün kılar — .NET agentlarınız diğer framework'lerde çalışan agentlarla koordinasyon kurabilir. A2A 1.0 desteği yakında geliyor.

## Takip etmeye değer önizleme özellikleri

Bazı özellikler 1.0'da önizleme olarak yayımlandı — işlevsel ama API'lar gelişebilir:

- **DevUI** — agent yürütmesini, mesaj akışlarını ve araç çağrılarını gerçek zamanlı olarak görselleştirmek için tarayıcı tabanlı yerel hata ayıklayıcı. Application Insights gibi ama agent muhakemesi için.
- **GitHub Copilot SDK ve Claude Code SDK** — Copilot veya Claude'u doğrudan orkestrasyon kodunuzdan agent harness'i olarak kullanın. Kod yazabilen bir agentı aynı iş akışındaki diğer agentlarla birleştirin.
- **Agent Harness** — agentlara shell, dosya sistemi ve mesajlaşma döngülerine erişim sağlayan özelleştirilebilir yerel çalışma zamanı. Kodlama agentları ve otomasyon desenlerini düşünün.
- **Skills** — agentlara kullanıma hazır yapılandırılmış yetenekler sunan yeniden kullanılabilir alan yetkinliği paketleri.

## Semantic Kernel veya AutoGen'den geçiş

Mevcut Semantic Kernel veya AutoGen kodunuz varsa, kodunuzu analiz eden ve adım adım geçiş planları üreten özel geçiş asistanları mevcuttur. [Semantic Kernel geçiş rehberi](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel) ve [AutoGen geçiş rehberi](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen) her şeyi adım adım anlatıyor.

RC paketlerindeyseniz, 1.0'a yükseltme sadece bir sürüm güncellemesidir.

## Sonuç

Agent Framework 1.0, kurumsal ekiplerin beklediği üretim mihenk taşıdır. Kararlı API'lar, çoklu sağlayıcı desteği, gerçek ölçekte çalışan orkestrasyon desenleri ve hem Semantic Kernel hem de AutoGen'den geçiş yolları.

Framework [GitHub'da tamamen açık kaynak](https://github.com/microsoft/agent-framework) ve `dotnet add package Microsoft.Agents.AI` ile bugün başlayabilirsiniz. Ellerinizi kirletmek için [hızlı başlangıç rehberine](https://learn.microsoft.com/en-us/agent-framework/get-started/) ve [örneklere](https://github.com/microsoft/agent-framework) göz atın.

"Üretimde kullanmak güvenli" sinyalini bekliyorsanız — işte bu.
