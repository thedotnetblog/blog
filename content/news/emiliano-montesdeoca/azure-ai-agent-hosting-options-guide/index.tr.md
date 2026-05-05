---
title: "Azure'da AI Ajanlarınızı Nerede Barındırmalısınız? Pratik Bir Karar Rehberi"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure, AI ajanları barındırmak için ham container'lardan tam yönetimli Foundry Hosted Agents'a kadar altı yol sunuyor. .NET iş yükünüz için doğru seçeneği nasıl belirleyeceğinizi burada bulabilirsiniz."
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

Şu an .NET ile AI ajanları geliştiriyorsanız, muhtemelen bunu fark etmişsinizdir: Azure'da bunları barındırmanın *pek çok* yolu var. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — ve gerçekten birini seçmeniz gerekene kadar hepsi makul görünüyor. Microsoft, bunu netleştiren [Azure AI ajan barındırma için kapsamlı bir rehber](https://devblogs.microsoft.com/all-things-azure/hostedagent/) yayımladı ve ben bunu pratik bir .NET geliştirici perspektifinden ele almak istiyorum.

## Altı seçeneğe genel bakış

Ortamı şöyle özetlerim:

| Seçenek | En iyi kullanım | Siz yönetirsiniz |
|---------|-----------------|------------------|
| **Container Apps** | K8s karmaşıklığı olmadan tam container kontrolü | Gözlemlenebilirlik, durum, yaşam döngüsü |
| **AKS** | Kurumsal uyumluluk, çok kümeli, özel ağ | Her şey (bu onun amacı) |
| **Azure Functions** | Olay odaklı, kısa süren ajan görevleri | Çok az — gerçek serverless |
| **App Service** | Basit HTTP ajanları, öngörülebilir trafik | Dağıtım, ölçeklendirme yapılandırması |
| **Foundry Agents** | Portal/SDK aracılığıyla kod gerektirmeyen ajanlar | Neredeyse hiçbir şey |
| **Foundry Hosted Agents** | Yönetilen altyapıyla özel framework ajanları | Yalnızca ajan kodunuz |

İlk dördü genel amaçlı işlem — üzerlerinde ajan *çalıştırabilirsiniz*, ancak bunlar bunun için tasarlanmadı. Son ikisi ajan doğasında: konuşmaları, araç çağrılarını ve ajan yaşam döngülerini birinci sınıf kavramlar olarak anlıyorlar.

## Foundry Hosted Agents — .NET ajan geliştiricileri için tatlı nokta

İşte dikkatimi çeken kısım. Foundry Hosted Agents tam ortada duruyor: kendi kodunuzu çalıştırma esnekliğini alıyorsunuz (Semantic Kernel, Agent Framework, LangGraph — her neyse), ancak platform altyapıyı, gözlemlenebilirliği ve konuşma yönetimini üstleniyor.

Kilit parça **Hosting Adapter** — ajan framework'ünüzü Foundry platformuna köprüleyen ince bir soyutlama katmanı. Microsoft Agent Framework için şöyle görünüyor:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Barındırma hikayenizin tamamı bu. Adapter, protokol çevirisini, server-sent events aracılığıyla streaming'i, konuşma geçmişini ve OpenTelemetry izlemeyi otomatik olarak hallediyor. Özel middleware yok, manuel bağlantı yok.

## Dağıtım gerçekten basit

Daha önce Container Apps'e ajan dağıttım ve çalışıyor, ancak durum yönetimi ve gözlemlenebilirlik için çok fazla yapıştırıcı kod yazıyorsunuz. Hosted Agents ve `azd` ile dağıtım şöyle:

```bash
# AI agent uzantısını yükle
azd ext install azure.ai.agents

# Bir şablondan başlat
azd ai agent init

# Derle, gönder, dağıt — tamam
azd up
```

Tek `azd up` komutu, container'ınızı derliyor, ACR'a gönderiyor, Foundry projesini oluşturuyor, model endpoint'lerini dağıtıyor ve ajanınızı başlatıyor. Beş adım tek komuta indirgeniyor.

## Yerleşik konuşma yönetimi

Bu, üretimde en çok zaman kazandıran kısım. Kendi konuşma durum deposunuzu oluşturmak yerine, Hosted Agents bunu doğal olarak hallediyor:

```python
# Kalıcı bir konuşma oluştur
conversation = openai_client.conversations.create()

# İlk tur
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Unutma: favori numaram 42.",
)

# İkinci tur — bağlam korunuyor
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Favori numamı 10 ile çarp.",
)
```

Redis yok. Cosmos DB oturum deposu yok. Mesaj serileştirme için özel middleware yok. Platform sadece hallediyor.

## Karar çerçevem

Altı seçeneğin tamamını inceledikten sonra, işte hızlı zihinsel modelim:

1. **Sıfır altyapı mı istiyorsunuz?** → Foundry Agents (portal/SDK, container yok)
2. **Özel ajan kodunuz var ama yönetilen barındırma mı istiyorsunuz?** → Foundry Hosted Agents
3. **Olay odaklı, kısa ömürlü ajan görevlerine mi ihtiyacınız var?** → Azure Functions
4. **K8s olmadan maksimum container kontrolü mü istiyorsunuz?** → Container Apps
5. **Katı uyumluluk ve çok kümeli mimariye mi ihtiyacınız var?** → AKS
6. **Öngörülebilir trafikli basit bir HTTP ajanınız mı var?** → App Service

Semantic Kernel veya Microsoft Agent Framework ile geliştiren çoğu .NET geliştirici için, Hosted Agents muhtemelen doğru başlangıç noktası. Sıfıra ölçekleme, yerleşik OpenTelemetry, konuşma yönetimi ve framework esnekliği alıyorsunuz — Kubernetes yönetmeden veya kendi gözlemlenebilirlik yığınınızı bağlamadan.

## Özet

Azure'daki ajan barındırma ortamı hızla olgunlaşıyor. Bugün yeni bir AI ajan projesi başlatıyorsanız, alışkanlıkla Container Apps veya AKS'e uzanmadan önce Foundry Hosted Agents'ı ciddi olarak değerlendirirdim. Yönetilen altyapı gerçek zaman kazandırıyor ve hosting adapter modeli, framework seçiminizi korumanıza olanak tanıyor.

Çalışan örnekler için [Microsoft'ın tam rehberine](https://devblogs.microsoft.com/all-things-azure/hostedagent/) ve [Foundry Samples reposuna](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) göz atın.
