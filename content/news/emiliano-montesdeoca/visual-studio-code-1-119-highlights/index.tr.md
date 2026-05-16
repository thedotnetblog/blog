---
title: "VS Code 1.119: Ajan Oturumları için OpenTelemetry, Tarayıcı Entegrasyonu ve Güvenlik"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (Mayıs 2026), ajan oturumları için OpenTelemetry izleme, tarayıcı sekme paylaşımı, güven ve güvenlik iyileştirmeleri ve 1.119.1 güvenlik yaması ekliyor."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119), 6 Mayıs 2026'da yayınlandı (kısa süre sonra 1.119.1 güvenlik yaması ile). Sürüm; ajan gözlemlenebilirliği, tarayıcı etkileşimi ve kesintileri azaltmaya odaklanıyor.

## Ajan Oturumları için OpenTelemetry İzleme

Bu, ajanları üretimde çalıştıran veya ajan iş akışlarını hata ayıklayan herkes için öne çıkan özellik. İki ayarla etkinleştirin:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

İzler GenAI semantik kurallarını takip ediyor. Her ajan isteği, iç içe geçmiş alt izlerle birlikte `invoke_agent` kök yayılımı oluşturuyor: `chat`, `execute_tool` ve `execute_hook`. Token kullanımı istek başına raporlanıyor — önbellek okuma ve önbellek oluşturma sayaçları dahil.

Yerel ajan, Copilot CLI arka plan ajanı ve Claude ajanıyla çalışıyor. Herhangi bir OTLP uyumlu arka uç izleri kabul ediyor — [bağımsız Aspire panosu](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) yerel geliştirme için iyi çalışıyor.

## Ajanlar Artık Tarayıcı Sekmelerine Erişebiliyor

Ajanlar yerleşik tarayıcı sekmelerine erişim talep edebilir — ancak otomatik olarak değil. Bir sekmeyi açıkça bağlam seçici, sürükle-bırak veya önerilen bağlam aracılığıyla paylaşmanız gerekiyor. Tarayıcıda erişimi iptal eden bir paylaşım düğmesi var. Bir ajan zaten açık olan (paylaşılmamış) bir sekmeyle aynı etki alanında yeni bir sekme açmaya çalıştığında, VS Code mevcut sekmeyi yeniden kullanmayı öneriyor.

## Token Kullanımı Optimizasyonu

Deneysel bir hafif model artık ajan görev listelerini yönetiyor ve bu rutin iş için ana modeli serbest bırakıyor. Tam akıl yürütme gücü gerektirmeyen görevler için token kullanımını azaltıyor.

## Güven ve Güvenlik

Daha az kesinti: VS Code 1.119, ajanlardan ağ erişimi ve geçici klasörlere yazma isteklerini azaltıyor. 1.119.1 yaması belirli güvenlik sorunlarını ele alıyor — henüz güncellemediyseniz güncellemeye değer.

## Markdown Önizlemeye Hızlı Geçiş

Küçük ama kullanışlı: gezinme olmadan mevcut düzenleyiciyi hızlıca Markdown önizlemesine geçirebilirsiniz.

## VS Code Agents (Insiders Önizlemesi)

Yeniden tasarlanmış ajan oturumu arayüzü — yeni depo seçici (yerel/depolar/uzak), alt oturum iyileştirmeleri, web ve mobil iyileştirmeleri, ilerleme animasyonları — Insiders'ta [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents) adresinde mevcut.

Tam değişiklik günlüğü: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
