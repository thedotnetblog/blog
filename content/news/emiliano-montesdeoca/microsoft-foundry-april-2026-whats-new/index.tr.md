---
title: "Microsoft Foundry Nisan 2026: Foundry Local GA, GPT-5.5, Hyperlight ile CodeAct"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Nisan'ın Foundry özeti ağır: Foundry Local GA'ya ulaştı, GPT-5.5 geldi, Agent Framework OpenTelemetry izleme aldı, CodeAct Python'ı Hyperlight mikro-VM'lerde çalıştırdı ve Agent Monitoring Dashboard kullanıma sunuldu."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Microsoft Foundry için yoğun bir aydı. İşte en önemli duyurular.

## Foundry Local Genel Kullanıma Açıldı

Foundry Local — Microsoft'un çapraz platform yerel AI çalışma zamanı — Windows, macOS (Apple Silicon) ve Linux x64'te önizlemeden GA'ya geçti. Geliştirici dostu SDK ile üretime hazır yerel model çıkarımı. Sürüm 1.1, transkripsiyon, embeddings ve Responses API desteği ekler.

## GPT-5.5

GPT-5 ailesinin en yeni modeli artık Foundry'de kullanılabilir. Tier 5 ve Tier 6 abonelikleri için varsayılan kota. Önceki GPT-5 varyantlarıyla çalışıyorsanız, kullanım durumunuza göre değerlendirmeye değer.

## Foundry'de Agent Framework İzleme

Bu ay iki izleme özelliği önizleme olarak geliyor:

**Microsoft Agent Framework İzleme** — MAF ajanları artık Foundry'e OpenTelemetry izleri gönderebilir. Ajan davranışını hata ayıkla, çok adımlı yürütmeleri izle, araç çağrıları genelindeki gecikme ve hataları ortaya çıkar. Bu gerçek bir boşluğu doldurur: *ajanın üretimde gerçekte ne yaptığını* bilmek, yalnızca ne döndürdüğünü değil.

**Barındırılan Ajan İzleme** — Barındırılan ajanların oturumları, araç çağrıları ve çalışma adımları da Foundry izlerinde görünür. Aynı gözlemlenebilirlik hikayesi barındırılan katmana genişler.

## Hyperlight ile CodeAct (Alpha)

Bu, teknik açıdan en ilginç eklenti: Agent Framework artık [Hyperlight](https://github.com/hyperlight-dev/hyperlight) mikro sanal makineleri içinde Python kodu çalıştırabilir.

CodeAct, ajanların araç olarak Python kodu üretip çalıştırdığı modeldir. Açık endişe güvenliktir — model tarafından üretilen kodu çalıştırıyorsunuz. Hyperlight'ın mikro-VM'leri, yerel'e yakın başlatma süreleriyle işlem düzeyinde izolasyon sağlar; tam kapsayıcıların veya VM'lerin yükü olmadan sandbox kod yürütmeyi pratik hale getirir.

Kod yürütme gerektiren ajan iş akışları için bu, host sürecinde kod çalıştırmaya kıyasla önemli bir güvenlik iyileştirmesidir.

## Agent Monitoring Dashboard (Önizleme)

Token kullanımı, gecikme, çalışma başarı oranı ve değerlendirici puanlarını tek bir görünümde birleştiren birleşik bir operasyonel pano. Normal gözlemlenebilirlik panolarından farkı: operasyonel metriklerin yanında değerlendirme sonuçlarını içerir, böylece "ajan daha yavaş hale geldi"yi "değerlendirici puanları düştü" ile ilişkilendirebilir — veya bunların ilgisiz olduğunu doğrulayabilirsiniz.

## Sürekli Değerlendirme Özel Değerlendiricileri (Önizleme)

Artık kendi kod tabanlı veya prompt tabanlı değerlendiricilerinizi sürekli değerlendirme ardışık düzenine getirebilirsiniz. Daha önce, sürekli değerlendirme yerleşik değerlendiricilerle sınırlıydı. Özel değerlendiriciler, üretim izleme döngüsünde takıma özgü kalite standartlarını uygulamanıza olanak tanır.

## Control Plane'de Ajan Envanteri

Foundry Control Plane Operate görünümü artık aboneliğinizdeki desteklenen tüm ajanları gösterir: Foundry ajanları, Azure SRE Agent, Logic Apps ajan döngüleri ve kayıtlı özel ajanlar. Neyin nerede dağıtıldığını anlamak için tek bir görünüm.

Orijinal gönderi: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
