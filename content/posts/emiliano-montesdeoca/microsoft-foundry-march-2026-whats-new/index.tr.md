---
title: "Microsoft Foundry Mart 2026 — GPT-5.4, Agent Service GA ve Her Şeyi Değiştiren SDK Güncellemesi"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Foundry'nin Mart 2026 güncellemesi muazzam: Agent Service GA'ya ulaşıyor, GPT-5.4 güvenilir akıl yürütme getiriyor, azure-ai-projects SDK tüm dillerde stabil."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "microsoft-foundry-march-2026-whats-new" >}}).*

Aylık "Microsoft Foundry'de Yenilikler" yazıları genellikle küçük iyileştirmelerin karışımıdır. [Mart 2026 baskısı](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? Neredeyse tamamen ana özellikler.

## Foundry Agent Service üretime hazır

Yeni nesil agent runtime'ı genel kullanıma sunuldu — OpenAI Responses API üzerine inşa edildi, OpenAI agentlarıyla wire-uyumlu.

Temel eklemeler: uçtan uca özel ağ, MCP auth genişletmesi, Voice Live önizlemesi ve 6 yeni bölgede hosted agents.

## GPT-5.4 — ham zekadan çok güvenilirlik

GPT-5.4 daha akıllı olmakla ilgili değil. Daha güvenilir olmakla ilgili.

| Model | Fiyat (M token başına) | En iyi için |
|-------|----------------------|----------|
| GPT-5.4 (≤272K) | $2.50 / $15 output | Üretim agentları |
| GPT-5.4 Pro | $30 / $180 output | Derin analiz |
| GPT-5.4 Mini | Uygun maliyetli | Sınıflandırma, çıkarım |

## SDK sonunda kararlı

`azure-ai-projects` SDK tüm dillerde kararlı sürümler yayımladı — .NET 2.0.0 dahil.

## Fireworks AI Azure'a açık modeller getiriyor

DeepSeek V3.2, gpt-oss-120b, Kimi K2.5 başlangıçta mevcut.

[Tam özeti](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) okuyun.
