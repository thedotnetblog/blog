---
title: "Patch This Now: .NET 10.0.7 OOB Security Update for ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 is an out-of-band release fixing a security vulnerability in Microsoft.AspNetCore.DataProtection — the managed authenticated encryptor was computing HMAC over the wrong bytes, leading to potential elevation of privilege. Update immediately."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

This one is not optional. If your application uses `Microsoft.AspNetCore.DataProtection`, you need to update to 10.0.7.

## What Happened

After the Patch Tuesday `.NET 10.0.6` release, some users started reporting that decryption was failing in their applications. The issue was filed as [aspnetcore#66335](https://github.com/dotnet/aspnetcore/issues/66335).

While investigating that regression, the team discovered it also exposed a security vulnerability: **CVE-2026-40372**.

In versions `10.0.0` through `10.0.6` of `Microsoft.AspNetCore.DataProtection`, the managed authenticated encryptor had a bug where it computed its HMAC validation tag over the **wrong bytes** of the payload and then discarded the computed hash. This could result in elevation of privilege.

In plain terms: the integrity check wasn't doing what it was supposed to do. Data Protection uses authenticated encryption to prevent tampering — the HMAC is the "has this been modified?" check. If the HMAC is computed over the wrong data, you lose that guarantee.

## Who Is Affected

Any .NET 10 application using `Microsoft.AspNetCore.DataProtection` — versions 10.0.0 through 10.0.6. The good news is this package is specific to .NET 10. If you're still on .NET 8 or 9, you're not affected by this specific CVE.

Common use cases for Data Protection: cookie encryption, antiforgery tokens, temp data in MVC, and any other use of `IDataProtector` in your application.

## How to Fix It

Update the `Microsoft.AspNetCore.DataProtection` NuGet package to **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Or update your SDK/runtime: [download .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

Verify you're on the right version:

```bash
dotnet --info
```

Then **rebuild and redeploy** your application. The fix doesn't take effect until you're running the updated package.

## The Bigger Picture

Out-of-band security releases are uncommon — they happen when a vulnerability is serious enough that it can't wait for the next scheduled Patch Tuesday. This one is a direct consequence of a regression in 10.0.6 creating a security gap. The fact that it was discovered through bug reports is a good sign that the process worked. The fix is fast and the scope is narrow.

If you're running .NET 10 in production with any web application framework, this is a same-day update situation.

Original announcement by Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
