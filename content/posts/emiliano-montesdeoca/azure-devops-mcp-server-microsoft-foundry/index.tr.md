---
title: "Azure DevOps MCP Server Microsoft Foundry'ye Geldi: AI Agent'larınız İçin Ne Anlama Geliyor"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server artık Microsoft Foundry'de mevcut. AI agent'larınızı birkaç tıklamayla DevOps iş akışlarına — iş öğeleri, repolar, pipeline'lar — doğrudan bağlayın."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-devops-mcp-server-microsoft-foundry" >}}).*

MCP (Model Context Protocol) son dönemde çok konuşuluyor. AI agent ekosistemine dikkat ettiyseniz, MCP server'ların her yerde belirdiğini fark etmişsinizdir — agent'lara standart bir protokol üzerinden harici araçlar ve servislerle etkileşim kurma yeteneği kazandırıyorlar.

Artık [Azure DevOps MCP Server Microsoft Foundry'de mevcut](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) ve bu, pratik olasılıklar üzerine düşündüren entegrasyonlardan biri.

## Aslında ne oluyor

Microsoft, Azure DevOps MCP Server'ı [genel önizleme](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) olarak zaten yayınlamıştı — bu MCP server'ın kendisi. Yeni olan şey ise Foundry entegrasyonu. Artık Azure DevOps MCP Server'ı araç kataloğundan doğrudan Foundry agent'larınıza ekleyebilirsiniz.

Foundry'ye henüz aşina olmayanlar için: Microsoft'un AI destekli uygulama ve agent'ları ölçekli şekilde oluşturma ve yönetme için birleşik platformu. Model erişimi, orkestrasyon, değerlendirme, dağıtım — hepsi tek bir yerde.

## Kurulum

Kurulum şaşırtıcı derecede basit:

1. Foundry agent'ınızda **Add Tools** > **Catalog** bölümüne gidin
2. "Azure DevOps" arayın
3. Azure DevOps MCP Server (önizleme) seçin ve **Create** tıklayın
4. Organizasyon adınızı girin ve bağlanın

Hepsi bu. Agent'ınız artık Azure DevOps araçlarına erişebilir.

## Agent'ınızın nelere erişeceğini kontrol etme

Takdir ettiğim kısım şu: ya hep ya hiç yaklaşımına mahkum değilsiniz. Agent'ınıza hangi araçların sunulacağını belirtebilirsiniz. Yalnızca iş öğelerini okusun ama pipeline'lara dokunmasın istiyorsanız bunu yapılandırabilirsiniz. En az ayrıcalık ilkesi, AI agent'larınıza uygulanmış hali.

Bu, birinin "sürümle ilgili yardım et" demesi üzerine agent'ın kazara bir dağıtım pipeline'ını tetiklemesini istemediğiniz kurumsal senaryolarda önem taşıyor.

## Bu .NET ekipleri için neden ilginç

Pratikte neleri mümkün kıldığını düşünün:

- **Sprint planlama asistanları** — iş öğelerini çekebilen, hız verilerini analiz edebilen ve sprint kapasitesi önerebilen agent'lar
- **Kod inceleme botları** — repolarınızı ve bağlantılı iş öğelerinizi gerçekten okuyabildikleri için PR bağlamınızı anlayan agent'lar
- **Olay müdahalesi** — iş öğesi oluşturabilen, son dağıtımları sorgulayabilen ve hataları son değişikliklerle ilişkilendirebilen agent'lar
- **Geliştirici onboarding'i** — "Ne üzerinde çalışmalıyım?" sorusuna gerçek proje verileriyle desteklenmiş gerçek bir yanıt

CI/CD pipeline'ları ve proje yönetimi için Azure DevOps'u zaten kullanan .NET ekipleri için, bir AI agent'ının bu sistemlerle doğrudan etkileşim kurabilmesi, yararlı otomasyona doğru önemli bir adım (sıradan chatbot-as-a-service değil).

## Daha geniş MCP resmi

Bu, daha geniş bir trendin parçası: MCP server'lar, AI agent'larının dış dünyayla etkileşim kurmasının standart yolu haline geliyor. GitHub, Azure DevOps, veritabanları, SaaS API'leri için MCP server'lar görüyoruz — ve Foundry, tüm bu bağlantıların bir araya geldiği merkez haline geliyor.

.NET ekosisteminde agent geliştiriyorsanız MCP'ye dikkat etmeye değer. Protokol standartlaşmış, araç kitleri olgunlaşıyor ve Foundry entegrasyonu, server bağlantılarını manuel olarak kurmak zorunda kalmadan erişilebilir hale getiriyor.

## Sonuç

Foundry'deki Azure DevOps MCP Server önizleme aşamasında, bu yüzden gelişmeye devam etmesini bekleyin. Ancak temel iş akışı sağlam: bağlanın, araç erişimini yapılandırın ve agent'larınızın DevOps verilerinizle çalışmasına izin verin. Zaten Foundry ekosistemindeyseniz, birkaç tıklama uzaktasınız. Bir deneyin ve hangi iş akışlarını oluşturabileceğinizi görün.

Adım adım kurulum ve daha fazla ayrıntı için [tam duyuruya](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) göz atın.
