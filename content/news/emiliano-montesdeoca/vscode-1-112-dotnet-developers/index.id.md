---
title: "VS Code 1.112: Apa yang Benar-benar Perlu Diperhatikan Developer .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 baru saja rilis dan penuh dengan peningkatan agen, debugger browser terintegrasi, sandboxing MCP, dan dukungan monorepo. Inilah yang sebenarnya penting jika kamu membangun dengan .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "vscode-1-112-dotnet-developers" >}}).*

VS Code 1.112 baru saja mendarat, dan jujur saja? Yang satu ini terasa berbeda jika kamu menghabiskan hari-harimu di dunia .NET. Ada banyak hal di [catatan rilis resmi](https://code.visualstudio.com/updates/v1_112), tapi biarkan aku menghemat scrolling dan fokus pada apa yang sebenarnya penting bagi kita.

## Copilot CLI menjadi jauh lebih berguna

Tema besar rilis ini adalah **otonomi agen** — memberi Copilot lebih banyak ruang untuk bekerja tanpa kamu mengawasi setiap langkah.

### Steering pesan dan antrian

Kamu tahu momen saat Copilot CLI sedang di tengah-tengah tugas dan kamu menyadari lupa menyebutkan sesuatu? Sebelumnya, kamu harus menunggu. Sekarang kamu bisa mengirim pesan saat permintaan masih berjalan — baik untuk mengarahkan respons saat ini atau mengantri instruksi tindak lanjut.

### Tingkat izin

Ini yang paling bikin saya antusias. Sesi Copilot CLI sekarang mendukung tiga tingkat izin:

- **Default Permissions** — alur biasa di mana alat meminta konfirmasi sebelum berjalan
- **Bypass Approvals** — menyetujui segalanya secara otomatis dan mencoba ulang saat kesalahan
- **Autopilot** — berjalan sepenuhnya otonom: menyetujui alat, menjawab pertanyaannya sendiri, dan terus berjalan sampai tugas selesai

Kamu bisa mengaktifkan Autopilot dengan pengaturan `chat.autopilot.enabled`.

## Debug aplikasi web tanpa meninggalkan VS Code

Browser terintegrasi sekarang mendukung **debugging penuh**. Kamu bisa menetapkan breakpoint, melangkah melalui kode, dan memeriksa variabel — semua di dalam VS Code.

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Untuk developer Blazor, ini adalah perubahan besar.

## Sandboxing server MCP

Jika kamu menggunakan server MCP, sekarang kamu bisa mem-sandbox-nya:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

## Penemuan kustomisasi monorepo

Jika kamu bekerja di monorepo, dengan pengaturan `chat.useCustomizationsInParentRepositories`, VS Code berjalan naik ke root `.git` dan menemukan segalanya.

## /troubleshoot untuk debugging agen

Pernah menyiapkan instruksi atau skill kustom dan bertanya-tanya mengapa tidak terpilih? Aktifkan skill `/troubleshoot` baru dengan:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

## Kesimpulan

VS Code 1.112 jelas mendorong keras pengalaman agen — lebih banyak otonomi, debugging yang lebih baik, keamanan yang lebih ketat. [Unduh VS Code 1.112](https://code.visualstudio.com/updates/v1_112) atau perbarui dari dalam VS Code melalui **Help > Check for Updates**.
