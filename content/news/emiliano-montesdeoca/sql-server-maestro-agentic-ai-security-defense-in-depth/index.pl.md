---
title: "MAESTRO, Obrona w Głąb i Dlaczego SQL Server Jest Teraz Granicą Bezpieczeństwa dla AI"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Agentyczna AI wprowadza zagrożenia, do których tradycyjne modele STRIDE nie zostały zaprojektowane. Oto jak Microsoft SQL mapuje się na framework MAESTRO, aby zapewnić zarządzaną granicę wykonania."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Modele zagrożeń bezpieczeństwa budowane są na założeniach dotyczących tego, kto lub co wysyła żądania. STRIDE zakłada ludzkich aktorów wchodzących w interakcje z systemami poprzez zdefiniowane interfejsy. Agenci AI nie działają w ten sposób.

## STRIDE Nie Został Zaprojektowany dla Agentów AI

Systemy agentyczne działają autonomicznie, łączą narzędzia poprzez wywołania API, podejmują decyzje o tym, jakie dane pobrać i jakie działania wykonać, oraz mogą otrzymywać instrukcje z wielu źródeł — poleceń użytkownika, wyników narzędzi, pobranych danych. Model zagrożeń STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) nie rejestruje odpowiednio wektorów ataków specyficznych dla agentów, takich jak wstrzykiwanie promptów, zatruwanie kontekstu czy nadużywanie narzędzi.

Cloud Security Alliance opublikował framework MAESTRO specjalnie dla ryzyka agentów AI.

## Framework MAESTRO

MAESTRO organizuje ryzyko agentycznej AI w siedmiu warstwach:

1. **Foundation Models** — bazowe LLM i ich podatności szkoleniowe
2. **Data Operations** — pobieranie, przechowywanie i manipulacja danymi
3. **Agent Frameworks** — oprogramowanie pośredniczące do orkiestracji i koordynacji agentów
4. **Deployment & Infrastructure** — gdzie agenci są uruchamiani i jak są skonfigurowani
5. **Evaluation & Observability** — monitorowanie zachowania agentów w czasie
6. **Security & Compliance** — kontrola dostępu, audyt i zgodność regulacyjna
7. **Agent Ecosystem** — jak agenci współdziałają ze sobą i zewnętrznymi narzędziami

Każda warstwa ma specyficzne wektory ataków, których tradycyjne mechanizmy kontroli bezpieczeństwa bezpośrednio nie adresują.

## Microsoft SQL jako Zarządzana Granica Wykonania

SQL Server 2025 mapuje się na warstwy MAESTRO w konkretny sposób:

**Warstwa Data Operations**: `AI_GENERATE_EMBEDDINGS` zintegrowany z T-SQL utrzymuje operacje wektorowe w zarządzanych granicach bazy danych. Dane nie muszą opuszczać bazy danych do serwisu modelu w celu przetwarzania embeddingów.

**Warstwy Security & Compliance**: Bezpieczeństwo na poziomie wierszy (RLS) i dynamiczne maskowanie danych (DDM) stosuje się niezależnie od tego, jak przyszło żądanie — czy od ludzkiego użytkownika, czy agenta AI. Agent nie może ominąć kontroli, które są egzekwowane przez samą bazę danych.

**Warstwa Agent Frameworks**: Procedury składowane służą jako granice narzędzi. Zamiast dawać agentom dowolny dostęp SQL, definiujesz dozwolone operacje jako procedury i eksponujesz je jako narzędzia agentów. Sparametryzowane zapytania zapobiegają wstrzyknięciom na poziomie wykonania.

**Warstwa Evaluation & Observability**: Rejestrowanie audytu i Query Store rejestrują to, co każdy agent faktycznie wykonał — nie tylko to, o co go poproszono. Ta identyfikowalność jest kluczowa dla dochodzeń incydentów w systemach agentycznych, gdzie atrybucja jest złożona.

## Obrona w Głąb dla Agentycznej AI

Zasada pozostaje taka sama jak w tradycyjnym bezpieczeństwie: żadna pojedyncza kontrola nie jest wystarczająca. Zmienia się to, które kontrole są najważniejsze dla agentów:

**Zmniejszenie promienia wybuchu**: granice narzędzi poprzez procedury składowane oznaczają, że skompromitowany agent może wykonywać tylko wstępnie zdefiniowane operacje. Nie może przestawić się na dowolne zapytania.

**Obserwowalność**: po incydencie musisz być w stanie odpowiedzieć na pytanie "co dokładnie zrobił ten agent?". Systemy agentycznej AI bez identyfikowalności na poziomie bazy danych mają martwe punkty, których rejestrowanie aplikacji nie pokrywa.

**Ograniczone wykonanie**: parametryzacja, RLS i DDM są zasobami bezpieczeństwa niezależnie od tego, czy wywołujący jest człowiekiem. Nie osłabiaj ich, aby przystosować agentów.

**Odpowiedzialność**: rejestrowanie audytu SQL Server tworzy zapis tego, kto (który agent, przy użyciu jakich poświadczeń) wykonał co i kiedy. To ma znaczenie, gdy systemy agentyczne podejmują działania z realnymi konsekwencjami na świecie.

SQL Server 2025 nie został zbudowany do abstrakcyjnego rozwiązywania ryzyka agentycznego — został zbudowany jako relacyjna baza danych. Ale zarządzanie, które sprawia, że korporacyjna baza danych jest godna zaufania, okazuje się być dokładnie tym, co sprawia, że granica wykonania agentów jest bezpieczna.

Oryginalny post: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
