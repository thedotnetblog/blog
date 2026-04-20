---
title: "Dizüstü Bilgisayardan Üretime: İki Komutla AI Agent'larını Microsoft Foundry'ye Dağıtma"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI artık 'azd ai agent' komutlarına sahip; bu komutlar AI agent'ınızı yerel geliştirmeden canlı bir Foundry endpoint'ine dakikalar içinde taşıyor. İşte tam iş akışı."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

"Makinemde çalışıyor" ile "dağıtıldı ve trafik sunuyor" arasındaki o boşluğu bilirsiniz? AI agent'ları için bu boşluk acı verici derecede geniş oldu. Kaynak sağlamanız, modelleri dağıtmanız, kimliği bağlamanız, izlemeyi kurmanız gerekiyor — ve bütün bunlar herhangi biri agent'ınızı çağırabilmeden önce.

Azure Developer CLI bunu [iki komutluk bir iş](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) haline getirdi.

## Yeni `azd ai agent` iş akışı

Bunun gerçekte nasıl göründüğünü anlatalım. Bir AI agent projeniz var — diyelim ki bir otel danışman agent'ı. Yerel olarak çalışıyor. Microsoft Foundry üzerinde çalışmasını istiyorsunuz.

```bash
azd ai agent init
azd up
```

Hepsi bu. İki komut. `azd ai agent init`, reponuzda altyapı-kod olarak iskele oluşturur ve `azd up` her şeyi Azure'da sağlayıp agent'ınızı yayımlar. Foundry portalında agent'ınıza doğrudan bir bağlantı alırsınız.

## Arka planda ne oluyor

`init` komutu reponuzda gerçek, incelenebilir Bicep şablonları oluşturuyor:

- Bir **Foundry Kaynağı** (üst düzey kapsayıcı)
- Bir **Foundry Projesi** (agent'ınızın bulunduğu yer)
- **Model dağıtımı** yapılandırması (GPT-4o vb.)
- Uygun RBAC rol atamalarıyla **Yönetilen kimlik**
- Servis haritası için `azure.yaml`
- Agent meta verileri ve ortam değişkenleriyle `agent.yaml`

İşte kilit nokta: bunların hepsi size ait. Reponuzda sürümlendirilmiş Bicep. İnceleyebilir, özelleştirebilir ve agent kodunuzun yanı sıra commit edebilirsiniz. Sihirli kara kutular yok.

## Geliştirme döngüsü

Gerçekten beğendiğim şey yerel geliştirme hikayesi. Agent mantığını geliştirirken, her prompt değişikliğinde yeniden dağıtmak istemezsiniz:

```bash
azd ai agent run
```

Bu, agent'ınızı yerel olarak başlatır. Bunu test promptları göndermek için `azd ai agent invoke` ile eşleştirin, sıkı bir geri bildirim döngüsü elde edersiniz. Kodu düzenleyin, yeniden başlatın, çağırın, tekrarlayın.

`invoke` komutu yönlendirme konusunda da akıllı — yerel bir agent çalışırken otomatik olarak onu hedefler. Çalışmıyorken uzak endpoint'e isabet eder.

## Gerçek zamanlı izleme

Bu beni ikna eden özellik. Agent'ınız dağıtıldığında:

```bash
azd ai agent monitor --follow
```

Agent'ınızdan geçen her istek ve yanıt gerçek zamanlı olarak terminalinize akıyor. Üretim sorunlarını hata ayıklamak için bu paha biçilmez. Log analitiğini karıştırmak yok, metriklerin toplanmasını beklemek yok — şu an ne olduğunu görüyorsunuz.

## Tam komut seti

İşte hızlı referans:

| Komut | Ne yapıyor |
|---------|-------------|
| `azd ai agent init` | IaC ile bir Foundry agent projesi iskele oluşturur |
| `azd up` | Azure kaynaklarını sağlar ve agent'ı dağıtır |
| `azd ai agent invoke` | Uzak veya yerel agent'a prompt gönderir |
| `azd ai agent run` | Geliştirme için agent'ı yerel olarak çalıştırır |
| `azd ai agent monitor` | Yayımlanan agent'dan gerçek zamanlı logları akıtır |
| `azd ai agent show` | Agent sağlığını ve durumunu kontrol eder |
| `azd down` | Tüm Azure kaynaklarını temizler |

## .NET geliştiricileri için neden önemli

Duyuruda örnek Python tabanlı olsa da, altyapı hikayesi dilden bağımsız. .NET agent'ınız aynı Bicep iskeleleme, aynı yönetilen kimlik kurulumu, aynı izleme pipeline'ı alıyor. .NET Aspire uygulamalarınız veya Azure dağıtımları için zaten `azd` kullanıyorsanız, bu mevcut iş akışınıza tam oturuyor.

AI agent'ları için dağıtım boşluğu, ekosistemdeki en büyük sürtüşme noktalarından biri oldu. Çalışan bir prototipi uygun kimlik, ağ ve izlemeyle bir üretim endpoint'ine götürmek bir haftalık DevOps çalışması gerektirmemeli. Artık iki komut ve birkaç dakika gerektiriyor.

## Sonuç

`azd ai agent` şu an mevcut. AI agent'larınızı dağıtmayı erteliyorsanız çünkü altyapı kurulumu çok fazla iş gibi geliyordu, bunu bir deneyin. Ön uç sohbet uygulaması entegrasyonu dahil adım adım tam kılavuz için [tam anlatıma](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) göz atın.
