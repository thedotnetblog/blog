---
title: "Aspire 13.2 Bir Dokümantasyon CLI'ı Sunuyor — ve AI Ajanınız da Kullanabilir"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2, aspire docs'u ekliyor — terminali terk etmeden resmi belgeleri aramanızı, gezmenizi ve okumanızı sağlayan bir CLI. AI ajanları için de araç olarak çalışıyor. Bunun neden önemli olduğunu burada açıklıyoruz."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-docs-cli-ai-skills" >}}).*

Bir Aspire AppHost'un içinde derinlere dalıp entegrasyonları bağlarken Redis entegrasyonunun tam olarak hangi parametreleri beklediğini kontrol etmeniz gereken o anı biliyor musunuz? Tarayıcınıza geçersiniz, aspire.dev'de arama yaparsınız, API dokümanlarını incelersiniz, sonra editörünüze dönersiniz. Bağlam kaybolmuş. Akış bozulmuş.

Aspire 13.2 tam da [bunun için bir çözüm sundu](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). `aspire docs` CLI'ı, terminali terk etmeden resmi Aspire belgelerini doğrudan arayıp okuyabilmenizi sağlıyor. Yeniden kullanılabilir servisler tarafından desteklendiği için, AI ajanları ve skill'ler de var olmayan API'ları uydurmak yerine belge aramak amacıyla aynı komutları kullanabiliyor.

## Bu aslında ne sorunu çözüyor

David Pine orijinal yazısında konuyu net olarak özetliyor: AI ajanlar, geliştiricilere Aspire uygulamaları geliştirmede yardım etmekte *berbattı*. `aspire run` yerine `dotnet run` öneriyorlar, aspire.dev'deki belgeleri learn.microsoft.com'a yönlendiriyorlardı, güncel olmayan NuGet paketleri öneriyorlardı ve — kişisel favorim — var olmayan API'ları uyduruyorlardı.

Neden? Çünkü Aspire, çok dilli olmadan çok daha uzun süre .NET'e özel kaldı ve LLM'ler en son özelliklerin öncesindeki eğitim verileriyle çalışıyor. Bir AI ajanına mevcut belgeleri gerçekten arama yeteneği verdiğinizde, tahmin etmeyi bırakıp işe yarar hale geliyor.

## Üç komut, sıfır tarayıcı sekmesi

CLI ferahlatıcı derecede basit:

### Tüm belgeleri listele

```bash
aspire docs list
```

aspire.dev'de mevcut her belge sayfasını döndürür. Makine tarafından okunabilir çıktı mı istiyorsunuz? `--format Json` ekleyin.

### Bir konu arayın

```bash
aspire docs search "redis"
```

Ağırlıklı ilgi puanlamasıyla hem başlıkları hem içeriği arar. Dahili olarak dokümantasyon araçlarını destekleyen arama motorunun aynısı. Başlıklar, slug'lar ve ilgi puanlarıyla sıralı sonuçlar alırsınız.

### Tam sayfayı okuyun (ya da yalnızca bir bölümü)

```bash
aspire docs get redis-integration
```

Tam sayfayı markdown olarak terminalinize akıtır. Yalnızca bir bölüme mi ihtiyacınız var?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Cerrahi hassasiyet. 500 satır kaydırma yok. Sadece ihtiyacınız olan kısım.

## AI ajan boyutu

İşte AI araçlarıyla geliştirme yapan bizim için ilginç olan kısım. Aynı `aspire docs` komutları, AI ajanları için araç olarak çalışıyor — skill'ler, MCP sunucuları veya basit CLI sarmalayıcıları aracılığıyla.

AI asistanınızın eski eğitim verilerine dayalı Aspire API'ları uydurmak yerine, `aspire docs search "postgres"` çağırabilir, resmi entegrasyon belgelerini bulabilir, doğru sayfayı okuyabilir ve size belgelenmiş yaklaşımı sunabilir. Gerçek zamanlı, güncel belgeler — modelin altı ay önce ezberledikleri değil.

Bunun arkasındaki mimari kasıtlı. Aspire ekibi tek seferlik bir entegrasyon yerine yeniden kullanılabilir servisler (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) inşa etti. Bu, aynı arama motorunun terminaldeki insanlar, editörünüzdeki AI ajanları ve CI pipeline'ınızdaki otomasyonlar için çalışması anlamına geliyor.

## Gerçek dünya senaryoları

**Hızlı terminal aramaları:** Üç dosya derindesiniz ve Redis yapılandırma parametrelerine ihtiyacınız var. İki komut, doksan saniye, işe geri dönüş:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**AI destekli geliştirme:** VS Code skill'iniz CLI komutlarını sarmalıyor. "AppHost'uma bir PostgreSQL veritabanı ekle" diyorsunuz ve ajan cevap vermeden önce gerçek belgelere bakıyor. Halüsinasyon yok.

**CI/CD doğrulama:** Pipeline'ınız, AppHost yapılandırmalarını programatik olarak resmi belgelerle doğruluyor. `--format Json` çıktısı `jq` ve diğer araçlara temiz şekilde aktarılıyor.

**Özel bilgi tabanları:** Kendi AI araçlarınızı mı geliştiriyorsunuz? Yapılandırılmış JSON çıktısını doğrudan bilgi tabanınıza aktarın:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Web scraping yok. API anahtarı yok. Dokümantasyon araçlarının dahili olarak kullandığı aynı yapılandırılmış veri.

## Belgeler her zaman canlı

En çok takdir ettiğim kısım bu. CLI bir anlık görüntü indirmiyor — aspire.dev'i ETag tabanlı önbelleklemeyle sorguluyor. Belgeler güncellenir güncellenmez, CLI'ınız ve üzerine inşa edilmiş tüm skill'ler bunu yansıtıyor. Eski kopyalar yok, "ama wiki şöyle diyordu..." anları yok.

## Özet

`aspire docs`, gerçek bir sorunu temiz biçimde çözen küçük özelliklerden biri. İnsanlar terminale özgü belge erişimi kazanıyor. AI ajanları tahmin etmeyi bırakıp gerçek belgelere başvurmanın bir yolunu buluyor. Ve hepsi aynı gerçek kaynakla destekleniyor.

.NET Aspire ile geliştirme yapıyorsanız ve CLI'ı henüz denemediyseniz, `aspire docs search "konunuz"` çalıştırın ve nasıl hissettirdiğini görün. Sonra bu komutları kullandığınız AI skill veya otomasyon kurulumuna entegre etmeyi düşünün — ajanlarınız size teşekkür edecek.

Dokümantasyon araçlarının nasıl oluşturulduğuna dair [David Pine'ın derinlemesine incelemesine](https://davidpine.dev/posts/aspire-docs-mcp-tools/) ve tüm ayrıntılar için [resmi CLI referansına](https://aspire.dev/reference/cli/commands/aspire-docs/) göz atın.
