---
title: "Patcher Immédiatement : Mise à Jour de Sécurité OOB .NET 10.0.7 pour ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 est une version hors-bande corrigeant une vulnérabilité de sécurité dans Microsoft.AspNetCore.DataProtection — l'encrypteur calculait HMAC sur les mauvais octets, pouvant mener à une élévation de privilèges."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Cette mise à jour n'est pas optionnelle. Si votre application utilise `Microsoft.AspNetCore.DataProtection`, vous devez mettre à jour vers 10.0.7.

## Ce Qui S'est Passé

Après la version Patch Tuesday `.NET 10.0.6`, certains utilisateurs ont signalé des échecs de déchiffrement. En enquêtant, l'équipe a découvert **CVE-2026-40372** : le tag HMAC était calculé sur les **mauvais octets**, pouvant mener à une élévation de privilèges.

## Comment Corriger

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Puis **reconstruire et redéployer**.

Annonce originale de Rahul Bhandari : [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
