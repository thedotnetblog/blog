---
title: ".NET Aspire 13.2 AI Ajanınızın En İyi Dostu Olmak İstiyor"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 ajansal geliştirmeye tam anlamıyla odaklanıyor — yapılandırılmış CLI çıktısı, izole çalıştırmalar, otomatik iyileştirme ortamları ve tam OpenTelemetry verisi sayesinde AI ajanlarınız uygulamalarınızı gerçekten derleyip çalıştırabilir ve izleyebilir."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-agentic-development-build-run-observe" >}}).*

AI kodlama ajanınızın sağlam bir kod yazdığı, heyecanlandığınız ve ardından uygulamayı çalıştırmaya çalışırken her şeyin dağıldığı o anı biliyor musunuz? Port çakışmaları, hayalet süreçler, yanlış ortam değişkenleri — ve bir anda ajanınız özellik geliştirmek yerine başlangıç sorunlarını çözmek için token harcamaya başlıyor.

Aspire ekibi tam da bu sorun hakkında [gerçekten düşünceli bir yazı](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) yayımladı ve cevapları ikna edici: Aspire 13.2 yalnızca insanlar için değil, AI ajanları için de tasarlanmış.

## Sorun gerçek

AI ajanları kod yazmakta inanılmaz derecede başarılı. Ancak çalışan bir full-stack uygulama göndermek, dosya oluşturmaktan çok daha fazlasını gerektiriyor. Servisleri doğru sırayla başlatmanız, portları yönetmeniz, ortam değişkenlerini ayarlamanız, veritabanlarını bağlamanız ve bir şeyler bozulduğunda geri bildirim almanız gerekiyor. Şu an çoğu ajan bunların hepsini deneme-yanılma yoluyla hallediypr — komutları çalıştırıyor, hata çıktısını okuyor, yeniden deniyor.

Markdown talimatları, özel skill'ler ve prompt'lar ekleyerek onlara rehberlik etmeye çalışıyoruz, ancak bunlar öngörülemez, derlenemiyor ve ayrıştırılmaları bile token harcıyor. Aspire ekibi temel içgörüyü doğru yakaladı: ajanların daha fazla Markdown'a değil, **derleyicilere ve yapılandırılmış API'lara** ihtiyacı var.

## Ajan altyapısı olarak Aspire

Aspire 13.2'nin ajansal geliştirme masasına getirdikleri:

**Tüm yığınınız yazılı kodda.** AppHost, tam topolojinizi — API, frontend, veritabanı, önbellek — derlenebilir TypeScript veya C# olarak tanımlıyor:

```typescript
import { createBuilder } from './.modules/aspire.js';

const builder = await createBuilder();

const postgres = await builder.addPostgres("pg").addDatabase("catalog");
const cache = await builder.addRedis("cache");

const api = await builder
  .addNodeApp("api", "./api", "src/index.ts")
  .withHttpEndpoint({ env: "PORT" })
  .withReference(postgres)
  .withReference(cache);

await builder
  .addViteApp("frontend", "./frontend")
  .withReference(api)
  .waitFor(api);

await builder.build().run();
```

Bir ajan, uygulama topolojisini anlamak, kaynak eklemek, bağlantıları oluşturmak ve *doğrulamak için derlemek* amacıyla bunu okuyabilir. Derleyici bir şeyin yanlış olduğunu anında söylüyor. Tahmin yok, yapılandırma dosyalarıyla deneme-yanılma yok.

**Her şeyi yöneten tek komut.** Ajanların `docker compose up`, `npm run dev` ve veritabanı başlangıç betikleri arasında denge kurması yerine tek yapmaları gereken şey `aspire start`. Tüm kaynaklar doğru sırayla, doğru portlarda, doğru yapılandırmayla başlıyor. Uzun süre çalışan süreçler ajanı engellemez — bunları Aspire yönetiyor.

**Paralel ajanlar için isolated mod.** `--isolated` seçeneğiyle her Aspire çalıştırması kendi rastgele portlarını ve ayrı user secret'larını alıyor. Git worktree'lerinde çalışan birden fazla ajanınız mı var? Çakışmayacaklar. Bu, paralel ortamlar açan VS Code'un background agent'ları gibi araçlar için çok büyük bir gelişme.

**Telemetri aracılığıyla ajan gözleri.** İşte burada gerçekten güçlü oluyor. Aspire CLI, geliştirme sırasında tam OpenTelemetry verilerini açığa çıkarıyor — trace'ler, metrikler, yapılandırılmış loglar. Ajanınız yalnızca konsol çıktısını okuyup en iyisini ummak zorunda değil. Başarısız bir isteği servisler arasında izleyebilir, yavaş endpoint'lerin profilini çıkarabilir ve neyin tam olarak nerede bozulduğunu saptayabilir. Bu, geliştirme döngüsünde üretim kalitesinde gözlemlenebilirlik demek.

## Bowling koruma bandı analojisi

Aspire ekibi harika bir analoji kullanıyor: Aspire'ı AI ajanları için bowling koruma bantları olarak düşünün. Ajan mükemmel olmasa da (ve olmayacak), bantlar onu oluktan atmaktan koruyor. Yığın tanımı yanlış yapılandırmayı önlüyor, derleyici hataları yakalıyor, CLI süreç yönetimini üstleniyor ve telemetri geri bildirim döngüsünü sağlıyor.

Bunu Playwright CLI gibi bir şeyle birleştirdiğinizde, ajanınız uygulamanızı gerçekten *kullanabilir* — akışlara tıklayabilir, DOM'u kontrol edebilir, telemetride kırık şeyleri görebilir, kodu düzeltebilir, yeniden başlatabilir ve tekrar test edebilir. Derle, çalıştır, gözlemle, düzelt. Bu, peşinden koştuğumuz özerk geliştirme döngüsü.

## Başlarken

Aspire'a yeni misiniz? CLI'ı [get.aspire.dev](https://get.aspire.dev) adresinden yükleyin ve [başlangıç rehberini](https://aspire.dev/get-started/first-app) takip edin.

Zaten Aspire kullanıyor musunuz? 13.2'yi almak için `aspire update --self` komutunu çalıştırın, ardından favori kodlama ajanınızı repoya yönlendirin. Aspire'ın koruma bantlarıyla ne kadar daha ileri gittiğini görünce şaşırabilirsiniz.

## Özet

Aspire 13.2 artık sadece bir dağıtık uygulama framework'ü değil — temel ajan altyapısına dönüşüyor. Yapılandırılmış yığın tanımları, tek komutla başlangıç, izole paralel çalıştırmalar ve gerçek zamanlı telemetri, AI ajanlarına kod yazmaktan uygulama göndermek için tam olarak ihtiyaç duydukları şeyleri veriyor.

Tüm ayrıntılar ve demo videolar için Aspire ekibinin [tam yazısını](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) okuyun.
