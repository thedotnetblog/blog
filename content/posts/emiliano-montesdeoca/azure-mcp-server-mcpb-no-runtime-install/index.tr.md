---
title: "Azure MCP Server Artık .mcpb — Herhangi Bir Runtime Olmadan Yükle"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server artık MCP Bundle (.mcpb) olarak kullanılabilir — indirin, Claude Desktop'a sürükleyin ve bitti. Node.js, Python veya .NET gerekmiyor."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

MCP sunucularını kurarken can sıkıcı olan ne olduğunu biliyor musunuz? Bir runtime gerekiyordu. npm sürümü için Node.js, pip/uvx için Python, dotnet varyantı için .NET SDK.

[Azure MCP Server bunu değiştirdi](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Artık `.mcpb` — MCP Bundle — olarak kullanılabilir ve kurulum sürükle-bıraktır.

## MCP Bundle Nedir?

VS Code uzantısı (`.vsix`) veya tarayıcı uzantısı (`.crx`) gibi düşünün, ama MCP sunucuları için. `.mcpb` dosyası, sunucu ikilisini ve tüm bağımlılıklarını içeren bağımsız bir ZIP arşividir.

## Nasıl Kurulur

**1. Platformunuz için bundle'ı indirin**

[GitHub Releases sayfasına](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) gidin ve OS ve mimarinize uygun `.mcpb` dosyasını indirin.

**2. Claude Desktop'a kurun**

En kolay yol: Uzantılar ayarları sayfasındayken (`☰ → Dosya → Ayarlar → Uzantılar`) `.mcpb` dosyasını Claude Desktop penceresine sürükleyip bırakın. Sunucu ayrıntılarını inceleyin, Yükle'ye tıklayın, onaylayın.

**3. Azure'da kimlik doğrulaması yapın**

```bash
az login
```

## Başlamak için

- **İndirme**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Depo**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Belgeler**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

[Tam makaleye](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/) bakın.
