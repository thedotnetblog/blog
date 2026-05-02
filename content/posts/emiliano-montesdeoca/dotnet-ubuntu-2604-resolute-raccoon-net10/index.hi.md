---
title: ".NET 10 Ubuntu 26.04 LTS के साथ आया — क्या नया है"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) .NET 10 को फर्स्ट-क्लास टूलचेन के रूप में लेकर आया। Native AOT, Chiseled कंटेनर, Linux 7.0।"
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

Ubuntu LTS का दिन है। [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) आज लॉन्च हुआ, और हर Ubuntu LTS की तरह, यह नवीनतम .NET LTS — इस मामले में [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) — के साथ आया है।

## .NET 10 दो commands में install करें

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## Containers: `-noble` को `-resolute` में बदलें

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: 3ms startup, 1.4MB binary

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# 1.4MB native binary, 3ms startup
```

Cloud-native workloads के लिए जहाँ cold-start time मायने रखता है — Functions, containers, serverless — यह एक असली game changer है।

## .NET 8 या 9 चाहिए?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[पूरी पोस्ट](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) में cgroup v2, post-quantum cryptography और Linux 7.0 के बारे में अधिक जानकारी है।
