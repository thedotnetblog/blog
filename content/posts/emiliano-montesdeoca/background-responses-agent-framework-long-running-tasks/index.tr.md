---
title: "Microsoft Agent Framework'te Arka Plan Yanıtları: Zaman Aşımı Kaygısına Son"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework artık uzun süren AI görevlerini continuation token'larla arka plana almanıza olanak tanıyor. Arka plan yanıtlarının nasıl çalıştığını ve .NET agent'larınız için neden önemli olduğunu açıklıyoruz."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

o3 veya GPT-5.2 gibi akıl yürütme modelleriyle bir şeyler geliştirdiyseniz, o acıyı biliyorsunuzdur. Agent'ınız karmaşık bir görev üzerinde düşünmeye başlıyor, istemci beklemeye devam ediyor ve "bu tamam" ile "çöktü mü acaba?" arasında bir yerde bağlantınız zaman aşımına uğruyor. Tüm o emek? Gitti.

Microsoft Agent Framework yeni [arka plan yanıtlarını](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) yayınladı — ve dürüst olmak gerekirse bu, ilk günden beri var olması gereken özelliklerden biri.

## Engelleyen çağrıların sorunu

Geleneksel istek-yanıt kalıbında, agent işini bitirene kadar istemciniz bekler. Hızlı görevler için bu sorunsuz çalışır. Ama bir akıl yürütme modelinden derin araştırma, çok adımlı analiz veya 20 sayfalık rapor oluşturması istediğinizde? Gerçek zamanlı dakikalar söz konusu. Bu pencerede:

- HTTP bağlantıları zaman aşımına uğrayabilir
- Ağ kesintileri tüm işlemi mahvedebilir
- Kullanıcınız bir şeylerin olup olmadığını merak ederek dönen bir simgeye bakmak zorunda kalır

Arka plan yanıtları bunu tersine çeviriyor.

## Continuation token'lar nasıl çalışır

Engellemek yerine, agent görevini başlatırsınız ve geriye bir **continuation token** alırsınız. Bunu bir tamirhanedeki teslimat fişi gibi düşünün — tezgahın önünde beklemezsiniz, hazır olduğunda gelirsiniz.

Akış basit:

1. `AllowBackgroundResponses = true` ile isteğinizi gönderin
2. Agent arka plan işlemeyi destekliyorsa bir continuation token alırsınız
3. Token `null` döndürene kadar kendi zamanlamanızda sorgulama yapın — bu, sonucun hazır olduğu anlamına gelir

.NET versiyonu şöyle:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Tamamlanana kadar sorgula
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Agent hemen tamamlarsa (basit görevler, arka plan işleme gerektirmeyen modeller), continuation token döndürülmez. Kodunuz sadece çalışır — özel bir işlem gerekmez.

## Devam ettirme özellikli streaming: asıl sihir

Sorgulama, fırlat-unut senaryoları için uygun, ama gerçek zamanlı ilerleme izlemek istediğinizde ne olur? Arka plan yanıtları aynı zamanda yerleşik devam ettirme özelliğiyle streaming'i de destekliyor.

Her streaming güncellemesi kendi continuation token'ını taşıyor. Bağlantınız streaming ortasında kesilirse, tam kaldığınız yerden devam ediyorsunuz:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Ağ kesintisini simüle et
}

// Tam kaldığımız yerden devam et
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

Agent, istemcinizde ne olursa olsun sunucu tarafında işlemeye devam ediyor. Bu, retry mantığı veya circuit breaker yazmadan yerleşik hata toleransı demek.

## Bunu gerçekten ne zaman kullanmalısınız

Her agent çağrısının arka plan yanıtlarına ihtiyacı yok. Hızlı tamamlamalar için gereksiz yere karmaşıklık ekliyor olursunuz. Ama bunların parlattığı durumlar şunlar:

- **Karmaşık akıl yürütme görevleri** — çok adımlı analiz, derin araştırma, bir akıl yürütme modelinin gerçekten düşünmesi gereken her şey
- **Uzun içerik üretimi** — ayrıntılı raporlar, çok bölümlü belgeler, kapsamlı analizler
- **Güvenilmez ağlar** — mobil istemciler, edge dağıtımlar, kararsız kurumsal VPN'ler
- **Asenkron UX kalıpları** — görevi gönder, başka bir şey yap, sonuçlar için geri gel

Kurumsal uygulamalar geliştiren .NET geliştiricileri olarak bizim için özellikle son madde ilginç. Kullanıcının karmaşık bir rapor talep ettiği bir Blazor uygulaması düşünün — agent görevini başlatırsınız, ilerleme göstergesi gösterirsiniz ve kullanıcının çalışmaya devam etmesine izin verirsiniz. WebSocket karmaşası yok, özel kuyruk altyapısı yok, sadece bir token ve bir sorgulama döngüsü.

## Sonuç

Arka plan yanıtları Microsoft Agent Framework üzerinden şu anda hem .NET hem de Python'da mevcut. Basit soru-cevabın ötesinde herhangi bir şey yapan agent'lar geliştiriyorsanız, bunu araç kutunuza eklemeye değer. Continuation token kalıbi, gerçek bir üretim sorununu çözerken işleri basit tutuyor.

Tam API referansı ve daha fazla örnek için [belgelere](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) bakın.
