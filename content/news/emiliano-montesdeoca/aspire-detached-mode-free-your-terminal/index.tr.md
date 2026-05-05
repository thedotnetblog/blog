---
title: "Terminalinizi Serbest Bırakın: Aspire'ın Detached Modu İş Akışını Değiştiriyor"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2, AppHost'unuzu arka planda çalıştırmanıza ve terminalinizi geri almanıza olanak tanıyor. Yeni CLI komutları ve agent desteğiyle birlikte bu, göründüğünden çok daha büyük bir gelişme."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Bir Aspire AppHost çalıştırdığınız her seferinde terminaliniz kayboluyor. Kilitli. Ctrl+C ile çıkana kadar meşgul. Hızlı bir komut çalıştırmanız mı gerekiyor? Yeni bir sekme açın. Logları kontrol etmek ister misiniz? Başka bir sekme. Bu küçük sürtünme hızla birikerek büyüyor.

Aspire 13.2 bunu düzeltiyor. James Newton-King [tüm ayrıntıları yazdı](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) ve dürüstçe söylemek gerekirse bu, çalışma şeklinizi anında değiştiren özelliklerden biri.

## Detached mod: bir komut, terminal geri

```bash
aspire start
```

Bu, `aspire run --detach` için kısayol. AppHost'unuz arka planda başlıyor ve terminalinizi anında geri alıyorsunuz. Ekstra sekme yok. Terminal çoğullayıcı yok. Sadece prompt'unuz, hazır ve bekliyor.

## Çalışanları yönetmek

İşte şu an — arka planda çalıştırmak yalnızca orada ne olduğunu gerçekten yönetebiliyorsanız işe yarıyor. Aspire 13.2 tam bunun için eksiksiz bir CLI komut seti sunuyor:

```bash
# Çalışan tüm AppHost'ları listele
aspire ps

# Belirli bir AppHost'un durumunu incele
aspire describe

# Çalışan bir AppHost'tan log akışı al
aspire logs

# Belirli bir AppHost'u durdur
aspire stop
```

Bu, Aspire CLI'ı gerçek anlamda bir süreç yöneticisine dönüştürüyor. Birden fazla AppHost başlatabilir, durumlarını kontrol edebilir, loglarını takip edebilir ve bunları kapatabilirsiniz — hepsi tek bir terminal oturumundan.

## Isolated modla birleştirin

Detached mod, isolated modla doğal olarak uyum içinde çalışır. Port çakışması olmadan aynı projenin iki örneğini arka planda çalıştırmak ister misiniz?

```bash
aspire start --isolated
aspire start --isolated
```

Her biri rastgele portlar, ayrı secret'lar ve kendi yaşam döngüsü alıyor. Her ikisini görmek için `aspire ps`, işi bitenini kapatmak için `aspire stop` kullanın.

## Bu neden kodlama ajanları için büyük bir gelişme

İşte gerçekten ilgi çekici olan kısım. Terminalinizde çalışan bir kodlama ajanı artık şunları yapabiliyor:

1. `aspire start` ile uygulamayı başlatmak
2. `aspire describe` ile durumunu sorgulamak
3. Sorunları teşhis etmek için `aspire logs` ile logları kontrol etmek
4. İşi bittiğinde `aspire stop` ile durdurmak

Terminal oturumunu kaybetmeden. Detached moddan önce, AppHost'unuzu çalıştıran bir ajan kendi terminaline erişimini kaybederdi. Artık başlatabilir, gözlemleyebilir, yineleyebilir ve temizleyebilir — tam olarak özerk bir ajanın çalışmasını isteyeceğiniz şekilde.

Aspire ekibi bunu benimsedi. `aspire agent init` çalıştırmak, ajanlara bu komutları öğreten bir Aspire skill dosyası kuruyor. Bu sayede Copilot'un kodlama ajanı gibi araçlar Aspire iş yüklerinizi kutudan çıkar çıkmaz yönetebiliyor.

## Özet

Detached mod, basit bir bayrak kılığında gizlenmiş bir iş akışı yükseltmesi. Terminaller arasında bağlam geçişlerini bırakıyorsunuz, ajanlar kendilerini bloke etmekten kurtuluyor ve yeni CLI komutları çalışanlar hakkında gerçek görünürlük sağlıyor. Pratik, temiz ve günlük geliştirme döngüsünü belirgin biçimde daha akıcı hale getiriyor.

Tüm ayrıntılar için [tam yazıyı](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) okuyun ve `aspire update --self` ile Aspire 13.2'yi edinin.
