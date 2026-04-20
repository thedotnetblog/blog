---
title: "Dizüstü Bilgisayardan Üretime: İki Komutla Microsoft Foundry'e AI Agentları Dağıtma"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI artık AI agentınızı yerel geliştirmeden canlı Foundry endpoint'e dakikalar içinde taşıyan 'azd ai agent' komutlarına sahip."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

Yerel geliştirme ile "dağıtıldı ve trafik sunuyor" arasındaki boşluğu biliyorsunuzdur? AI agentları için bu boşluk acı verici şekilde genişti.

Azure Developer CLI bunu [iki komutluk bir iş](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) haline getirdi.

## Yeni `azd ai agent` iş akışı

```bash
azd ai agent init
azd up
```

Hepsi bu. `azd ai agent init` reponuzda kod-olarak-altyapı iskeletini oluşturur, `azd up` ise Azure'da her şeyi sağlar ve agentınızı yayımlar.

## Perde arkasında ne oluyor

`init` komutu reponuzda gerçek, incelenebilir Bicep şablonları oluşturur — Foundry Resource, Foundry Project, model dağıtım yapılandırması, RBAC ile yönetilen kimlik.

## Geliştirici iç döngüsü

```bash
azd ai agent run    # agenti yerel olarak başlatın
azd ai agent invoke # test istekleri gönderin
azd ai agent monitor --follow  # gerçek zamanlı log akışı
```

## Tam komut seti

| Komut | Ne yapar |
|---------|-------------|
| `azd ai agent init` | IaC ile Foundry agent projesi oluştur |
| `azd up` | Kaynakları sağla ve agenti dağıt |
| `azd ai agent invoke` | Uzak veya yerel agente istem gönder |
| `azd ai agent run` | Agenti yerel olarak çalıştır |
| `azd ai agent monitor` | Gerçek zamanlı log akışı |
| `azd down` | Tüm Azure kaynaklarını temizle |

[Tam adım adım kılavuzu](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) inceleyin.
