---
title: "VS Code için MSSQL uzantısı sessizce çok daha büyük bir platforma dönüşüyor"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "MSSQL uzantısının en son güncellemesi Azure SQL provisioning, Copilot destekli şema tasarımı, Data API builder ve notebook'lar ekliyor. İlginç olan, artık ne kadar çok veritabanı işinin VS Code içinde kalabildiği."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Bu makale otomatik olarak çevrildi. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

VS Code için MSSQL uzantısı bir süredir büyüyordu, ama bu son güncelleme yönü çok daha net hale getiriyor.

Artık sadece «bağlan ve birkaç sorgu çalıştır» değil.

**Azure SQL provisioning**, **Copilot destekli Schema Designer**, **SQL Notebooks** ve **Data API builder** tek bir sürümde ileri taşınırken, uzantı veritabanı merkezli geliştirme için çok daha eksiksiz bir çalışma alanına dönüşüyor.

## Pratik çekim noktası, doğrudan editörden provisioning

Kaynak yazı, artık free tier kullanarak «doğrudan editöründen ve ücretsiz olarak» tam yönetilen bir bulut veritabanı oluşturabileceğini söylüyor.

Bu, ne kadar çok setup sürtünmesi kaldırdığını fark edene kadar küçük görünen türden bir özellik.

Birçok geliştirici için veri ağırlıklı denemelerin can sıkıcı kısmı SQL'in kendisi değildir. Sorun şu environment boşluğudur:

- fikir
- veritabanı
- şema
- API
- test edilebilir backend

Bu boşluk tek bir araç içinde kısalırsa, tüm workflow daha çekici hale gelir.

## Veri işi için daha güçlü bir inner loop böyle görünür

Bu sürümde sevdiğim şey, veritabanı workflow'unun daha fazlasını tek yerde tutması:

- veritabanı provision etme
- şema tasarlama
- değişiklikleri gözden geçirme
- ORM script'leri üretme
- API'ler sunma
- endpoint'leri test etme
- notebook'lar üzerinden dokümantasyon ve sorgu

Bu, SQL'i stack içinde kopuk bir yan araç gibi görmekten çok daha ikna edici bir hikâye.

## Copilot destekli şema workflow'u, AI value'nun gerçekten hissedildiği yer

Schema designer eklemeleri özellikle ilginç, çünkü iyi bir denge yakalamış gibi duruyorlar.

Değer «AI veri modelinizi tasarlar ve siz körü körüne güvenirsiniz» değil.

Değer şunlar:

- daha hızlı başlangıç noktaları
- görsel review
- değişiklik takibi
- migration odaklı çıktı
- açık accept/undo kontrolleri

Bu, inspection path'i olmayan tam auto-generation'dan çok daha sağlıklı bir AI workflow'u.

Ve veritabanı işlerinde reviewability çok önemlidir.

## Data API builder sessiz bir çarpan

Göz ardı etmeyeceğim diğer özellik Data API builder entegrasyonu.

Aynı environment içinde şemadan şunlara geçebiliyorsanız:

- REST
- GraphQL
- MCP endpoints

bu, backend prototype'ları ve internal tool'lar için çok verimli bir yol oluşturur.

Bu, daha derin backend engineering'in yerini almaz. Ama veritabanı fikrinden çalışan bir arayüze giden yolu ciddi biçimde kısaltır.

## Değerlendirmem

Bu sürüm MSSQL uzantısını basit bir add-on yerine VS Code içinde küçük bir platform gibi hissettiriyor.

API, data tool, admin tool veya SQL-backed prototype geliştirenler için bu önemli bir değişim.

Ve Microsoft bu loop'u sıkılaştırmaya devam ederse, uzantı bugün birçok kişinin düşündüğünden çok daha stratejik olarak faydalı olacak.

Orijinal gönderi: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)