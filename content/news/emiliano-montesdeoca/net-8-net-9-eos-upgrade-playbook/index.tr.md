---
title: '.NET 8 ve .NET 9 Destek Sonu: Buna Bir Teslimat Son Tarihi Olarak Davranın'
date: 2026-07-19
author: 'Emiliano Montesdeoca'
description: '10 Kasım 2026 sadece bir destek tarihi değil; ertelenen yükseltme riskinin açık hale geldiği noktadır.'
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Orijinal kaynak: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Bu duyuru açık sözlüdür ve ekipler aynı netlikle yanıt vermelidir: 10 Kasım 2026'dan sonra .NET 8 veya .NET 9'da gönderim yapmaya devam etmeyi planlıyorsanız, kasıtlı bir desteklenmeyen çalışma zamanı kararı veriyorsunuz demektir.

Uygulamalar çalışmaya devam edecek. Mesele bu değil. Mesele, güvenlik ve bakım güncellemelerinin durmasıdır. Bu gerçekleştiğinde, geri yaması olmayan her bilinen güvenlik açığı sizin operasyonel sorumluluğunuz haline gelir.

Benim görüşümlü düşüncem: kuruluşlar genellikle çerçeve yükseltmelerini isteğe bağlı bakım olarak ele alır ve ardından bu kararın bedelini acil durum pencerelerinde, denetim bulgularında ve aceleye getirilmiş satıcı eskülasyonlarında öder. Yükseltme planlaması, bir yan görev değil, ürün yol haritası öğesi olmalıdır.

.NET ekipleri için pratik bir geçiş duruşu:

.NET 10'u yeniden hedeflemeyi açık uçlu bir birikmiş iş öğesi değil, tarihli bir hedef olarak belirleyin.

Uyumluluk ve regresyon testlerini Q4'te değil, şimdi özellik çalışmalarına paralel olarak çalıştırın.

Bağımlılık ve barındırma hazırlığını ayrı iş akışları olarak izleyin çünkü birçok başarısızlık proje dosyasının dışında gerçekleşir.

Sürprizleri önceden yakalamak için Upgrade Assistant ve breaking-change belgelerini erken kullanın.

Birden çok ürün tarafından kullanılan paylaşılan kitaplıklara sahipseniz, .NET 10 destek zaman çizelgenizi kuruluş içinde yayınlayın. Alt ekiplerin hazırlık süresine ihtiyacı vardır.

Visual Studio'nun destek dışı bileşen işaretlemesi de operasyonel olarak önemlidir. Araç zinciri temizliğinin uyumlu kalmanın bir parçası olduğuna dair net bir sinyal oluşturur. Bunu görmezden gelen ekipler genellikle karışık SDK durumlarına ve tutarsız derleme davranışına sürüklenir.

Az tartışılan bir detay: .NET 8 ve .NET 9 aynı bitiş tarihinde birleşiyor. Bu, daha fazla yastık bekleyerek benimsemeyi kademelendiren kuruluşlar için yükseltme pencerelerini sıkıştırıyor. Özellik erişimi için .NET 9'a geçtiyseniz, yine de aynı destek uçurumuna varırsınız.

Platform liderleri için karar matrisi basittir: son tarihten önce geçiş yapın veya desteklenmeyen riski telafi edici kontrollerle belgeleyin ve kabul edin. Hiçbir şeyin değişmediği üçüncü bir seçenek yoktur.

İyi haber şu ki .NET 10, Kasım 2028'e kadar bir LTS hedefidir, bu da taşımayı tamamladığınızda istikrarlı bir yol sağlar.

Başlamak için son Patch Tuesday'i beklemeyin. Buna güvenlik sonuçları olan bir teslimat son tarihi olarak davranın, çünkü tam olarak budur.