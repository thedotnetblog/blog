---
title: "Azure Functions Üzerindeki MCP Sunucularınızı Foundry Agentlarına Bağlayın — İşte Nasıl"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "MCP sunucunuzu bir kez oluşturun, Azure Functions'a dağıtın ve uygun kimlik doğrulamayla Microsoft Foundry agentlarına bağlayın."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

MCP ekosistemi hakkında sevdiğim bir şey var: sunucunuzu bir kez oluşturursunuz ve her yerde çalışır.

Azure SDK ekibinden Lily Ma, [Azure Functions'a dağıtılmış MCP sunucularını Microsoft Foundry agentlarıyla bağlamak için pratik bir kılavuz yayımladı](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/).

## Bu kombinasyon neden mantıklı

Azure Functions size MCP sunucularını barındırmak için ölçeklenebilir altyapı, yerleşik kimlik doğrulama ve sunucusuz faturalandırma sağlar. Microsoft Foundry size mantık yürütebilen AI agentları sağlar. İkisini bağlamak, özel araçlarınızın kurumsal AI yetenekleri haline gelmesi anlamına gelir.

## Kimlik doğrulama seçenekleri

| Yöntem | Kullanım Senaryosu |
|--------|----------|
| **Key-based** | Geliştirme veya Entra auth olmayan sunucular |
| **Microsoft Entra** | Yönetilen kimliklerle üretim |
| **OAuth identity passthrough** | Kullanıcı bağlamının önemli olduğu üretim |
| **Kimlik doğrulamasız** | Geliştirme/test veya yalnızca public veri |

## Kurulum

1. **MCP sunucunuzu Azure Functions'a dağıtın** — [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) için örnekler mevcut
2. **Yerleşik MCP kimlik doğrulamasını etkinleştirin**
3. **Endpoint URL'sini alın** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Foundry'de MCP sunucusunu araç olarak ekleyin**

[Tam kılavuzu](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) okuyun.
