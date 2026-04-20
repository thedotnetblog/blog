---
title: "Ocena Modernizacji GitHub Copilot To Najlepsze Narzędzie Migracji, Którego Jeszcze Nie Używasz"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Rozszerzenie modernizacji GitHub Copilot nie tylko sugeruje zmiany kodu — produkuje pełną ocenę migracji z wykonalnymi problemami, porównaniami celów Azure i współpracującym przepływem pracy."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "dotnet-modernization-assessment-github-copilot" >}}).*

Migrowanie starszej aplikacji .NET Framework do nowoczesnego .NET to jedno z tych zadań, które wszyscy wiedzą, że powinni wykonać, ale nikt nie chce zaczynać.

Jeffrey Fritz właśnie opublikował [dogłębną analizę oceny modernizacji GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/).

## To nie jest tylko silnik sugestii kodu

Rozszerzenie VS Code podąża za modelem **Oceń → Planuj → Wykonaj**. Faza oceny analizuje całą bazę kodu i produkuje ustrukturyzowany dokument, który wszystko przechwytuje.

Ocena jest przechowywana pod `.github/modernize/assessment/`. Każde uruchomienie produkuje niezależny raport.

## Dwa sposoby na start

**Zalecana ocena** — szybka ścieżka. Wybierz z kuratorowanych domenach (Java/.NET Upgrade, Cloud Readiness, Security).

**Niestandardowa ocena** — ścieżka ukierunkowana. Skonfiguruj dokładnie co analizować: docelowe obliczenia (App Service, AKS, Container Apps), docelowy system operacyjny, analiza konteneryzacji.

## Podział problemów jest wykonalny

Każdy problem ma poziom krytyczności:

- **Obowiązkowy** — musi być naprawiony lub migracja się nie powiedzie
- **Potencjalny** — może wpłynąć na migrację, wymaga ludzkiego osądu
- **Opcjonalny** — zalecane ulepszenia, nie blokuje migracji

## Moje zdanie

Jeśli masz starsze aplikacje .NET Framework, to jest *najlepsze* narzędzie do rozpoczęcia. Sam dokument oceny jest wart poświęconego czasu.

Przeczytaj [pełny przewodnik](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) i pobierz [rozszerzenie VS Code](https://aka.ms/ghcp-appmod/vscode-ext).
