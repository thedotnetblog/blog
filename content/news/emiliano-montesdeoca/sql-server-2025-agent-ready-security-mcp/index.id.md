---
title: "SQL Server 2025 sebagai basis data siap agen: keamanan, backup, dan MCP dalam satu engine"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Bagian terakhir dari seri Polyglot Tax membahas masalah produksi yang sulit: Row-Level Security terpadu di data relasional, JSON, graph, dan vector, plus jejak audit kriptografis dan integrasi MCP yang membuat SQL Server 2025 benar-benar siap agen."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Saya sudah mengikuti seri Polyglot Tax karya Aditya Badramraju dengan sangat tertarik. Bagian 1-3 membangun argumen yang kuat untuk SQL Server 2025 sebagai database multi-model yang benar-benar nyata — JSON, graph, vector, dan data relasional dalam satu engine dengan query planner terpadu. Bagian 4 menutup seri ini dengan bagian yang benar-benar menentukan apakah Anda akan mempercayai arsitektur ini di production.

Spoiler: cerita production-nya solid.

## Satu Model Keamanan untuk Semua Model Data

Inilah masalah dengan stack poliglot: ketika auditor bertanya "buktikan bahwa Tenant A tidak bisa melihat data Tenant B", Anda harus menjawab pertanyaan itu untuk setiap database secara terpisah. Lima database, lima model keamanan, lima bukti.

Dengan SQL Server 2025, Anda mendefinisikan satu kebijakan Row-Level Security dan kebijakan itu mencakup semua model data:

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

Mulai saat itu, setiap query — relational joins, query path JSON, traversal graph, similarity search vector — otomatis difilter berdasarkan tenant. Engine menyuntikkan predicate ke execution plan sebelum data apa pun keluar dari storage. Kode pemanggil Anda tidak perlu `WHERE TenantID = @id` di mana-mana. Anda menguji kebijakan itu sekali.

Lapisan-lapisannya juga saling melengkapi: Dynamic Data Masking untuk kolom yang tidak boleh menampilkan nilai penuh ke role tertentu, Always Encrypted untuk enkripsi end-to-end (bahkan DBA tidak bisa membacanya), dan stored procedure sebagai batas izin sehingga agen hanya memanggil apa yang Anda buka secara eksplisit.

Ini adalah bagian arsitektur yang paling penting untuk SaaS yang penuh tuntutan kepatuhan. Satu kebijakan, satu bukti.

## Backup Terpadu = Pemulihan Atomik

Satu perintah, semua model data, titik waktu yang konsisten:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

Dalam stack poliglot, point-in-time recovery di lima database berarti mengoordinasikan lima operasi restore dan berharap timestamp-nya selaras dalam satu atau dua detik. Untuk data finansial, ketidakkonsistenan dua detik itu tidak dapat diterima. Dengan satu database, satu transaction log, satu restore — recovery bersifat atomik secara definisi.

## Ledger Tables untuk Jejak Audit yang Tahan Manipulasi

Untuk industri yang diatur, Anda membutuhkan lebih dari sekadar "kami punya logs". Anda membutuhkan bukti kriptografis bahwa logs itu tidak diubah:

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

Setiap insert, update, dan delete di-hash secara kriptografis ke dalam struktur bergaya blockchain. Anda bisa membuktikan kepada auditor — secara matematis — bahwa sebuah row belum dimanipulasi sejak ditulis. Dalam stack poliglot, kemampuan seperti ini tidak tersedia secara seragam di semua database Anda.

## Integrasi MCP: Agen Tanpa Middleware yang Ditulis Manual

Seri ini memang mengarah ke sini: SQL Server 2025 mendukung SQL MCP Server secara langsung, yang berarti agen Anda bisa memanggil database lewat tool call natural language tanpa Anda menulis middleware untuk setiap operasi.

Gabungkan itu dengan stored procedure sebagai batas izin dan Row-Level Security yang ditegakkan di engine, dan Anda mendapatkan model di mana:

1. Agen memanggil tool, misalnya "ambil konteks pelanggan untuk akun 12345"
2. MCP menerjemahkannya ke stored procedure yang Anda definisikan
3. Engine SQL menegakkan isolasi tenant dan masking kolom secara otomatis
4. Agen mendapatkan tepat data yang boleh dilihatnya

Tidak ada lapisan middleware. Tidak ada risiko ad-hoc query injection. Engine yang menangani authorization, bukan agen.

## Mengapa Ini Penting bagi Developer .NET

Jika Anda membangun layanan .NET dengan SQL Server sebagai primary store, pesan dari seri ini adalah: Anda tidak perlu menambahkan Redis untuk caching, database graph untuk relasi, atau vector store untuk embeddings — SQL Server 2025 menangani semuanya, dengan konsistensi operasional yang lebih baik daripada stack poliglot dan keamanan terpadu yang benar-benar bisa diaudit.

Integrasi MCP berarti agen Semantic Kernel atau workflow Microsoft Agent Framework Anda bisa berinteraksi dengan data tier melalui SQL MCP Server yang sama, dengan jaminan keamanan yang sama yang Anda terapkan untuk query manusia.

## Penutup

Seri Polyglot Tax layak dibaca dari awal sampai akhir. Bagian 1-3 membuktikan cerita query planner. Bagian 4 membuktikan cerita production. Bagi developer .NET yang membangun aplikasi agent-first atau AI-augmented di Azure SQL, arsitektur ini layak dipertimbangkan dengan serius.

Post asli oleh Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).