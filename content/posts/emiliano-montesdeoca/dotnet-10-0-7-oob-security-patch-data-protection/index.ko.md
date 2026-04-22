---
title: "지금 바로 패치하세요: .NET 10.0.7 OOB 보안 업데이트 (ASP.NET Core Data Protection)"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7은 Microsoft.AspNetCore.DataProtection의 보안 취약점을 수정하는 비정기 릴리스 — 관리된 인증 암호화기가 잘못된 바이트에서 HMAC을 계산하여 권한 상승이 발생할 수 있었습니다."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*이 게시물은 자동 번역되었습니다. 원본 버전은 [여기를 클릭](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/)하세요.*

이 업데이트는 선택 사항이 아닙니다. 애플리케이션이 `Microsoft.AspNetCore.DataProtection`을 사용한다면 10.0.7로 업데이트해야 합니다.

## 무슨 일이 있었나요

Patch Tuesday `.NET 10.0.6` 릴리스 후 일부 사용자가 복호화 실패를 보고했습니다. 조사 중 **CVE-2026-40372**가 발견되었습니다: HMAC 검증 태그가 **잘못된 바이트**에서 계산되어 권한 상승으로 이어질 수 있었습니다.

## 수정 방법

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

그런 다음 애플리케이션을 **재빌드하고 재배포**하세요.

Rahul Bhandari의 원본 발표: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
