---
title: "VS Code 1.112: Na Co Programiści .NET Powinni Zwrócić Uwagę"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 właśnie wylądował i jest pełen ulepszeń agentów, zintegrowanego debuggera przeglądarki, piaskownicy MCP i obsługi monorepo. Oto co naprawdę ma znaczenie, jeśli budujesz z .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-112-dotnet-developers" >}}).*

VS Code 1.112 właśnie wylądował i szczerze? Ten trafił w serce, jeśli spędzasz dni w środowisku .NET. W [oficjalnych notatkach do wydania](https://code.visualstudio.com/updates/v1_112) jest dużo, ale pozwól, że oszczędzę ci przewijania i skupię się na tym, co naprawdę ma znaczenie dla nas.

## Copilot CLI właśnie stał się o wiele bardziej użyteczny

Głównym tematem tego wydania jest **autonomia agenta** — dawanie Copilotowi więcej przestrzeni do działania bez konieczności nadzorowania każdego kroku.

### Sterowanie wiadomościami i kolejkowanie

Znasz ten moment, gdy Copilot CLI jest w połowie zadania i zdajesz sobie sprawę, że zapomniałeś coś wspomnieć? Wcześniej musiałeś czekać. Teraz możesz po prostu wysyłać wiadomości, gdy żądanie jest nadal uruchomione — albo żeby sterować bieżącą odpowiedzią, albo ustawić w kolejce kolejne instrukcje.

### Poziomy uprawnień

To jest to, co mnie najbardziej ekscytuje. Sesje Copilot CLI teraz obsługują trzy poziomy uprawnień:

- **Default Permissions** — normalny przepływ, w którym narzędzia proszą o potwierdzenie przed uruchomieniem
- **Bypass Approvals** — automatycznie zatwierdza wszystko i ponawia próby przy błędach
- **Autopilot** — działa w pełni autonomicznie: zatwierdza narzędzia, odpowiada na własne pytania i kontynuuje, aż zadanie jest zakończone

Możesz włączyć Autopilot z ustawieniem `chat.autopilot.enabled`.

## Debugowanie aplikacji webowych bez opuszczania VS Code

Zintegrowana przeglądarka obsługuje teraz **pełne debugowanie**. Możesz ustawiać punkty przerwania, przechodzić przez kod krok po kroku i sprawdzać zmienne — wszystko wewnątrz VS Code.

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Dla programistów Blazor, to rewolucja. Już uruchamiasz `dotnet watch` w terminalu — teraz debugowanie zostaje w tym samym oknie.

## Piaskownica serwerów MCP

Jeśli używasz serwerów MCP — może skonfigurowany własny dla zasobów Azure lub zapytań bazodanowych — teraz możesz je umieścić w piaskownicy:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

## Odkrywanie dostosowań monorepo

Jeśli pracujesz w monorepo, z ustawieniem `chat.useCustomizationsInParentRepositories`, VS Code idzie w górę do katalogu `.git` i odkrywa wszystko.

## /troubleshoot do debugowania agentów

Kiedykolwiek skonfigurować niestandardowe instrukcje lub umiejętności i zastanawiać się, dlaczego nie są pobierane? Nowa umiejętność `/troubleshoot` czyta dzienniki debugowania agentów i mówi Ci, co się stało.

## Podsumowanie

VS Code 1.112 wyraźnie mocno naciska na doświadczenie agenta — większa autonomia, lepsze debugowanie, silniejsze bezpieczeństwo. [Pobierz VS Code 1.112](https://code.visualstudio.com/updates/v1_112) lub zaktualizuj z poziomu VS Code przez **Help > Check for Updates**.
