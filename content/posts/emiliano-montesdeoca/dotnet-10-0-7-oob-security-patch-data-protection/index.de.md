---
title: "Jetzt patchen: .NET 10.0.7 OOB Sicherheitsupdate für ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 ist ein Out-of-Band Release, das eine Sicherheitslücke in Microsoft.AspNetCore.DataProtection behebt — der Encryptor berechnete HMAC über falsche Bytes, was zu Privilege Escalation führen konnte."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Dieses Update ist nicht optional. Wenn deine Anwendung `Microsoft.AspNetCore.DataProtection` verwendet, musst du auf 10.0.7 aktualisieren.

## Was Passiert Ist

Nach dem Patch Tuesday Release `.NET 10.0.6` berichteten einige Benutzer von Entschlüsselungsfehlern. Während der Untersuchung entdeckte das Team die Sicherheitslücke **CVE-2026-40372**: Der HMAC-Validierungs-Tag wurde über die **falschen Bytes** berechnet, was zu Privilege Escalation führen konnte.

## Wie Beheben

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Dann **neu bauen und deployen**.

Originalankündigung von Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
