---
title: "AI Ajanınızın Bir Kimlik Sorunu Var (Ve İşte Bunu Çözen Şablon)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Curity ve Microsoft'tan yeni bir azd şablonu, ince taneli kapsamlara sahip kısa ömürlü OAuth belirteçleri kullanan AI ajanlarının nasıl oluşturulacağını gösteriyor — böylece ajanlar asla görmemesi gereken verileri göremez."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Her AI ajan projesinde şöyle bir an gelir: Demo mükemmel çalışır, ajan doğal dili yorumlar, doğru API'leri çağırır, doğru verileri döndürür. Sonra gerçek kullanıcıları düşünmeye başlarsınız.

Bir kullanıcının ajan oturumunun başka bir kullanıcının verilerini görmesini ne engeller? Ya ajan, istem enjeksiyonu yoluyla kandırılırsa? Ya bir aracı beklenmedik bir şekilde çağırırsa?

Bunlar kenar durumlar değil. Bunlar yayın öncesinde vermeniz gereken tasarım kararları.

Curity ve Microsoft'tan yeni bir `azd` şablonu, tam olarak bu sorun için çalışan bir referans sağlar.

## Temel Sorun: Kimlik Doğrulama ≠ Yetkilendirme

Çoğu ajan örneği, kullanıcı kimlik doğrulamasını iyi şekilde ele alır. Yetkilendirmeyi ise kötü şekilde ele alır. Kullanıcının *kim* olduğunu bilmek, hangi *verileri* görmeleri gerektiğini söylemez.

Geleneksel bir istemci uygulaması öngörülebilir API çağrıları yapar. Bir AI ajanı deterministik değildir — doğal dili yorumlar ve neyi çağıracağına karar verir. Yaratıcı olabilir. Aynı zamanda yanılabilir. Ve istem enjeksiyonu yoluyla manipüle edilirse, AI'nin iyi davranmasına bağlı olmayan kurallara ihtiyacınız vardır.

Bu şablonun gösterdiği çözüm: **Her atlama için tam olarak doğru bilgiyi taşıyan kısa ömürlü belirteçler**.

## Belirteç Zinciri Nasıl Çalışır

Şablon, her adımda izinleri daraltmak için belirteç değişimi ile OAuth 2.0 erişim belirteçlerini kullanır. Kullanıcı belirteci, MCP sunucusuna ulaşmadan önce iki kez değiştirilir:

1. **Birinci değişim** — Kapsamı daraltır ve opak belirteci JWT'ye dönüştürür
2. **İkinci değişim** — MCP sunucu atlaması için ajan kimliği ve yeni bir hedef kitle ekler

MCP sunucu belirtecinin görünümü:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

`customer_id`, ajanın kontrol ettiği bir parametre olarak geçirilmez, yetkilendirme sunucusu tarafından belirtece gömülür. API, ajanın talimatlarını değil, belirteci kontrol eder.

Bu şu anlama gelir: Birisi ajanı başka bir müşterinin verilerini almaya zorlamaya çalışsa bile, belirteç buna izin vermez.

## Şablonun Dağıttıkları

Birkaç `azd` komutuyla şunları elde edersiniz:

- Microsoft Foundry üzerinde bir arka uç ajan (C#, Microsoft A2A ve MCP SDK'ları)
- Örnek bir portföy API'si sunan bir MCP sunucusu
- Kimlik doğrulama için Entra ID ile birlikte yetkilendirme sunucusu olarak Curity Identity Server
- Belirteç değişimini ve denetim kaydını işleyen harici ve dahili API ağ geçitleri
- Tüm Azure altyapısı için Bicep: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, depolama

Desenin tamamı incelenebilir ve özelleştirilebilir.

## Ödünç Almaya Değer Tasarım İlkesi

Curity kullanmasanız bile, desen aktarılabilir: **Ajanlar asla kalıcı API erişimine sahip olmamalıdır**. Her eylem, söz konusu spesifik çağrı için gereken minimum kapsama sahip kısa ömürlü bir belirteç kullanmalı, spesifik ajan kimliği için düzenlenmeli, API'nin yetkilendirme kararları almak için ihtiyaç duyduğu talepleri taşımalıdır.

Bu, yaratıcı ajanlara, hatalara ve istem enjeksiyonuna karşı "sadece ajanın kötü şeyler yapmamasını sağlayın"ın asla sağlayamayacağı şekillerde dayanıklıdır.

## Sonuç

AI ajanlar için güvenlik desenleri hâlâ sektör genelinde şekilleniyor. Bu şablon, gördüğüm en kapsamlı referans uygulamalarından biri — yalnızca kimlik doğrulamayı değil, gerçek yetkilendirme akışını da ele alıyor.

Orijinal gönderi: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
