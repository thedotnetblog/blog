---
title: ".NET 10 يأتي مع Ubuntu 26.04 LTS — ما الجديد"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "أُطلق Ubuntu 26.04 LTS (Resolute Raccoon) مع .NET 10 كسلسلة أدوات من الدرجة الأولى. Native AOT وحاويات Chiseled وLinux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*تمت ترجمة هذا المقال تلقائيًا. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

يوم Ubuntu LTS. أُطلق [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) اليوم مع [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

## ثبّت .NET 10 بأمرين

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## الحاويات: استبدل `-noble` بـ `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: بدء في 3ms، ثنائي بحجم 1.4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# ثنائي أصلي 1.4MB، بدء في 3ms
```

بالنسبة لأعباء العمل السحابية الأصلية حيث يهم وقت البدء الفعلي — Functions، الحاويات، serverless — هذا تغيير حقيقي في قواعد اللعبة.

## تحتاج .NET 8 أو 9؟

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

يتضمن [المقال الكامل](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) مزيدًا من التفاصيل.
