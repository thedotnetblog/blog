---
title: "Zastosuj poprawkę teraz: aktualizacja bezpieczeństwa OOB .NET 10.0.7 dla ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 to wydanie poza harmonogramem, które naprawia lukę bezpieczeństwa w Microsoft.AspNetCore.DataProtection — zarządzany uwierzytelniony szyfrator obliczał HMAC na niewłaściwych bajtach, co mogło prowadzić do eskalacji uprawnień. Zaktualizuj natychmiast."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Ten post został automatycznie przetłumaczony. Aby zobaczyć oryginalną wersję, [kliknij tutaj](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Ta aktualizacja nie jest opcjonalna. Jeśli twoja aplikacja używa `Microsoft.AspNetCore.DataProtection`, musisz zaktualizować do wersji 10.0.7.

## Co Się Stało

Po wydaniu `.NET 10.0.6` w ramach Patch Tuesday część użytkowników zaczęła zgłaszać, że deszyfrowanie przestaje działać w ich aplikacjach. Podczas badania tej regresji zespół odkrył również lukę bezpieczeństwa: **CVE-2026-40372**.

W wersjach `10.0.0` do `10.0.6` `Microsoft.AspNetCore.DataProtection` zarządzany uwierzytelniony szyfrator obliczał znacznik walidacji HMAC na **niewłaściwych bajtach** ładunku, a następnie odrzucał obliczony hash. Mogło to prowadzić do eskalacji uprawnień.

Mówiąc prościej: kontrola integralności nie robiła tego, co powinna. Data Protection używa szyfrowania uwierzytelnionego, aby zapobiegać manipulacji — HMAC to sprawdzenie „czy to zostało zmienione?”. Jeśli HMAC jest liczony na złych danych, tracisz tę gwarancję.

## Kogo To Dotyczy

Każdej aplikacji .NET 10 używającej `Microsoft.AspNetCore.DataProtection` — wersji od 10.0.0 do 10.0.6. Dobra wiadomość jest taka, że ten pakiet jest specyficzny dla .NET 10. Jeśli nadal jesteś na .NET 8 lub 9, ta konkretna CVE cię nie dotyczy.

Typowe zastosowania Data Protection to: szyfrowanie ciasteczek, tokeny antiforgery, dane tymczasowe w MVC oraz każdy inny użytek `IDataProtector` w twojej aplikacji.

## Jak To Naprawić

Zaktualizuj pakiet NuGet `Microsoft.AspNetCore.DataProtection` do **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Albo zaktualizuj swój SDK/runtime: [pobierz .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

Sprawdź, czy jesteś na właściwej wersji:

```bash
dotnet --info
```

Następnie **przebuduj i wdroż ponownie** swoją aplikację. Poprawka nie zacznie działać, dopóki nie uruchamiasz zaktualizowanego pakietu.

## Szerszy Obraz

Wydania bezpieczeństwa poza harmonogramem są rzadkie — pojawiają się tylko wtedy, gdy luka jest na tyle poważna, że nie może czekać do następnego Patch Tuesday. Ta była bezpośrednim skutkiem regresji w 10.0.6, która stworzyła lukę bezpieczeństwa. To, że wykryto ją dzięki zgłoszeniom błędów, jest dobrym znakiem: proces zadziałał. Poprawka jest szybka, a zakres ograniczony.

Jeśli uruchamiasz .NET 10 w produkcji z jakimkolwiek frameworkiem aplikacji webowych, to jest aktualizacja na ten sam dzień.

Oryginalne ogłoszenie Rahula Bhandariego: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).