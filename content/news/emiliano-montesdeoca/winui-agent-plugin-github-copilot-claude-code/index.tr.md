---
title: "GitHub Copilot ve Claude Code için WinUI Ajan Eklentisi"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft, WinUI geliştirme için ajan becerilerini yayımladı: scaffold, derleme, çalıştırma, test, iterasyon — hepsi GitHub Copilot CLI veya Claude Code ile. Temel yenilik: ajanı WinUI'ya özgü gerçeklere sabitleyen amaca yönelik araçlar."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft, WinUI uygulama geliştirme için açık kaynaklı ajan becerileri seti yayımladı; [aka.ms/winui-skills](https://aka.ms/winui-skills) adresinde kullanılabilir.

## Kurulum ve Yapılandırma

Eklentiyi `/plugin install winui@awesome-copilot` ile yükleyin, ardından `/winui:winui-setup` ile ilk yapılandırmayı çalıştırın. Kurulum süreci ön koşulları doğrular, gerekli bağımlılıkları yükler ve WinUI uygulama geliştirme ortamını yapılandırır.

## Uçtan Uca Geliştirme Döngüsü

Beceriler tam geliştirme döngüsünü kapsar:

- **Scaffold:** Uygun parametrelerle `dotnet new WinUI` kullanarak doğru proje şablonunu oluşturur — ajan doğru şablonları ve varsayılan yapılandırma değerlerini bilir.
- **Derleme:** WinUI uygulamalarının gerektirdiği paketlenmiş yürütme modelini yönetir; paket imzalama ve manifes yapılandırmalarını içerir.
- **Etkileşim ve doğrulama:** Uygulamayı başlatır, onunla etkileşime girer ve davranışı doğrular.
- **Derleme hatalarını düzeltme:** Ajan, WinUI'ya özgü hata mesajlarını anlar ve bunların nasıl çözüleceğini bilir.

## Amaca Yönelik Araçlarla Token Verimliliği

Temel yenilik, becerilerin talep üzerine somut referans verilerini getiren amaca yönelik araçlar içermesidir:

- WinUI ve Fluent Design API ayrıntıları
- MVVM desenleri ve en iyi uygulamalar
- MSIX paketleme, kod imzalama ve Store gönderimi
- Erişilebilirlik, tema oluşturma ve UI otomasyonu

Tüm WinUI belgelerini bağlama enjekte etmek yerine, araçlar tam olarak ajanın ihtiyaç duyduğu anda tam olarak ihtiyacı olanı getirir. Bu, bağlam kullanımını verimli tutar ve özelleşmiş alanlarda doğruluğu artırır.

## Amaca Yönelik Becerilerin Neden Önemli Olduğu

Genel amaçlı dil modellerinin WinUI'ya özgü nüanslar hakkında sınırlı bilgisi vardır: paketlenmiş yürütme modeli, Fluent Design API'leri, MSIX entegrasyonu veya Windows App SDK'nın Win32 işlevselliğini nasıl sardığı. Amaca yönelik araçlar bunu, ajanı potansiyel olarak eski veya yanlış model bilgisi yerine doğrulanmış WinUI gerçeklerine sabitleyerek çözer.

Aynı desen, genel geliştirme desenlerinden farklı kendi kural ve gereksinimleri olan her özel çerçeve veya SDK için geçerlidir.

Orijinal gönderi: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
