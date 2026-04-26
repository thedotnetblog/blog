---
title: "Azure SDK April 2026: AI Foundry 2.0 dan Hal yang Perlu Diketahui Developer .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Rilis Azure SDK April 2026 menghadirkan Azure.AI.Projects 2.0.0 stable dengan breaking changes penting, perbaikan keamanan kritis untuk Cosmos DB, dan gelombang library Provisioning baru untuk .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Rilis SDK bulanan sering mudah dilewatkan. Yang satu ini punya beberapa hal yang layak diperhatikan — terutama jika Anda membangun dengan AI Foundry, Cosmos DB di Java, atau melakukan provisioning infrastruktur dari kode .NET.

## Azure.AI.Projects 2.0.0 — Breaking changes yang masuk akal

Paket NuGet `Azure.AI.Projects` mencapai stable 2.0.0 dengan beberapa perubahan arsitektur yang signifikan. Jika Anda sudah memakai preview, inilah yang berubah:

- **Pemisahan namespace**: Evaluations pindah ke `Azure.AI.Projects.Evaluation`, dan operasi memory pindah ke `Azure.AI.Projects.Memory`. Anda perlu memperbarui `using` statements.
- **Tipe yang diganti nama**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Konvensi penamaan**: properti boolean sekarang konsisten mengikuti konvensi `Is*`

Ini jenis breaking changes yang terasa menyakitkan sekali lalu terasa benar selamanya. Jika Anda sudah membangun di atas preview, perbarui import dan biarkan compiler menunjukkan sisanya.

Kabar baiknya: sekarang ini stable. Anda bisa benar-benar mengandalkan API ini.

## Cosmos DB Java: perbaikan keamanan kritis (RCE)

Ini serius. Library Java Cosmos DB (`azure-cosmos`) versi 4.79.0 menyertakan perbaikan keamanan kritis untuk **Remote Code Execution vulnerability (CWE-502)**.

Masalahnya adalah Java deserialization di `CosmosClientMetadataCachesSnapshot`, `AsyncCache`, dan `DocumentCollection`. Perbaikannya mengganti Java deserialization dengan serialization berbasis JSON, sehingga menghapus seluruh kelas serangan deserialization.

Jika Anda punya layanan Java yang menggunakan Azure Cosmos DB, segera perbarui ke 4.79.0. Ini tidak opsional.

## Library Provisioning baru untuk .NET

Sejumlah library Provisioning stabil mencapai 1.0.0 bulan ini — inilah library yang memungkinkan Anda mendefinisikan infrastruktur Azure dalam kode C# alih-alih ARM template atau Bicep:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

Ada beberapa lagi di beta.1, mencakup API Management, Batch, Compute, Monitor, MySQL, dan Security Center. Jika Anda melakukan infrastructure-as-code dari .NET — terutama dengan deployment Aspire — library ini adalah titik awal Anda.

## Azure AI Agents Java: 2.0.0 GA

Library Java Azure AI Agents juga mencapai general availability bulan ini. Perubahan breaking utama:

- Beberapa tipe enum diubah menjadi kelas berbasis `ExpandableStringEnum` (lebih fleksibel untuk nilai baru)
- Kelas model `*Param` diganti nama menjadi `*Parameter`
- `MCPToolConnectorId` → `McpToolConnectorId` (konsistensi kapitalisasi)
- Overload kenyamanan baru untuk `beginUpdateMemories`

## Penutup

Sorotan utama untuk developer .NET bulan ini adalah `Azure.AI.Projects 2.0.0` yang menjadi stable — jika Anda membangun dengan AI Foundry, sekarang waktunya pin ke stable dan memperbarui import. Untuk tim Java yang memakai Cosmos DB, pembaruan keamanan ini mendesak.

Catatan rilis lengkap ada di [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases). Post asli: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).