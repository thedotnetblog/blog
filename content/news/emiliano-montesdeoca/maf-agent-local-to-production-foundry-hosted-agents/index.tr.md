---
title: "Yerel MAF Ajansınız Artık Üretimde Bir Yuva Buldu"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents, Microsoft Agent Framework ajanınıza kimlik, ölçekleme, oturum kalıcılığı ve ekstra kurulum gerektirmeyen gözlemlenebilirlik sağlar. Pratikte nasıl göründüğünü inceleyelim."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Bir ajanı yerel olarak çalıştırmak eğlenceli kısımdır. Zor kısım sonrasında gelen her şeydir: aklını kaybetmeden deploy etmek, oturumları yönetmek, kimlik oluşturmak, gözlemlenebilirliği bağlamak. Genellikle bu çok sayıda özel altyapı gerektirmek anlamına gelir.

Foundry Hosted Agents, Microsoft Agent Framework (MAF) kullanıcıları için bu altyapının büyük bölümünü ortadan kaldırdı.

## Foundry Hosted Agents Gerçekte Ne Yapar

Bir MAF ajanını Foundry Hosted Agents'a deploy ettiğinizde, platform normalde kendiniz oluşturmanız gereken şaşırtıcı derecede uzun bir liste işlemi üstlenir:

- **Sıfıra ölçekleme** — ajanınız boşta iken hiçbir şey ücretlendirmez ve otomatik olarak yeniden başlar
- **Oturum başına VM-izole sandbox'lar** — her kullanıcı oturumu, ölçek küçültme olaylarını atlatan dosya sistemi kalıcılığı olan kendi sandbox'ını alır
- **Yerleşik Entra ID** — her ajan, imaja gömülü sırlar olmaksızın Foundry modellerini, Toolbox'ı ve Azure hizmetlerini çağırabilmek için kendi kimliğini alır
- **Sürümlü deployment'lar** — her deployment, blue/green ve canary rollout desteği olan değiştirilemez bir snapshot'tır
- **Sıfır yapılandırmalı gözlemlenebilirlik** — `APPLICATIONINSIGHTS_CONNECTION_STRING` çalışma zamanında enjekte edilir, böylece MAF'ın OpenTelemetry izleri App Insights'a otomatik olarak akar

Sonuncusu gerçekten güzel. Ekstra kablo bağlantısı yok, ekstra yapılandırma yok. İzler sadece görünür.

## Kod Farkı Minimumdur

Bu entegrasyonda en çok takdir ettiğim budur. Ajanınızı yeniden yazmanıza gerek yok. Sadece sarmanız yeterli:

**.NET'te:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Python'da:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Hepsi bu kadar. Yerel olarak test ettiğiniz mantığın aynısı üretimde çalışır. Platform bunu oturum yönetimi, kimlik ve ölçekleme altyapısıyla sarar.

## İki Protokol, Bir Ajan

Hosted Agents iki endpoint stili destekler:

- **Responses** (`/responses`) — OpenAI uyumlu, konuşma geçmişini ve akışı yönetir. Sohbet biçimli ajanlar için iyi varsayılan.
- **Invocations** (`/invocations`) — istek/yanıt şemasını kendiniz tanımlarsınız. Konuşma dışı iş akışları için uygundur.

Konuşmaya benzeyen bir şey oluşturuyorsanız Responses ile başlayın. Yapılandırılmış girdi alan ve yapılandırılmış çıktı döndüren API biçimli bir ajan oluşturuyorsanız Invocations size esneklik sağlar.

## `azd` ile Deployment Akışı

Bir MAF ajanıyla `azd up` çalıştırdığınızda:

1. İsteğe bağlı olarak Foundry projesi oluşturur ve model deploy eder
2. Kodunuzu paketler ve Azure Container Registry'ye imaj iter
3. ACR imajından işlem kapasitesi sağlar
4. Ajana özel bir Entra ID atar
5. Stabil bir endpoint açar (`https://{project_endpoint}/agents/{agent_name}`)
6. O noktadan itibaren geri kalan her şeyi yönetir

Oturumlar 30 güne kadar devam eder. Boşta işlem kapasitesi 15 dakika sonra kaldırılır ve bir sonraki istekte şeffaf şekilde geri yüklenir. Ajanın bakış açısından hiçbir şey değişmemiştir.

## Sonuç

"Yerel olarak çalışan" ile "üretimde çalışan" arasındaki mesafe, AI ajanları için tarihsel olarak uzun ve acı verici olmuştur. Foundry Hosted Agents + MAF bu boşluğu önemli ölçüde kapatır. Agent Framework ile oluşturulmuş yerel bir ajanınız varsa bugün denemek değer.

Ekip GA'nın yakında geleceğini söylüyor — bu şu anda önizlemede. Başlamak için [MAF Hosted Agent entegrasyon belgelerine](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) ve [.NET örneklerine](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) bakın.

Orijinal makale: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
