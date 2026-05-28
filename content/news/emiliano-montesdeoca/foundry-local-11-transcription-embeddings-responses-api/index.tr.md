---
title: "Foundry Local 1.1: Gerçek Zamanlı Transkripsiyon, Embeddings ve Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1, canlı mikrofon transkripsiyonu, metin embeddings ve Responses API desteği ekliyor — hepsi bulut bağımlılığı olmadan, ağ gecikmesi olmadan, token başına maliyet olmadan yerel olarak çalışıyor."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 kavramı kanıtladı: Windows, macOS (Apple Silicon) ve Linux x64'te geliştirici dostu bir SDK ile AI modellerini yerel olarak çalıştırmak. Sürüm 1.1, birçok gerçek üretim kullanım senaryosunu kapsayan üç yetenek ekliyor.

## Canlı Ses Transkripsiyonu

En önemli yeni özellik: mikrofondan doğrudan gerçek zamanlı konuşmadan metne akışı. Altyazılar, ses arayüzleri, toplantı transkripsiyonu, erişilebilirlik araçları — hepsi herhangi bir bulut bağımlılığı olmadan yerel olarak çalışıyor.

API, oturum tabanlıdır ve sonuçları gelir gelmez akışla iletir; geçici metni sonlandırılmış metinden ayırt etmek için `is_final` işaretçileri kullanır. JavaScript, C#, Python ve Rust dahil tüm dil bağlamalarında kullanılabilir.

Katalogdan bir akış konuşma modeli yükleyin, ses ayarlarıyla (örnekleme hızı, kanal, dil) bir oturum oluşturun, başlatın, ham PCM ses parçaları gönderin ve sonuçların zaman uyumsuz akışını tüketin. Gönderide tam Python ve C# örnekleri yer alıyor.

## Metin Embeddings

Anlamsal arama, RAG işlem hatları, kümeleme, benzerlik eşleştirme — bunların hepsi embeddings gerektirir. Foundry Local 1.1, cloud endpoint'e veri göndermeden aynı SDK'dan yerel olarak vektörler oluşturabilmeniz için embedding model desteği ekler.

Veri ikametinin önemli olduğu veya hassas içerik işlediğiniz uygulamalar için yerel embedding oluşturma anlamlı bir yetenektir.

## Responses API

Foundry Local artık [Responses API](https://platform.openai.com/docs/api-reference/responses)'ı destekliyor — ajansal etkileşimler için tasarlanmış yapılandırılmış arayüz. Bu şunları ekliyor:

- **Araç çağırma** — yerel çalışan modellerin tanımladığınız araçları çağırmasına izin verin
- **Çok modlu görüş-dil girişi** — görüş yeteneğine sahip modellere görüntü + metin aktarın
- Standart API şekliyle uyumlu, bu nedenle OpenAI'nin Responses API'sini hedefleyen mevcut ajanlar yerel modellere karşı çalışır

## Paket Boyutu İyileştirmeleri

İki değişiklik JavaScript paket boyutunu azaltır:
- `koffi` FFI katmanı özel bir Node-API C eklentisiyle değiştirildi
- WebGPU yürütme sağlayıcısı ayrı bir eklenti olarak geliyor, bu nedenle GPU hızlandırmaya ihtiyaç duymayan uygulamalar boyut maliyeti ödemez

C# SDK artık daha geniş .NET uyumluluğu için daha düşük framework sürümlerini hedefliyor.

## Neden Önemli

Üç yetenek birlikte — transkripsiyon, embeddings, araç çağırma — birçok AI uygulamasının temel yapı taşlarını kapsıyor. Bunları yerel olarak çalıştırmak şu anlama gelir:
- İnternet gerekmiyor
- Token başına maliyet yok
- Veri makineden çıkmıyor
- Ağ koşullarından bağımsız tutarlı gecikme

Foundry Local, edge senaryoları, gizlilik duyarlı iş yükleri, çevrimdışı uygulamalar veya geliştirme sırasında bulut bağımlılığından kaçınmak istediğiniz her şey için doğru seçimdir.

Orijinal gönderi: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
