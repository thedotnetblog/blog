---
title: "Aspire 13.2 Bun'u, Daha İyi Konteynerleri ve Daha Az Hata Ayıklama Sürtünmesini Getiriyor"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2, Vite uygulamaları için Bun'a birinci sınıf destek ekliyor, Yarn güvenilirliğini düzeltiyor ve yerel geliştirme davranışını daha dürüst kılan konteyner iyileştirmeleri sunuyor. Gerçekte ne değişti ve neden önemli, işte burada."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Aspire'da JavaScript ön yüzlerle .NET arka uçlar geliştiriyorsanız, 13.2 gününüzü sessizce iyileştiren türden bir güncelleme. Gösterişli yeni paradigmalar yok. Sadece biraz can sıkan şeylere sağlam iyileştirmeler.

Gerçekte neler geldiğine bakalım.

## Bun Artık Birinci Sınıf

Manşet özellik: Aspire'da Vite uygulamaları için Bun desteği. Tek bir akıcı çağrı, iş tamam.

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

Ekibiniz zaten Bun kullanıyorsa — ve muhtemelen kullanıyordur, çünkü kurulum süreleri çok daha hızlı ve başlatma da daha seri — Aspire artık sizi akıntıya karşı yüzmeye zorlamıyor. Daha önce Aspire npm varsayıyordu ve bunun etrafından dolaşmanız gerekiyordu. Şimdi `.withBun()`, `.withYarn()` ve varsayılan npm davranışının yanında birinci sınıf bir seçenek.

Bu neden önemli? Çünkü JavaScript araç zincirinin hızı inner dev loop'unuzu doğrudan etkiler. Her yeni ortam kurduğunuzda frontend'inizin bağımlılıkları yüklemek için 30 saniye harcaması birikir gider. Bun bunu ciddi ölçüde azaltır.

C#'ta yazmayı tercih ediyorsanız, C# AppHost karşılıkları [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun) üzerinde belgelenmiş durumda — aynı desenler geçerli.

## Yarn Daha Güvenilir Hale Geldi

Bun manşetleri alıyor, ama Yarn kullanıcıları belki daha da önemli bir şey kazanıyor: daha az gizemli hata. Aspire 13.2, `addViteApp()` ile birlikte `withYarn()` güvenilirliğini iyileştiriyor.

Bu tür düzeltmeler, Yarn tabanlı bir frontend kaynağının neden başlamadığını anlamaya 20 dakika harcamadıkça heyecan verici görünmez. Konuyu düzelmiş sayın.

## Gerçekten Anlaşılabilen Konteyner Yayınlama

Bilmeniz gereken iki konteyner iyileştirmesi var:

### Açık Pull Policy

Docker Compose yayınlama artık `PullPolicy` destekliyor; buna `Never` seçeneği de dahil:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

Bu, kabaca "zaten build ettiğim image'ı kullan ve registry'yi işin dışında tut" diyen iş akışı. Localde manuel olarak build edip yayınladığınız image'lar üzerinde iterasyon yaparken ya da CI bir image ürettiğinde Compose'un tam olarak o image'ı kullanmasını isterken çok kullanışlıdır; uzaktaki bir pull'un araya girmesi gerekmez.

### PostgreSQL 18+ Volume'ları Yeniden Çalışıyor

PostgreSQL 18, veri dizininin iç düzenini değiştirdi. Bu, Aspire'da volume eşlemesini sessizce bozdu — veri volume'ünüz kuruluyordu ama kalıcılık düzgün çalışmıyordu. 13.2 bunu düzeltiyor.

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

PostgreSQL 18 veya daha yenisini bir veri volume'üyle çalıştırıyorsanız, Aspire 13.2'ye güncelleyin ve bir daha düşünmeyin.

## Hata Ayıklamada Daha İyi Bir Günlük Deneyim

AppHost oturumunda adım adım ilerlerken işleri daha az sinir bozucu yapan birkaç şey:

- **Temel türlerde `DebuggerDisplayAttribute`** — `DistributedApplication`, kaynaklar ve endpoint ifadeleri artık nesne ağaçlarında gezinmek yerine debugger'da faydalı değerler gösteriyor
- **Daha iyi `WaitFor` hata mesajları** — kaynaklar başlatılamadığında hata bağlamı artık gerçekten yardımcı
- **`BeforeResourceStartedEvent` doğru zamanda tetikleniyor** — yalnızca bir kaynak gerçekten başlarken, alakasız durum geçişlerinde değil
- **`launchSettings.json` daha dayanıklı** — bozuk bir ayarın geliştirme başlangıcını bozma ihtimali daha düşük

Bu iyileştirmelerin hiçbiri tek başına devrimsel değil, ama birlikte debug deneyimindeki sürtünmeyi azaltıyorlar. Aspire resource nesnesinin içinde üç kat aşağı inip hangi endpoint'i kullandığını anlamaya çalıştıysanız, yalnızca debugger display iyileştirmesi bile güncellemeye değer.

## Kapanış

Aspire 13.2 kalite odaklı bir sürüm. Bun desteği manşet olabilir, ama günlük işi akıcı hale getiren şeyler konteyner ve hata ayıklama iyileştirmeleri. Özellikle PostgreSQL 18'i veri volume'leriyle kullanıyorsanız, güncellemek değer.

Tüm ayrıntılar [David Pine'ın orijinal yazısında](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) ve [Aspire 13.2 yenilikler dokümanında](https://aspire.dev/whats-new/aspire-13-2/) yer alıyor.