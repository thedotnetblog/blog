---
title: "GPT-5.5 Burada ve Azure Foundry'e Geliyor — .NET Geliştiricilerinin Bilmesi Gerekenler"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 Microsoft Foundry'de genel kullanıma sunuldu. GPT-5'ten 5.5'e evrim, gerçekte ne gelişti ve bugün agentlarınızda nasıl kullanmaya başlayacağınız."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Microsoft, [GPT-5.5'in Microsoft Foundry'de genel kullanıma sunulduğunu](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) duyurdu. Azure'da agent oluşturuyorsanız, beklediğiniz güncelleme bu.

## GPT-5 Evrimi

- **GPT-5**: akıl yürütme ve hızı tek bir sistemde birleştirdi
- **GPT-5.4**: daha güçlü çok adımlı akıl yürütme, enterprise için erken ajansal özellikler
- **GPT-5.5**: daha derin uzun bağlam akıl yürütme, daha güvenilir ajansal yürütme, daha iyi token verimliliği

## Gerçekte ne değişti

**Geliştirilmiş ajansal kodlama**: GPT-5.5, büyük kod tabanlarında bağlamı korur, mimari düzeydeki hataları teşhis eder ve test gereksinimlerini öngörür. Model, harekete geçmeden önce bir düzeltmenin *başka neyi* etkilediğini akıl yürütür.

**Token verimliliği**: Daha az token ve daha az yeniden denemeyle daha yüksek kaliteli çıktılar. Üretimde doğrudan düşük maliyet ve gecikme.

## Fiyatlandırma

| Model | Girdi ($/M token) | Önbelleğe alınmış | Çıktı ($/M token) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5,00 | $0,50 | $30,00 |
| GPT-5.5 Pro | $30,00 | $3,00 | $180,00 |

## Foundry Neden Önemli

Foundry Agent Service, agentları YAML'de tanımlamanıza veya Microsoft Agent Framework, GitHub Copilot SDK, LangGraph ya da OpenAI Agents SDK ile bağlamanıza olanak tanır — ve bunları kalıcı dosya sistemi, Microsoft Entra kimliği ve sıfıra ölçekleme fiyatlandırmasıyla izole barındırılan agentlar olarak çalıştırır.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Yardımcı bir asistansınız.", name: "BenimAgentim");
```

Tüm ayrıntılar için [tam duyuruya](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) bakın.
