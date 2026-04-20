---
title: "GitHub Copilot'un Modernizasyon Değerlendirmesi, Henüz Kullanmadığınız En İyi Göç Aracı"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "GitHub Copilot'un modernizasyon uzantısı yalnızca kod değişikliği önermekle kalmıyor — uygulanabilir sorunlar, Azure hedef karşılaştırmaları ve iş birliğine dayalı bir iş akışıyla eksiksiz bir göç değerlendirmesi üretiyor. Değerlendirme belgesinin neden her şeyin anahtarı olduğunu işte burada açıklıyoruz."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "dotnet-modernization-assessment-github-copilot" >}}).*

Eski bir .NET Framework uygulamasını modern .NET'e taşımak, herkesin yapması gerektiğini bildiği ama kimsenin başlamak istemediği işlerden biri. Bu hiçbir zaman sadece "hedef framework'ü değiştir" meselesi değildir. Ortadan kalkan API'lar, artık mevcut olmayan paketler, tamamen farklı çalışan hosting modelleri ve neyin container'a alınacağı, neyin yeniden yazılacağı, neyin olduğu gibi bırakılacağına dair binlerce küçük karar var.

Jeffrey Fritz, [GitHub Copilot'un modernizasyon değerlendirmesine derin bir dalış](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) yayımladı ve dürüst olmak gerekirse? Bu, .NET için gördüğüm en iyi göç araçları. Kod oluşturma nedeniyle değil — bu artık herkes için temel gereksinim. Ürettiği değerlendirme belgesi nedeniyle.

## Bu sadece bir kod öneri motoru değil

VS Code uzantısı bir **Değerlendir → Planla → Uygula** modeli izliyor. Değerlendirme aşaması tüm kod tabanınızı analiz ediyor ve her şeyi yakalayan yapılandırılmış bir belge üretiyor: neyin değişmesi gerektiği, hangi Azure kaynaklarının sağlanacağı, hangi dağıtım modelinin kullanılacağı. Aşağıdaki her şey — altyapı-kodu, containerlaştırma, dağıtım manifestoları — değerlendirmenin bulduklarından akıyor.

Değerlendirme, projenizde `.github/modernize/assessment/` altında saklanıyor. Her çalıştırma bağımsız bir rapor üretiyor, böylece bir geçmiş oluşturabilir ve sorunları düzelttikçe göç pozisyonunuzun nasıl geliştiğini takip edebilirsiniz.

## Başlamanın iki yolu

**Önerilen Değerlendirme** — hızlı yol. Seçilmiş alanlardan birini seçin (Java/.NET Yükseltme, Bulut Hazırlığı, Güvenlik) ve yapılandırmaya dokunmadan anlamlı sonuçlar alın. Uygulamanızın nerede durduğuna ilk bakış için harika.

**Özel Değerlendirme** — hedefli yol. Neyin analiz edileceğini tam olarak yapılandırın: hedef hesaplama (App Service, AKS, Container Apps), hedef işletim sistemi, containerlaştırma analizi. Göç yaklaşımlarını yan yana karşılaştırmak için birden fazla Azure hedefi seçin.

Bu karşılaştırma görünümü gerçekten yararlı. App Service için 3 zorunlu sorunu olan bir uygulamanın AKS için 7 sorunu olabilir. Her ikisini de görmek, bir göç yoluna bağlanmadan önce hosting kararını yönlendirmeye yardımcı oluyor.

## Sorun dökümü uygulanabilir

Her sorun bir kritiklik düzeyiyle geliyor:

- **Zorunlu** — düzeltilmeli, yoksa göç başarısız olur
- **Olası** — göçü etkileyebilir, insan değerlendirmesi gerektirir
- **İsteğe bağlı** — önerilen iyileştirmeler, göçü engellemez

Ve her sorun etkilenen dosyalara ve satır numaralarına bağlantı veriyor, neyin yanlış olduğunu ve neden hedef platformunuz için önemli olduğunu ayrıntılı açıklıyor, somut düzeltme adımları sunuyor (sadece "bunu düzelt" değil) ve resmi belgelere bağlantılar içeriyor.

Bireysel sorunları geliştiricilere verebilir ve harekete geçmek için ihtiyaç duydukları her şeye sahip olurlar. Bu, "bir sorun var" diyen bir araç ile nasıl çözüleceğini söyleyen bir araç arasındaki farktır.

## Kapsanan yükseltme yolları

.NET için özellikle:
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Her yükseltme yolunun, hangi API'ların kaldırıldığını, hangi desenlerin doğrudan eşdeğerinin bulunmadığını ve hangi güvenlik sorunlarının ele alınması gerektiğini bilen algılama kuralları var.

Birden fazla uygulamayı yöneten ekipler için çok-repo toplu değerlendirmeleri destekleyen bir CLI de var — tüm repoları klonlayın, hepsini değerlendirin, uygulama başına raporlar artı toplu portföy görünümü alın.

## Benim düşüncem

Eski .NET Framework uygulamalarının üzerinde oturuyorsanız (ve gerçekçi olalım, çoğu kurumsal ekip oturuyor), bu başlamak için *tek* araçtır. Değerlendirme belgesi tek başına zamana değer — belirsiz bir "modernize etmeliyiz"i, somut ve önceliklendirilmiş, net ileriye dönük yolları olan bir iş öğeleri listesine dönüştürür.

İş birliğine dayalı iş akışı da akıllıca: değerlendirmeleri dışa aktarın, ekibinizle paylaşın, yeniden çalıştırmadan içe aktarın. Karar vericilerin araçları çalıştıranlar olmadığı mimari incelemeler? Karşılandı.

## Sonuç

GitHub Copilot'un modernizasyon değerlendirmesi, .NET göçünü korkunç, tanımsız bir projeden yapılandırılmış, izlenebilir bir sürece dönüştürüyor. Nerede durduğunuzu görmek için önerilen değerlendirmeyle başlayın, ardından Azure hedeflerini karşılaştırmak ve göç planınızı oluşturmak için özel değerlendirmeleri kullanın.

[Tam anlatımı](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) okuyun ve kendi kod tabanınızda denemek için [VS Code uzantısını](https://aka.ms/ghcp-appmod/vscode-ext) alın.
