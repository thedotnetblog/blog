---
title: ".NET 11 Preview 5: Co Faktycznie Wypróbowałbym Najpierw"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 dostarcza ulepszenia w SDK, środowisku wykonawczym, C#, ASP.NET Core i EF Core. Oto aktualizacje, które moim zdaniem najbardziej warto przetestować wcześnie, jeśli budujesz prawdziwe aplikacje .NET."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

Wpisy o podglądach .NET są zawsze pełne.

To dobra wiadomość dla platformy, ale oznacza też, że praktyczne pytanie zostaje pogrzebane: **co powinieneś faktycznie przetestować najpierw?**

.NET 11 Preview 5 przynosi dużo w SDK, środowisku wykonawczym, bibliotekach, ASP.NET Core, C#, MAUI i EF Core. Zamiast zamieniać to w gigantyczne podsumowanie dziennika zmian, chcę skupić się na częściach, które moim zdaniem zasługują na prawdziwą uwagę programistów już teraz.

## Szablon serwera MCP w `dotnet new` to sygnał

To prawdopodobnie najbardziej strategiczna pozycja w sekcji SDK.

Gdy szablon projektu ląduje bezpośrednio w SDK, oznacza to, że platforma nie traktuje już scenariusza jako niszowego. Posiadanie **szablonu serwera MCP** wbudowanego w `dotnet new` obniża koszt wypróbowania wzorca i wysyła jasny komunikat o tym, dokąd zmierza ekosystem.

Jeśli budujesz narzędzia agentowe, wewnętrznych asystentów lub narzędzia programistyczne zintegrowane z AI w .NET, to jest jedna z pierwszych rzeczy, które bym przetestował.

## Sprawdzanie podatności i końca wsparcia w czasie kompilacji to dokładnie takie domyślne ustawienia, jakie lubię

Świadomość bezpieczeństwa i cyklu życia jest znacznie lepsza, gdy platforma pomaga ci *podczas kompilacji*, a nie po fakcie w osobnym raporcie, którego nikt nie czyta.

Nowe kontrole SDK dla podatności i pakietów z końcem wsparcia podczas kompilacji to rodzaj funkcji, które uwielbiam, ponieważ czynią lepsze zachowanie domyślnym.

Nie są efektowne, ale to ulepszenia, które starzeją się naprawdę dobrze.

## C# staje się coraz bardziej wyrazisty we właściwych miejscach

Elementy C# w Preview 5 są interesujące, zwłaszcza:

- zamknięte hierarchie klas
- deklaracje unii i wzorce unii
- kontynuacja prac nad unsafe evolution

Nie przyjąłbym tego wszystkiego na ślepo w kodzie produkcyjnym, ponieważ funkcje języka w podglądzie zawsze zasługują na trzeźwy cykl testowy. Ale kierunek jest dobry. C# zmierza w kierunku bogatszego modelowania bez utraty swojej tożsamości.

## ASP.NET Core i EF Core mają praktyczne aktualizacje warte wczesnego testowania

Dwa obszary, które zdecydowanie przepuściłbym przez spike:

### Ulepszenia Blazor

Walidacja po stronie klienta dla Blazor SSR i ulepszenia QuickGrid bez interaktywności to oba rodzaje funkcji jakości życia, które mogą uprościć prawdziwe aplikacje.

### Domyślne ustawienia i ostrzeżenia EF Core

Przesunięcie przez EF Core domyślnej kompatybilności na SQL Server 2022 i dodanie ostrzeżeń dla asynchronicznych zapytań EF działających synchronicznie to dokładnie ten rodzaj zmian, które mogą ujawnić ukryte problemy w prawdziwych bazach kodów.

To oznacza, że warto testować wcześniej niż później.

## Moja krótka lista na pierwszy przebieg

Gdybym miał pół dnia na eksplorację Preview 5, zrobiłbym to:

1. wypróbuj szablon serwera MCP
2. uruchom kompilacje i sprawdź nowe kontrole podatności/EOL
3. przetestuj dowolną bazę kodów, która może skorzystać z nowych funkcji modelowania C#
4. zweryfikuj scenariusze Blazor SSR, jeśli jesteś na tym stosie
5. uruchom ścieżki obciążone EF Core i obserwuj zmiany ostrzeżeń lub różnice SQL

To tam, gdzie moim zdaniem jest wczesna wartość.

## Moje zdanie

.NET 11 Preview 5 wydaje się jedną z tych wersji, w których platforma pcha w dwóch kierunkach jednocześnie:

- bardziej ambitne możliwości programistyczne
- lepsze domyślne ustawienia dla zespołów zorientowanych produkcyjnie

Ta kombinacja jest tym, czego chcę od cyklu podglądowego.

Wypróbuj, ale próbuj z celem.

Oryginalny wpis: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)