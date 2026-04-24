---
title: "Pedaça això ara: actualització de seguretat OOB de .NET 10.0.7 per a ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 és una versió fora de banda que corregeix una vulnerabilitat de seguretat a Microsoft.AspNetCore.DataProtection — l'encriptador autenticat gestionat calculava l'HMAC sobre bytes incorrectes, cosa que podia provocar una escalada de privilegis. Actualitza immediatament."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Aquesta actualització no és opcional. Si la teva aplicació fa servir `Microsoft.AspNetCore.DataProtection`, has d'actualitzar a 10.0.7.

## Què Va Passar

Després del Patch Tuesday de `.NET 10.0.6`, alguns usuaris van començar a informar que el desxifrat fallava a les seves aplicacions. Mentre investigava aquesta regressió, l'equip també va descobrir una vulnerabilitat de seguretat: **CVE-2026-40372**.

A les versions `10.0.0` fins a `10.0.6` de `Microsoft.AspNetCore.DataProtection`, l'encriptador autenticat gestionat calculava el seu tag de validació HMAC sobre els **bytes equivocats** de la càrrega útil i després descartava l'hash calculat. Això podia provocar una escalada de privilegis.

Dit d'una altra manera: la comprovació d'integritat no feia el que havia de fer. Data Protection usa xifrat autenticat per evitar manipulacions — l'HMAC és la comprovació de "s'ha modificat això?". Si l'HMAC es calcula sobre dades errònies, perds aquesta garantia.

## Qui Se'n Veu Afectat

Qualsevol aplicació .NET 10 que faci servir `Microsoft.AspNetCore.DataProtection` — versions 10.0.0 fins a 10.0.6. La bona notícia és que aquest paquet és específic de .NET 10. Si encara ets a .NET 8 o 9, aquesta CVE concreta no t'afecta.

Usos habituals de Data Protection: xifrat de cookies, tokens antiforgery, dades temporals en MVC i qualsevol altre ús de `IDataProtector` a la teva aplicació.

## Com Solucionar-ho

Actualitza el paquet NuGet `Microsoft.AspNetCore.DataProtection` a **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

O actualitza el teu SDK/runtime: [descarrega .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

Verifica que ets a la versió correcta:

```bash
dotnet --info
```

Després **torna a compilar i desplega** la teva aplicació. La correcció no s'aplica fins que estàs executant el paquet actualitzat.

## El Quadre General

Les versions de seguretat fora de banda són poc habituals — passen quan la vulnerabilitat és prou greu per no poder esperar al següent Patch Tuesday. Aquesta va ser una conseqüència directa d'una regressió a 10.0.6 que va obrir una bretxa de seguretat. El fet que s'hagi descobert a partir d'informes d'errors és una bona senyal. La solució és ràpida i l'abast és reduït.

Si estàs executant .NET 10 en producció amb qualsevol framework d'aplicacions web, aquesta és una actualització per fer el mateix dia.

Anunci original de Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).