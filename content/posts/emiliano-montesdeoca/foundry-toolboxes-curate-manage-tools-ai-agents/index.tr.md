---
title: "Foundry Toolboxes: Tüm Ajan Araçları için Tek Bir Endpoint"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry, Toolboxes'ı genel önizleme olarak yayımladı — AI ajan araçlarını tek bir MCP uyumlu endpoint üzerinden yönetmenin ve sunmanın yolu."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Bizzat yaşayana kadar önemsiz görünen bir sorun var: Kuruluş birden fazla yapay zeka ajanı oluşturuyor, her birinin araçlara ihtiyacı var ve her ekip sıfırdan yapılandırıyor. Aynı web arama entegrasyonu, aynı Azure AI Search yapılandırması, aynı GitHub MCP sunucusu bağlantısı — ama farklı bir depoda, farklı bir ekip tarafından, farklı kimlik bilgileriyle ve paylaşılan yönetim olmadan.

Microsoft Foundry, genel önizlemede [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) yayımladı ve bu soruna doğrudan bir yanıt niteliğinde.

## Toolbox nedir?

Toolbox, Foundry'de bir kez tanımlanıp tek bir MCP uyumlu endpoint üzerinden sunulan, adlandırılmış ve yeniden kullanılabilir bir araç paketidir. MCP konuşabilen herhangi bir ajan çalışma zamanı bunu tüketebilir — Foundry Agents'a bağımlılık yoktur.

Vaat basittir: **build once, consume anywhere**. Araçları tanımla, kimlik doğrulamayı merkezi olarak yapılandır (OAuth doğrudan geçiş, Entra yönetilen kimlik), endpoint'i yayımla. Bu araçlara ihtiyaç duyan her ajan endpoint'e bağlanır ve tümünü alır.

## Dört sütun (bugün ikisi mevcut)

| Sütun | Durum | Ne yapar |
|-------|-------|---------|
| **Discover** | Yakında | Elle arama yapmadan onaylı araçları bulma |
| **Build** | Mevcut | Araçları yeniden kullanılabilir pakete gruplama |
| **Consume** | Mevcut | Tek MCP endpoint tüm araçları sunar |
| **Govern** | Yakında | Merkezi kimlik doğrulama + tüm araç çağrılarının gözlemlenebilirliği |

## Pratik örnek

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Dokümanlarda arama yap ve GitHub sorunlarına yanıt ver.",
    tools=[
        {"type": "web_search", "description": "Genel belgelerde arama yap"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Yayımlandıktan sonra Foundry birleşik bir endpoint sağlar. Tek bağlantı, tüm araçlar.

## Foundry Agents'a bağımlılık yok

Toolboxes, Foundry'de **oluşturulur ve yönetilir**; ancak tüketim yüzeyi açık MCP protokolüdür. Bunları özel ajanlardan (Microsoft Agent Framework, LangGraph), GitHub Copilot ve diğer MCP destekli IDE'lerden kullanabilirsiniz.

## Neden şimdi önemli?

Çoklu ajan dalgası üretime ulaşıyor. Her yeni ajan, yinelenen yapılandırma, eski kimlik bilgileri ve tutarsız davranış için yeni bir yüzeydir. Build + Consume temeli merkezileşmeye başlamak için yeterlidir. Govern sütunu geldiğinde, tüm ajan filosu için tam gözlemlenebilir ve merkezi olarak kontrol edilen bir araç katmanı elde edilmiş olacak.

## Sonuç

Henüz erken — genel önizleme, önce Python SDK, Discover ve Govern henüz yolda. Ancak model sağlam ve MCP yerel tasarımı, zaten inşa ettiğiniz araçlarla çalıştığı anlamına geliyor. Ayrıntılar için [resmi duyuruya](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) bakın.
