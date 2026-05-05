---
title: "立即打补丁：.NET 10.0.7 OOB安全更新 (ASP.NET Core Data Protection)"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7是修复Microsoft.AspNetCore.DataProtection中安全漏洞的带外发布——管理的认证加密器在错误的字节上计算HMAC，可能导致权限提升。"
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*本文已自动翻译。要查看原始版本，请[点击这里](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/)。*

此更新不是可选的。如果您的应用程序使用`Microsoft.AspNetCore.DataProtection`，您需要更新到10.0.7。

## 发生了什么

Patch Tuesday `.NET 10.0.6`发布后，一些用户报告解密失败。调查过程中，团队发现了安全漏洞**CVE-2026-40372**：HMAC验证标签在payload的**错误字节**上计算，可能导致权限提升。

## 如何修复

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

然后**重新构建和重新部署**您的应用程序。

Rahul Bhandari的原始公告：[.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/)。
