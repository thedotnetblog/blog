---
title: "Aspire 13.2'nin Dashboard'ı Artık Telemetry API'ya Sahip — Bu Her Şeyi Değiştiriyor"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2, daha akıllı telemetri dışa aktarma, izleme ve günlükler için programlanabilir API ve GenAI görselleştirme iyileştirmeleri sunuyor. Bu, hata ayıklama iş akışınız için neden önemli?"
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-132-dashboard-export-telemetry" >}}).*

.NET Aspire ile dağıtık uygulamalar geliştiriyorsanız, dashboard'ın tüm deneyimin en iyi tarafı olduğunu zaten biliyorsunuzdur. Aspire 13.2 onu önemli ölçüde iyileştirdi.

## Telemetriyi normal bir şekilde dışa aktarma

Aspire 13.2, şunları yapabileceğiniz uygun bir **Günlükleri ve telemetriyi yönet** diyalogu ekler:
- Tüm telemetriyi temizle
- Seçili telemetriyi standart OTLP/JSON formatında ZIP dosyasına aktar
- Bu ZIP'i daha sonra herhangi bir Aspire dashboard'ına yeniden içe aktar

Bu son kısım killer özellik. Bir hatayı yeniden üretirsiniz, telemetriyi dışa aktarırsınız, iş öğenize eklersiniz ve ekibiniz kendi dashboard'ına içe aktararak tam olarak ne gördüğünüzü görebilir.

## Telemetry API asıl oyun değiştirici

Dashboard artık telemetri verilerini programatik olarak sorgulamak için `/api/telemetry` altında bir HTTP API sunuyor:
- `GET /api/telemetry/resources` — telemetrili kaynakları listele
- `GET /api/telemetry/spans` — filtrelerle span sorgula
- `GET /api/telemetry/logs` — filtrelerle log sorgula
- `GET /api/telemetry/traces` — izleri listele

Bu, yeni `aspire agent mcp` ve `aspire otel` CLI komutlarını besliyor.

## GenAI telemetrisi pratik hale geliyor

VS Code Copilot chat ve Copilot CLI, `OTEL_EXPORTER_OTLP_ENDPOINT` yapılandırmayı destekliyor — Aspire dashboard'ına yöneltin ve AI ajanlarınızın gerçek zamanlı olarak telemetri aracılığıyla düşündüğünü izleyebilirsiniz.

## Sonuç

Aspire 13.2, dashboard'ı "güzel hata ayıklama UI'sinden" "programlanabilir gözlemlenebilirlik platformuna" dönüştürüyor. [aspire.dev](https://aspire.dev)'i inceleyin.
