---
title: "Ajanınız Şeyleri Nerede Hatırlıyor? Sohbet Geçmişi Depolama için Pratik Rehber"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Servis tarafından mı yoksa istemci tarafından mı yönetiliyor? Doğrusal mı yoksa dallanma destekli mi? AI ajanınızın ne yapabileceğini belirleyen mimari karar — C# ve Python örnekleriyle."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Bir AI ajanı oluştururken enerjinizin büyük bölümünü modele, araçlara ve istemlere harcarsınız. *Konuşma geçmişinin nerede tutulduğu* sorusu bir uygulama ayrıntısı gibi görünür — ancak alacağınız en önemli mimari kararlardan biridir.

Kullanıcıların konuşmaları dallandırıp dallandıramayacağını, yanıtları geri alıp alamayacağını, yeniden başlatmadan sonra oturumları devam ettirip ettiremeyeceğini ve verilerinizin altyapınızı terk edip etmediğini belirler. [Agent Framework ekibi derinlemesine bir analiz yayımladı](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## İki temel desen

**Servis tarafından yönetilen**: AI servisi konuşma durumunu depolar. Uygulamanız bir referans tutar ve servis her istekte ilgili geçmişi otomatik olarak ekler.

**İstemci tarafından yönetilen**: Uygulamanız tam geçmişi tutar ve her istekte ilgili mesajları gönderir. Servis durumsuzdur. Her şeyi siz kontrol edersiniz.

## Agent Framework bunu nasıl soyutlar

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Adım Alice.", session);
var second = await agent.RunAsync("Benim adım ne?", session);
```

```python
session = agent.create_session()
first = await agent.run("Adım Alice.", session=session)
second = await agent.run("Benim adım ne?", session=session)
```

## Sağlayıcı hızlı referans

| Sağlayıcı | Depolama | Model | Sıkıştırma |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | İstemci | Yok | Siz |
| Foundry Agent Service | Servis | Doğrusal | Servis |
| Responses API (varsayılan) | Servis | Dallanma | Servis |
| Anthropic Claude, Ollama | İstemci | Yok | Siz |

## Nasıl seçilir

1. **Dallanma veya "geri al" gerekiyor mu?** → Servis tarafından yönetilen Responses API
2. **Veri egemenliği gerekiyor mu?** → DB destekli istemci tarafından yönetilen
3. **Basit bir sohbet botu mu?** → Servis tarafından yönetilen doğrusal yeterli

Tam karar ağacı için [tam makaleyi](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) okuyun.
