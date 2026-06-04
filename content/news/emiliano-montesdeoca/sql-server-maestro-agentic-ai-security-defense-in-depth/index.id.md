---
title: "MAESTRO, Pertahanan Berlapis, dan Mengapa SQL Server Kini Menjadi Batas Keamanan untuk AI"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "AI agentik memperkenalkan ancaman yang tidak dirancang oleh model STRIDE tradisional. Begini cara Microsoft SQL memetakan ke framework MAESTRO untuk menyediakan batas eksekusi yang dikelola."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Model ancaman keamanan dibangun di atas asumsi tentang siapa atau apa yang membuat permintaan. STRIDE mengasumsikan aktor manusia yang berinteraksi dengan sistem melalui antarmuka yang ditentukan. Agen AI tidak bekerja dengan cara itu.

## STRIDE Tidak Dirancang untuk Agen AI

Sistem agentik beroperasi secara otonom, menghubungkan alat melalui panggilan API, membuat keputusan tentang data apa yang akan diambil dan tindakan apa yang akan dieksekusi, dan dapat menerima instruksi dari berbagai sumber — prompt pengguna, hasil alat, data yang diambil. Model ancaman STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) tidak secara memadai menangkap vektor serangan spesifik agen seperti injeksi prompt, keracunan konteks, atau penyalahgunaan alat.

Cloud Security Alliance menerbitkan framework MAESTRO khusus untuk risiko agen AI.

## Framework MAESTRO

MAESTRO mengorganisir risiko AI agentik dalam tujuh lapisan:

1. **Foundation Models** — LLM yang mendasari dan kerentanan pelatihannya
2. **Data Operations** — pengambilan, penyimpanan, dan manipulasi data
3. **Agent Frameworks** — middleware orkestrasi dan koordinasi agen
4. **Deployment & Infrastructure** — di mana agen dijalankan dan cara dikonfigurasi
5. **Evaluation & Observability** — pemantauan perilaku agen dari waktu ke waktu
6. **Security & Compliance** — kontrol akses, audit, dan kepatuhan regulasi
7. **Agent Ecosystem** — cara agen berinteraksi satu sama lain dan dengan alat eksternal

Setiap lapisan memiliki vektor serangan spesifik yang tidak langsung ditangani oleh kontrol keamanan tradisional.

## Microsoft SQL sebagai Batas Eksekusi yang Dikelola

SQL Server 2025 memetakan ke lapisan MAESTRO dengan cara yang konkret:

**Lapisan Data Operations**: `AI_GENERATE_EMBEDDINGS` yang terintegrasi di T-SQL menjaga operasi vektor dalam batas yang dikelola dari database. Data tidak perlu keluar ke layanan model untuk pemrosesan embedding.

**Lapisan Security & Compliance**: Keamanan tingkat baris (RLS) dan penyamaran data dinamis (DDM) berlaku terlepas dari bagaimana permintaan tiba — baik dari pengguna manusia maupun agen AI. Agen tidak dapat melewati kontrol yang diterapkan oleh database itu sendiri.

**Lapisan Agent Frameworks**: Prosedur tersimpan berfungsi sebagai batas alat. Alih-alih memberikan agen akses SQL sembarangan, Anda mendefinisikan operasi yang diizinkan sebagai prosedur dan mengeksposnya sebagai alat agen. Kueri terparameter mencegah injeksi pada tingkat eksekusi.

**Lapisan Evaluation & Observability**: Log audit dan Query Store menangkap apa yang sebenarnya dieksekusi setiap agen — bukan hanya apa yang diminta untuk dilakukan. Keterlacakan ini sangat penting untuk investigasi insiden dalam sistem agentik di mana atribusi kompleks.

## Pertahanan Berlapis untuk AI Agentik

Prinsipnya tetap sama seperti keamanan tradisional: tidak ada kontrol tunggal yang cukup. Yang berubah adalah kontrol mana yang paling penting untuk agen:

**Mengurangi radius ledakan**: batas alat melalui prosedur tersimpan berarti agen yang dikompromikan hanya dapat mengeksekusi operasi yang telah ditentukan sebelumnya. Ia tidak dapat beralih ke kueri sembarangan.

**Observabilitas**: Anda harus mampu menjawab "apa yang sebenarnya dilakukan agen ini?" setelah insiden. Sistem AI agentik tanpa keterlacakan tingkat database memiliki titik buta yang tidak dicakup oleh pencatatan aplikasi.

**Eksekusi terbatas**: parameterisasi, RLS, dan DDM adalah aset keamanan terlepas dari apakah pemanggil manusia atau bukan. Jangan melemahkannya untuk mengakomodasi agen.

**Akuntabilitas**: log audit SQL Server membuat catatan tentang siapa (agen mana, menggunakan kredensial apa) yang mengeksekusi apa pada waktu tertentu. Ini penting ketika sistem agentik mengambil tindakan dengan konsekuensi nyata di dunia.

SQL Server 2025 tidak dibangun untuk menyelesaikan risiko agentik secara abstrak — ia dibangun untuk menjadi database relasional. Namun tata kelola yang membuat database enterprise dapat dipercaya ternyata adalah persis apa yang membuat batas eksekusi agen aman.

Pos asli: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
