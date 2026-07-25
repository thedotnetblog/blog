---
title: "Agent Governance Toolkit MCP Uzantıları .NET'te Güvenli Yolu Çok Daha Kolay Hale Getiriyor"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: ".NET için yeni Agent Governance Toolkit MCP uzantıları, politika uygulamayı, başlangıç taramasını ve yanıt sanitizasyonunu doğrudan MCP sunucu oluşturucu akışına yerleştiriyor. Görmek istediğim türden güvenli-varsayılan hikâye tam olarak bu."
tags:
  - .NET
  - MCP
  - AI
  - Security
  - Agent Governance Toolkit
---

Ajan araç ekosisteminde şu anki en büyük sorunlardan biri, mutlu yolun genellikle güvensiz yol olması.

Bir MCP sunucusunu ayağa kaldırabilirsiniz. Araçları hızla açığa çıkarabilirsiniz. Demoyu çalıştırabilirsiniz.

Sonra rahatsız edici sorular hemen ardından gelir:

- kimin neyi çağırmasına izin veriliyor?
- araç meta verisi kötü niyetli veya yanıltıcıysa ne olur?
- güvensiz çıktı doğrudan modele geri akarsa ne olur?
- bunun ne kadarı politika, ne kadarı sadece gelenek?

İşte bu yüzden yeni **.NET için Agent Governance Toolkit MCP uzantıları** önemli.

Ajan ekosistemindeki her güvenlik sorununu çözmüyorlar, ama çok önemli bir şey yapıyorlar: varsayılan .NET oluşturucu akışını sertleştirmeyi çok daha kolay hale getiriyorlar.

## Duyurudaki en önemli cümle

Kaynak yazıya göre paket, `IMcpServerBuilder`'a "**tek çağrılık yönetişim**" ekliyor.

Odaklanacağım tam ifade bu.

Çünkü çoğu ekip, farkındalık eksikliği yüzünden ajan yönetişimi kurmakta başarısız olmuyor. Güvenli yol daha fazla iş, daha fazla bağlantı, daha fazla özel kod ve temizliği erteleme için daha fazla fırsat sunduğu için başarısız oluyorlar.

Ve "sonra", riskin yaşamayı sevdiği yerdir.

## Bunun neden iyi bir .NET hikâyesi olduğu

Burada beğendiğim şey, paketin mevcut oluşturucu modeline ne kadar doğal biçimde uyduğu.

Ekipleri şuna zorlamak yerine:

- yan bir işlem (sidecar)
- ayrı bir proxy
- özel bir sarmalayıcı mimarisi
- ya da tuhaf bir alternatif SDK

paket, resmi C# MCP oluşturucu akışını doğrudan genişletiyor.

Bu çok önemli.

Güvenlik mimari cambazlığı gerektiriyorsa, benimseme hemen düşer. Güvenlik, sunucuyu yapılandırmanın normal bir parçası gibi görünüyorsa, benimseme çok daha gerçekçi hale gelir.

## Tehdit modeli artık teorik değil

Ekiplerin küçümsememesi gerektiğini düşündüğüm bir şey, MCP ile ilgili riskin üretim sistemlerinde ne kadar hızlı gerçek hale geldiği.

Kaynak makale şu tür sorular ortaya koyuyor:

- "**Kayıtlı her araç, her ajan tarafından çağrılabilmeli mi?**"
- "**Bir araç açıklaması prompt enjeksiyonu tarzı talimatlar içeriyorsa ne olur?**"

Bunlar tam olarak doğru sorular.

Çünkü araçlar ajanlar için yürütme yüzeyi haline geldiğinde, sistem artık yalnızca metin üretmiyor. Güvenlik, güvenilirlik ve yönetişim sonuçları olabilecek kararlar alıyor.

Bu, çıtayı değiştiriyor.

## Paketin doğru yaptığı şey

Uzantının en güçlü tasarım kararı, birden fazla güvenlik katmanını tek bir tutarlı akışta birleştirmesi:

- güvensiz araç tanımları için başlangıç taraması
- yürütme üzerinde politika uygulaması
- kimlik farkında yönetişim
- içerik istemciye veya modele geri akmadan önce yanıt sanitizasyonu
- denetim ve metrik kancaları

Bu doğru şekil.

Tek bir dev "güvenlik modu" değil. Yaşam döngüsündeki farklı hata noktalarını kapsayan bir dizi özel kontrol.

### Başlangıç taraması çoğu ekibin fark ettiğinden daha önemli

Güvensiz araç meta verisinin varsayılan olarak başlangıcı başarısız kılabilmesini özellikle beğeniyorum.

Bu güçlü bir görüş ve bence doğru olanı.

Zehirlenmiş veya şüpheli bir araç tanımını ne kadar erken engelleyebilirseniz o kadar iyi. Çalışma zamanına kadar beklemek, bir bütün sorun sınıfı için zaten çok geç.

### Yanıt sanitizasyonu da çok pratik bir katman

Duyurudaki bir diğer hafife alınan nokta, çıktı sanitizasyonuna verilen odak.

Birçok ekip tehlikeli girdiyi düşünüyor.

Daha azı, bir araçtan geri gelen ve doğrudan bir ajan döngüsüne verilen tehlikeli çıktıyı yeterince dikkatli düşünüyor.

Bu, kolayca yanmanıza yol açabilecek bir nokta.

## Hâlâ dikkatle izleyeceğim şey

Bu paketi çok beğenmeme rağmen, hâlâ bir konuda dikkatli olurdum: yönetişim araçları yalnızca ekipler anlamlı politikaları gerçekten tanımlayıp sürdürdüğünde işe yarar.

Uzantı, mekanizmayı bağlamayı kolaylaştırıyor. Bu harika.

Ama ekiplerin hâlâ şu daha zor kurumsal işi yapması gerekiyor:

- hangi araçlara izin veriliyor
- hangi ajanlar veya kimlikler bunları çağırabilir
- ortamlarında "varsayılan olarak reddet" gerçekten ne anlama gelmeli
- yanlış pozitifler ve istisnalar nasıl ele alınmalı

Bu yüzden bu paketi mimari muhakemenin yerine geçen bir şey olarak değil, güçlü bir uygulama katmanı olarak ele alırdım.

## Görüşüm

Bu, bir süredir gördüğüm en net **güvenli-varsayılan** .NET ajan duyurularından biri.

Sihir vaat ettiği için değil, ekiplerin muhtemelen tutarsız bir şekilde uygulayacağı bir güvenlik iş kategorisini alıp oluşturucu boru hattında daha temiz, daha doğal bir yuvaya kavuşturduğu için.

Bu ekosistemde istediğim tam olarak bu tür paket.

Daha geniş yönetişim tartışmasını sona erdirmiyor. Daha pratik bir şey yapıyor: yönetişimin başka birinin ileride yapacağı bir temizlik işi olduğunu iddia etmeyi çok daha zorlaştırıyor.

Ve bu gerçek ilerleme.

Orijinal yazı: [Announcing Agent Governance Toolkit MCP Extensions for .NET](https://devblogs.microsoft.com/dotnet/announcing-agent-governance-toolkit-mcp-extensions-for-dotnet/)
