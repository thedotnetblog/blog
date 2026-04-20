---
title: "azd Artık AI Ajanlarınızı Yerel Ortamda Çalıştırıp Hata Ayıklamanıza İzin Veriyor — Mart 2026'daki Değişiklikler"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI, Mart 2026'da yedi sürüm yayımladı. Öne çıkanlar: AI ajanları için yerel çalıştırma ve hata ayıklama döngüsü, proje kurulumunda GitHub Copilot entegrasyonu ve Container App Jobs desteği."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azd-march-2026-local-ai-agent-debugging" >}}).*

Bir ayda yedi sürüm. Azure Developer CLI (`azd`) ekibinin Mart 2026'da yaptığı bu ve başlık özelliği benim beklediğim şey: **AI ajanları için yerel çalıştırma ve hata ayıklama döngüsü**.

PC Chan [tam özeti yayımladı](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) ve orada pek çok şey olsa da, AI destekli uygulamalar geliştiren .NET geliştiricileri için gerçekten önem taşıyan şeyleri özetleyeyim.

## AI ajanlarını dağıtmadan çalıştırın ve hata ayıklayın

En büyük yenilik bu. Yeni `azure.ai.agents` uzantısı, AI ajanları için düzgün bir iç döngü deneyimi sunan bir dizi komut ekliyor:

- `azd ai agent run` — ajanı yerel olarak başlatır
- `azd ai agent invoke` — ona mesaj gönderir (yerel veya dağıtılmış)
- `azd ai agent show` — container durumunu ve sağlığını gösterir
- `azd ai agent monitor` — container loglarını gerçek zamanlı akıtır

Bundan önce, bir AI ajanını test etmek her değişiklik yaptığınızda Microsoft Foundry'e dağıtmak anlamına geliyordu. Artık yerel olarak yineleyebilir, ajanın davranışını test edebilir ve yalnızca hazır olduğunuzda dağıtabilirsiniz. Microsoft Agent Framework veya Semantic Kernel ile ajan geliştiriyorsanız, bu günlük iş akışınızı değiştiriyor.

invoke komutu hem yerel hem de dağıtılmış ajanlara karşı çalışıyor; bu, ajanın nerede çalıştığından bağımsız olarak aynı test iş akışını kullanabileceğiniz anlamına geliyor. Bu tür bir ayrıntı, iki ayrı test betiği setini sürdürmek zorunda kalmaktan sizi kurtarıyor.

## GitHub Copilot azd projenizi iskelet oluşturuyor

`azd init` artık "GitHub Copilot ile Kur (Önizleme)" seçeneği sunuyor. Proje yapınız hakkındaki prompt'lara manuel olarak yanıt vermek yerine, bir Copilot ajanı yapılandırmayı sizin için iskelet oluşturuyor. Herhangi bir şeyi değiştirmeden önce kirli çalışma dizinini kontrol ediyor ve MCP sunucusu araç iznini önceden istiyor.

Bir komut başarısız olduğunda, `azd` artık AI destekli sorun giderme sunuyor: bir kategori seçin (açıkla, rehberlik, sorun gider veya atla), ajanın bir düzeltme önermesine izin verin ve yeniden deneyin — hepsi terminali terk etmeden. Karmaşık altyapı kurulumları için bu gerçek anlamda zaman kazandırıyor.

## Container App Jobs ve dağıtım iyileştirmeleri

Dikkat çekmeye değer birkaç dağıtım özelliği:

- **Container App Jobs**: `azd` artık mevcut `host: containerapp` yapılandırması aracılığıyla `Microsoft.App/jobs` dağıtıyor. Bicep şablonunuz hedefin Container App mı yoksa Job mu olduğunu belirliyor — ekstra kurulum gerekmez.
- **Yapılandırılabilir dağıtım zaman aşımları**: `azd deploy` üzerinde yeni `--timeout` bayrağı ve `azure.yaml`'da `deployTimeout` alanı. Varsayılan 1200 saniyelik sınırı artık tahmin etmek zorunda değilsiniz.
- **Uzak derleme yedeklemesi**: Uzak ACR derlemesi başarısız olduğunda, `azd` otomatik olarak yerel Docker/Podman derlemesine geri düşüyor.
- **Yerel ön uçuş doğrulama**: Bicep parametreleri, Azure'a bir gidiş-dönüş yapmadan eksik parametreleri yakalamak için dağıtımdan önce yerel olarak doğrulanıyor.

## Geliştirici deneyimi iyileştirmeleri

Toplanınca fark yaratan küçük iyileştirmeler:

- JS/TS projeleri için **otomatik pnpm/yarn algılama**
- Python paketleme için **pyproject.toml desteği**
- **Yerel şablon dizinleri** — `azd init --template` artık çevrimdışı yineleme için dosya sistemi yollarını kabul ediyor
- `--no-prompt` modunda **daha iyi hata mesajları** — eksik tüm değerler çözüm komutlarıyla birlikte bir kerede raporlanıyor
- **Derleme ortam değişkenleri** tüm framework derleme alt süreçlerine enjekte ediliyor (.NET, Node.js, Java, Python)

Son madde ince ama önemli: .NET derlemeniz artık `azd` ortam değişkenlerine erişebilir; bu, ekstra betik yazmadan derleme zamanı yapılandırma enjeksiyonu yapabileceğiniz anlamına geliyor.

## Özet

Yerel AI ajan hata ayıklama döngüsü bu sürümün yıldızı, ancak dağıtım iyileştirmeleri ve geliştirici deneyimi cilasının birikmesi `azd`'yi her zamankinden daha olgun hissettiriyor. .NET uygulamalarını Azure'a — özellikle AI ajanlarını — dağıtıyorsanız, bu güncelleme kuruluma değer.

Her ayrıntı için [tam sürüm notlarına](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) bakın ya da [azd kurulumu](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) ile başlayın.
