---
title: ".NET April 2026 Servicing — Security Patches जो आपको आज Apply करने चाहिए"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "April 2026 servicing release .NET 10, .NET 9, .NET 8, और .NET Framework में 6 CVEs patch करता है — दो remote code execution vulnerabilities सहित।"
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

.NET और .NET Framework के लिए [April 2026 servicing updates](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) out हैं, और इसमें security fixes हैं जो आप जल्द apply करना चाहेंगे। छह CVEs patched, दो remote code execution (RCE) vulnerabilities सहित।

## क्या patch किया गया है

| CVE | Type | Affects |
|-----|------|---------|
| CVE-2026-26171 | Security Feature Bypass | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Remote Code Execution** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Remote Code Execution** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denial of Service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denial of Service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denial of Service | .NET Framework 2.0–4.8.1 |

## Updated versions

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

## क्या करें

अपने projects और CI/CD pipelines को latest patch versions में update करें। दो RCE vulnerabilities वे नहीं हैं जिन्हें आप postpone करते हैं।
