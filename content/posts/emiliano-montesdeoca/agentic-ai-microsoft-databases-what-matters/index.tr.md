---
title: "SQL MCP Server, SSMS'de Copilot ve AI Agentlı Veritabanı Hub'ı: SQLCon 2026'dan Gerçekten Önemli Olanlar"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft, SQLCon 2026'da bir dizi veritabanı duyurusu yaptı. Azure SQL üzerine AI destekli uygulamalar geliştiriyorsanız gerçekten önemli olanlar burada."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agentic-ai-microsoft-databases-what-matters" >}}).*

Microsoft, Atlanta'da [FabCon ile birlikte SQLCon 2026'yı başlattı](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) ve açılacak çok şey var. Orijinal duyuru, tasarruf planlarından kurumsal uyumluluk özelliklerine kadar her şeyi kapsıyor. Kurumsal fiyatlandırma slaytlarını atlayarak, Azure SQL ve AI ile bir şeyler geliştiren bir geliştirici olarak önemli olanlara odaklanacağım.

## SQL MCP Server genel önizlemede

Bu, benim için manşet. Azure SQL Database Hyperscale artık, [Model Context Protocol](https://modelcontextprotocol.io/) kullanarak SQL verilerinizi AI agentlarına ve Copilot'lara güvenli biçimde bağlamanıza olanak tanıyan genel önizlemede bir **SQL MCP Server**'a sahip.

MCP dalgasını takip ediyorsanız — ve dürüst olmak gerekirse, şu anda bunu kaçırmak zor — bu büyük bir gelişme. AI agentlarınıza veritabanından bağlam sağlamak için özel veri pipeline'ları oluşturmak yerine, SQL verilerini doğrudan sergilemek için standart bir protokol elde ediyorsunuz. Agentlarınız canlı veritabanı bilgilerini sorgulayabilir, üzerinde akıl yürütebilir ve harekete geçebilir.

Semantic Kernel veya Microsoft Agent Framework ile AI agentları geliştiriyoruz için bu, temiz bir entegrasyon yolu açıyor. Agentınızın envanteri kontrol etmesi mi gerekiyor? Müşteri kaydına bakması mı? Bir siparişi doğrulaması mı? MCP, her senaryo için özel veri-getirme kodu yazmadan bunu yapmanın yapılandırılmış bir yolunu sunar.

## SSMS 22'de GitHub Copilot artık GA'da

SQL Server Management Studio'da zaman geçiriyorsanız — ve dürüst olalım, çoğumuz hâlâ geçiriyoruz — GitHub Copilot artık SSMS 22'de genel kullanım için hazır. VS Code ve Visual Studio'da zaten kullandığınız Copilot deneyiminin aynısı, ama T-SQL için.

Buradaki pratik değer açık: sorgu yazma, saklı yordam yeniden düzenleme, performans sorunlarını giderme ve yönetim görevleri için sohbet tabanlı yardım. Kavram olarak devrimci bir şey yok, ama SSMS'in içinde olması, veritabanı işleriniz için AI yardımı almak üzere başka bir editöre geçmenize gerek kalmadığı anlamına gelir.

## Vektör indeksler ciddi bir yükseltme aldı

Azure SQL Database artık tam ekleme, güncelleme ve silme desteğiyle daha hızlı, daha yetenekli vektör indekslerine sahip. Bu, vektör verilerinizin gerçek zamanlı güncel kalması anlamına gelir — toplu yeniden indeksleme gerekmez.

İşte yenilikler:
- Daha küçük indeks boyutları için fazla doğruluk kaybetmeden **quantization (niceleme)**
- Daha hassas sonuçlar için **iterative filtering (yinelemeli filtreleme)**
- Öngörülebilir performans için **daha sıkı sorgu optimize edici entegrasyonu**

Azure SQL'i vektör deposu olarak kullanarak RAG (Retrieval-Augmented Generation) yapıyorsanız, bu iyileştirmeler doğrudan işe yarar. Vektörlerinizi aynı veritabanındaki ilişkisel verilerle birlikte tutabilirsiniz; bu, ayrı bir vektör veritabanı çalıştırmaya kıyasla mimarinizi önemli ölçüde basitleştirir.

Aynı vektör geliştirmeleri Fabric'teki SQL veritabanında da mevcut; çünkü her ikisi de aynı SQL motoru üzerinde çalışıyor.

## Fabric'te Database Hub: ajanlı yönetim

Bu daha ileriye dönük ama ilginç. Microsoft, Azure SQL, Cosmos DB, PostgreSQL, MySQL ve Arc üzerinden SQL Server genelinde tek bir cam panel sunan **Microsoft Fabric'te Database Hub**'ı (erken erişim) duyurdu.

İlginç taraf, yalnızca birleşik görünüm değil — yönetimin ajanlı yaklaşımı. AI agentlar veritabanı altyapınızı sürekli izler, nelerin değiştiğini öne çıkarır, neden önemli olduğunu açıklar ve ne yapılması gerektiğini önerir. Agentın ön çalışmayı yaptığı ve siz kararları aldığınız bir human-in-the-loop modelidir.

Ondan fazla veritabanını yöneten ekipler için bu, operasyonel gürültüyü gerçekten azaltabilir. Portaller arasında atlayıp metrikleri manuel olarak kontrol etmek yerine, agent sinyali size getirir.

## .NET geliştiricileri için ne anlama geliyor

Tüm bu duyuruları birbirine bağlayan ip açık: Microsoft, veritabanı yığınının her katmanına AI agentları yerleştiriyor. Bir hile olarak değil, pratik bir araç katmanı olarak.

Azure SQL tarafından desteklenen .NET uygulamaları geliştiriyorsanız, gerçekten yapacaklarım şunlar:

1. AI agentları geliştiriyorsanız **SQL MCP Server'ı deneyin**. Agentlarınıza özel bağlantı kodu olmadan veritabanı erişimi vermenin en temiz yolu.
2. Henüz yapmadıysanız **SSMS'de Copilot'u etkinleştirin** — günlük SQL çalışması için ücretsiz üretkenlik kazanımı.
3. RAG yapıyorsanız ve şu anda ayrı bir vektör deposu çalıştırıyorsanız **vektör indekslerine bakın**. Azure SQL'de birleştirmek, yönetilecek bir servis daha az demek.

## Sonuç

Tam duyuruda daha fazlası var — tasarruf planları, geçiş asistanları, uyumluluk özellikleri — ancak geliştirici hikayesi MCP Server'da, vektör iyileştirmelerinde ve ajanlı yönetim katmanında. Bunlar, bütçenizi değil, oluşturduğunuz şeyleri değiştiren parçalar.

Tam tablo için [Shireesh Thota'nın tam duyurusuna](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) göz atın; yeni yönetim deneyimini denemek istiyorsanız [Database Hub erken erişimine kaydolun](https://aka.ms/database-hub).
