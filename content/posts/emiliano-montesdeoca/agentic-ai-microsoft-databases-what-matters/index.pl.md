---
title: "SQL MCP Server, Copilot w SSMS i centrum baz danych z agentami AI: co naprawdę ważne z SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft zaprezentował stos ogłoszeń dotyczących baz danych na SQLCon 2026. Oto rzeczy, które naprawdę mają znaczenie, jeśli budujesz aplikacje oparte na AI na Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "agentic-ai-microsoft-databases-what-matters" >}}).*

Microsoft właśnie zainaugurował [SQLCon 2026 razem z FabCon w Atlancie](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) i jest wiele do omówienia. Oryginalne ogłoszenie obejmuje wszystko od planów oszczędnościowych po funkcje zgodności dla przedsiębiorstw. Pominę slajdy z cenami dla enterprise i skupię się na kawałkach, które mają znaczenie, jeśli jesteś programistą budującym na Azure SQL i AI.

## SQL MCP Server jest w publicznym podglądzie

To jest dla mnie nagłówek. Azure SQL Database Hyperscale ma teraz **SQL MCP Server** w publicznym podglądzie, który pozwala bezpiecznie połączyć dane SQL z agentami AI i Copilotami za pomocą [Model Context Protocol](https://modelcontextprotocol.io/).

Jeśli śledziłeś falę MCP — a szczerze, trudno ją przeoczyć — to jest poważna sprawa. Zamiast budować niestandardowe potoki danych, by dostarczać kontekst z bazy danych do agentów AI, masz standardowy protokół do bezpośredniego eksponowania danych SQL. Twoje agenty mogą odpytywać, analizować i działać na żywych danych bazy danych.

Dla tych z nas budujących agenty AI z Semantic Kernel lub Microsoft Agent Framework, otwiera to czystą ścieżkę integracji. Agent musi sprawdzić stan magazynu? Wyszukać rekord klienta? Zweryfikować zamówienie? MCP daje mu ustrukturyzowany sposób na zrobienie tego bez pisania niestandardowego kodu pobierania danych dla każdego scenariusza.

## GitHub Copilot w SSMS 22 jest teraz ogólnie dostępny

Jeśli spędzasz czas w SQL Server Management Studio — a bądźmy szczerzy, większość z nas nadal to robi — GitHub Copilot jest teraz ogólnie dostępny w SSMS 22. To samo doświadczenie Copilot, którego już używasz w VS Code i Visual Studio, ale dla T-SQL.

Praktyczna wartość jest prosta: pomoc oparta na czacie do pisania zapytań, refaktoryzacji procedur składowanych, rozwiązywania problemów z wydajnością i obsługi zadań administracyjnych. Nic rewolucyjnego w koncepcji, ale mając to bezpośrednio w SSMS, nie musisz przełączać kontekstu do innego edytora tylko po to, by uzyskać pomoc AI przy pracy z bazą danych.

## Indeksy wektorowe otrzymały poważną aktualizację

Azure SQL Database ma teraz szybsze i bardziej wydajne indeksy wektorowe z pełnym wsparciem wstawiania, aktualizacji i usuwania. To oznacza, że dane wektorowe pozostają aktualne w czasie rzeczywistym — bez wsadowego ponownego indeksowania.

Co nowego:
- **Kwantyzacja** dla mniejszych rozmiarów indeksów bez zbytniej utraty dokładności
- **Filtrowanie iteracyjne** dla precyzyjniejszych wyników
- **Ściślejsza integracja z optymalizatorem zapytań** dla przewidywalnej wydajności

Jeśli robisz generowanie wspomagane pobieraniem (RAG) z Azure SQL jako magazynem wektorów, te ulepszenia są bezpośrednio przydatne. Możesz trzymać wektory obok danych relacyjnych w tej samej bazie danych, co znacznie upraszcza architekturę w porównaniu do osobnej bazy wektorowej.

Te same ulepszenia wektorów są również dostępne w SQL database w Fabric, ponieważ oba działają na tym samym silniku SQL.

## Database Hub w Fabric: zarządzanie agentyczne

Ten jest bardziej perspektywiczny, ale interesujący. Microsoft ogłosił **Database Hub w Microsoft Fabric** (wczesny dostęp), który daje jeden widok na Azure SQL, Cosmos DB, PostgreSQL, MySQL i SQL Server przez Arc.

Interesujący kąt nie polega tylko na ujednoliconym widoku — to agentyczne podejście do zarządzania. Agenty AI ciągłe monitorują twoją infrastrukturę baz danych, wyświetlają zmiany, wyjaśniają dlaczego mają znaczenie i sugerują co zrobić dalej. To model z człowiekiem w pętli, gdzie agent wykonuje ciężką pracę, a ty podejmujesz decyzje.

Dla zespołów zarządzających więcej niż garścią baz danych, może to naprawdę zmniejszyć operacyjny szum. Zamiast skakać między portalami i ręcznie sprawdzać metryki, agent przynosi sygnał do ciebie.

## Co to oznacza dla programistów .NET

Wątek łączący wszystkie te ogłoszenia jest jasny: Microsoft wbudowuje agenty AI w każdą warstwę stosu baz danych. Nie jako gadżet, ale jako praktyczną warstwę narzędziową.

Jeśli budujesz aplikacje .NET wspierane przez Azure SQL, oto co bym faktycznie zrobił:

1. **Wypróbuj SQL MCP Server** jeśli budujesz agenty AI. To najczystszy sposób, by dać agentom dostęp do bazy danych bez niestandardowej hydrauliki.
2. **Włącz Copilot w SSMS** jeśli jeszcze tego nie zrobiłeś — bezpłatne zwiększenie produktywności przy codziennej pracy z SQL.
3. **Przyjrzyj się indeksom wektorowym** jeśli robisz RAG i obecnie używasz osobnego magazynu wektorów. Konsolidacja do Azure SQL oznacza jedną usługę mniej do zarządzania.

## Podsumowanie

Pełne ogłoszenie ma więcej — plany oszczędnościowe, asystentów migracji, funkcje zgodności — ale historia dla programistów jest w MCP Server, ulepszeniach wektorowych i agentycznej warstwie zarządzania. To są kawałki, które zmieniają sposób budowania, a nie tylko budżetowania.

Sprawdź [pełne ogłoszenie od Shireesha Thoty](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) po pełny obraz i [zarejestruj się na wczesny dostęp do Database Hub](https://aka.ms/database-hub) jeśli chcesz wypróbować nowe doświadczenie zarządzania.

