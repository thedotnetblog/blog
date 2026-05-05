---
title: "Membangun UI Multi-Agen Real-Time yang Tidak Terasa Seperti Kotak Hitam"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI dan Microsoft Agent Framework bergabung untuk memberikan alur kerja multi-agen frontend yang layak — dengan streaming real-time, persetujuan manusia, dan visibilitas penuh atas apa yang dilakukan agen Anda."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Begini kenyataan tentang sistem multi-agen: tampilannya luar biasa dalam demo. Tiga agen saling mengoper pekerjaan, memecahkan masalah, mengambil keputusan. Lalu Anda mencoba menampilkannya kepada pengguna nyata dan... sunyi. Indikator yang berputar. Tidak ada yang tahu agen mana yang melakukan apa atau mengapa sistem berhenti. Ini bukan produk — ini masalah kepercayaan.

Tim Microsoft Agent Framework baru saja menerbitkan [panduan yang luar biasa](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) tentang cara memadukan alur kerja MAF dengan [AG-UI](https://github.com/ag-ui-protocol/ag-ui), protokol terbuka untuk mengalirkan peristiwa eksekusi agen ke frontend melalui Server-Sent Events. Dan jujur saja? Inilah jembatan yang selama ini kita butuhkan.

## Mengapa ini penting bagi developer .NET

Jika Anda membangun aplikasi bertenaga AI, Anda mungkin sudah pernah menabrak dinding ini. Orkestrasi backend Anda bekerja dengan baik — agen saling meneruskan pekerjaan, alat berjalan, keputusan dibuat. Tapi frontend tidak tahu apa yang terjadi di balik layar. AG-UI mengatasi ini dengan mendefinisikan protokol standar untuk mengalirkan peristiwa agen (`RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) langsung ke lapisan UI Anda melalui SSE.

Demo yang mereka bangun adalah alur kerja dukungan pelanggan dengan tiga agen: agen triase yang merutekan permintaan, agen pengembalian dana yang menangani urusan keuangan, dan agen pesanan yang mengelola penggantian. Setiap agen memiliki alat-alatnya sendiri, dan topologi handoff didefinisikan secara eksplisit — tidak ada nuansa "cari tahu dari prompt".

## Topologi handoff adalah bintang sesungguhnya

Yang menarik perhatian saya adalah bagaimana `HandoffBuilder` memungkinkan Anda mendeklarasikan graf perutean berarah antar agen:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Setiap `add_handoff` membuat sisi berarah dengan deskripsi bahasa alami. Framework menghasilkan alat handoff untuk setiap agen berdasarkan topologi ini. Jadi keputusan perutean didasarkan pada struktur orkestrasi Anda, bukan pada apa yang ingin dilakukan LLM. Ini sangat penting untuk keandalan produksi.

## Human-in-the-loop yang benar-benar bekerja

Demo ini memperlihatkan dua pola interupsi yang dibutuhkan oleh aplikasi agen mana pun di dunia nyata:

**Interupsi persetujuan alat** — ketika agen memanggil alat yang ditandai dengan `approval_mode="always_require"`, alur kerja dijeda dan mengeluarkan peristiwa. Frontend merender modal persetujuan dengan nama alat dan argumennya. Tidak ada loop percobaan ulang yang membakar token — hanya alur jeda-setujui-lanjutkan yang bersih.

**Interupsi permintaan informasi** — ketika agen membutuhkan lebih banyak konteks dari pengguna (seperti ID pesanan), agen berhenti dan bertanya. Frontend menampilkan pertanyaan, pengguna merespons, dan eksekusi dilanjutkan dari tepat di mana ia berhenti.

Kedua pola dialirkan sebagai peristiwa AG-UI standar, sehingga frontend Anda tidak memerlukan logika khusus per agen — cukup merender peristiwa apa pun yang masuk melalui koneksi SSE.

## Menghubungkannya sangat sederhana

Integrasi antara MAF dan AG-UI adalah satu panggilan fungsi:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

`workflow_factory` membuat alur kerja baru per thread, sehingga setiap percakapan mendapat status yang terisolasi. Endpoint menangani semua plumbing SSE secara otomatis. Jika Anda sudah menggunakan FastAPI (atau bisa menambahkannya sebagai lapisan ringan), ini hampir tanpa gesekan.

## Pandangan saya

Bagi developer .NET, pertanyaan langsung adalah: "Bisakah saya melakukan ini di C#?" Agent Framework tersedia untuk .NET dan Python, dan protokol AG-UI bersifat language-agnostic (ini hanyalah SSE). Jadi meskipun demo ini menggunakan Python dan FastAPI, polanya langsung dapat diterapkan. Anda bisa menghubungkan ASP.NET Core minimal API dengan endpoint SSE mengikuti skema peristiwa AG-UI yang sama.

Kesimpulan yang lebih besar adalah bahwa UI multi-agen menjadi perhatian kelas satu, bukan renungan. Jika Anda membangun apa pun di mana agen berinteraksi dengan manusia — dukungan pelanggan, alur kerja persetujuan, pemrosesan dokumen — kombinasi orkestrasi MAF dan transparansi AG-UI adalah pola yang harus diikuti.

## Kesimpulan

AG-UI + Microsoft Agent Framework memberi Anda yang terbaik dari kedua dunia: orkestrasi multi-agen yang kuat di backend dan visibilitas real-time di frontend. Tidak ada lagi interaksi agen sebagai kotak hitam.

Lihat [panduan lengkap](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) dan [repositori protokol AG-UI](https://github.com/ag-ui-protocol/ag-ui) untuk mendalami lebih jauh.
