---
title: "Cerita observability-to-ROI Foundry adalah yang dibutuhkan platform agen yang serius"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: "Pengumuman observability terbaru dari Foundry penting karena menghubungkan tracing, evaluation, optimization, dan ROI ke dalam satu loop operasional bagi AI agents."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Observability
  - Evaluations
---

*Tulisan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Jika AI agents akan hidup di production, observability tidak boleh berhenti di logs dan traces.

Itulah sebabnya cerita baru Foundry dari observability ke ROI terasa penting.

Pesan sebenarnya bukan "kami menambahkan lebih banyak dashboard".

Pesan sebenarnya adalah bahwa platform agen yang serius membutuhkan loop operasional yang berkelanjutan:

- trace apa yang terjadi
- evaluate apakah hasilnya baik
- optimize bagian yang perlu diperbaiki
- hubungkan hasilnya dengan nilai bisnis

Itu jauh lebih kuat daripada retorika platform yang biasa.

## Kalimat kunci dari artikel sumber mengatakan semuanya

Postingan asli dibuka dengan satu kalimat yang menurut saya harus diperhatikan oleh setiap tim yang membangun agen:

> "Meluncurkan AI agent itu bagian yang mudah. Menjaganya tetap akurat, aman, dan dapat dipertanggungjawabkan di production adalah tempat tim tersangkut."

Itu tepat sekali.

Kita sudah melewati fase ketika pertanyaan utamanya adalah, "apakah saya bisa membuat agen melakukan sesuatu yang keren?"

Pertanyaan yang lebih sulit dan lebih bernilai adalah:

**apakah saya bisa mengoperasikan sistem itu setelah ia mulai berinteraksi dengan pengguna nyata, tools nyata, dan biaya nyata?**

Di situlah Foundry mencoba mendorong percakapan.

## Mengapa ini lebih penting daripada demo agen lain

Banyak pengumuman AI agent masih berfokus pada creation: bangun agen, hubungkan tools, arahkan tasks, kirim interface.

Itu semua baik.

Tapi pertanyaan operasional adalah titik di mana sebagian besar sistem serius menjadi berkelanjutan atau berubah menjadi eksperimen mahal:

- apa yang sebenarnya dilakukan agen di production?
- apakah ia melakukan hal yang benar?
- apakah performanya memburuk seiring waktu?
- apakah biayanya terlalu tinggi dibanding nilai yang ia hasilkan?
- perubahan konfigurasi mana yang benar-benar meningkatkan quality?

Itulah sebabnya saya pikir pengumuman Foundry lebih penting daripada ringkasan fitur biasa. Ini mencoba mendefinisikan loop Agent DevOps, bukan hanya cerita pembuatan agen.

## Loop empat bagian adalah produk yang sebenarnya di sini

Artikel ini pada dasarnya mengorganisasi platform di sekitar empat capability:

- Trace
- Evaluate
- Monitor
- Optimize

Itu bentuk yang tepat.

Saya bahkan berpendapat bahwa platform apa pun yang ingin dianggap serius untuk workload produksi agen pada akhirnya membutuhkan keempatnya.

Tracing saja tidak cukup.

Evaluation saja tidak cukup.

Optimisasi tanpa bukti hanyalah menebak.

Dan membicarakan ROI tanpa telemetry biasanya cuma teater.

## Sisi interoperabilitasnya sangat cerdas

Salah satu keputusan terkuat dalam pengumuman ini adalah bahwa Foundry tidak berpura-pura bahwa semua agen akan dibangun dalam satu framework.

Postingan sumber secara eksplisit membahas tracing dan evals yang meluas ke:

- LangChain
- LangGraph
- OpenAI SDK
- Microsoft Agent Framework
- framework kustom via OpenTelemetry

Ini penting.

Karena platform lock-in adalah salah satu cara tercepat untuk membuat cerita operasi yang sebenarnya berguna menjadi kurang menarik.

Jika tim bisa mempertahankan pilihan framework mereka dan tetap mendapatkan telemetry serta surface evaluation tingkat production, friksi turun secara signifikan.

## Rubric evaluation bisa jadi lebih penting daripada yang orang kira

Bagian rubric evaluator juga layak disorot.

Saya pikir ini salah satu tambahan paling praktis di seluruh post.

Mengapa? Karena "baik" itu tergantung konteks.

Artikel mengatakan rubric evaluation menghasilkan "context-aware evaluation criteria dari perilaku yang dimaksudkan untuk agent Anda." Itu memang arah yang dibutuhkan sistem seperti ini.

Penilaian kualitas generik memang berguna.

Tetapi pada akhirnya tim perlu menilai agen berdasarkan standar mereka sendiri:

- tone
- task completion
- policy adherence
- latency expectations
- batas biaya
- aturan bisnis spesifik domain

Di situlah evaluation mulai menjadi bermakna secara operasional, bukan sekadar menarik secara akademis.

## ROI adalah bagian yang paling tidak nyaman, dan justru karena itu penting

Saya juga pikir bagian ROI dari pengumuman ini penting justru karena ia tidak nyaman.

Postingan sumber menanyakan langsung:

> "apakah agent ini sepadan dengan biayanya?"

Pertanyaan itu sering dihindari dalam percakapan AI.

Tapi itu pertanyaan yang benar.

Jika platform benar-benar bisa menghubungkan biaya, task completion, waktu yang dihemat, dan production traces di satu tempat, itu memberi engineering dan leadership bahasa bersama yang jauh lebih baik.

Dan jujur saja, bahasa bersama seperti itu sangat dibutuhkan.

## Pendapat saya

Ini salah satu pengumuman level platform yang lebih baik dalam batch ini karena fokus pada mengoperasikan agen, bukan hanya membangunnya.

Dan di situlah pekerjaan berat sebenarnya dimulai.

Platform AI terkuat dalam beberapa tahun ke depan bukan hanya yang punya akses ke lebih banyak model atau lebih banyak demo. Mereka adalah yang membantu tim trace perilaku, evaluate hasil, optimize dengan aman, dan membenarkan biaya dengan bukti.

Cerita Foundry ini mencoba bergerak tepat ke arah itu.

Itulah sebabnya cerita ini layak dianggap serius.

Post asli: [Build 2026: From observability to ROI for AI agents on any framework](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/)