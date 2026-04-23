---
title: "Patch dit nu: .NET 10.0.7 OOB-beveiligingsupdate voor ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 is een out-of-band release die een beveiligingslek in Microsoft.AspNetCore.DataProtection verhelpt — de beheerde geauthenticeerde encryptor berekende HMAC over de verkeerde bytes, wat tot privilege escalation kon leiden. Werk direct bij."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Deze update is niet optioneel. Als je applicatie `Microsoft.AspNetCore.DataProtection` gebruikt, moet je upgraden naar 10.0.7.

## Wat Er Is Gebeurd

Na de Patch Tuesday-release van `.NET 10.0.6` begonnen sommige gebruikers te melden dat decryptie mislukte in hun applicaties. Tijdens het onderzoek naar die regressie ontdekte het team ook een beveiligingslek: **CVE-2026-40372**.

In versies `10.0.0` tot en met `10.0.6` van `Microsoft.AspNetCore.DataProtection` berekende de beheerde geauthenticeerde encryptor zijn HMAC-validatietag over de **verkeerde bytes** van de payload en gooide daarna de berekende hash weg. Dat kon leiden tot privilege escalation.

Eenvoudig gezegd: de integriteitscontrole deed niet wat hij moest doen. Data Protection gebruikt geauthenticeerde versleuteling om manipulatie te voorkomen — HMAC is de controle "is dit gewijzigd?". Als HMAC over de verkeerde data wordt berekend, ben je die garantie kwijt.

## Wie Wordt Getroffen

Elke .NET 10-applicatie die `Microsoft.AspNetCore.DataProtection` gebruikt — versies 10.0.0 tot en met 10.0.6. Het goede nieuws is dat dit pakket specifiek is voor .NET 10. Als je nog op .NET 8 of 9 zit, word je niet getroffen door deze specifieke CVE.

Typische use-cases voor Data Protection: cookie-encryptie, antiforgery-tokens, temp data in MVC en elk ander gebruik van `IDataProtector` in je applicatie.

## Hoe Los Je Het Op

Werk het NuGet-pakket `Microsoft.AspNetCore.DataProtection` bij naar **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Of update je SDK/runtime: [download .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

Controleer dat je op de juiste versie zit:

```bash
dotnet --info
```

Daarna **bouw en rol je applicatie opnieuw uit**. De fix is pas actief wanneer je de bijgewerkte package daadwerkelijk draait.

## Het Grotere Plaatje

Out-of-band beveiligingsreleases zijn zeldzaam — ze komen alleen wanneer een kwetsbaarheid ernstig genoeg is om niet te wachten op de volgende Patch Tuesday. Dit was een direct gevolg van een regressie in 10.0.6 die een beveiligingslek creëerde. Dat het probleem via bugrapporten werd ontdekt, is een goed teken: het proces werkte. De fix is snel en de impact is klein.

Als je .NET 10 in productie draait met een webframework, dan is dit een update voor dezelfde dag.

Oorspronkelijke aankondiging door Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).