---
title: "Agentic Platform Engineering Menjadi Nyata — Git-APE Menunjukkan Caranya"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Proyek Git-APE Microsoft mempraktikkan agentic platform engineering — menggunakan agen GitHub Copilot dan Azure MCP untuk mengubah permintaan bahasa alami menjadi infrastruktur cloud yang tervalidasi."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform engineering telah menjadi salah satu istilah yang terdengar hebat di konferensi tetapi biasanya berarti "kami membangun portal internal dan wrapper Terraform." Janji sebenarnya — self-service infrastruktur yang benar-benar aman, terkendali, dan cepat — selalu beberapa langkah menjauh.

Tim Azure baru saja menerbitkan [Bagian 2 dari seri agentic platform engineering mereka](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/). Mereka menyebutnya **Git-APE** — sebuah proyek open-source yang menggunakan agen GitHub Copilot dan server Azure MCP untuk mengubah permintaan bahasa alami menjadi infrastruktur yang tervalidasi dan ter-deploy.

## Apa yang sebenarnya dilakukan Git-APE

Ide inti: alih-alih mempelajari modul Terraform, developer berbicara dengan agen Copilot. Agen menginterpretasikan niat, menghasilkan Infrastructure-as-Code, memvalidasi terhadap kebijakan, dan mendeploy — semuanya dalam VS Code.

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Buka workspace di VS Code, dan file konfigurasi agen ditemukan otomatis oleh GitHub Copilot:

```
@git-ape deploy a function app with storage in West Europe
```

Pembersihan sama mudahnya:

```
@git-ape destroy my-resource-group
```

## Mengapa ini penting

Bagi yang membangun di Azure, ini menggeser percakapan platform engineering dari "bagaimana kami membangun portal" menjadi "bagaimana kami mendeskripsikan guardrail kami sebagai API."

Sebagai developer .NET: Azure MCP Server dan agen GitHub Copilot bekerja dengan semua workload Azure — ASP.NET Core API Anda, tumpukan .NET Aspire — semuanya bisa menjadi target alur deployment agentik.

## Kesimpulan

Git-APE adalah pandangan awal tetapi konkret tentang agentic platform engineering dalam praktik. Clone [repositorinya](https://github.com/Azure/git-ape) dan baca [postingan lengkap](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/).
