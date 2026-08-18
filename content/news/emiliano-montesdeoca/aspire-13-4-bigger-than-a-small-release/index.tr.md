---
title: "Aspire 13.4'ün Küçük Bir Yayın Olması Gerekiyordu — Ama Öyle Okunmuyor"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Aspire 13.4, TypeScript AppHost'u GA'ya taşıyor, daha güçlü kaynak komutları, daha sağlam Kubernetes desteği, Go entegrasyonu ve yapay zeka odaklı CLI iyileştirmeleri getiriyor. Sözde küçük bir yayın için bu epey fazla."
tags:
  - Aspire
  - TypeScript
  - Kubernetes
  - CLI
  - Developer Tools
---

Aspire 13.4'ü küçük bir yayın olarak adlandırmak, yalnızca platform ekiplerinin anlayabileceği çok özel bir şekilde komik.

Kaynak yazı, birkaç hafta içinde **519 PR**'den rastgele bahsederken onu "**küçük**" bir yayın olarak adlandırarak açılıyor. Bu, minik bir bakım yamasıyla karşı karşıya olmadığımızın zaten iyi bir işareti.

Ve gerçekte neyin geldiğini okuduğunuzda, etiket daha da inandırıcılıktan uzaklaşıyor.

## Manşet tek bir özellik değil. Platform olgunluğu

Evet, burada birkaç somut duyuru var.

Ama en önemli olduğunu düşündüğüm şey daha büyük desen: Aspire, umut vaat eden bir orkestrasyon fikri olmaktan çıkıp, dağıtık uygulamalar için ciddi bir **geliştirme kontrol düzlemine** dönüşmeye devam ediyor.

Bu, 13.4'te birkaç şekilde ortaya çıkıyor:

- TypeScript AppHost GA'ya ulaşıyor
- kaynak komutları çok daha güçlü hale geliyor
- Kubernetes ve AKS desteği gerçek dağıtımlar için daha gerçekçi hale geliyor
- Go desteği ana depoya taşınıyor
- CLI iyileştirmeleri yapay zeka destekli iş akışlarını daha temiz ve daha ucuz hale getirmeye devam ediyor

Bu ufak bir liste değil.

## TypeScript AppHost'un GA'ya ulaşması ilk göründüğünden daha önemli

Bunun yayındaki en büyük hamlelerden biri olduğunu düşünüyorum.

Kaynak makale, hedefin asla "**çevrilmiş C# apphost**" olmadığını söylüyor. Bu, konuyu düşünmenin tam olarak doğru yolu.

Aspire yalnızca C# rahatlık alanının ötesinde önemli olmak istiyorsa, diğer ekosistemlerin aynı kod öncelikli uygulama modelini doğal hissettiren şekillerde kullanmasına izin vermesi gerekiyor.

TypeScript AppHost'u GA yapmak bunu sağlıyor.

Bu, uygulama modelinin şu ekiplere daha erişilebilir hale geldiği anlamına geliyor:

- arka uç kodu karma dilliyse
- ön uç ve altyapı iş akışları birbirine yakın yaşıyorsa
- platform mühendisliği .NET ile JavaScript/TypeScript katkıcıları arasında paylaşılıyorsa

Bu, Aspire'ın ağırlık merkezini sağlıklı bir şekilde genişletiyor.

## Kaynak komutları Aspire'ın en iyi fikirlerinden biri olmaya devam ediyor

Kaynak komutlarının hâlâ Aspire'ın en hafife alınmış özelliklerinden biri olduğunu düşünüyorum.

Ve 13.4 bunları doğru yönde daha da ileri götürüyor.

Tipli argümanlar, daha zengin sonuçlar ve `WithProcessCommand()`, özelliği bir kolaylıktan çok operasyonel görevler için uygun bir model gibi hissettiriyor.

Bu önemli, çünkü her ciddi uygulama, geliştiricilerin yapması gereken ve basitçe "uygulamayı çalıştır" olmayan uzun bir görev listesi biriktiriyor:

- veri tohumlama
- teşhis çalıştırma
- yerel araçları çağırma
- iş akışlarını tetikleme
- betikleri doğru bağlamla yürütme

Bu işlemler uygulama modelinin kendisinin bir parçası olabiliyorsa, bunları unutulmuş bir dokümantasyon klasöründe gizlemekten çok daha iyi.

Ve evet, bu kod yazan ajanlar için de önemli.

Operasyonel davranış ne kadar açık ve yapılandırılmış hale gelirse, ajanların o kadar az tahmin yürütmesi gerekir.

## Kubernetes desteği daha az teorik hale geliyor

Aspire'ın daha ciddi bir yöne gittiğini düşündüğüm bir diğer alan bu.

Yayın, cert-manager desteği, Gateway API ve Azure Application Gateway for Containers entegrasyonu, harici Helm chart desteği ve ham manifest kaçış yolları ekliyor.

Bu, ekiplerin "bu dağıtılabilir mi?" sorusundan "bu gerçek bir ortamda gerçekten güveneceğimiz şekilde dağıtılabilir mi?" sorusuna geçtiğinde ihtiyaç duyduğu türden şeyler.

Bu ayrım önemli.

Çünkü Kubernetes desteğini genel anlamda iddia etmek kolay. Giriş (ingress), TLS, yönlendirme, üçüncü taraf chart'lar ve gerçek üretim boru tesisatı konuşmaya girdiğinde bunu yararlı kılmak çok daha zor.

## Yapay zeka odaklı CLI iyileştirmeleri daha fazla ilgiyi hak ediyor

Yayında, insanların zamanla daha çok takdir edeceğini düşündüğüm bir detay, gürültüyü azaltma ve CLI'de aranabilirliği iyileştirme odağı.

Loglar ve OTEL için sunucu tarafı `--search` desteği, küçük göründüğü ve günlük işte büyük hissettiren tam olarak türden bir değişiklik.

Kaynak yazı açıkça "**Daha az gürültü, daha az yakılan token**" diyor, ve bu satırın ilk göründüğünden daha çok şey ortaya koyduğunu düşünüyorum.

Aspire artık yalnızca insan operatörler için gelişmiyor. Giderek yapay zeka destekli araçların iş akışının bir parçası olduğu ortamlar için de gelişiyor.

Bu akıllı bir yön.

## İlk deneyeceğim şeyler

Bugün zaten Aspire kullanıyor olsaydım, 13.4'ten sonra ilk test edeceğim şeyler şunlar olurdu:

1. depoda karma dilli katkıcılar varsa TypeScript AppHost
2. tekrarlayan yerel görevler için daha zengin kaynak komutları
3. gerçek hata ayıklama oturumlarında iyileştirilmiş CLI arama akışları
4. önceki rahatlık alanının dışında hizmetler varsa Go entegrasyonu
5. ekip daha az garip bir dağıtım hikâyesi bekliyorsa Kubernetes/AKS desteği

Pratik değerin hızla ortaya çıkacağını düşündüğüm yer burası.

## Görüşüm

Aspire 13.4, yüzeyde özellik birikimi gibi görünen ama altında platform konsolidasyonu olan yayınlardan biri.

Bu yüzden önemli olduğunu düşünüyorum.

Aspire bir orkestrasyon yardımcısından fazlası olmaya devam ediyor. Giderek daha iyi dil esnekliği, daha iyi komutlar, daha güçlü dağıtım hikâyeleri ve şu anda gerçekten inşa ettiğimiz türden dağıtık uygulama iş akışları için daha iyi destek sunan bir geliştirme kontrol düzlemi haline geliyor.

Yani hayır, "küçük yayın" etiketini pek satın almıyorum.

Ve bu bir iltifat.

Orijinal yazı: [Aspire 13.4 is here](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-4/)
