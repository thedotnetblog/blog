---
title: "NL2SQL to SQL Injection epoki agentów"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Zanim pozwolisz agentowi odpytywać bazę danych językiem naturalnym, przeczytaj to. NL2SQL wydaje się proste, dopóki nie przemyślisz kompletności schematu, niedeterminizmu i tego, co SQL MCP Server naprawdę rozwiązuje."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Istnieje wersja prezentacji NL2SQL, która brzmi idealnie: użytkownicy zadają pytania w języku naturalnym, agenci generują SQL, dane są zwracane. Mniej ekranów, mniej zapytań, mniej kodu. Proste.

Potem myślisz o tym przez kolejne pięć minut.

## Problemy, o których nikt nie mówi w demo

**Schematy nie były projektowane, żeby coś wyjaśniać.** Kryptyczne nazwy tabel, niespójne nazwy kolumn, technicznie poprawne relacje, które są semantycznie nieważne bez dodatkowych predykatów — to norma w bazach danych przedsiębiorstw. To nie są błędy, to tylko nagromadzona historia zmian biznesowych. Ale kiedy prosisz model o wywnioskowanie intencji ze schematu, który nie był projektowany do przekazywania intencji, model i tak spróbuje. Nie podda się. Wygeneruje swoje najlepsze zapytanie i z przekonaniem zwróci wyniki.

**Modele są niedeterministyczne.** Zadaj to samo pytanie tej samej bazie danych dwa razy i możesz otrzymać inny SQL. Model oblicza prawdopodobieństwa, a małe zmiany w kontekście powodują różne wyniki. Nie możesz osiągnąć przez testowanie gwarancji, że agent zawsze generuje poprawne zapytanie.

**Przegląd użytkownika nie skaluje się.** "Po prostu przeglądaj każde zapytanie przed wykonaniem" brzmi bezpiecznie. Ale zakłada, że użytkownicy są ekspertami zarówno w modelu danych, jak i SQL — dokładnie ludzie, którzy nie potrzebowali interfejsu języka naturalnego. Wprowadza też przeciążenie poznawcze i nową klasę błędu potwierdzenia, gdzie użytkownicy przytłoczeni złożonością zapytania zatwierdzają nieważne zapytania zamiast je sprawdzać.

**I jest jeszcze wstrzykiwanie.** W tradycyjnym rozwoju SQL parametryzacja rozwiązywała problem wstrzykiwania, ponieważ dane wejściowe użytkownika wypełniały parametry, nie strukturę SQL. W NL2SQL model sam generuje SQL. Prompt, kontekst schematu, historia rozmowy i pobrane dane — wszystko wpływa na to, co jest wykonywane. Jeśli ktoś spreparuje prompt zmieniający to, co generuje model, to jest wstrzykiwanie — nie na poziomie parametrów, ale na poziomie generowania zapytań. I w przeciwieństwie do DROP TABLE (oczywiste, odwracalne), wstrzykiwanie NL2SQL produkuje zapytania zwracające błędne wyniki bez widocznego błędu. Decyzje biznesowe są podejmowane na podstawie złych danych.

## Co SQL MCP Server naprawdę rozwiązuje

Tu artykuł stawia swój najbardziej użyteczny praktyczny punkt. Zamiast dawać agentowi dowolny dostęp do schematu i mieć nadzieję na najlepsze, SQL MCP Server udostępnia **wyselekcjonowaną powierzchnię API** zbudowaną na [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

Różnica ma znaczenie: agent nie generuje SQL. Wywołuje nazwane endpointy, które zwracają z góry zdefiniowane kształty wyników. SQL jest pisany raz, przez programistę, i jest deterministyczny. Niedeterminizm agenta jest ograniczony do wyboru *którego* endpointu wywołać, nie do tworzenia dowolnych zapytań.

To jest analogiczne do tego, co parametryzacja zrobiła z wstrzykiwaniem SQL w tradycyjnym modelu aplikacji — usuwa możliwość tworzenia dowolnych zapytań z niezaufanych danych wejściowych.

## Właściwe pytanie

Artykuł nie mówi "nigdy nie używaj NL2SQL." Mówi: bądź świadomy *gdzie* to stosujesz i *co* udostępniasz. Do eksploracyjnej analizy w kontrolowanym środowisku, z ograniczonym schematem i dostępem tylko do odczytu, NL2SQL może być w porządku. Dla systemów produkcyjnych, gdzie decyzje biznesowe zależą od wyników, wyselekcjonowana warstwa API jest znacznie bezpieczniejsza.

Uczciwie: niektóre problemy są naprawdę lepiej rozwiązywane przez strukturowane zapytania za nazwanymi endpointami niż przez język naturalny do SQL. SQL MCP Server daje ci tę opcję bez całkowitego rezygnowania z interfejsu agentowego.

Oryginalny post: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
