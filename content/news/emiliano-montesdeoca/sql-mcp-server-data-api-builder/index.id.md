---
title: "SQL MCP Server — Cara yang Tepat untuk Memberi Agen AI Akses Database"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server dari Data API builder memberi agen AI akses database yang aman dan deterministik tanpa mengekspos skema atau mengandalkan NL2SQL."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "sql-mcp-server-data-api-builder" >}}).*

Jujur saja: sebagian besar server MCP database yang tersedia saat ini sangat menakutkan. Mereka mengambil kueri bahasa alami, menghasilkan SQL secara langsung, dan menjalankannya pada data produksi Anda.

Tim Azure SQL baru saja [memperkenalkan SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), dan mengambil pendekatan yang secara fundamental berbeda.

## Mengapa tidak NL2SQL?

Model tidak deterministik. SQL MCP Server menggunakan pendekatan **NL2DAB**. Agen bekerja dengan lapisan abstraksi entitas Data API builder untuk menghasilkan T-SQL yang akurat secara deterministik.

## Tujuh alat, bukan tujuh ratus

SQL MCP Server mengekspos tepat tujuh alat DML:

- `describe_entities` — temukan entitas yang tersedia
- `create_record` — sisipkan baris
- `read_records` — kueri tabel dan view
- `update_record` — modifikasi baris
- `delete_record` — hapus baris
- `execute_entity` — jalankan stored procedure
- `aggregate_records` — kueri agregasi

## Mulai dalam tiga perintah

```bash
dab init   --database-type mssql   --connection-string "@env('sql_connection_string')"

dab add Customers   --source dbo.Customers   --permissions "anonymous:*"

dab start
```

## Cerita keamanan solid

RBAC di setiap lapisan, integrasi Azure Key Vault, Microsoft Entra + OAuth kustom.

Lihat [posting lengkap](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) dan [dokumentasi](https://aka.ms/sql/mcp).
