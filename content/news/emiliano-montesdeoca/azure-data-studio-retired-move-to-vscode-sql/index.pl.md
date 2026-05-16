---
title: "Azure Data Studio zostało wycofane: przenieś przepływ pracy Azure SQL do VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio zostało wycofane 6 lutego 2025 roku, wsparcie kończy się 28 lutego 2026. Oto kompletna ścieżka migracji do VS Code z rozszerzeniem MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Azure Data Studio zostało wycofane 6 lutego 2025 roku](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), wsparcie kończy się 28 lutego 2026 — zalecanym zamiennikiem jest VS Code z rozszerzeniem MSSQL.

## Co zainstalować

Trzy rzeczy na start:

- **Rozszerzenie MSSQL** — wyszukaj "SQL Server (mssql)" w VS Code Marketplace
- **Rozszerzenie SQL Database Projects** — schemat jako kod, walidacja kompilacji, publikacja z przewodnikiem
- **.NET 8 SDK** — wymagany przez system kompilacji; brak SDK to najczęstszy problem przy pierwszym uruchomieniu

## Migracja połączeń i ustawień ADS

Rozszerzenie MSSQL zawiera **ADS Migration Toolkit**, który obsługuje jednorazową migrację w przepływie z przewodnikiem: zapisane połączenia, grupy połączeń, ustawienia i skróty klawiszowe są importowane automatycznie.

## Odzyskanie odruchu F5

Użytkownicy ADS polegają na F5 do uruchamiania zapytań. Zainstaluj rozszerzenie **MSSQL Database Management Keymap**, aby odzyskać skróty klawiszowe w stylu ADS, w tym F5.

## SQL Database Projects: schemat jako kod

Kliknij prawym przyciskiem na projekt → **Publikuj** → skonfiguruj cel → przejrzyj wygenerowany skrypt T-SQL → wdróż. Podgląd skryptu przed wdrożeniem to kluczowa funkcja bezpieczeństwa. Szablony elementów generują szablony dla tabel, procedur składowanych i widoków — ten sam przepływ co w SSDT.

Częsty problem: **niezgodność platformy docelowej** w pliku `.sqlproj` spowoduje błędy kompilacji, jeśli projekt został utworzony dla innej wersji SQL Server.

## Schema Compare i Schema Designer

Rozszerzenie zawiera również **Schema Compare** (różnice między projektem a wdrożoną bazą danych) i **Schema Designer** (wizualna edycja schematu bez ręcznego pisania DDL).

## Deweloperzy Microsoft Fabric

Konfiguracja jest identyczna, ale zacznij od **portalu Fabric** i najpierw połącz bazę danych z Git, zanim otworzysz ją w VS Code. Microsoft ma dedykowany przewodnik: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Podsumowanie

Migracja to jednorazowy przepływ z przewodnikiem, a nie ręczna przebudowa. Zainstaluj trzy narzędzia, uruchom ADS Migration Toolkit, przywróć skróty klawiszowe — i wróć do normalnej pracy w mniej niż 10 minut.

Zobacz [pełny artykuł](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) z instrukcją krok po kroku i przewodnikiem dla Fabric.
