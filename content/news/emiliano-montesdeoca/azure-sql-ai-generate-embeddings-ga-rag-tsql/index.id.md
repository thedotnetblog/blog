---
title: "Azure SQL Kini Bisa Menghasilkan Embedding — Dalam T-SQL Murni, Tanpa Lapisan Aplikasi"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS dan CREATE EXTERNAL MODEL kini sudah GA di Azure SQL Database dan Managed Instance. Pipeline RAG yang dibangun sepenuhnya dalam T-SQL, tanpa perpindahan data."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Jika Anda pernah membangun pipeline RAG, Anda mengenal pajak pipeline: data Anda hidup di SQL, tetapi untuk menghasilkan embedding Anda perlu mengekstraknya, memanggil API embedding, menangani batching dan batas rate, dan menyimpan hasilnya di tempat yang bisa dicari secara vektor. Seringkali di database yang sama sekali berbeda.

Azure SQL baru saja menghilangkan sebagian besar itu dengan dua fitur yang kini telah tersedia secara umum: `CREATE EXTERNAL MODEL` dan `AI_GENERATE_EMBEDDINGS`.

## Apa yang Mereka Lakukan

Dua fitur T-SQL ini bekerja sebagai pipeline terintegrasi:

**`CREATE EXTERNAL MODEL`** — mendaftarkan endpoint model AI eksternal sebagai objek database bernama. Anda mengatur lokasi, format API, tipe model, dan kredensial sekali saja. Digunakan ulang di mana saja.

**`AI_GENERATE_EMBEDDINGS`** — fungsi T-SQL skalar yang memanggil model terdaftar dan mengembalikan array JSON dari nilai vektor. Bekerja dalam pernyataan SELECT, INSERT, UPDATE, dan MERGE.

Bersama-sama membentuk pipeline embedding end-to-end tanpa meninggalkan mesin SQL.

## Alur Kerja Lengkap

```sql
-- Langkah 1: Daftarkan penyedia embedding Anda sekali
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Langkah 2: Hasilkan embedding secara inline dalam T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Langkah 3: Cari dengan jarak vektor
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Itulah seluruh pipeline: data di SQL, embedding yang dihasilkan di SQL, pencarian kemiripan di SQL. Tidak ada lapisan orkestrasi, tidak ada ETL, tidak ada database vektor terpisah.

## Format API dan Opsi yang Didukung

Saat GA, `API_FORMAT` mendukung **Azure OpenAI** dan **OpenAI**. `MODEL_TYPE` saat ini terkunci pada `EMBEDDINGS`. JSON `PARAMETERS` memungkinkan pengaturan default tingkat model termasuk jumlah percobaan ulang:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Autentikasi menggunakan kredensial database, sehingga rahasia tetap berada di luar kode aplikasi Anda.

## Apa yang Ini Aktifkan untuk Aplikasi .NET

Bagi pengembang .NET yang membangun fitur AI di atas data SQL yang ada, ini signifikan. Anda tidak perlu:

- Mengekstrak data ke penyimpanan perantara untuk embedding
- Mengelola pipeline embedding eksternal
- Menyiapkan database vektor terpisah (meskipun Anda bisa menggunakan Azure AI Search jika menginginkan penyimpanan vektor berfitur lengkap)
- Mengubah lapisan akses data aplikasi Anda

Anda dapat menambahkan pencarian semantik ke aplikasi SQL yang ada secara bertahap, menggunakan alat T-SQL yang sama yang sudah Anda miliki.

## Kesimpulan

Pola RAG pada data SQL menjadi jauh lebih sederhana. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` berarti aplikasi SQL yang ada dapat memperoleh kemampuan pencarian vektor tanpa menambahkan infrastruktur baru.

Kedua fitur tersebut sudah GA hari ini di Azure SQL Database dan Azure SQL Managed Instance.

Post asli: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
