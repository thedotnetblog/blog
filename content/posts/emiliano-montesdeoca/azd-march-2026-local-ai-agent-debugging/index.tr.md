---
title: "azd Artık AI Agentlarını Yerel Olarak Çalıştırmanıza ve Hata Ayıklamanıza İzin Veriyor — Mart 2026'da Ne Değişti"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI, Mart 2026'da yedi sürüm yayımladı. Öne çıkanlar: AI agentlar için yerel çalıştırma-hata ayıklama döngüsü, proje kurulumunda GitHub Copilot entegrasyonu ve Container App Jobs desteği."
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

Bir ayda yedi sürüm. Azure Developer CLI (`azd`) ekibinin Mart 2026'da yayımladığı bu kadar, ve en önemli özellik beklediğim şey: **AI agentlar için yerel çalıştırma-hata ayıklama döngüsü**.

## AI agentları dağıtmadan çalıştırın ve hata ayıklayın

Bu büyük. Yeni `azure.ai.agents` uzantısı bir dizi komut ekliyor:

- `azd ai agent run` — agentı yerel olarak başlatır
- `azd ai agent invoke` — ona mesaj gönderir (yerel veya dağıtılmış)
- `azd ai agent show` — container durumunu ve sağlığını gösterir
- `azd ai agent monitor` — container günlüklerini gerçek zamanlı olarak yayınlar

Eskiden, bir AI agentını test etmek her değişiklikte Microsoft Foundry'ye dağıtmak anlamına geliyordu. Artık yerel olarak yineleyebilirsiniz.

## GitHub Copilot azd projenizi iskele kuruyor

`azd init` artık "GitHub Copilot ile Kur (Önizleme)" seçeneği sunuyor. Copilot agentı proje yapınız için yapılandırmayı otomatik olarak oluşturuyor.

## Container App Jobs ve dağıtım iyileştirmeleri

- **Container App Jobs**: `azd` artık mevcut `host: containerapp` konfigürasyonu aracılığıyla `Microsoft.App/jobs` dağıtıyor
- **Yapılandırılabilir dağıtım zaman aşımları**: `azd deploy`'da yeni `--timeout` flag'i
- **Uzak build geri dönüşü**: Uzak ACR build başarısız olduğunda `azd` otomatik olarak yerel Docker/Podman build'e döner
- **Yerel ön uçuş doğrulaması**: Bicep parametreleri dağıtmadan önce yerel olarak doğrulanır

## Sonuç

Yerel AI agent hata ayıklama döngüsü bu sürümün yıldızı. [Tam sürüm notlarına](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) bakın.
