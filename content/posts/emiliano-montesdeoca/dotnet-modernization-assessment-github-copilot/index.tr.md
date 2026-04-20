---
title: "GitHub Copilot Modernizasyon Değerlendirmesi Henüz Kullanmadığınız En İyi Migrasyon Aracı"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "GitHub Copilot modernizasyon uzantısı sadece kod değişiklikleri önermez — uygulanabilir sorunlar, Azure hedef karşılaştırmaları ve işbirliği iş akışıyla tam bir migrasyon değerlendirmesi üretir."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "dotnet-modernization-assessment-github-copilot" >}}).*

Eski bir .NET Framework uygulamasını modern .NET'e geçirmek, herkesin yapması gerektiğini bildiği ama kimsenin başlamak istemediği görevlerden biridir.

Jeffrey Fritz, [GitHub Copilot modernizasyon değerlendirmesine derinlemesine bir bakış yayımladı](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/).

## Bu sadece kod öneri motoru değil

VS Code uzantısı **Değerlendir → Planla → Uygula** modelini izler. Değerlendirme aşaması tüm kod tabanınızı analiz eder ve her şeyi yakalayan yapılandırılmış bir belge üretir.

Değerlendirme `.github/modernize/assessment/` altında saklanır. Her çalıştırma bağımsız bir rapor üretir.

## Başlangıç için iki yol

**Önerilen Değerlendirme** — hızlı yol. Küratörlüğü yapılmış domenlerden seçin (Java/.NET Yükseltme, Cloud Hazırlığı, Güvenlik).

**Özel Değerlendirme** — hedefli yol. Tam olarak neyin analiz edileceğini yapılandırın: hedef hesaplama (App Service, AKS, Container Apps), hedef işletim sistemi, konteynerleştirme analizi.

## Sorun dökümleri eyleme geçirilebilir

Her sorun bir kritiklik düzeyiyle gelir:

- **Zorunlu** — düzeltilmeli yoksa migrasyon başarısız olur
- **Olası** — migrasyonu etkileyebilir, insan değerlendirmesi gerektirir
- **İsteğe bağlı** — önerilen iyileştirmeler, migrasyonu engellemez

## Düşüncem

Eski .NET Framework uygulamalarınız varsa, buradan başlamak için *en iyi* araç budur.

[Tam rehberi](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) okuyun ve [VS Code uzantısını](https://aka.ms/ghcp-appmod/vscode-ext) edinin.
