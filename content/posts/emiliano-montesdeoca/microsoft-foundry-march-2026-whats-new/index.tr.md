---
title: "Microsoft Foundry Mart 2026 — GPT-5.4, Agent Service GA ve Her Şeyi Değiştiren SDK Yenilemesi"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry'nin Mart 2026 güncellemesi devasa: Agent Service GA'ya geçiyor, GPT-5.4 güvenilir akıl yürütme getiriyor, azure-ai-projects SDK tüm dillerde kararlı hale geliyor ve Fireworks AI açık modelleri Azure'a taşıyor."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "microsoft-foundry-march-2026-whats-new" >}}).*

Aylık "Microsoft Foundry'de Neler Yeni" yazıları genellikle kademeli iyileştirmelerin ve ara sıra bir manşet özelliğinin karışımı olur. [Mart 2026 sayısı](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? Bu neredeyse tamamen manşet özelliklerden oluşuyor. Foundry Agent Service GA'ya geçiyor, GPT-5.4 üretime geliyor, SDK büyük bir kararlı sürüm alıyor ve Fireworks AI, Azure'a açık model çıkarımı getiriyor. .NET geliştiricileri için önemli olanları ele alayım.

## Foundry Agent Service Üretime Hazır

Bu büyük haber. Yeni nesil agent runtime genel kullanıma sunuldu — OpenAI Responses API üzerine kurulu, OpenAI agent'larıyla wire uyumlu ve birden fazla sağlayıcının modellerine açık. Bugün Responses API ile geliştirme yapıyorsanız, Foundry'ye geçiş mevcut agent mantığınızın üstüne kurumsal güvenlik, özel ağ desteği, Entra RBAC, tam izleme ve değerlendirme ekler.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Önemli eklemeler: uçtan uca özel ağ desteği, MCP auth genişlemesi (OAuth passthrough dahil), konuşmadan konuşmaya agent'lar için Voice Live önizlemesi ve 6 yeni bölgede barındırılan agent'lar.

## GPT-5.4 — Ham Zekadan Çok Güvenilirlik

GPT-5.4, daha akıllı olmak için değil. Daha güvenilir olmak için. Uzun etkileşimlerde daha güçlü akıl yürütme, daha iyi talimat uyumu, daha az iş akışı ortası başarısızlık ve entegre bilgisayar kullanım yetenekleri. Üretim agent'ları için o güvenilirlik, kıyaslama puanlarından çok daha önemlidir.

| Model | Fiyatlandırma (M token başına) | En İyi Kullanım |
|-------|-------------------------------|-----------------|
| GPT-5.4 (≤272K) | $2,50 / $15 çıktı | Üretim agent'ları, kodlama, belge iş akışları |
| GPT-5.4 Pro | $30 / $180 çıktı | Derin analiz, bilimsel akıl yürütme |
| GPT-5.4 Mini | Maliyet etkin | Sınıflandırma, çıkarım, hafif araç çağrıları |

Akıllı hamle bir yönlendirme stratejisidir: GPT-5.4 Mini yüksek hacimli, düşük gecikmeli işleri yönetirken GPT-5.4 akıl yürütme ağırlıklı istekleri alır.

## SDK Nihayet Kararlı

`azure-ai-projects` SDK tüm dillerde kararlı sürümler gönderdi — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0 ve .NET 2.0.0 (1 Nisan). `azure-ai-agents` bağımlılığı kalktı — her şey `AIProjectClient` altında yaşıyor. `pip install azure-ai-projects` ile kurun; paket `openai` ve `azure-identity`'yi doğrudan bağımlılık olarak birlikte getiriyor.

.NET geliştiricileri için bu, tam Foundry yüzeyi için tek bir NuGet paketi anlamına geliyor. Artık ayrı agent SDK'larını dengeleme yok.

## Fireworks AI Açık Modelleri Azure'a Taşıyor

Belki de mimarısal açıdan en ilginç ekleme: günlük ~180K istek/saniye ile 13+ trilyon token işleyen Fireworks AI artık Foundry üzerinden kullanılabilir. Lansmanında DeepSeek V3.2, gpt-oss-120b, Kimi K2.5 ve MiniMax M2.5.

Asıl hikaye **kendi ağırlıklarını getir** — sunum yığınını değiştirmeden her yerden nicel veya fine-tune edilmiş ağırlıklar yükleyin. Sunucusuz token başına ödeme veya sağlanan iş hacmi ile dağıtın.

## Diğer Öne Çıkanlar

- **Phi-4 Reasoning Vision 15B** — grafikler, diyagramlar ve belge düzenleri için çok modlu akıl yürütme
- **Evaluations GA** — Azure Monitor'a aktarılan sürekli üretim izlemeyle hazır değerlendiriciler
- **Priority Processing** (Önizleme) — gecikmeye duyarlı iş yükleri için ayrılmış hesaplama şeridi
- **Voice Live** — doğrudan Foundry agent'larına bağlanan konuşmadan konuşmaya runtime
- **Tracing GA** — sıralama ve filtrelemeyle uçtan uca agent iz incelemesi
- **PromptFlow kullanımdan kaldırma** — Ocak 2027'ye kadar Microsoft Framework Workflows'a geçiş

## Son Söz

Mart 2026, Foundry için bir dönüm noktası. Agent Service GA, tüm dillerde kararlı SDK'lar, güvenilir üretim agent'ları için GPT-5.4 ve Fireworks AI üzerinden açık model çıkarımı — platform ciddi iş yükleri için hazır.

Başlamak için [tam özeti](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) okuyun ve [ilk agent'ınızı oluşturun](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code).
