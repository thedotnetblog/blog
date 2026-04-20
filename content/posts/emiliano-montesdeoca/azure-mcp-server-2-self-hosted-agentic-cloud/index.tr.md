---
title: "Azure MCP Server 2.0 Çıktı — Self-Hosted Agentic Cloud Otomasyonu Burada"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0, self-hosted uzak dağıtımlar, 57 Azure hizmetinde 276 araç ve kurumsal sınıf güvenlikle kararlı sürüme ulaşıyor."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

Son zamanlarda MCP ve Azure ile bir şeyler geliştiriyorsanız, yerel deneyimin iyi çalıştığını muhtemelen biliyorsunuzdur. Peki bu kurulumu ekip genelinde paylaşmanız gerektiğinde? İşte orada işler karmaşıklaşıyordu.

Artık değil. Azure MCP Server [2.0 kararlı sürümüne ulaştı](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), ve başlık özelliği tam olarak kurumsal ekiplerin istediği şey: **self-hosted uzak MCP sunucu desteği**.

## Azure MCP Server nedir?

Azure MCP Server, [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) spesifikasyonunu uygular ve Azure yeteneklerini yapılandırılmış, keşfedilebilir araçlar olarak sunar. Sayılar kendisi konuşuyor: **57 Azure hizmetinde 276 MCP aracı**.

## Büyük özellik: self-hosted uzak dağıtımlar

Gerçek bir ekip senaryosunda ihtiyacınız olan:
- Geliştiriciler ve dahili agent sistemleri için paylaşılan erişim
- Merkezi yapılandırma
- Kurumsal ağ ve politika sınırları
- CI/CD pipeline entegrasyonu

Azure MCP Server 2.0 bunların hepsini karşılıyor. Kimlik doğrulama için iki sağlam seçenek:
1. **Managed Identity** — [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) ile çalışırken
2. **On-Behalf-Of (OBO) akışı** — kullanıcının gerçek izinleriyle

## Güvenlik güçlendirmesi

2.0 sürümü güçlendirilmiş endpoint doğrulaması, injection pattern korumaları ve sıkı izolasyon kontrolleri ekliyor.

## Başlarken

- **[GitHub Repo](https://aka.ms/azmcp)** — kaynak kodu, belgeler
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — konteyner dağıtımı
- **[VS Code Eklentisi](https://aka.ms/azmcp/download/vscode)** — IDE entegrasyonu
- **[Self-hosting kılavuzu](https://aka.ms/azmcp/self-host)** — 2.0'ın amiral gemisi özelliği
