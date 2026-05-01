---
title: "Pembaruan April Azure DevOps MCP Server: Kueri WIQL, Autentikasi PAT, dan MCP Apps Eksperimental"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server mendapat kueri work item berbasis WIQL, autentikasi Personal Access Token, anotasi MCP, dan fitur MCP Apps eksperimental yang membungkus alur kerja umum menjadi alat yang dapat digunakan ulang."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Azure DevOps MCP Server terus membaik. Pembaruan April dari Dan Hellem mencakup server lokal dan remote, dan ada beberapa tambahan yang benar-benar berguna — terutama jika Anda menggunakan Copilot untuk menavigasi board dan repo.

## Dukungan Kueri WIQL

Fitur utamanya: tool baru `wit_query_by_wiql` yang memungkinkan Anda menjalankan kueri Work Item Query Language langsung dari client MCP.

Jika Anda sudah lama memakai Azure Boards, Anda tahu WIQL. Ini adalah sintaks kueri mirip SQL untuk work items: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. Menyediakannya sebagai tool MCP berarti sesi Copilot Anda kini bisa mengambil kumpulan work item yang presisi tanpa perlu memfilter manual atau klik sana-sini di tampilan board.

Satu catatan: di remote MCP Server, tool ini saat ini membutuhkan feature flag **Insiders** saat mereka memvalidasi performa kueri pada skala besar. Tool ini akan tersedia untuk semua orang setelah telemetrinya terlihat bagus.

## Personal Access Token di Server Lokal

Server MCP lokal sekarang mendukung autentikasi PAT. Ini terdengar seperti perbaikan kecil, tetapi penting untuk skenario integrasi — terutama saat Anda menjalankan server MCP di konteks tanpa autentikasi interaktif, atau saat Anda terhubung dari client eksternal dan otomasi.

Langkah pengaturannya didokumentasikan di [panduan Getting Started](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat).

## Anotasi MCP di Server Remote

Anotasi adalah tag metadata pada tool MCP yang memberi tahu LLM cara menggunakannya dengan aman. Azure DevOps MCP Server kini menerapkan anotasi untuk:

- **Tool read-only** — model tahu bahwa tool ini aman dipanggil tanpa konfirmasi pengguna
- **Tool destruktif** — model tahu harus berhati-hati dan mengonfirmasi sebelum melanjutkan
- **Tool open-world** — model memahami bahwa tool ini bisa mengembalikan hasil tak terduga

Ini penting untuk keandalan agen. Tanpa anotasi, model harus menebak dari nama tool apakah aman dipanggil. Dengan anotasi, perilakunya eksplisit dan agen bisa mengambil keputusan lebih baik.

## Konsolidasi Tool Wiki

Server remote mulai mengonsolidasikan tool terkait menjadi lebih sedikit tool yang lebih mampu. Tool wiki adalah yang pertama mendapatkan perlakuan ini:

| Tool baru | Menggantikan |
|----------|----------|
| `wiki` (hanya baca) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

Lebih sedikit tool = performa model yang lebih baik. Ini adalah pola yang konsisten dalam desain server MCP — kumpulan tool yang lebih kecil dan lebih fokus bekerja lebih baik karena model tidak perlu memilih di antara lima tool yang hampir sama.

## Eksperimental: MCP Apps

Ini tambahan yang paling menarik, dan jelas masih eksperimental. MCP Apps adalah workflow yang dibungkus dan berjalan di lingkungan server MCP:

```json
{
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "mcp-server-azuredevops",
      "args": ["contoso", "-d", "core", "work", "work-items", "mcp-apps"]
    }
  }
}
```

Contoh pertamanya adalah `mcp_app_my_work_item` — pengalaman work item mandiri yang memungkinkan Anda melihat, memfilter, dan mengedit work item yang ditugaskan kepada Anda tanpa harus merangkai banyak pemanggilan tool secara manual.

Idenya menarik: alih-alih agen Anda memanggil `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` dalam beberapa putaran, satu MCP App menyediakan seluruh workflow sebagai unit yang terstruktur dan dapat digunakan ulang. Waktu setup lebih singkat, perilaku konsisten, dan lebih sedikit komponen yang harus diatur.

## Penutup

Azure DevOps MCP Server berkembang dengan cepat. Dukungan WIQL dan autentikasi PAT adalah kemenangan langsung bagi siapa pun yang memakai Copilot dengan Azure Boards. Pekerjaan anotasi membuat remote server lebih aman untuk skenario agentic. Dan MCP Apps, meski masih eksperimental, menunjukkan arah ke depan: dari tool mentah ke workflow yang dapat dikomposisi.

Ada baiknya memantau [dokumentasi](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) saat remote server terus berkembang.

Posting asli oleh Dan Hellem: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).