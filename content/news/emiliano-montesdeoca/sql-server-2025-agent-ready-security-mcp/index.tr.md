---
title: "SQL Server 2025 ajanlara hazır veritabanı olarak: güvenlik, yedekleme ve MCP tek bir motorda"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Polyglot Tax serisinin son bölümü, üretimdeki zor sorunları ele alıyor: ilişkisel, JSON, graph ve vector veriler üzerinde birleşik Row-Level Security, ayrıca SQL Server 2025'i gerçekten ajanlara hazır hale getiren kriptografik denetim izleri ve MCP entegrasyonu."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Aditya Badramraju'nun Polyglot Tax serisini büyük bir ilgiyle takip ettim. 1-3. bölümler, SQL Server 2025'i gerçekten çok modelli bir veritabanı olarak güçlü biçimde savundu — JSON, graph, vector ve ilişkisel veriler tek bir motorda, birleşik bir query planner ile. 4. bölüm, bu mimariye production'da gerçekten güvenip güvenmeyeceğinizi belirleyen kısmı kapatıyor.

Spoiler: production hikayesi sağlam.

## Tüm Veri Modelleri İçin Tek Güvenlik Modeli

Poliglot stack'lerin sorunu şu: bir denetçi "Tenant A'nın Tenant B'nin verisini göremediğini kanıtla" dediğinde, bu soruya her veritabanı için ayrı ayrı cevap vermen gerekir. Beş veritabanı, beş güvenlik modeli, beş kanıt.

SQL Server 2025 ile tek bir Row-Level Security policy tanımlarsınız ve bu tüm veri modellerini kapsar:

```sql
CREATE FUNCTION dbo.fn_TenantFilter(@TenantID INT)
RETURNS TABLE WITH SCHEMABINDING
AS RETURN SELECT 1 AS fn_result
WHERE @TenantID = CAST(SESSION_CONTEXT(N'TenantID') AS INT);

CREATE SECURITY POLICY TenantIsolation
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Customers,     -- Relational
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Events,        -- JSON data
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Relationships, -- Graph edges
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Embeddings     -- Vector data
WITH (STATE = ON);
```

O noktadan sonra her query — ilişkisel join'ler, JSON path sorguları, graph traversalları, vector similarity aramaları — otomatik olarak tenant'a göre filtrelenir. Motor, storage'dan herhangi bir veri çıkmadan önce predicate'i execution plan'a enjekte eder. Çağıran kodunuzun her yere `WHERE TenantID = @id` yazmasına gerek kalmaz. Policy'yi bir kez test edersiniz.

Katmanlar da birbirini tamamlar: bazı rollerin tam değerleri görmemesi gereken kolonlar için Dynamic Data Masking, uçtan uca şifreleme için Always Encrypted (DBA'lar bile okuyamaz), ve ajanların yalnızca açıkça expose ettiğiniz şeyleri çağırması için izin sınırı olarak stored procedure'ler.

Bu, compliance ağırlıklı SaaS için mimarinin en önemli kısmıdır. Tek policy, tek kanıt.

## Birleştirilmiş Yedekleme = Atomik Kurtarma

Tek bir komut, tüm veri modelleri, tutarlı bir zaman noktası:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

Poliglot bir stack'te beş veritabanı boyunca point-in-time recovery yapmak, beş restore işlemini koordine etmek ve timestamp'lerin bir iki saniye içinde hizalanmasını ummak demektir. Finansal veri için bu iki saniyelik tutarsızlık kabul edilemez. Tek veritabanı, tek transaction log, tek restore — recovery tanım gereği atomiktir.

## Kurcalamaya Dayanıklı Denetim İzleri için Ledger Tabloları

Düzenlemeye tabi sektörlerde "loglarımız var" demek yetmez. Bu logların değiştirilmediğine dair kriptografik kanıta ihtiyacınız vardır:

```sql
CREATE TABLE FinancialTransactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT NOT NULL,
    Amount MONEY NOT NULL,
    TransactionType NVARCHAR(20),
    TransactionDate DATETIME2 DEFAULT SYSUTCDATETIME()
)
WITH (SYSTEM_VERSIONING = ON, LEDGER = ON);
```

Her insert, update ve delete, blockchain benzeri bir yapıya kriptografik olarak hash'lenir. Bir satırın yazıldığı andan beri manipüle edilmediğini bir denetçiye matematiksel olarak kanıtlayabilirsiniz. Poliglot stack'te bu yetenek tüm veritabanlarınızda aynı şekilde mevcut değildir.

## MCP Entegrasyonu: Elle Kodlanmış Middleware Olmadan Agent'lar

Seri tam olarak buraya doğru ilerliyordu: SQL Server 2025, SQL MCP Server'ı doğrudan destekliyor; yani agent'larınız her işlem için middleware yazmadan doğal dil tool call'larıyla veritabanını çağırabiliyor.

Bunu stored procedure'leri izin sınırı olarak kullanmak ve Row-Level Security'yi motor seviyesinde uygulamak ile birleştirdiğinizde şu modeli elde edersiniz:

1. Agent bir tool çağırır, örneğin "12345 hesabı için müşteri bağlamını getir"
2. MCP bunu tanımladığınız stored procedure'e çevirir
3. SQL engine tenant izolasyonunu ve column masking'i otomatik uygular
4. Agent yalnızca görmeye yetkili olduğu veriyi alır

Middleware katmanı yok. Ad-hoc query injection riski yok. Authorization'ı agent değil, engine yönetir.

## Bunun .NET Geliştiricileri İçin Önemi

Eğer .NET servisleri geliştiriyor ve SQL Server'ı birincil veri deposu olarak kullanıyorsanız, bu serinin mesajı şu: caching için Redis, ilişkiler için graph database, embeddings için vector store eklemenize gerek yok. SQL Server 2025 bunların hepsini halleder — poliglot bir stack'ten daha iyi operasyonel tutarlılıkla ve gerçekten denetlenebilir birleşik güvenlikle.

MCP entegrasyonu, Semantic Kernel agent'larınızın veya Microsoft Agent Framework workflow'larınızın aynı SQL MCP Server üzerinden veri katmanınızla etkileşime girebileceği, insan sorgularına uygulayacağınız aynı güvenlik garantileriyle çalışabileceği anlamına gelir.

## Kapanış

Polyglot Tax serisi baştan sona okunmaya değer. 1-3. bölümler query planner hikayesini kanıtlıyor. 4. bölüm production hikayesini kanıtlıyor. Azure SQL üzerinde agent-first veya AI-augmented uygulamalar geliştiren .NET geliştiricileri için bu mimari ciddi biçimde düşünülmeyi hak ediyor.

Aditya Badramraju'nun orijinal yazısı: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).