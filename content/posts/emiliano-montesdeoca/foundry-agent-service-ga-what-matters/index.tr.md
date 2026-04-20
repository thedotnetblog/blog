---
title: "Foundry Agent Service GA'ya Geçti: .NET Agent Geliştiricileri İçin Gerçekten Önemli Olan Nedir?"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft'un Foundry Agent Service'i özel ağ desteği, Voice Live, üretim değerlendirmeleri ve açık çok modelli runtime ile GA'ya geçti. İşte bilmeniz gerekenler."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

Kabul edelim — bir AI agent prototipi oluşturmak kolay kısım. Zor olan ise sonrasındaki her şey: uygun ağ izolasyonuyla üretime almak, gerçekten anlamlı değerlendirmeler yapmak, uyumluluk gereksinimlerini karşılamak ve gece 2'de her şeyin çökmemesini sağlamak.

[Foundry Agent Service az önce GA'ya geçti](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) ve bu sürüm tam da bu "sonrasındaki her şey" boşluğuna odaklanıyor.

## Responses API Üzerine İnşa Edildi

İşte manşet haber: yeni nesil Foundry Agent Service, OpenAI Responses API üzerine kurulu. Eğer bu wire protokolüyle zaten geliştirme yapıyorsanız, Foundry'ye geçiş minimal kod değişikliği gerektiriyor. Kazandıklarınız: kurumsal güvenlik, özel ağ desteği, Entra RBAC, tam izleme ve değerlendirme — mevcut agent mantığınızın üstüne.

Mimari kasıtlı olarak açık tasarlanmış. Tek bir model sağlayıcısına veya tek bir orkestrasyon framework'üne bağlı değilsiniz. Planlama için DeepSeek, üretim için OpenAI, orkestrasyon için LangGraph kullanabilirsiniz — runtime tutarlılık katmanını halleder.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> `azure-ai-agents` paketinden geliyorsanız, agent'lar artık `azure-ai-projects` içindeki `AIProjectClient` üzerinde birinci sınıf operasyonlar. Bağımsız paketi bırakın ve response'ları yönetmek için `get_openai_client()` kullanın.

## Özel Ağ Desteği: Kurumsal Engel Kaldırıldı

Bu, kurumsal benimsemeyi engelleyen sorunu ortadan kaldıran özelliktir. Foundry artık BYO VNet ile uçtan uca tam özel ağ desteği sunuyor:

- **Genel çıkış yok** — agent trafiği hiçbir zaman genel internete çıkmıyor
- **Container/alt ağ enjeksiyonu** yerel iletişim için ağınıza entegre ediliyor
- **Araç bağlantısı dahil** — MCP server'lar, Azure AI Search, Fabric data agent'ları hepsi özel yollar üzerinden çalışıyor

Son nokta kritik. Yalnızca çıkarım çağrıları değil, her araç çağrısı ve her veri alma işlemi de ağ sınırınızın içinde kalıyor. Dışarıya yönlendirmeyi yasaklayan veri sınıflandırma politikaları altında çalışan ekipler için işte bu eksik olan parçaydı.

## Doğru Yapılmış MCP Kimlik Doğrulaması

MCP server bağlantıları artık tüm auth pattern yelpazesini destekliyor:

| Auth Yöntemi | Ne Zaman Kullanılır |
|--------------|---------------------|
| Key tabanlı | Kurum geneli dahili araçlar için basit paylaşımlı erişim |
| Entra Agent Identity | Servisten servise; agent kendisi olarak kimlik doğrular |
| Entra Managed Identity | Proje bazında izolasyon; kimlik bilgisi yönetimi yok |
| OAuth Identity Passthrough | Kullanıcı delegeli erişim; agent kullanıcılar adına hareket eder |

OAuth Identity Passthrough ilginç olan. Kullanıcıların bir agent'a kişisel verilerine — OneDrive'larına, Salesforce organizasyonlarına, kullanıcı kapsamlı bir SaaS API'sine — erişim vermesi gerektiğinde, agent standart OAuth akışlarıyla onlar adına hareket eder. Herkesi temsil etmeye çalışan paylaşımlı bir sistem kimliği yok.

## Voice Live: Tesisatla Uğraşmadan Konuşmadan Konuşmaya

Bir agent'a ses eklemek eskiden STT, LLM ve TTS'i bir araya getirmek anlamına geliyordu — üç servis, üç gecikme adımı, üç faturalama yüzeyi, hepsi elle senkronize. **Voice Live** bunu tek bir yönetilen API'ye indirgiyor:

- Semantik ses aktivitesi ve konuşma sonu algılama (anlamı anlıyor, sadece sessizliği değil)
- Sunucu taraflı gürültü bastırma ve yankı giderme
- Araya girme desteği (kullanıcılar yanıt ortasında sözü kesebilir)

Ses etkileşimleri, metinle aynı agent runtime'ından geçiyor. Aynı değerlendiriciler, aynı izler, aynı maliyet görünürlüğü. Müşteri desteği, saha hizmeti veya erişilebilirlik senaryoları için bu, daha önce özel bir ses pipeline'ı gerektiren şeyin yerini alıyor.

## Değerlendirmeler: Onay Kutusundan Sürekli İzlemeye

Foundry'nin üretim kalitesi konusunda ciddiye geldiği yer burası. Değerlendirme sistemi artık üç katmana sahip:

1. **Hazır değerlendiriciler** — tutarlılık, alaka, temellendirilme, erişim kalitesi, güvenlik. Bir veri kümesine veya canlı trafiğe bağlayın, puanları geri alın.

2. **Özel değerlendiriciler** — kendi iş mantığınızı, ton standartlarınızı ve alana özgü uyumluluk kurallarınızı kodlayın.

3. **Sürekli değerlendirme** — Foundry canlı üretim trafiğini örnekliyor, değerlendirici paketinizi çalıştırıyor ve sonuçları dashboard'lar aracılığıyla sunuyor. Temellendirilme düştüğünde veya güvenlik eşikleri aşıldığında Azure Monitor uyarıları ayarlayın.

Her şey Azure Monitor Application Insights'a yayımlanıyor. Agent kalitesi, altyapı sağlığı, maliyet ve uygulama telemetrisi — hepsi tek bir yerde.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Barındırılan Agent'lar İçin Altı Yeni Bölge

Barındırılan agent'lar artık East US, North Central US, Sweden Central, Southeast Asia, Japan East ve daha fazlasında kullanılabilir. Bu, veri yerleşim gereksinimleri için ve agent'ınız veri kaynaklarına yakın çalıştığında gecikmeyi azaltmak için önemlidir.

## .NET Geliştiricileri İçin Neden Önemli?

GA duyurusundaki kod örnekleri Python öncelikli olsa da, altta yatan altyapı dilden bağımsız — ve `azure-ai-projects` için .NET SDK aynı pattern'leri takip ediyor. Responses API, değerlendirme framework'ü, özel ağ desteği, MCP auth — bunların hepsi .NET'ten erişilebilir.

AI agent'larının "harika demo" aşamasından "bunu işte gerçekten gönderebilirim" aşamasına geçmesini bekliyorsanız, bu GA sürümü sinyaldir. Özel ağ desteği, uygun auth, sürekli değerlendirme ve üretim izleme — işte eksik olan parçalar bunlardı.

## Son Söz

Foundry Agent Service şu anda kullanılabilir. SDK'yı kurun, [portal'ı](https://ai.azure.com) açın ve geliştirmeye başlayın. [Hızlı başlangıç kılavuzu](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) sıfırdan çalışan bir agent'a dakikalar içinde ulaştırıyor.

Tüm kod örnekleriyle birlikte tam teknik derinlemesine bakış için [GA duyurusunu](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) inceleyin.
