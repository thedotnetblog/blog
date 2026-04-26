---
title: "अभी पैच करें: ASP.NET Core Data Protection के लिए .NET 10.0.7 OOB सुरक्षा अपडेट"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 एक out-of-band रिलीज़ है जो Microsoft.AspNetCore.DataProtection में एक सुरक्षा भेद्यता को ठीक करती है — managed authenticated encryptor गलत bytes पर HMAC बना रहा था, जिससे privilege escalation हो सकती थी. तुरंत अपडेट करें."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल संस्करण के लिए, [यहाँ क्लिक करें](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

यह वैकल्पिक नहीं है। यदि आपका application `Microsoft.AspNetCore.DataProtection` का उपयोग करता है, तो आपको 10.0.7 पर अपडेट करना होगा।

## क्या हुआ

Patch Tuesday के बाद जारी `.NET 10.0.6` रिलीज़ के बाद, कुछ users ने रिपोर्ट करना शुरू किया कि उनके applications में decryption fail हो रहा था। इस regression की जांच करते समय टीम को एक security vulnerability भी मिली: **CVE-2026-40372**।

`10.0.0` से `10.0.6` तक के versions में, managed authenticated encryptor ने अपने HMAC validation tag को payload के **गलत bytes** पर calculate किया, और फिर computed hash को discard कर दिया। इससे privilege escalation हो सकती थी।

साधारण शब्दों में: integrity check वही नहीं कर रहा था जो उसे करना चाहिए था। Data Protection tampering रोकने के लिए authenticated encryption use करता है — HMAC "क्या इसे modify किया गया है?" वाला check है। अगर HMAC गलत data पर calculate होता है, तो वह guarantee खो जाती है।

## कौन प्रभावित है

कोई भी .NET 10 application जो `Microsoft.AspNetCore.DataProtection` use करती है — versions 10.0.0 से 10.0.6 तक। अच्छी खबर यह है कि यह package सिर्फ .NET 10 के लिए है। यदि आप अभी भी .NET 8 या 9 पर हैं, तो आप इस specific CVE से प्रभावित नहीं हैं।

Data Protection के common use cases: cookie encryption, antiforgery tokens, MVC में temp data, और आपके application में `IDataProtector` का कोई भी अन्य उपयोग।

## इसे कैसे ठीक करें

`Microsoft.AspNetCore.DataProtection` NuGet package को **10.0.7** पर update करें:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

या अपना SDK/runtime update करें: [डाउनलोड करें .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

सुनिश्चित करें कि आप सही version पर हैं:

```bash
dotnet --info
```

फिर **अपने application को rebuild और redeploy** करें। Fix तब तक लागू नहीं होगा जब तक updated package चल नहीं रहा हो।

## बड़ी तस्वीर

Out-of-band security releases कम ही आते हैं — वे तब जारी होते हैं जब vulnerability इतनी गंभीर हो कि अगला Patch Tuesday इंतज़ार न कर सके। यह मामला 10.0.6 में हुई regression का सीधा परिणाम था जिसने security gap बना दिया। यह कि इसे bug reports के जरिए खोजा गया, अच्छा संकेत है — process ने काम किया। Fix तेज़ है और scope सीमित है।

यदि आप production में किसी web application framework के साथ .NET 10 चला रहे हैं, तो यह same-day update है।

मूल घोषणा राहुल भंडारी द्वारा: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).