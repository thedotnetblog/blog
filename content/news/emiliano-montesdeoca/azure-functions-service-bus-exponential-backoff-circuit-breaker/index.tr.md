---
title: "Zorlanan Bir Bağımlılığı Dövmeyi Bırakın: Azure Functions + Service Bus için Yeniden Deneme Desenleri"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Üstel geri çekilme ve devre kesici desenleri artık Service Bus tarafından tetiklenen Azure Functions için yerel olarak desteklenmektedir — nasıl çalıştıkları ve neden her ikisini de istediğiniz aşağıda açıklanmıştır."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Bir Functions uygulamasında kurtarılabilir bir hatanın nasıl kesintiye dönüştüğü şöyle işler: bir bağımlılık zaman aşımına uğramaya başlar, her Functions örneği hemen ve süresiz olarak yeniden dener, bağımlılık yüzlerce eş zamanlı başarısız istekle dövülür ve geçici bir aksaklık olarak başlayan şey sistem genelinde bir geri basınç olayına dönüşür.

Bu hikayeyi muhtemelen biliyorsunuzdur. Azure Functions hızla ölçeklenir — tüm nokta bu. Ancak "hızlı ölçekleme" ve "anında yeniden deneme" bir arada hataları dramatik biçimde kötüleştirebilir.

İki desen yardımcı olur. Üstel geri çekilme ve devre kesici. Her ikisi de artık Service Bus tarafından tetiklenen Azure Functions için yerel olarak desteklenmektedir.

## İki Desen, Farklı Roller

Bu desenler birbirini tamamlar, alternatif değildir:

**Üstel geri çekilme** şunu yanıtlar: *ne zaman tekrar denemem gerekir?*
Bir bağımlılığın iyileşmesi için zaman tanımak adına yeniden denemeler arasındaki gecikmeyi artırır. Mesaj düzeyinde, yeniden deneme zamanlamasının ayarlanması.

**Devre kesici** şunu yanıtlar: *şu anda bu bağımlılığı çağırmalı mıyım?*
Bir başarısızlık eşiğine ulaşıldıktan sonra sağlıksız bir bağımlılığa yönelik tekrarlanan çağrıları durdurur, ardından soğuma süresinden sonra dikkatli bir şekilde araştırır. Sistem düzeyinde, yeniden deneme fırtınalarını önler.

Her ikisini de istiyorsunuz. Geri çekilme mesaj başına yeniden deneme hızlandırmasını yönetir. Devre kesici toplu sağlık kararlarını yönetir.

## Bu Özellikle Service Bus için Neden Önemli

Kuyruk veri trafiği artışlarını emer, bu iyidir. Ancak kontroller olmadan, çalışanlar başarısız olacak çağrılara hesaplama kaynaklarını boşa harcamaya devam ederken kuyruk büyüyebilir. Zehirli mesajlar olması gerekenden daha uzun süre aktif kalır. Sıcak bölümler veya sınırlı alt akış kapasitesi basamaklı sorunlara yol açar.

Daha güvenli tasarım:

1. Geçici hatayı tespit et
2. Sonraki girişimi üstel geri çekilme ile ertele
3. Bir başarısızlık eşiğine ulaşıldığında bağımlılığa çağrıları durdur (devre açık)
4. Soğuma süresinden sonra dikkatli bir şekilde devam et (devre araştırması)
5. Kurtarılamaz çalışmayı dead-letter'a veya karantina yoluna taşı

## Yerel Desteğin Görünümü

Yeni destek mevcut Azure Functions ana bilgisayar modeliyle entegre olur — ek kitaplık yok, özel uygulama yok. Yapılandırma `host.json` dosyanıza gider:

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

Devre kesici yapılandırması, sağlıksız bağımlılıkların kurtarma sırasında dövülmemesi için başarısızlık eşiğini ve sıfırlama aralığını ayarlar.

## Desteklenen Diller

Bu yalnızca .NET için değil. Özellik dotnet, JavaScript, TypeScript ve Python'ı kapsar — Azure Functions'taki Service Bus tetikleyici tarafından desteklenen tam dil seti.

## Sonuç

Yeniden deneme desenlerini yapılandırmak, bir alt akış kesintisinin Functions'larınızın zarif bir şekilde bozunmak yerine sorunu daha da kötüleştirmesine yol açtığı ilk ana kadar heyecan verici değildir. Bunları proaktif olarak ayarlamak ucuzdur. Bir olay sırasında yeniden düzenlemek değildir.

Orijinal gönderi: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
