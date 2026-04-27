---
title: "Copilot'a Günde 68 Dakika Kodu Yeniden Açıklamak mı? Bir Çözümü Var"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context rot gerçek — AI agent'iniz 30 turdan sonra yolunu şaşıyor ve her saat compaction vergisi ödüyorsunuz. auto-memory, GitHub Copilot CLI'a binlerce token yakmadan cerrahi düzeyde recall sağlıyor."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Copilot oturumunuz `/compact`'e ulaştığında ve agent yaptığınız işi tamamen unuttuğunda o anı biliyor musunuz? Sonraki beş dakika dosya yapısını, başarısız testi ve daha önce denediğiniz üç yaklaşımı yeniden açıklarsınız. Sonra bu tekrar olur. Ve yine.

Desi Villanueva bunu ölçtü: **günde 68 dakika** — yalnızca yeniden yönlendirme için. Kod yazmak için değil. PR incelemek için değil. Sadece AI'ı zaten bildiği şeylerle yeniden hizalamak için.

Bunun neden olduğunu ve bunun için somut bir çözüm bulunduğunu ortaya koyuyor.

## Bağlam Penceresinin Yalanı

Agent'iniz kutuda büyük bir sayı ile geliyor. 200K token. Kulağa devasa geliyor. Pratikte bu bir tavan, garanti değil.

İşte gerçek matematik:

- Toplam 200K context
- Başlangıçta yüklenen MCP araçları için yaklaşık 65K eksik (~33%)
- `AGENTS.md` veya `copilot-instructions.md` gibi instruction dosyaları için yaklaşık 10K eksik

Böylece size yaklaşık **125K kalıyor, daha ilk kelimeyi yazmadan önce**. Ve durum daha da kötü — LLM'ler context doldukça düzgün şekilde degrade olmaz. Yaklaşık %60 kapasitede duvara çarparlar. Model, 30 tur önce söylenen şeyleri kaybetmeye başlar, önceki cevaplarla çelişir ve 10 dakika önce güvenle söylediği dosya adlarını halüsinasyon olarak üretir. Sektör buna "lost in the middle" problemi diyor.

Etkin sınır: kalite düşmeye başlamadan önce **45K token**. Bu da muhtemelen agent'in kaymaya başlamasından önce sadece 20-30 aktif konuşma turu demek. Bu yüzden `/compact`'e her 45 dakikada bir gidiyorsunuz — 200K token doldurduğunuz için değil, model 120K'de zaten bozulmaya başladığı için.

## Compaction Vergisi

Her `/compact` akış durumunuzu alır götürür. Derin bir debug oturumundasınız. Paylaşılan context 30 dakikadır oluşuyor. Agent dosya yapısını, başarısız testi ve hipotezi biliyor. Sonra uyarı geliyor.

- Görmezden gelin → agent giderek aptallaşır ve eski state'i halüsinasyonla doldurmaya başlar
- `/compact` çalıştırın → agent'a 30 dakikalık bir incelemenin iki paragraflık özeti verilir

Her iki durumda da kaybedersiniz. Her iki durumda da projenizi ilk günündeki yeni bir çalışana anlatıyormuşsunuz gibi yeniden anlatırsınız.

Kötü tarafı? **Memory zaten var**. Copilot CLI her oturumu `~/.copilot/session-store.db` içindeki yerel bir SQLite veritabanına yazar — dokunulan her dosya, her tur, her checkpoint. Hepsi diskte duruyor. Agent sadece okuyamıyor.

## auto-memory: bir recall katmanı, memory sistemi değil

auto-memory'nin arkasındaki ana fikir bu: yeni bir memory sistemi kurmayın — zaten var olanın üstüne yalnızca okunabilir bir query katmanı kurun.

```bash
pip install auto-memory
```

Yaklaşık 1.900 satır Python. Sıfır bağımlılık. 30 saniyede kurulur.

Context'i grep sonuçlarıyla doldurmak yerine, agent'e gerçekten önemli olana cerrahi erişim verirsiniz:

| İşlem | Token | Ne elde edersiniz |
|-------|-------|-------------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 sonuç, çoğu alakasız |
| `find . -name "*.py"` | ~2,000 | Tüm Python dosyaları, contextsiz |
| Agent yeniden yönlendirme | ~2,000 | Ona zaten bilmesi gereken şeyi siz anlatırsınız |
| **`auto-memory files --json --limit 10`** | **~50** | **Dün üzerinde çalıştığınız 10 dosya** |

Bu 200x iyileşme demek. Agent arkeolojik kazıyı atlar ve doğrudan önemli olana gider.

Önerilen akış: context kullanımınız %50-70'e yaklaşınca `/clear` çalıştırın ve ardından şunu yazın: "X konusunu tartıştığımız son oturumları incele". Kör aramalara 12K token harcamak yerine, auto-memory ilgili context'i 50 token içinde çeker.

## Bu .NET Geliştiricileri İçin Neden Önemli

GitHub Copilot CLI'ı .NET işleri için kullanıyorsanız — servisler scaffold etmek, EF Core sorgularını debug etmek, Blazor bileşenleri üzerinde yinelemek — context rot problemi size de aynı sertlikle çarpar. Birden fazla proje, paylaşılan kütüphaneler ve derin call chain'ler içeren karmaşık çözümler, agent'in en hızlı yolunu kaybettiği codebase türüdür.

Kurulum kılavuzu Copilot CLI'ı buna nasıl yönlendireceğinizi anlatıyor. Bu tek seferlik bir kurulum.

Dürüst olmak gerekirse? Günde 68 dakikayı geri kazanmak küçük bir yaşam kalitesi ayarı değil. Bu haftada neredeyse 6 saat eder.

## Kapanış

Context rot gerçek bir mimari kısıt, sonradan patch'lenecek bir bug değil. auto-memory, agent'inize pahalı ve gürültülü yeniden keşif yerine ucuz ve kesin bir recall mekanizması vererek bunu aşıyor. GitHub Copilot CLI ile ciddi AI destekli geliştirme yapıyorsanız, 30 saniyelik kurulum buna değer.

Göz atın: [GitHub'da auto-memory](https://github.com/dezgit2025/auto-memory). Desi Villanueva'nın orijinal yazısı: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).