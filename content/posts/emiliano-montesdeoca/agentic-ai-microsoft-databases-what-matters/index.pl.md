---
title: "SQL MCP Server, Copilot w SSMS i Database Hub z agentami AI: Co naprawdę liczy się z SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft zaprezentował stos ogłoszeń dotyczących baz danych na SQLCon 2026. Oto to, co naprawdę liczy się, jeśli budujesz aplikacje zasilane AI na Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "agentic-ai-microsoft-databases-what-matters" >}}).*

Microsoft właśnie uruchomił [SQLCon 2026 obok FabCon w Atlancie](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/). Pominę slajdy z cenami enterprise i skupię się na elementach, które mają znaczenie dla deweloperów budujących z Azure SQL i AI.

## SQL MCP Server jest w publicznej wersji zapoznawczej

To jest nagłówek dla mnie. Azure SQL Database Hyperscale ma teraz **SQL MCP Server** w publicznej wersji zapoznawczej, który pozwala bezpiecznie podłączyć dane SQL do agentów AI i Copilotów za pomocą [Model Context Protocol](https://modelcontextprotocol.io/).

Dla deweloperów .NET budujących agenty AI z Semantic Kernel lub Microsoft Agent Framework otwiera to czystą ścieżkę integracji. Twój agent musi sprawdzić stan magazynu? Wyszukać rekord klienta? Walidować zamówienie? MCP daje mu ustrukturyzowany sposób na to bez pisania niestandardowego kodu pobierania danych.

## GitHub Copilot w SSMS 22 jest teraz GA

Jeśli spędzasz czas w SQL Server Management Studio, GitHub Copilot jest teraz ogólnie dostępny w SSMS 22. Ten sam Copilot, którego używasz w VS Code i Visual Studio, ale dla T-SQL.

Praktyczna wartość jest prosta: pomoc oparta na czacie przy pisaniu zapytań, refaktoryzacji procedur składowanych i rozwiązywaniu problemów z wydajnością.

## Indeksy wektorowe dostały poważną aktualizację

Azure SQL Database ma teraz szybsze, bardziej zaawansowane indeksy wektorowe z pełną obsługą wstawiania, aktualizacji i usuwania. To oznacza, że dane wektorowe pozostają aktualne w czasie rzeczywistym — bez potrzeby ponownego indeksowania wsadowego.

Co nowego:
- **Kwantyzacja** dla mniejszych rozmiarów indeksu bez utraty dokładności
- **Filtrowanie iteracyjne** dla bardziej precyzyjnych wyników
- **Głębsza integracja z optymalizatorem zapytań** dla przewidywalnej wydajności

Jeśli robisz RAG z Azure SQL jako magazynem wektorów, te ulepszenia są bezpośrednio użyteczne.

## Database Hub w Fabric: agentyczne zarządzanie

Microsoft ogłosił **Database Hub w Microsoft Fabric** (wczesny dostęp) z pojedynczym panelem zarządzania dla Azure SQL, Cosmos DB, PostgreSQL, MySQL i SQL Server przez Arc.

Agenci AI stale monitorują twoją bazę danych, sygnalizują co się zmieniło, wyjaśniają dlaczego ma to znaczenie i sugerują co zrobić dalej.

## Co to oznacza dla deweloperów .NET

1. **Wypróbuj SQL MCP Server** jeśli budujesz agenty AI — najczystszy sposób na dostęp do bazy danych.
2. **Włącz Copilot w SSMS** jeśli jeszcze tego nie zrobiłeś.
3. **Sprawdź indeksy wektorowe** jeśli robisz RAG z oddzielnym magazynem wektorów.

Sprawdź [pełne ogłoszenie od Shireesh Thoty](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) i [zapisz się na wczesny dostęp do Database Hub](https://aka.ms/database-hub).
