---
title: "Foundry Agent Service GA Oldu: .NET Agent Geliştiricileri için Gerçekten Önemli Olan"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry Agent Service, özel ağ, Voice Live, üretim değerlendirmeleri ve açık çok modelli çalışma zamanıyla GA oldu."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

Dürüst olalım — AI agent prototipi oluşturmak kolay kısımdır. Zor kısım sonrasındaki her şeydir.

[Foundry Agent Service GA oldu](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) ve bu sürüm o "sonrasındaki her şey" açığına odaklanıyor.

## Responses API Üzerine İnşa Edildi

Yeni nesil Foundry Agent Service, OpenAI Responses API üzerine inşa edildi. Mimari kasıtlı olarak açık — tek bir model sağlayıcısına bağlı değilsiniz.

## Özel ağ: kurumsal engel kaldırıldı

- **Genel çıkış yok** — agent trafiği hiç genel internete dokunmuyor
- **Konteyner/alt ağ enjeksiyonu** ağınıza
- **Araç bağlantısı dahil** — MCP sunucuları, Azure AI Search özel yollar üzerinden

## MCP kimlik doğrulama

| Auth yöntemi | Ne zaman kullanılır |
|-------------|-------------|
| Key-based | Basit paylaşılan erişim |
| Entra Agent Identity | Service-to-service |
| Entra Managed Identity | Proje başına izolasyon |
| OAuth Identity Passthrough | Kullanıcı delegeli erişim |

## Voice Live

Voice Live, STT, LLM ve TTS'yi tek bir yönetilen API'ye sıkıştırır.

## Değerlendirmeler

1. **Hazır değerlendiriciler** — tutarlılık, alaka, temellenme
2. **Özel değerlendiriciler** — kendi iş mantığınız
3. **Sürekli değerlendirme** — canlı üretim trafiği örnekleme

[Hızlı başlangıç kılavuzuna](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) ve [GA duyurusuna](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) bakın.
