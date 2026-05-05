---
title: "SQL MCP Server — AI Ajanlarına Veritabanı Erişimi Vermenin Doğru Yolu"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Data API builder'dan SQL MCP Server, AI ajanlara şema açıklamadan ve NL2SQL'e dayanmadan güvenli, deterministik veritabanı erişimi sağlar. RBAC, önbellekleme, çoklu veritabanı desteği — hepsi yerleşik."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "sql-mcp-server-data-api-builder" >}}).*

Dürüst olalım: bugün mevcut veritabanı MCP sunucularının çoğu gerçekten ürkütücü. Doğal dil sorgusu alıyor, anında SQL üretiyor ve bunu üretim verinize karşı çalıştırıyor. Ne yanlış gidebilir ki? (Her şey. Her şey yanlış gidebilir.)

Azure SQL ekibi az önce [SQL MCP Server'ı tanıttı](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) ve bu yaklaşım temelden farklı. Data API builder (DAB) 2.0'ın bir özelliği olarak geliştirilen bu araç, AI ajanlarına NL2SQL olmadan, şemanızı açıklamadan ve her adımda tam RBAC ile veritabanı işlemlerine yapılandırılmış, deterministik erişim sağlıyor.

## Neden NL2SQL yok?

Bu, en ilginç tasarım kararı. Modeller deterministik değil ve karmaşık sorgular en büyük hata riskini taşıyan yapılar. AI'ın üretmesini umduğunuz tam sorgular da deterministik olmayan şekilde üretildiğinde en dikkatli incelenmesi gereken sorgular oluyor.

Bunun yerine SQL MCP Server bir **NL2DAB** yaklaşımı benimsiyor. Ajan, Data API builder'ın varlık soyutlama katmanı ve yerleşik sorgu oluşturucu ile birlikte çalışarak doğru ve düzgün biçimlendirilmiş T-SQL deterministik olarak üretiyor. Kullanıcı için aynı sonuç, ancak hayali JOIN'ler veya kazara veri ifşası riski olmadan.

## Yedi araç, yedi yüz değil

SQL MCP Server, veritabanının büyüklüğünden bağımsız olarak tam olarak yedi DML aracı sunuyor:

- `describe_entities` — mevcut varlıkları ve işlemleri keşfet
- `create_record` — satır ekle
- `read_records` — tablolar ve görünümleri sorgula
- `update_record` — satırları değiştir
- `delete_record` — satırları sil
- `execute_entity` — saklı yordamları çalıştır
- `aggregate_records` — toplama sorguları

Bu akıllıca bir tasarım çünkü bağlam pencereleri ajanın düşünme alanıdır. Yüzlerce araç tanımıyla doldurmak, muhakeme için daha az alan bırakır. Yedi sabit araç, ajanın *gezinmek* yerine *düşünmeye* odaklanmasını sağlar.

Her araç ayrı ayrı etkinleştirilebilir veya devre dışı bırakılabilir:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Üç komutla başlangıç

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Bu kadar. Customers tablonuzu açığa çıkaran çalışan bir SQL MCP Server'ınız var. Varlık soyutlama katmanı, adları ve sütunları takma adla kullanmanıza, rol başına alanları sınırlamanıza ve iç şema ayrıntılarını açıklamadan ajanların tam olarak neyi göreceğini kontrol etmenize olanak tanıyor.

## Güvenlik hikayesi sağlam

Data API builder'ın olgunluğu burada meyvesini veriyor:

- **Her katmanda RBAC** — her varlık hangi rollerin okuyabileceğini, oluşturabileceğini, güncelleyebileceğini veya silebileceğini ve hangi alanların görünür olduğunu tanımlıyor
- **Azure Key Vault entegrasyonu** — bağlantı dizeleri ve gizli anahtarlar güvenli şekilde yönetiliyor
- **Microsoft Entra + özel OAuth** — üretim düzeyinde kimlik doğrulama
- **Content Security Policy** — ajanlar ham SQL değil, denetimli bir sözleşme üzerinden etkileşim kuruyor

Şema soyutlaması özellikle önemli. İç tablo ve sütun adlarınız asla ajana açıklanmıyor. Veritabanı ERD'nize göre değil, AI etkileşimi için mantıklı olan varlıkları, takma adları ve açıklamaları siz tanımlıyorsunuz.

## Çok veritabanı ve çok protokol

SQL MCP Server, Microsoft SQL, PostgreSQL, Azure Cosmos DB ve MySQL'i destekliyor. Ve bir DAB özelliği olduğundan, aynı yapılandırmadan eş zamanlı olarak REST, GraphQL ve MCP endpoint'leri elde ediyorsunuz. Aynı varlık tanımları, aynı RBAC kuralları, aynı güvenlik — üç protokol genelinde.

DAB 2.0'daki otomatik yapılandırma, hızlı prototipleme için daha az soyutlamaya razıysanız veritabanınızı inceleyebilir ve yapılandırmayı dinamik olarak oluşturabilir.

## Kişisel görüşüm

AI ajanları için kurumsal veritabanı erişimi işte böyle çalışmalı. "Hey LLM, biraz SQL yaz da üretime at bakalım" değil. Bunun yerine: iyi tanımlanmış bir varlık katmanı, deterministik sorgu üretimi, her adımda RBAC, önbellekleme, izleme ve telemetri. En iyi anlamda sıkıcı.

.NET geliştiricileri için entegrasyon hikayesi temiz — DAB bir .NET aracıdır, MCP Server bir container olarak çalışır ve çoğumuzun zaten kullandığı Azure SQL ile çalışır. Veri erişimine ihtiyaç duyan AI ajanları geliştiriyorsanız buradan başlayın.

## Sonuç

SQL MCP Server ücretsiz, açık kaynaklı ve her yerde çalışır. AI ajanlarına güvenli veritabanı erişimi sağlamak için Microsoft'un öngörülü yaklaşımıdır. Başlamak için [tam yazıyı](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) ve [dokümantasyonu](https://aka.ms/sql/mcp) inceleyin.
