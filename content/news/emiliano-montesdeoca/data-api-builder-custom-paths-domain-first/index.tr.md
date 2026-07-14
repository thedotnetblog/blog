---
title: "Data API Builder Özel Yolları, API'leri İnsanlar İçin Tasarlamanızı Sağlar, Tablolar İçin Değil"
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: "DAB'deki bileşik REST yolları, alan odaklı API tasarımı için küçük bir özellik ancak büyük mimari etkiye sahiptir."
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Orijinal kaynak: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

Data API Builder'daki yeni bileşik REST yolu desteği, küçük bir yapılandırma iyileştirmesi gibi görünebilir, ancak aslında uzun süredir devam eden bir API tasarım gerilimini çözer: veritabanı topolojisinin genel uç nokta tasarımına sızması.

Varsayılan varlık tabanlı yollar hızlı başlangıçlar için harikadır. Uzun vadeli ürün API'leri için genellikle yanlıştır. Gerçek sistemlerin, iş kavramlarına, sahiplik sınırlarına ve tüketici zihinsel modellerine uygun rota yapılarına ihtiyacı vardır.

Bu DAB değişikliğinin önemli olmasının nedeni budur. Oluşturulan API kolaylığını korurken daha temiz bir alan-ilk yüzey sunabilirsiniz.

Benim görüşümlü düşüncem basittir: API yol yapınız üretimde ham tablo adlarını yansıtıyorsa, genellikle istemci netliği pahasına arka uç kolaylığı için optimize ediyorsunuz demektir.

Özel yollarla ekipler daha iyi sınırlar modelleyebilir: satış, fatura, destek veya ortağa özel yüzeyler gibi. Bu, uygun API yönetişiminin yerini almaz, ancak DAB kullanıcılarına rota tasarımını ürün diliyle hizalamak için pratik bir yol verir.

Bu özelliği benimseyen ekipler için pratik rehberlik:

Yolları gelişigüzel eklemeden önce bir adlandırma politikası tanımlayın. Tutarsız alt segmentler uzun vadeli karmaşa haline gelir.

Uç noktaları organizasyon şemalarına değil, sınırlı bağlamlara eşleyin. Ekipler değişir; alan semantiği kararlı olmalıdır.

Yol yapısını sürüm oluşturma stratejinizin bir parçası olarak ele alın ve kırıcı değişiklikleri açıkça belgeleyin.

Özel rota yapıları boyunca yetkilendirme davranışını doğrulayın, böylece rota netliği güvenlik netliği ile eşleşir.

DAB'da genel olarak takdir ettiğim şey kaldıraç modelidir: tekrarlayan denetleyici kodu yazmadan sayfalama, filtreleme, projeksiyon ve diğer uç nokta mekaniğini elde edersiniz. Özel yollar, API mimarlarının en büyük itirazlarından birini azaltarak bu kaldıracı daha üretime hazır hale getirir.

Bir uyarı var. Daha iyi yol oluşturma, üretmenin kolay hissettirmesi nedeniyle ekipleri çok fazla şeyi çok hızlı açığa çıkarmaya cezbedebilir. Korkuluklar hala önemlidir: varlık pozlamasını kasıtlı tutun, politikayı merkezi olarak uygulayın ve dahili şema deneylerinden kazara kamuya açık sözleşmeler oluşturmaktan kaçının.

Teslimat baskısı altındaki .NET kuruluşları için bu özellik, disiplinle kullanılırsa bir üretkenlik artışıdır. Elişi API katmanlarından daha hızlı hareket edebilirken yine de tutarlı ve iş dostu bir uç nokta yüzeyi koruyabilirsiniz.

Alt satır: DAB özel yolları URL'leri güzelleştirmekle ilgili değildir. Oluşturulan uç noktaların operasyonel verimliliğini korurken API tasarım niyetini geri kazanmakla ilgilidir.