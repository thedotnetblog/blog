---
title: "Azure DevOps MCP Server Microsoft Foundry'e Geldi: AI Agentlarınız İçin Ne Anlama Geliyor?"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server artık Microsoft Foundry'de kullanılabilir. AI agentlarınızı doğrudan DevOps iş akışlarına bağlayın — iş öğeleri, depolar, pipeline'lar — birkaç tıklamayla."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-devops-mcp-server-microsoft-foundry" >}}).*

MCP (Model Context Protocol) gündemdeki yerini aldı. AI agent ekosistemini takip ettiyseniz, MCP sunucularının her yerde belirdiğini muhtemelen fark etmişsinizdir.

Şimdi [Azure DevOps MCP Server Microsoft Foundry'de kullanılabilir](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), ve bu pratik olasılıkları düşündüren entegrasyonlardan biri.

## Ne oluyor aslında

Microsoft, Azure DevOps MCP Server'ı [genel önizleme](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) olarak zaten yayımlamıştı. Yeni olan Foundry entegrasyonu. Azure DevOps MCP Server'ı artık araç kataloğundan doğrudan Foundry agentlarınıza ekleyebilirsiniz.

## Kurulum

Kurulum şaşırtıcı derecede basit:

1. Foundry agentınızda **Araç Ekle** > **Katalog**'a gidin
2. "Azure DevOps" arayın
3. Azure DevOps MCP Server'ı seçin ve **Oluştur**'a tıklayın
4. Organizasyon adınızı girin ve bağlanın

## Agentınızın erişimini kontrol etme

Hangi araçların agentınız için kullanılabilir olduğunu belirleyebilirsiniz. Yalnızca iş öğelerini okusun ama pipeline'lara dokunmasın istiyorsanız, bunu yapılandırabilirsiniz.

## .NET ekipleri için neden ilginç

- **Sprint planlama asistanları** — iş öğelerini çekip sprint kapasitesini öneren agentlar
- **Kod review botları** — PR bağlamını anlayan agentlar
- **Olay müdahalesi** — iş öğeleri oluşturup hataları ilişkilendiren agentlar
- **Geliştirici işe alımı** — gerçek proje verilerine dayalı cevaplar

## Sonuç

[Tam duyuruyu](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) inceleyin.
