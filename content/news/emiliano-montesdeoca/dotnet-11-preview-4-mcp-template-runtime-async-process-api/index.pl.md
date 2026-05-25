---
title: ".NET 11 Preview 4: Szablon Serwera MCP, Biblioteki Runtime-Async, API Procesów"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 jest dostępny. Najważniejsze: szablon serwera MCP w SDK, biblioteki runtime skompilowane z runtime-async, dotnet watch dla urządzeń mobilnych i duże rozszerzenie API Procesów."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 jest dostępny. Każde wydanie głównej wersji zapoznawczej .NET dodaje długą listę elementów obejmujących runtime, SDK, biblioteki, ASP.NET Core, MAUI, C# i Entity Framework. Zamiast powtarzać pełną listę, oto rzeczy, które przykuły moją uwagę.

## Szablon Serwera MCP w SDK .NET

Najciekawszy element: szablon projektu serwera MCP jest teraz zawarty w SDK. Oznacza to, że `dotnet new mcp-server` (lub jak ostatecznie będzie nazywać się polecenie) działa od razu. Dla każdego, kto buduje narzędzia MCP w .NET, znacznie redukuje to początkowe trudności. Integracja MCP w łańcuchu narzędzi platformy wskazuje kierunek, w którym zmierza ekosystem.

## Biblioteki Runtime Skompilowane z Runtime-Async

Sam runtime teraz kompiluje swoje biblioteki standardowe przy użyciu funkcji runtime-async. To wewnętrzna zmiana wpływająca na wydajność — maszyny stanów async w runtime stają się bardziej wydajne. Znaczenie tutaj nie leży w widocznych zmianach API; chodzi o to, że runtime-async jest wystarczająco dojrzały, żeby być używanym w samej BCL, co jest ważnym sygnałem dotyczącym gotowości tej funkcji.

## Optymalizacje JIT i Wewnętrzne Funkcje Sprzętowe

Preview 4 kontynuuje prace nad JIT. Ulepszenia wewnętrznych funkcji sprzętowych i generowania kodu trafiają tutaj — szczegóły można znaleźć w informacjach o wydaniu runtime. Tego rodzaju zmiany zazwyczaj poprawiają przepustowość w intensywnych pętlach obliczeniowych bez żadnych zmian w kodzie z twojej strony.

## Rozszerzenie API Procesów

Duże aktualizacje `System.Diagnostics.Process` pojawiają się w Preview 4:

- `Process.RunAndCaptureTextAsync` — uruchom proces, przechwytuj stdout/stderr, poczekaj na zakończenie, wszystko w jednym wywołaniu bez ryzyka deadlocka
- `KillOnParentExit` — lekkie powiązanie cyklu życia między procesem nadrzędnym a podrzędnym
- API oparte na `SafeProcessHandle`, bardziej przyjazne dla trimmera

Jeśli kiedykolwiek pisałeś powtarzający się kod do przechwytywania danych wyjściowych procesu bez powodowania deadlocków (asynchroniczne odczytywanie zarówno z stdout *jak i* stderr jednocześnie), `RunAndCaptureTextAsync` jest właśnie tym API, którego brakowało.

## dotnet watch dla Android i iOS

`dotnet watch` teraz obsługuje wybór urządzenia dla projektów .NET MAUI Android i iOS. Szybsza iteracja na urządzeniach mobilnych bez ręcznego zarządzania połączeniami urządzeń w pętli kompilacji.

## Oparte na Span API Kompresji

Nowe API kodera/dekodera Deflate, ZLib i GZip oparte na span trafiają do bibliotek. Mniej alokacji przy pracy ze skompresowanymi danymi — istotne w przypadku przetwarzania danych o wysokiej przepustowości.

## Wypróbuj

[Pobierz .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — to wersja zapoznawcza, niegotowa na produkcję, ale warto uruchomić ją na swoich projektach, żeby wykryć problemy wcześnie przed cyklem RC.

Oryginalny post: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
