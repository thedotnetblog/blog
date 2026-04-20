---
title: "Microsoft Agent Framework'te Arka Plan Yanıtları: Timeout Endişesine Son"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework artık devam tokenları ile uzun süreli yapay zeka görevlerini arka plana almanıza izin veriyor. Arka plan yanıtlarının nasıl çalıştığı ve .NET agentlarınız için neden önemli olduğu."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

o3 veya GPT-5.2 gibi akıl yürütme modelleriyle bir şeyler geliştirdiyseniz, acıyı biliyorsunuzdur. Agentınız karmaşık bir görevi işlemeye başlar, istemci bekler ve bir yerlerde bağlantı zaman aşımına uğrar.

Microsoft Agent Framework, [arka plan yanıtlarını](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) yeni yayımladı — ve dürüst olmak gerekirse, bu özelliklerin ilk günden beri var olması gerekirdi.

## Devam tokenları nasıl çalışır

Engelleme yerine, agent görevini başlatır ve bir **devam tokeni** alırsınız. Bunun için tamir dükkânındaki iş fişi gibi düşünün:

1. `AllowBackgroundResponses = true` ile isteğinizi gönderin
2. Agent arka plan işlemeyi destekliyorsa bir devam tokeni alırsınız
3. Token `null` dönene kadar zamanlananıza göre sorgulayın

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

## Ne zaman kullanılır

- **Karmaşık akıl yürütme görevleri** — çok adımlı analiz, derin araştırma
- **Uzun içerik üretimi** — ayrıntılı raporlar, çok parçalı belgeler
- **Güvenilmez ağlar** — mobil istemciler, uç dağıtımlar
- **Asenkron UX kalıpları** — görevi gönder, başka şeyler yap, sonuçlar için geri gel

[Tam belgelere](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) göz atın.
