---
title: "Visual Studio'nun Mart Güncellemesiyle Özel Copilot Agentları Oluşturabilirsiniz — find_symbol Aracı Gerçekten Büyük"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studio'nun Mart 2026 güncellemesi özel Copilot agentları, yeniden kullanılabilir agent becerileri, dile duyarlı bir find_symbol aracı ve Test Gezgini'nden Copilot destekli profil oluşturmayı içeriyor. İşte önemli olanlar."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "visual-studio-march-2026-custom-copilot-agents" >}}).*

Visual Studio bugüne kadarki en önemli Copilot güncellemesini aldı. Mark Downie [Mart sürümünü duyurdu](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/) ve başlık özel agentlar — ama dürüstçe söylemek gerekirse, daha aşağılarda geçen `find_symbol` aracı iş akışınızı en çok değiştirecek özellik olabilir.

Gerçekte neler olduğunu açıklayayım.

## Reponuzda özel Copilot agentları

Copilot'un ekibinizin kodlama standartlarını izlemesini, build pipeline'ınızı çalıştırmasını veya dahili belgelerinizi sorgulamasını ister misiniz? Artık tam olarak bunu oluşturabilirsiniz.

Özel agentlar, reponuzdaki `.github/agents/` klasörüne bıraktığınız `.agent.md` dosyaları olarak tanımlanıyor. Her agent, çalışma alanı farkındalığına, kod anlayışına, araçlara, tercih ettiğiniz modele ve harici servislere MCP bağlantılarına tam erişim elde ediyor. Yerleşik agentların yanında agent seçicisinde görünüyorlar.

Bu, VS Code'un süredir desteklediği desenin aynısı — ve Visual Studio'nun yetişmesini görmek harika. VS Code için zaten agent oluşturmuş ekipler için `.agent.md` dosyalarınız her iki IDE'de de çalışmalı (ancak araç adları farklılık gösterebilir, bu yüzden test edin).

[awesome-copilot](https://github.com/github/awesome-copilot) reposunda başlangıç noktası olarak kullanabileceğiniz topluluk katkılı agent yapılandırmaları var.

## Agent becerileri: yeniden kullanılabilir talimat paketleri

Beceriler, reponuzdaki `.github/skills/` klasöründen veya profilinizdeki `~/.copilot/skills/` konumundan otomatik olarak alınıyor. Her beceri, [Agent Skills spesifikasyonunu](https://agentskills.io/specification) takip eden bir `SKILL.md` dosyası.

Becerileri, karıştırıp eşleştirebileceğiniz modüler uzmanlık alanları olarak düşünün. API kurallarınız için bir beceri, test desenleriniz için bir diğeri ve dağıtım iş akışınız için başka biri olabilir. Bir beceri etkinleştiğinde, uygulandığını bilmeniz için sohbette görünüyor.

VS Code'da beceri kullandıysanız Visual Studio'da da aynı şekilde çalışıyorlar.

## find_symbol: agentlar için dile duyarlı navigasyon

İşler burada gerçekten ilginçleşiyor. Yeni `find_symbol` aracı, Copilot'un agent moduna gerçek dil servisi destekli sembol navigasyonu sağlıyor. Kodunuzu metin olarak aramak yerine agent şunları yapabiliyor:

- Projeniz genelinde bir sembole yapılan tüm referansları bul
- Tür bilgisine, bildirimlere ve kapsam meta verilerine eriş
- Tam dil farkındalığıyla çağrı noktalarında gezin

Pratikte ne anlama geliyor: Copilot'tan bir metodu yeniden düzenlemesini veya çağrı noktaları genelinde parametre imzasını güncellemesini istediğinizde, kodunuzun yapısını gerçekten görebiliyor. Artık "agent metodu değiştirdi ama üç çağrı noktasını kaçırdı" durumu yok.

Desteklenen diller arasında C#, C++, Razor, TypeScript ve desteklenen LSP uzantısına sahip her şey yer alıyor. .NET geliştiricileri için bu büyük bir iyileştirme — derin tür hiyerarşileri ve arayüzlere sahip C# kod tabanları, sembol farkındalıklı navigasyondan büyük ölçüde yararlanıyor.

## Copilot ile testleri profilleyin

Test Gezgini bağlam menüsünde artık bir **Profile with Copilot** komutu var. Bir test seçin, profile tıklayın ve Profiling Agent onu otomatik olarak çalıştırıp performansı analiz eder — uygulanabilir içgörüler sunmak için CPU kullanımı ve enstrümantasyon verilerini birleştirir.

Artık profil oluşturucu oturumlarını manuel olarak yapılandırmak, testi çalıştırmak, sonuçları dışa aktarmak ve bir flame graph okumaya çalışmak yok. Agent analizi yapıp neyin yavaş olduğunu ve neden olduğunu söylüyor. Şu anda yalnızca .NET, ki bu Visual Studio'nun derin .NET tanı entegrasyonu göz önüne alındığında mantıklı.

## Canlı hata ayıklama sırasında performans ipuçları

Performans optimizasyonu artık sonrasında değil, hata ayıklarken gerçekleşiyor. Kod üzerinde adım adım ilerlerken Visual Studio satır içinde yürütme süresini ve performans sinyallerini gösteriyor. Yavaş bir satır mı gördünüz? Perf İpucu'na tıklayın ve Copilot'tan hemen orada optimizasyon önerileri isteyin.

Profiling Agent çalışma zamanı verilerini otomatik olarak yakalıyor — geçen süre, CPU kullanımı, bellek davranışı — ve Copilot bunu sıcak noktaları tespit etmek için kullanıyor. Bu, performans çalışmasını ertelediğiniz ayrı bir görev yerine hata ayıklama akışınızın bir parçası olarak tutuyor.

## Solution Explorer'dan NuGet güvenlik açıklarını düzeltin

Bir NuGet paketinde güvenlik açığı tespit edildiğinde, artık doğrudan Solution Explorer'da **Fix with GitHub Copilot** bağlantısıyla bir bildirim görüyorsunuz. Tıklayın ve Copilot güvenlik açığını analiz eder, doğru paket güncellemelerini önerir ve uygular.

Bağımlılıkları güncel tutmakta zorlanan ekipler için (ki bu esasen herkes), "bir güvenlik açığı olduğunu biliyorum ama doğru güncelleme yolunu bulmak başlı başına bir proje" sürtünmesini ortadan kaldırıyor.

## Sonuç

Özel agentlar ve beceriler başlık haberi, ancak `find_symbol` uyuyan dev — .NET kodunu yeniden düzenlerken Copilot'un ne kadar doğru olabileceğini temelden değiştiriyor. Canlı profil oluşturma entegrasyonu ve güvenlik açığı düzeltmeleriyle birleşince bu güncelleme, Visual Studio'nun AI özelliklerini demo hazır değil gerçekten pratik hissettiriyor.

Her şeyi denemek için [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/)'ı indirin.
