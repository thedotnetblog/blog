---
title: "A2A v1 Burada: Microsoft Agent Framework for .NET'te Platformlar Arası Ajan İletişimi"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "A2A Protokolü v1.0 yayınlandı ve Microsoft Agent Framework .NET paketleri güncellendi — sağlayıcılar arasında AI ajanlarını bağlamak ve açığa çıkarmak için kararlı birlikte çalışabilirlik standardı."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[A2A v1 Burada: Microsoft Agent Framework for .NET'te Platformlar Arası Ajan İletişimi](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — A2A Protokolü v1.0'a ulaştı ve .NET için hem A2A Agent (istemci) hem de A2A Hosting (sunucu) paketleri güncellendi.

## A2A v1 Gerçekte Nedir

A2A, AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP ve ServiceNow temsilcilerinden oluşan teknik yönlendirme komitesi tarafından desteklenen AI ajanları için açık bir birlikte çalışabilirlik protokolüdür. v1 etiketi, artık kararlı ve üretime hazır bir standart olduğu anlamına gelir. Bunu uygulayan SDK ve Agent Framework paketleri hâlâ önizleme aşamasında, ancak protokolün kendisi kilitlenmiş durumda.

v1, v0.3'ü çok kiracılı destek, kriptografik kimlik için imzalı Agent Cards, geliştirilmiş güvenlik akışları ve web uyumlu mimari ile iyileştiriyor.

## Uzak Bir A2A Ajanına Bağlanma

Uzak bir A2A ajanı kodunuzda sadece bir `AIAgent`'tır — aynı `RunAsync`, aynı akış, aynı oturum yönetimi:

```csharp
// Well-known URI aracılığıyla keşif
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Doğrudan yapılandırma
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Akış aynı şekilde çalışır
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Ajanınızı A2A Uç Noktası Olarak Açığa Çıkarma

Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic veya AWS Bedrock üzerinde oluşturduğunuz herhangi bir `AIAgent`, ASP.NET Core'da iki satırla A2A uç noktası olarak açığa çıkarılabilir:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

Ajan kartı `/.well-known/agent-card.json` adresinde otomatik olarak sunulur.

## Bu Pratikte Ne Anlama Gelir

Kararlı v1 protokolü, .NET ajanlarınızı Python, Java veya başka bir dilde oluşturulmuş ajanlarla yıkıcı değişiklikler konusunda endişelenmeden bağlayabileceğiniz anlamına gelir. İmzalı Agent Cards'taki kriptografik kimlik, ajanlar arasındaki güven doğrulaması için de bir temel sağlar.

Tam değişiklik günlüğü ve v0.3'ten geçiş notları için [tam gönderiye](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) bakın.
