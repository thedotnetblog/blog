---
title: "NL2SQL, Ajan Çağının SQL Enjeksiyonudur"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Bir ajanın doğal dille veritabanınızı sorgulamasına izin vermeden önce bunu okuyun. NL2SQL, şema bütünlüğünü, belirsizliği ve SQL MCP Server'ın aslında ne çözdüğünü düşünene kadar basit görünür."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

NL2SQL sunumunun mükemmel duyulan bir versiyonu var: kullanıcılar doğal dilde sorular soruyor, ajanlar SQL üretiyor, veriler geri dönüyor. Daha az ekran, daha az sorgu, daha az kod. Basit.

Sonra beş dakika daha düşünüyorsunuz.

## Demoda Kimsenin Bahsetmediği Sorunlar

**Şemalar bir şeyleri açıklamak için tasarlanmamıştı.** Şifreli tablo adları, tutarsız sütun adları, ek koşullar olmadan anlamsal olarak geçersiz olan teknik olarak geçerli ilişkiler — bu kurumsal veritabanlarında yaygındır. Bunlar hatalar değil, sadece iş değişikliklerinin birikmiş tarihidir. Ancak bir modelden, niyeti aktarmak için tasarlanmamış bir şemadan niyet çıkarsamasını istediğinizde, model yine de deneyecektir. Vazgeçmez. En iyi sorgusunu üretir ve sonuçları güvenle döndürür.

**Modeller deterministik değildir.** Aynı veritabanına aynı soruyu iki kez sorun ve farklı SQL alabilirsiniz. Model olasılıkları hesaplıyor ve bağlamdaki küçük değişiklikler farklı çıktılar üretiyor. Test ederek ajanın her zaman doğru sorguyu ürettiğine dair bir garanti elde edemezsiniz.

**Kullanıcı incelemesi ölçeklenmiyor.** "Yürütmeden önce her sorguyu gözden geçirin" güvenli duyuluyor. Ama bu, kullanıcıların hem veri modelinde hem de SQL'de uzman olduğunu varsayar — tam olarak doğal dil arayüzüne ihtiyaç duymayan kişiler. Ayrıca bilişsel aşırı yükü ve yeni bir onaylama yanlılığı sınıfını da beraberinde getirir; burada sorgu karmaşıklığından bunalmış kullanıcılar araştırmak yerine geçersiz sorguları onaylar.

**Ve sonra enjeksiyon var.** Geleneksel SQL geliştirmede parametreleştirme enjeksiyonu çözüyordu çünkü kullanıcı girişi SQL yapısını değil, parametreleri dolduruyordu. NL2SQL ile model SQL'in kendisini üretiyor. İstem, şema bağlamı, konuşma geçmişi ve alınan veriler, neyin yürütüldüğünü etkiliyor. Eğer biri modelin ürettiğini değiştiren bir istem oluşturursa, bu bir enjeksiyondur — parametre düzeyinde değil, sorgu üretimi düzeyinde. DROP TABLE'ın aksine (belirgin, kurtarılabilir), NL2SQL enjeksiyonları görünür hata olmaksızın yanlış sonuçlar döndüren sorgular üretir. İş kararları yanlış veriye dayanılarak alınır.

## SQL MCP Server'ın Aslında Ne Çözdüğü

Makale burada en kullanışlı pratik noktasını yapıyor. Ajana rastgele şema erişimi verip en iyisini ummak yerine, SQL MCP Server [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview) üzerine inşa edilmiş **seçilmiş bir API yüzeyi** sunuyor.

Fark önemlidir: ajan SQL üretmiyor. Önceden tanımlanmış sonuç şekilleri döndüren adlandırılmış uç noktaları çağırıyor. SQL, bir geliştirici tarafından bir kez yazılır ve deterministiktir. Ajanın belirsizliği, rastgele sorgular oluşturmakla değil, *hangi* uç noktayı çağıracağını seçmekle sınırlıdır.

Bu, parametreleştirmenin geleneksel uygulama modelinde SQL enjeksiyonu için yaptığına benzer — güvenilmeyen girişten rastgele sorgular oluşturma yeteneğini ortadan kaldırır.

## Doğru Soru

Makale "NL2SQL'i asla kullanmayın" demiyor. *Nerede* uyguladığınıza ve *neyi* açığa çıkardığınıza dikkat edin, diyor. Kapsamlı şema ve salt okunur erişim ile kontrollü bir ortamda keşif analizi için NL2SQL uygun olabilir. İş kararlarının sonuçlara bağlı olduğu üretim sistemleri için, seçilmiş bir API katmanı çok daha güvenlidir.

Dürüstçe söylemek gerekirse: bazı sorunlar gerçekten doğal dilden SQL'e değil, adlandırılmış uç noktaların arkasındaki yapılandırılmış sorgularla daha iyi çözülüyor. SQL MCP Server, ajantik arayüzü tamamen terk etmeden o seçeneği size sunuyor.

Orijinal gönderi: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
