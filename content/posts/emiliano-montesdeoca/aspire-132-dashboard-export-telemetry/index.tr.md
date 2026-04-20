---
title: "Aspire 13.2 Dashboard'una Telemetri API'si Geldi — ve Her Şeyi Değiştiriyor"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2, daha akıllı telemetri dışa aktarma, izler ve loglar için programlanabilir bir API ve GenAI görselleştirme iyileştirmeleri sunuyor. Bunun hata ayıklama iş akışınız için neden önemli olduğu."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-132-dashboard-export-telemetry" >}}).*

.NET Aspire ile dağıtık uygulamalar geliştiriyorsanız, dashboard'un tüm deneyimin en iyi parçası olduğunu zaten bilirsiniz. Tüm izleriniz, loglarınız ve metrikleriniz tek bir yerde — harici Jaeger yok, Seq kurulumu yok, "öbür terminale bakayım" anı yok.

Aspire 13.2 bunu önemli ölçüde daha iyi hale getirdi. James Newton-King [güncellemeyi duyurdu](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/) ve dürüst olmak gerekirse? Telemetri dışa aktarma ve API özellikleri tek başına yükseltmeye değer.

## Telemetriyi sağlıklı bir şekilde dışa aktarın

Hepimizin yaşadığı senaryoyu düşünün: dağıtık bir sorunu ayıklıyorsunuz, yirmi dakikalık kurulumun ardından sonunda yeniden üretiyorsunuz ve şimdi yaşananları ekibinizle paylaşmanız gerekiyor. Önceden? Ekran görüntüleri. İz ID'lerini kopyala-yapıştır. Her zamanki karmaşa.

Aspire 13.2, şunları yapabileceğiniz uygun bir **Logları ve telemetriyi yönet** iletişim kutusu ekliyor:

- Tüm telemetriyi temizleme (yeniden üretim denemesinden önce kullanışlı)
- Seçili telemetriyi standart OTLP/JSON formatında ZIP dosyasına dışa aktarma
- Bu ZIP'i daha sonra herhangi bir Aspire dashboard'una yeniden içe aktarma

Son kısım öldürücü özellik. Bir hatayı yeniden üretirsiniz, telemetriyi dışa aktarırsınız, iş öğenize eklersiniz ve ekip arkadaşınız tam olarak gördüğünüzü görmek için kendi dashboard'una içe aktarabilir. Artık "kendi makinende yeniden üretebilir misin?" yok.

Bireysel izler, span'lar ve loglar da bağlam menülerinde "JSON Dışa Aktar" seçeneği kazanıyor. Tek bir izi paylaşmanız mı gerekiyor? Sağ tıklayın, JSON kopyalayın, PR açıklamanıza yapıştırın. Tamam.

## Telemetri API'si gerçek oyun değiştirici

En çok bu konuya heyecanlıyım. Dashboard artık telemetri verilerini programatik olarak sorgulamak için `/api/telemetry` altında bir HTTP API sunuyor. Kullanılabilir endpoint'ler:

- `GET /api/telemetry/resources` — telemetrisi olan kaynakları listele
- `GET /api/telemetry/spans` — filtrelerle span'ları sorgula
- `GET /api/telemetry/logs` — filtrelerle logları sorgula
- `GET /api/telemetry/traces` — izleri listele
- `GET /api/telemetry/traces/{traceId}` — belirli bir iz için tüm span'ları getir

Her şey OTLP JSON formatında dönüyor. Bu, yeni `aspire agent mcp` ve `aspire otel` CLI komutlarını besliyor, ama gerçek anlam daha büyük: artık uygulamanızın telemetrisini doğrudan sorgulayan araçlar, scriptler ve AI agent entegrasyonları oluşturabilirsiniz.

Hata ayıklarken gerçek dağıtık izlerinize bakabilen bir AI kodlama agentı hayal edin. Bu artık hayali değil — bu API'nin mümkün kıldığı şey tam olarak bu.

## GenAI telemetri pratikleşiyor

Semantic Kernel veya Microsoft.Extensions.AI ile AI destekli uygulamalar geliştiriyorsanız, geliştirilmiş GenAI telemetri görselleştiricisini takdir edeceksiniz. Aspire 13.2 şunları ekliyor:

- Markdown olarak render edilen AI araç açıklamaları
- AI iz erişimini hızlandırmak için izler sayfasında özel GenAI butonu
- Kesik veya standart olmayan GenAI JSON için daha iyi hata yönetimi
- Araç tanımları arasında tıkla-vurgula navigasyonu

Blog yazısı, VS Code Copilot chat, Copilot CLI ve OpenCode'un tümünün `OTEL_EXPORTER_OTLP_ENDPOINT` yapılandırmasını desteklediğinden bahsediyor. Bunları Aspire dashboard'una yönlendirin ve AI agentlarınızın telemetri aracılığıyla gerçek zamanlı olarak nasıl düşündüğünü izleyebilirsiniz. Bu, başka hiçbir yerde bulamayacağınız bir hata ayıklama deneyimidir.

## Sonuç

Aspire 13.2, dashboard'u "güzel bir hata ayıklama arayüzü"nden "programlanabilir bir gözlemlenebilirlik platformu"na taşıyor. Dışa aktarma/içe aktarma iş akışı tek başına dağıtık hata ayıklamada gerçek zaman kazandırıyor; telemetri API'si ise AI destekli tanılama kapısını açıyor.

Zaten Aspire kullanıyorsanız, yükseltin. Kullanmıyorsanız — bu, [aspire.dev](https://aspire.dev)'e göz atmak ve tüm meseleyi anlamak için iyi bir neden.
