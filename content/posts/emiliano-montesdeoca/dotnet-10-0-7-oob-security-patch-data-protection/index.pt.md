---
title: "Atualize Agora: .NET 10.0.7 Atualização de Segurança OOB para ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 é um lançamento fora de banda corrigindo uma vulnerabilidade de segurança no Microsoft.AspNetCore.DataProtection — o encriptador computava HMAC sobre bytes errados, podendo levar a elevação de privilégios."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Esta postagem foi traduzida automaticamente. Para a versão original, [clique aqui](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Esta atualização não é opcional. Se sua aplicação usa `Microsoft.AspNetCore.DataProtection`, você precisa atualizar para 10.0.7.

## O Que Aconteceu

Após o lançamento Patch Tuesday `.NET 10.0.6`, usuários reportaram falhas na descriptografia. Durante a investigação, a equipe descobriu o **CVE-2026-40372**: o tag de validação HMAC era calculado sobre os **bytes errados**, podendo resultar em elevação de privilégios.

## Como Corrigir

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Depois **reconstrua e reimplante** sua aplicação.

Anúncio original de Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
