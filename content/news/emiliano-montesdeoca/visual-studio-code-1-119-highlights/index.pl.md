---
title: "VS Code 1.119: OpenTelemetry dla sesji agentów, integracja przeglądarki i bezpieczeństwo"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (maj 2026) dodaje śledzenie OpenTelemetry dla sesji agentów, udostępnianie kart przeglądarki, ulepszenia zaufania i bezpieczeństwa oraz poprawkę bezpieczeństwa 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) ukazał się 6 maja 2026 roku (z poprawką bezpieczeństwa 1.119.1 wkrótce po niej). Wydanie koncentruje się na obserwowalności agentów, interakcji z przeglądarką i redukcji przerw.

## Śledzenie OpenTelemetry dla sesji agentów

To wyróżniająca się funkcja dla każdego, kto uruchamia agenty na produkcji lub debuguje przepływy pracy agentyczne. Włącz ją za pomocą dwóch ustawień:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Ślady przestrzegają semantycznych konwencji GenAI. Każde żądanie agenta tworzy span główny `invoke_agent` z zagnieżdżonymi spanami podrzędnymi: `chat`, `execute_tool` i `execute_hook`. Użycie tokenów jest raportowane na żądanie — w tym liczniki odczytu i tworzenia pamięci podręcznej.

Działa z lokalnym agentem, agentem działającym w tle Copilot CLI i agentem Claude. Każdy backend kompatybilny z OTLP akceptuje ślady — [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) dobrze sprawdza się do lokalnego rozwoju.

## Agenty mogą teraz uzyskiwać dostęp do kart przeglądarki

Agenty mogą żądać dostępu do kart zintegrowanej przeglądarki — ale nie automatycznie. Musisz jawnie udostępnić kartę za pomocą selektora kontekstu, przeciągania i upuszczania lub sugerowanego kontekstu. W przeglądarce znajduje się przycisk udostępniania do odwoływania dostępu. Gdy agent próbuje otworzyć nową kartę w tej samej domenie co już otwarta (nieudostępniona) karta, VS Code prosi o ponowne użycie istniejącej karty.

## Zoptymalizowane użycie tokenów

Eksperymentalny lekki model zarządza teraz listami zadań agentów, utrzymując tę pracę administracyjną z dala od droższego modelu podstawowego. Zmniejsza zużycie tokenów dla zadań, które nie wymagają pełnej zdolności rozumowania.

## Zaufanie i bezpieczeństwo

Mniej przerw: VS Code 1.119 zmniejsza monity o żądania dostępu do sieci i zapisy do folderów tymczasowych przez agenty. Poprawka 1.119.1 rozwiązuje konkretne problemy z bezpieczeństwem — warto zaktualizować, jeśli jeszcze tego nie zrobiono.

## Szybkie przełączanie do podglądu Markdown

Małe, ale przydatne: teraz możesz szybko przełączyć bieżący edytor do podglądu Markdown bez nawigowania.

## VS Code Agents (podgląd Insiders)

Przeprojektowany interfejs sesji agentów — nowy selektor repozytoriów (lokalne/repos/zdalne), ulepszenia podsesji, dopracowanie web i mobilne, animacje postępu — jest dostępny w Insiders pod adresem [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Pełny dziennik zmian: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
