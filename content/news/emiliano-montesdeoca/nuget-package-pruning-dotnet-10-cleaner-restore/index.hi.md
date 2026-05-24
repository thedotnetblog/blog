---
title: "NuGet package pruning in .NET 10 उस तरह का सुधार है जिसे आप हर जगह महसूस करते हैं"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10 में नया NuGet package pruning false-positive vulnerability reports को कम करता है, restore graph को सरल बनाता है, और restore performance को बेहतर करता है। यह उन platform changes में से एक है जो quietly daily work को बेहतर बनाती हैं।"
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *यह लेख स्वचालित रूप से अनुवादित किया गया है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

कुछ platform improvements इसलिए रोमांचक होते हैं क्योंकि वे नए scenarios खोलते हैं।

और कुछ इसलिए रोमांचक होते हैं क्योंकि वे मौजूदा workflows को कम noisy, कम fragile, और कम annoying बनाते हैं।

**.NET 10 में NuGet package pruning** साफ़ तौर पर दूसरी category में आता है, और यह मैं एक compliment के रूप में कह रहा हूँ।

## यह क्यों मायने रखता है

अगर आपने कभी transitive vulnerability noise, unnecessarily large restore graphs, या ऐसे packages से निपटा है जो तकनीकी रूप से मौजूद हैं लेकिन आपके app के runtime के लिए वास्तव में relevant नहीं हैं, तो यह बदलाव एक real pain point को छूता है।

Pruning मदद करता है platform-provided packages को effective dependency graph से हटाकर, जब runtime उन्हें पहले से ही प्रदान कर रहा होता है।

इसका मतलब है:

- fewer false-positive vulnerability reports
- cleaner transitive dependency graphs
- less restore overhead
- more actionable audit results

## मेरी राय

यही वह तरह का .NET improvement है जिसे मैं पसंद करता हूँ।

यह defaults को बेहतर बनाता है, mental overhead को कम करता है, और security signal quality और day-to-day tooling behavior दोनों को सुधारता है।

यह एक win है, भले ही यह कभी keynote slide तक न पहुँचे।

Original post: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
