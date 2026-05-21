---
title: "Rozszerzenie MSSQL dla VS Code po cichu staje się znacznie większą platformą"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Najnowsza aktualizacja rozszerzenia MSSQL dodaje provisioning Azure SQL, projektowanie schematów wspierane przez Copilot, Data API builder i notebooki. Ciekawe jest to, ile pracy z bazami danych może teraz zostać wewnątrz VS Code."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Ten artykuł został automatycznie przetłumaczony. Aby zobaczyć oryginał, [kliknij tutaj]({{< ref "index.md" >}}).*

Rozszerzenie MSSQL dla VS Code rozwija się od jakiegoś czasu, ale ta najnowsza aktualizacja sprawia, że kierunek jest znacznie jaśniejszy.

To już nie jest tylko „połącz się i uruchom kilka zapytań”.

Dzięki **provisioningowi Azure SQL**, **Schema Designer z Copilot**, **SQL Notebooks** i **Data API builderem** rozwijanym razem w jednym wydaniu, rozszerzenie staje się znacznie pełniejszym środowiskiem pracy dla rozwoju opartego na bazach danych.

## Praktyczny haczyk to provisioning bezpośrednio z edytora

Wpis źródłowy mówi, że teraz można utworzyć w pełni zarządzaną bazę danych w chmurze „bezpośrednio z edytora i bez kosztów” z użyciem darmowej warstwy.

To ten rodzaj funkcji, który wydaje się mały, dopóki nie uświadomisz sobie, ile tarcia związanego z konfiguracją usuwa.

Dla wielu deweloperów uciążliwa część eksperymentów z dużą ilością danych nie dotyczy SQL samego w sobie. Chodzi o lukę środowiskową między:

- pomysłem
- bazą danych
- schematem
- API
- testowalnym backendem

Jeśli ta luka skraca się w jednym narzędziu, cały workflow staje się bardziej atrakcyjny.

## Tak wygląda mocniejszy inner loop dla pracy z danymi

To, co podoba mi się w tym wydaniu, to utrzymanie większej części workflow bazy danych w jednym miejscu:

- provisioning bazy danych
- projektowanie schematu
- przegląd zmian
- generowanie skryptów ORM
- udostępnianie API
- testowanie endpointów
- dokumentowanie i wykonywanie zapytań przez notebooki

To znacznie bardziej przekonująca historia niż traktowanie SQL jako odłączonego narzędzia pobocznego w stacku.

## Workflow schematu wspierany przez Copilot to miejsce, gdzie wartość AI naprawdę czuć

Nowości w schema designerze są szczególnie interesujące, bo wydają się trafiać w dobry balans.

Wartość nie polega na tym, że „AI projektuje model danych, a ty ślepo mu ufasz”.

Wartość to:

- szybsze punkty startowe
- wizualny przegląd
- śledzenie zmian
- wynik ukierunkowany na migrację
- jawne kontrolki accept/undo

To dużo zdrowszy workflow AI niż pełna auto-generacja bez ścieżki inspekcji.

A w pracy z bazami danych możliwość przeglądu ma ogromne znaczenie.

## Data API builder to cichy wzmacniacz

Drugą funkcją, której bym nie ignorował, jest integracja z Data API builder.

Jeśli możesz przejść od schematu do:

- REST
- GraphQL
- endpointów MCP

wewnątrz tego samego środowiska, tworzy to bardzo wydajną ścieżkę dla backendowych prototypów i narzędzi wewnętrznych.

To nie zastępuje głębszej inżynierii backendowej. Ale zdecydowanie skraca drogę od pomysłu na bazę danych do działającego interfejsu.

## Moim zdaniem

To wydanie sprawia, że rozszerzenie MSSQL przypomina bardziej małą platformę wewnątrz VS Code niż zwykły dodatek.

Dla deweloperów budujących API, narzędzia danych, narzędzia administracyjne albo prototypy oparte na SQL, to znacząca zmiana.

A jeśli Microsoft będzie dalej dopracowywać tę pętlę, rozszerzenie stanie się dużo bardziej strategicznie użyteczne, niż dziś uważa wielu ludzi.

Oryginalny wpis: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)