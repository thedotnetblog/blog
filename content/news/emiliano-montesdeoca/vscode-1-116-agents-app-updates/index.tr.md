---
title: "VS Code 1.116 — Agents Uygulaması Klavye Navigasyonu ve Dosya Bağlamı Tamamlamaları Kazandı"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116, Agents uygulamasını geliştirmeye odaklanıyor — özel kısayol tuşları, erişilebilirlik iyileştirmeleri, dosya bağlamı tamamlamaları ve CSS @import bağlantı çözümlemesi."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "vscode-1-116-agents-app-updates" >}}).*

VS Code 1.116, Nisan 2026 sürümü; bazı yakın güncellemelerden daha hafif olsa da, değişiklikler odaklı ve anlamlı — özellikle Agents uygulamasını her gün kullanıyorsanız.

İşte [resmi sürüm notlarına](https://code.visualstudio.com/updates/v1_116) dayanarak neler geldi.

## Agents uygulaması iyileştirmeleri

Agents uygulaması, günlük iş akışlarında gerçek fark yaratan kullanılabilirlik geliştirmeleriyle olgunlaşmaya devam ediyor:

**Özel kısayol tuşları** — artık Changes görünümüne, Changes içindeki dosya ağacına ve Chat Customizations görünümüne özel komutlar ve klavye kısayollarıyla odaklanabilirsiniz. Agents uygulamasında gezinmek için tıklıyorsanız, bu tam klavye odaklı iş akışlarını getiriyor.

**Erişilebilirlik yardım diyaloğu** — sohbet giriş kutusunda `Alt+F1` tuşuna basmak artık mevcut komutları ve kısayol tuşlarını gösteren bir erişilebilirlik yardım diyaloğu açıyor. Ekran okuyucu kullanıcıları ayrıca duyuru ayrıntısını kontrol edebiliyor. İyi erişilebilirlik herkesin işine yarar.

**Dosya bağlamı tamamlamaları** — Agents uygulaması sohbetinde `#` yazarak mevcut çalışma alanınıza kapsamlı dosya bağlamı tamamlamalarını tetikleyin. Bu, her etkileşimi hızlandıran küçük bir yaşam kalitesi iyileştirmelerinden biri — koda referans verirken artık tam dosya yolları yazmak yok.

## CSS `@import` bağlantı çözümlemesi

Frontend geliştiricileri için güzel bir özellik: VS Code artık node_modules yollarını kullanan CSS `@import` referanslarını çözümlüyor. Bundler kullanırken `@import "some-module/style.css"` gibi importlar üzerinden `Ctrl+click` yapabilirsiniz. Küçük ama CSS iş akışlarındaki bir sürtünme noktasını ortadan kaldırıyor.

## Sonuç

VS Code 1.116, iyileştirmeyle ilgili — Agents uygulamasını daha kolay gezilebilir, daha erişilebilir ve klavye dostu hale getiriyor. Agents uygulamasında önemli zaman harcıyorsanız (ki pek çoğumuzun harcadığını düşünüyorum), bu değişiklikler birikir.

Tam liste için [sürüm notlarına](https://code.visualstudio.com/updates/v1_116) bakın.
