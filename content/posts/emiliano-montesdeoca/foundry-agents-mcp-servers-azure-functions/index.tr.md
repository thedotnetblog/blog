---
title: "Azure Functions Üzerindeki MCP Server'larınızı Foundry Agent'larına Bağlayın — İşte Nasıl Yapılır"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "MCP server'ınızı bir kez oluşturun, Azure Functions'a dağıtın ve uygun auth ile Microsoft Foundry agent'larına bağlayın. Araçlarınız her yerde çalışır — VS Code, Cursor ve artık kurumsal AI agent'ları."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

MCP ekosistemi hakkında sevdiğim bir şey var: server'ınızı bir kez oluşturuyorsunuz ve her yerde çalışıyor. VS Code, Visual Studio, Cursor, ChatGPT — her MCP istemcisi araçlarınızı keşfedip kullanabiliyor. Şimdi Microsoft bu listeye bir tüketici daha ekliyor: Foundry agent'ları.

Azure SDK ekibinden Lily Ma, Microsoft Foundry agent'larıyla Azure Functions'a dağıtılmış MCP server'larını bağlamaya dair [pratik bir kılavuz yayımladı](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/). Zaten bir MCP server'ınız varsa, bu tamamen katma değer — yeniden yapılandırma gerekmiyor.

## Bu Kombinasyon Neden Mantıklı?

Azure Functions, MCP server'larını barındırmak için ölçeklenebilir altyapı, yerleşik auth ve sunucusuz faturalama sunuyor. Microsoft Foundry ise akıl yürütebilen, plan yapabilen ve eylemler gerçekleştirebilen AI agent'ları sağlıyor. İkisini birleştirmek, özel araçlarınızın — veritabanı sorgulama, iş API'si çağrısı, doğrulama mantığı çalıştırma — kurumsal AI agent'larının özerk olarak keşfedip kullanabileceği yetenekler haline gelmesi anlamına geliyor.

Önemli nokta: MCP server'ınız aynı kalıyor. Yalnızca Foundry'yi başka bir tüketici olarak ekliyorsunuz. VS Code kurulumunuzda çalışan araçların aynısı artık ekibinizin veya müşterilerinizin etkileşime girdiği bir AI agent'ına güç veriyor.

## Kimlik Doğrulama Seçenekleri

Yazının gerçek değer kattığı yer burası. Senaryonuza bağlı olarak dört auth yöntemi:

| Yöntem | Kullanım Senaryosu |
|--------|-------------------|
| **Key tabanlı** (varsayılan) | Geliştirme veya Entra auth olmayan server'lar |
| **Microsoft Entra** | Yönetilen kimliklerle üretim |
| **OAuth identity passthrough** | Her kullanıcının bireysel olarak kimlik doğruladığı üretim |
| **Kimlik doğrulamasız** | Geliştirme/test veya yalnızca genel veriler |

Üretim için, agent kimliğiyle Microsoft Entra önerilen yoldur. OAuth identity passthrough, kullanıcı bağlamının önemli olduğu durumlar içindir — agent kullanıcıların giriş yapmasını ister ve her istek kullanıcının kendi token'ını taşır.

## Kurulum

Üst düzey akış:

1. **MCP server'ınızı Azure Functions'a dağıtın** — [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript ve Java için örnekler mevcut
2. **Function app'inizde yerleşik MCP kimlik doğrulamasını etkinleştirin**
3. **Endpoint URL'nizi alın** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **MCP server'ı Foundry'de araç olarak ekleyin** — portaldaki agent'ınıza gidin, yeni bir MCP aracı ekleyin, endpoint ve kimlik bilgilerini sağlayın

Ardından araçlarınızdan birini tetikleyecek bir prompt göndererek Agent Builder playground'unda test edin.

## Değerlendirmem

Buradaki kompozisyon hikayesi gerçekten güçleniyor. MCP server'ınızı .NET'te (veya Python, TypeScript, Java'da) bir kez oluşturun, Azure Functions'a dağıtın ve her MCP uyumlu istemci onu kullanabilsin — kodlama araçları, chat uygulamaları ve artık kurumsal AI agent'ları. Bu, gerçekten işleyen bir "bir kez yaz, her yerde kullan" pattern'ı.

.NET geliştiricileri için özellikle, [Azure Functions MCP extension](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) bunu kolaylaştırıyor. Araçlarınızı Azure Functions olarak tanımlayın, dağıtın ve Azure Functions'ın sağladığı tüm güvenlik ve ölçeklendirme özellikleriyle birlikte üretim kalitesinde bir MCP server'ınız olsun.

## Son Söz

Azure Functions üzerinde çalışan MCP araçlarınız varsa, bunları Foundry agent'larına bağlamak hızlı bir kazanımdır — özel araçlarınız, server'ın kendisinde hiçbir kod değişikliği yapmadan ve uygun auth ile kurumsal AI yeteneklerine dönüşür.

Her kimlik doğrulama yöntemi için adım adım talimatlar için [tam kılavuzu](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) okuyun ve üretim kurulumları için [ayrıntılı belgeleri](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) inceleyin.
