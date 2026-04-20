---
title: ".NET Kwiecień 2026 Serwisowanie — Poprawki Bezpieczeństwa, Które Powinieneś Zastosować Dziś"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Wydanie serwisowe z kwietnia 2026 roku łata 6 CVE w .NET 10, .NET 9, .NET 8 i .NET Framework — w tym dwie luki zdalnego wykonania kodu."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

[Aktualizacje serwisowe z kwietnia 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) dla .NET i .NET Framework są dostępne, i ta zawiera poprawki bezpieczeństwa, które będziesz chciał zastosować wkrótce. Sześć CVE załatanych, w tym dwie luki zdalnego wykonania kodu (RCE).

## Co zostało załatane

| CVE | Typ | Dotyczy |
|-----|-----|---------|
| CVE-2026-26171 | Obejście funkcji bezpieczeństwa | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Zdalne wykonanie kodu** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Zdalne wykonanie kodu** | .NET 10, 9, 8 |
| CVE-2026-32203 | Odmowa usługi | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Odmowa usługi | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Odmowa usługi | .NET Framework 2.0–4.8.1 |

## Zaktualizowane wersje

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

## Co zrobić

Zaktualizuj swoje projekty i pipeline'y CI/CD do najnowszych wersji. Dwie luki RCE to nie jest coś, co się odkłada.
