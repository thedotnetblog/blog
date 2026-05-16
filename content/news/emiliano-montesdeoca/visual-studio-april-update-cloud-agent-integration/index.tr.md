---
title: "Visual Studio 2026 Nisan Güncellemesi: Bulut Ajanı, Özel Ajanlar ve Hata Ayıklama Ajanı"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026 Nisan güncellemesi (18.5), bulut ajanı entegrasyonu, kullanıcı düzeyinde özel ajanlar, C++ araçları GA ve gerçek çalışma zamanı davranışına karşı düzeltmeleri doğrulayan Hata Ayıklama Ajanı'nı ekliyor."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[Visual Studio 2026 Nisan güncellemesi (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/), bulut ajanı entegrasyonu, kullanıcı düzeyinde özel ajanlar, GA'ya ulaşan C++ araçları ve yeni Hata Ayıklama Ajanı'nı içeriyor.

## Bulut Ajanı: İşi Uzak Copilot Oturumuna Devretme

Chat penceresindeki ajan seçicisinden **Cloud** seçildiğinde bir Copilot uzaktan kodlama ajanına iş devredilir. İşi açıklarsınız, ajan deponuzda bir GitHub issue açar, ardından tamamlandığında bir PR oluşturur. "View PR" / "Open in browser" düğmeleriyle bir bildirim alırsınız — siz kodlamaya devam ederken, hatta IDE kapalıyken bile çalışıyor.

## Özel Ajanlar Artık Sizi Takip Ediyor

`%USERPROFILE%/.github/agents/` konumunda saklanan özel ajanlar artık tek bir depoya bağlı değil — projeler arasında sizi takip ediyorlar. Depolama yolu Tools > Seçenekler > GitHub > Copilot > Chat'ten yapılandırılabilir. Ajan seçicisindeki `+` düğmesi doğrudan yeni ajanlar oluşturmanızı sağlıyor. Depo kapsamlı ajanlarla aynı yeteneklere sahipler: çalışma alanı farkındalığı, araçlar, model seçimi ve MCP bağlantıları.

Yerleşik ajanlar: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## C++ Kod Düzenleme Araçları GA Oluyor

`get_symbol_call_hierarchy` ve `get_symbol_class_hierarchy` — iki araç artık varsayılan olarak açık. C++ kod tabanları üzerinde Copilot'a dil navigasyonu sağlıyorlar; kalıtım hiyerarşilerini ve işlev çağrı zincirlerini kapsıyorlar. Copilot Chat'teki Tools simgesinden etkinleştirin. Araç çağrısını destekleyen modellerle en iyi şekilde çalışıyor.

## Hata Ayıklama Ajanı: Düzeltmeler Gerçek Çalışma Zamanı Davranışına Karşı Doğrulanıyor

GitHub veya Azure DevOps issue'su (veya doğal dil açıklaması) ile başlayın, Debugger moduna geçin; ajan:

1. Minimal bir yeniden üretici oluşturur
2. Hata hipotezleri üretir
3. Uygulamayı izleme noktaları ve koşullu kesme noktalarıyla enstrümante eder
4. Gerçek bir hata ayıklama oturumu çalıştırır
5. Canlı telemetriyi analiz eder
6. Kesin bir düzeltme önerir

Siz süreç boyunca döngüde kalırsınız — bu etkileşimli, tamamen otonom değil.

## IntelliSense Öncelik Düzeltmesi

VS artık IntelliSense listesi etkinken Copilot tamamlamalarını engelliyor. Aynı anda yalnızca bir öneri. Bu sık yaşanan bir sürtüşme noktasıydı ve artık varsayılan olarak etkin.

Tam sürüm notları ve indirme için [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
