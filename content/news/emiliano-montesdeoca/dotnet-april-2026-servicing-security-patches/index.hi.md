---
title: ".NET April 2026 Servicing — Security Patches जो आपको आज Apply करने चाहिए"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "April 2026 servicing release, .NET 10, .NET 9, .NET 8 और .NET Framework में 6 CVEs patch करती है — जिसमें दो remote code execution vulnerabilities शामिल हैं।"
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

.NET और .NET Framework के लिए [April 2026 servicing updates](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) आ गए हैं, और इसमें security fixes हैं जिन्हें आप जल्द apply करना चाहेंगे। छह CVEs patch किए गए हैं, जिनमें दो remote code execution (RCE) vulnerabilities शामिल हैं।

## क्या Patch किया गया है

यहाँ quick summary है:

| CVE | प्रकार | प्रभावित करता है |
|-----|------|---------|
| CVE-2026-26171 | Security Feature Bypass | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Remote Code Execution** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Remote Code Execution** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denial of Service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denial of Service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denial of Service | .NET Framework 2.0–4.8.1 |

दोनों RCE CVEs (CVE-2026-32178 और CVE-2026-33116) .NET versions की सबसे broad range को affect करते हैं और इन्हें priority देनी चाहिए।

## Updated Versions

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

सभी usual channels पर available हैं — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), MCR पर container images, और Linux package managers।

## क्या करें

अपने projects और CI/CD pipelines को latest patch versions पर update करें। अगर आप containers चला रहे हैं, तो latest images pull करें। अगर आप .NET Framework पर हैं, तो corresponding patches के लिए [.NET Framework release notes](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) देखें।

Production में .NET 10 चला रहे लोगों के लिए (यह current release है), 10.0.6 एक mandatory update है। वही .NET 9.0.15 और .NET 8.0.26 के लिए भी लागू होता है अगर आप उन LTS tracks पर हैं। दो RCE vulnerabilities ऐसी चीज़ नहीं हैं जिन्हें आप टालें।
