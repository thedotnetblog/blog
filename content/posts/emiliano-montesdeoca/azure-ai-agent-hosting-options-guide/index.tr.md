---
title: "Azure'da AI Agentlarınızı Nerede Barındırmalısınız? Pratik Bir Karar Kılavuzu"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure, AI agentlarını barındırmak için altı yol sunuyor — ham konteynerlerden tam yönetilen Foundry Hosted Agents'a kadar. .NET iş yükünüz için doğru olanı nasıl seçersiniz."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-ai-agent-hosting-options-guide" >}}).*

.NET ile şu anda AI agentları geliştiriyorsanız, muhtemelen fark etmişsinizdir: Azure'da onları barındırmanın *pek çok* yolu var. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents.

Microsoft [Azure AI agent barındırma için kapsamlı bir kılavuz](https://devblogs.microsoft.com/all-things-azure/hostedagent/) yayımladı.

## Altı seçeneğe genel bakış

| Seçenek | En iyi şunun için | Siz yönetirsiniz |
|---------|-----------------|-----------------|
| **Container Apps** | K8s karmaşıklığı olmadan tam konteyner kontrolü | Gözlemlenebilirlik, durum, yaşam döngüsü |
| **AKS** | Enterprise uyumluluk, çoklu küme | Her şeyi |
| **Azure Functions** | Olay güdümlü, kısa süreli görevler | Neredeyse hiçbir şeyi |
| **App Service** | Basit HTTP agentları | Dağıtım, ölçeklendirme |
| **Foundry Agents** | Kodsuz agentlar | Neredeyse hiçbir şeyi |
| **Foundry Hosted Agents** | Özel framework agentları | Sadece agent kodunuzu |

## Foundry Hosted Agents — .NET agent geliştiricileri için tatlı nokta

Dağıtım gerçekten basit:

```bash
azd ext install azure.ai.agents
azd ai agent init
azd up
```

O tek `azd up` konteyneri oluşturur, ACR'a gönderir, Foundry projesini sağlar ve agentı başlatır.

## Karar çerçevem

1. **Sıfır altyapı mı istiyorsunuz?** → Foundry Agents
2. **Özel agent kodunuz var ama yönetilen barındırma mı istiyorsunuz?** → Foundry Hosted Agents
3. **Olay güdümlü, kısa ömürlü görevler mi?** → Azure Functions
4. **Maksimum konteyner kontrolü mü?** → Container Apps
5. **Katı uyumluluk ve çoklu küme mi?** → AKS

## Sonuç

.NET geliştiricilerinin çoğu için Hosted Agents muhtemelen doğru başlangıç noktasıdır. [Microsoft'un tam kılavuzunu](https://devblogs.microsoft.com/all-things-azure/hostedagent/) inceleyin.
