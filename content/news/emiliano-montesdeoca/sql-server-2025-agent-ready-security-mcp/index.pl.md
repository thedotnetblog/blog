---
title: "SQL Server 2025 jako baza danych gotowa na agentów: bezpieczeństwo, backup i MCP w jednym silniku"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Końcowa część serii Polyglot Tax omawia najtrudniejsze problemy produkcyjne: ujednolicony Row-Level Security dla danych relacyjnych, JSON, graph i vector, a także kryptograficzne ślady audytu i integrację MCP, które czynią SQL Server 2025 naprawdę gotowym na agentów."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Ten post został automatycznie przetłumaczony. Aby zobaczyć oryginalną wersję, [kliknij tutaj](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Śledziłem serię Polyglot Tax Adityi Badramraju z dużym zainteresowaniem. Części 1-3 zbudowały mocny argument za SQL Server 2025 jako naprawdę wielomodelową bazą danych — JSON, graph, vector i dane relacyjne w jednym silniku z ujednoliconym query plannerem. Część 4 zamyka serię tym, co naprawdę decyduje o tym, czy zaufałbyś tej architekturze w produkcji.

Spoiler: historia produkcyjna jest solidna.

## Jeden Model Bezpieczeństwa dla Wszystkich Modeli Danych

To jest problem stacków poliglotycznych: gdy audytor pyta "udowodnij, że Tenant A nie widzi danych Tenant B", musisz odpowiedzieć na to pytanie osobno dla każdej bazy danych. Pięć baz danych, pięć modeli bezpieczeństwa, pięć dowodów.

W SQL Server 2025 definiujesz jedną politykę Row-Level Security i obejmuje ona wszystkie modele danych:

```sql
CREATE FUNCTION dbo.fn_TenantFilter(@TenantID INT)
RETURNS TABLE WITH SCHEMABINDING
AS RETURN SELECT 1 AS fn_result
WHERE @TenantID = CAST(SESSION_CONTEXT(N'TenantID') AS INT);

CREATE SECURITY POLICY TenantIsolation
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Customers,     -- Relational
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Events,        -- JSON data
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Relationships, -- Graph edges
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Embeddings     -- Vector data
WITH (STATE = ON);
```

Od tego momentu każde zapytanie — relacyjne joiny, zapytania po ścieżkach JSON, traversale graph, wyszukiwanie podobieństwa vector — jest automatycznie filtrowane po tenant. Silnik wstrzykuje predykat do planu wykonania, zanim jakiekolwiek dane opuszczą storage. Twój kod wywołujący nie musi wszędzie pisać `WHERE TenantID = @id`. Testujesz politykę raz.

Warstwy nakładają się dalej: Dynamic Data Masking dla kolumn, które nie powinny pokazywać pełnych wartości niektórym rolom, Always Encrypted dla szyfrowania end-to-end (nawet DBA nie mogą tego odczytać) oraz stored procedures jako granica uprawnień, aby agenci wywoływali tylko to, co jawnie udostępniłeś.

To jest część architektury, która ma największe znaczenie dla SaaS z dużymi wymaganiami compliance. Jedna polityka, jeden dowód.

## Ujednolicony Backup = Atomowe Odzyskiwanie

Jedna instrukcja, wszystkie modele danych, spójny punkt w czasie:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

W stacku poliglotycznym odzyskiwanie point-in-time dla pięciu baz danych oznacza koordynację pięciu operacji restore i nadzieję, że znaczniki czasu zbiegną się w ciągu jednej lub dwóch sekund. Dla danych finansowych taka dwusekundowa niespójność jest nie do zaakceptowania. Z jedną bazą danych, jednym logiem transakcji i jednym restore — odzyskiwanie jest atomowe z definicji.

## Tabele Ledger dla Ścieżek Audytu Odpornych na Manipulacje

W branżach regulowanych potrzebujesz czegoś więcej niż "mamy logi". Potrzebujesz kryptograficznego dowodu, że te logi nie zostały zmienione:

```sql
CREATE TABLE FinancialTransactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT NOT NULL,
    Amount MONEY NOT NULL,
    TransactionType NVARCHAR(20),
    TransactionDate DATETIME2 DEFAULT SYSUTCDATETIME()
)
WITH (SYSTEM_VERSIONING = ON, LEDGER = ON);
```

Każdy insert, update i delete jest kryptograficznie hashowany w strukturze podobnej do blockchaina. Możesz matematycznie udowodnić audytorowi, że wiersz nie był manipulowany od momentu zapisania. W stacku poliglotycznym taka możliwość nie istnieje w sposób jednolity we wszystkich twoich bazach danych.

## Integracja MCP: Agenci Bez Ręcznie Pisanej Warstwy Middleware

Seria prowadziła właśnie do tego: SQL Server 2025 wspiera SQL MCP Server bezpośrednio, co oznacza, że twoi agenci mogą wywoływać bazę danych przez natural language tool calls bez pisania middleware dla każdej operacji.

Połącz to ze stored procedures jako granicą uprawnień i Row-Level Security wymuszanym na poziomie silnika, a otrzymasz model, w którym:

1. Agent wywołuje narzędzie, na przykład "pobierz kontekst klienta dla konta 12345"
2. MCP tłumaczy to na zdefiniowaną przez ciebie stored procedure
3. Silnik SQL automatycznie wymusza izolację tenant i maskowanie kolumn
4. Agent dostaje dokładnie te dane, które może zobaczyć

Nie ma warstwy middleware. Nie ma ryzyka ad-hoc query injection. Autoryzację obsługuje silnik, nie agent.

## Dlaczego To Ma Znaczenie dla Programistów .NET

Jeśli budujesz usługi .NET, a SQL Server jest twoim podstawowym magazynem danych, przekaz tej serii jest prosty: nie musisz dodawać Redis do cache, graph database do relacji ani vector store do embeddings. SQL Server 2025 obsługuje to wszystko — z lepszą spójnością operacyjną niż stack poliglotyczny i z ujednoliconym bezpieczeństwem, które naprawdę da się audytować.

Integracja MCP oznacza, że twoi agenci Semantic Kernel lub workflow Microsoft Agent Framework mogą komunikować się z warstwą danych przez ten sam SQL MCP Server, z takimi samymi gwarancjami bezpieczeństwa, jakie zastosowałbyś do zapytań ludzi.

## Podsumowanie

Serię Polyglot Tax warto przeczytać od początku do końca. Części 1-3 dowodzą historii query planner. Część 4 dowodzi historii produkcyjnej. Dla programistów .NET budujących aplikacje agent-first lub AI-augmented na Azure SQL, ta architektura zasługuje na poważne rozważenie.

Oryginalny post autorstwa Adityi Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).