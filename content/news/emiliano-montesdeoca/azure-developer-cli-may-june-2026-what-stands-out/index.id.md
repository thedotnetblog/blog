---
title: "Azure Developer CLI terus menjadi alat inner loop yang lebih baik"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "Rilis Azure Developer CLI pada Mei dan Juni 2026 memang menambahkan banyak hal, tetapi nilai terbesarnya adalah bagaimana semuanya memperbaiki siklus harian: pengelolaan tool yang lebih baik, provisioning yang lebih aman, dukungan extension yang lebih kuat, dan alur eksekusi yang lebih praktis."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Artikel ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Roundup CLI bulanan bisa melelahkan untuk dibaca karena mencampur perbaikan workflow besar dan perbaikan kecil dalam satu dinding teks.

Jadi ini versi singkat saya: pembaruan terbaru **Azure Developer CLI** penting karena `azd` terus menjadi **alat inner loop yang lebih baik**, bukan hanya pembungkus deployment.

Itu pergeseran yang paling penting.

## Pengelolaan tool mulai menjadi bagian dari produk, bukan tugas sampingan

Salah satu tambahan favorit saya adalah perintah `azd tool` yang baru.

Apa pun yang mengurangi friksi setup layak diperhatikan, terutama dalam project di mana lingkungan kerja bergantung pada campuran SDK, CLI, Docker, Bicep, dan extension.

Jika tool sekarang dapat membantu menemukan, menginstal, memeriksa, dan meningkatkan dependency itu secara langsung, maka banyak mode kegagalan yang menyebalkan bisa dihilangkan, terutama yang paling sering mengenai pendatang baru.

Itu nilai yang nyata.

## `azd exec` juga terdengar lebih penting daripada namanya

Sekilas, `azd exec` bisa tampak seperti fitur kenyamanan kecil.

Saya tidak setuju.

Menjalankan perintah dengan konteks environment `azd` penuh, termasuk resolusi secret, adalah jenis kemampuan yang membuat otomasi lokal dan scripting jauh lebih rapi.

Itu mengurangi kebutuhan akan script glue tambahan dan membantu menjaga eksekusi tetap konsisten di berbagai environment.

Itu kemenangan praktis.

## Provisioning yang lebih aman dan perilaku cancellation yang lebih baik adalah peningkatan yang kurang dihargai

Rilis ini juga menyertakan perubahan pada dependency provisioning, penanganan cancellation, dan perilaku deployment, hal-hal yang mungkin tidak terlihat glamor tetapi sangat disambut baik.

Prompt cancel interaktif, pemodelan dependency yang lebih baik, dan status deployment yang lebih jelas adalah jenis perbaikan yang membuat CLI terasa andal saat bekerja dengan resource Azure sungguhan.

Dan trust adalah masalah besar untuk tool seperti ini.

## Pandangan saya

Semakin `azd` membaik dalam setup, scripting, keamanan deployment, dan dukungan extension, semakin terasa seperti sesuatu yang bisa Anda pertahankan di siklus harian, bukan hanya disentuh tepat sebelum deployment.

Itulah arah yang tepat.

Untuk tim yang membangun aplikasi cloud-native atau berbasis AI di Azure, ini membuat CLI lebih berguna di tempat yang paling penting: selama development yang sebenarnya.

Tulisan asli: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)