---
title: "Azure DevOps MCP Server Nisan 2026 Güncellemesi: WIQL Sorguları, PAT Kimlik Doğrulaması ve Deneysel MCP Apps"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server, WIQL tabanlı work item sorguları, Personal Access Token kimlik doğrulaması, MCP açıklamaları ve yaygın iş akışlarını yeniden kullanılabilir araçlara paketleyen deneysel bir MCP Apps özelliği kazanıyor."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "index.md" >}}).*

Azure DevOps MCP Server sürekli iyileşiyor. Dan Hellem'in Nisan güncellemesi hem yerel hem de uzak sunucuyu kapsıyor ve burada gerçekten faydalı birkaç ekleme var — özellikle de board'larda ve repository'lerde gezinmek için Copilot kullandıysanız.

## WIQL Sorgu Desteği

En dikkat çekici özellik: MCP client'ınızdan doğrudan Work Item Query Language sorguları çalıştırmanızı sağlayan yeni `wit_query_by_wiql` aracı.

Bir süredir Azure Boards kullanıyorsanız WIQL'i bilirsiniz. Bu, work item'lar için SQL benzeri sorgu sözdizimidir: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. Bunu bir MCP aracı olarak sunmak, Copilot oturumlarınızın artık elle filtreleme yapmadan veya board görünümlerinde tıklamadan doğru work item kümelerini çekebileceği anlamına geliyor.

Bir uyarı: uzak MCP Server'da bu araç şu anda ölçekli sorgu performansını doğrularken **Insiders** özellik bayrağını gerektiriyor. Telemetri iyi göründüğünde herkes için açılacak.

## Yerel Sunucuda Kişisel Erişim Jetonları

Yerel MCP Server artık PAT kimlik doğrulamasını destekliyor. Bu küçük bir yaşam kalitesi düzeltmesi gibi görünebilir ama entegrasyon senaryoları için önemlidir — özellikle de MCP server'ı etkileşimli kimlik doğrulamanın olmadığı bir bağlamda çalıştırıyorsanız veya harici istemciler ve otomasyonlardan bağlanıyorsanız.

Kurulum adımları [Getting Started kılavuzunda](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat) belgelenmiş.

## Uzak Sunucuda MCP Açıklamaları

Açıklamalar, LLM'lere bunları güvenli şekilde nasıl kullanacaklarını söyleyen MCP araçlarındaki meta veri etiketleridir. Azure DevOps MCP Server artık şu kategoriler için açıklamaları uyguluyor:

- **Salt okunur araçlar** — model bunları kullanıcı onayı olmadan çağırmanın güvenli olduğunu bilir
- **Yıkıcı araçlar** — model dikkatli olması ve devam etmeden önce onay alması gerektiğini bilir
- **Open-world araçlar** — model bunların öngörülemeyen sonuçlar döndürebileceğini anlar

Bu, ajan güvenilirliği için temel bir konudur. Açıklamalar olmadan model, aracın adına bakarak onu çağırmanın güvenli olup olmadığını tahmin etmek zorunda kalır. Açıklamalarla davranış açık hale gelir ve ajan daha iyi kararlar verebilir.

## Wiki Araçlarının Birleştirilmesi

Uzak sunucu, ilişkili araçları daha az ama daha güçlü araç altında birleştirmeye başlıyor. Wiki araçları bu tedaviyi ilk alanlar:

| Yeni araç | Yerine geçer |
|----------|----------|
| `wiki` (salt okunur) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

Daha az araç = daha iyi model performansı. Bu, MCP server tasarımında tutarlı bir desen — daha küçük ve daha odaklı araç kümeleri daha iyi çalışır çünkü modelin neredeyse aynı beş araç arasında seçim yapması gerekmez.

## Deneysel: MCP Apps

Bu en ilginç ekleme ve açıkça deneysel. MCP Apps, MCP server ortamında çalışan paketlenmiş iş akışlarıdır:

```json
{
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "mcp-server-azuredevops",
      "args": ["contoso", "-d", "core", "work", "work-items", "mcp-apps"]
    }
  }
}
```

İlk örnek `mcp_app_my_work_item` — size atanmış work item'ları manuel olarak birden fazla araç çağrısını zincirlemek zorunda kalmadan görüntülemenizi, filtrelemenizi ve düzenlemenizi sağlayan bağımsız bir work item deneyimi.

Fikir ikna edici: Agent'ınızın `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` çağrılarını birkaç tur boyunca yapması yerine, tek bir MCP App tüm iş akışını yapılandırılmış ve yeniden kullanılabilir bir birim olarak sağlıyor. Daha az kurulum süresi, tutarlı davranış ve daha az hareketli parça.

## Kapanış

Azure DevOps MCP Server hızla olgunlaşıyor. WIQL desteği ve PAT kimlik doğrulaması, Copilot ile Azure Boards kullanan herkes için doğrudan kazanım. Açıklama çalışması uzak sunucuyu ajan tabanlı kullanım senaryoları için daha güvenli hale getiriyor. Ve deneysel olsa da MCP Apps, buradaki yönü gösteriyor: ham araçlardan oluşturulabilir iş akışlarına.

Uzak sunucu gelişmeye devam ederken [belgelere](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) göz atmakta fayda var.

Dan Hellem'in orijinal yazısı: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).