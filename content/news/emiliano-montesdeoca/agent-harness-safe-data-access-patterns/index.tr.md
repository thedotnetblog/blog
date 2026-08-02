---
title: 'Gerçek Ajan UX Kazanımı Maksimum Özerklik Değil, Güvenli Özerkliktir'
date: 2026-07-11
author: 'Emiliano Montesdeoca'
description: 'Dosya erişimi, onaylar ve bellek tasarımı, üretimde güvenilir ajan davranışı için pratik üçlüdür.'
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Orijinal kaynak: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

Bu, bu yılın daha yararlı ajan mühendisliği yazılarından biri, çünkü yaygın "önce demo" özerklik tuzağını reddediyor. Bunun yerine, ajanların gerçek kullanıcı verileri ve gerçek sonuçlar etrafında nasıl çalışması gerektiğine odaklanıyor.

Burada vurgulanan üç yapı taşı tam olarak doğru.

Dosya erişimi, ajanlara kullanıcıya ait veriler üzerinde yararlı bir temellendirme sağlar.

Onay kapıları, sonuç doğuran eylemlerin sessizce yürütülmesini engeller.

Kalıcı bellek, kontrolden ödün vermeden tekrarlayan etkileşimlerden kaçınır.

Çoğu ekip araç genişliğine aşırı, izin semantiğine ise yetersiz yatırım yapıyor. Bu yanlış. On araca sahip ama zayıf onay sınırları olan bir ajan, üç araca sahip ama öngörülebilir kontrol noktaları olan bir ajandan daha az değerlidir.

Bu makaledeki en pratik desen, katmanlı onay stratejisi:

Alım satım veya yıkıcı işlemler gibi yüksek etkili araçlar için her zaman onay isteyin.

Akışı korumak için düşük riskli okumaları otomatik onaylayın.

Bir oturum içinde tekrarlayan güvenilir eylemler için kapsamlı standart onaylar kullanın.

Bu, sağlıklı bir risk gradyanı yaratır. Kullanıcılar zararsız okumalar için rahatsız edilmez, ama sonuçlar pahalı veya geri döndürülemez hale geldiğinde hâlâ döngüde kalırlar.

Dosya belleği ile Foundry belleği arasındaki açık ayrımı da beğeniyorum. Ekipler tek bir bellek modelini her sorunu çözmeye zorlamayı bırakmalı. Kaba, açık dosya yapıları; raporlar ve izleme listeleri gibi kullanıcıya görünür durum için mükemmel. Gerçek düzeyinde bellek çıkarımı ise tercihler ve konuşma bağlamı için daha iyi. İkisini birleştirmek, birinin tek başına yeterli olduğunu varsaymaktan daha iyi sonuçlar verir.

Öznel görüşüm: ajan kalitesinin geleceği daha az akıllı prompt'larla, daha çok güvenlik ergonomisiyle ölçülecek. Onay istemleriniz gürültülüyse, kullanıcılar düşünmeden tıklar. Bellek sınırlarınız belirsizse, kullanıcılar asistana güvenmeyi bırakır. Veri erişimi varsayılanlarınız izin verici ise, güvenlik ekipleri projeyi kapatır.

Bu deseni benimseyen .NET ve Python ekipleri için kilit hamle, politika geri çağırmalarını ve onay kurallarını temel iş mantığı olarak ele almaktır; herhangi bir kritik kod gibi sürümlenmiş ve test edilmiş. Bunları örneklerde gömülü rastgele lambda ifadeleri olarak bırakmayın.

Güven kazanan ajan sistemleri en çok şeyi yapanlar değildir. Kullanıcıların tam olarak amaçladığı şeyi yapan, ne fazla ne eksik, risk arttığında net kesinti noktalarına sahip olanlardır.

Etkileyici bir demo ile insanların gerçek işi devretmeye istekli olduğu yazılım arasındaki fark budur.
