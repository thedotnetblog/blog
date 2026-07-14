---
title: "Prawdziwa Granica dla Agentowego SQL: Audytowalność z OBO w SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "Uwierzytelnianie On-Behalf-Of w Data API builder plus SQL MCP Server to główny kamień milowy w zarządzaniu, ponieważ Azure SQL może w końcu audytować człowieka stojącego za działaniem agenta."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Jest bolesna prawda w korporacyjnych projektach AI: wiele zespołów obsesyjnie skupia się na jakości modelu i ignoruje odpowiedzialność. Gdy agent zapisuje lub odczytuje dane produkcyjne, pierwsze pytanie w przeglądzie incydentu nie brzmi „czy odpowiedź była dobra?" Brzmi „kto właściwie to zrobił?"

Oryginalne źródło: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

  ---


Z OBO, SQL uwierzytelnia **delegowany kontekst użytkownika**, a nie tożsamość hosta narzędzia. To daje zasadniczo lepszy model audytu: podmiot użytkownika, działanie, kontekst instrukcji i identyfikator aplikacji warstwy środkowej razem. Zyskujesz identyfikowalność bez utraty powierzchni kontrolnej narzędzi MCP i uprawnień encji DAB.

Moja opinia jest stanowcza: jeśli twój agent może dotykać wrażliwych danych SQL, OBO powinno być twoją domyślną architekturą, a nie opcjonalnym zadaniem hartowania. Konfiguracja jest bardziej złożona, ale dług tożsamościowy jest zawsze spłacany później, zwykle podczas incydentów bezpieczeństwa, audytów zgodności lub eskalacji wykonawczych.

### Praktyczne wskazówki implementacyjne

- **Zacznij od walidacji przepływu tożsamości** z minimalnym widokiem "WhoAmI" i zautomatyzowanymi kontrolami w testach integracyjnych. Jeśli podmiot SQL nie pasuje do zalogowanego użytkownika, zatrzymaj się i napraw przed wysyłką.
- **Podłącz zapytania Log Analytics** dla SQLSecurityAuditEvents do swoich dashboardów SOC i ostrzegaj o działaniach wysokiego ryzyka inicjowanych przez ścieżki OBO.
- **Dopasuj uprawnienia RBAC i DAB**, aby tożsamość na poziomie użytkownika i autoryzacja na poziomie działania były spójne end-to-end.

Jednym subtelnym, ale ważnym punktem projektowym w ogłoszeniu jest zachowanie cache. DAB jawnie blokuje buforowanie odpowiedzi, gdy włączone jest uwierzytelnianie delegowane użytkownika. Ten kompromis jest prawidłowy. Sztuczki wydajnościowe, które mogą wyciekać wyniki ograniczone do użytkownika, nie są warte ryzyka w środowiskach wielodzierżawczych lub regulowanych.