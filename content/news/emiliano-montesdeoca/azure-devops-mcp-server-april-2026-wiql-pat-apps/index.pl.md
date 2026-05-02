---
title: "Aktualizacja Azure DevOps MCP Server z kwietnia 2026: zapytania WIQL, uwierzytelnianie PAT i eksperymentalne MCP Apps"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server otrzymuje zapytania work item oparte na WIQL, uwierzytelnianie Personal Access Token, adnotacje MCP oraz eksperymentalną funkcję MCP Apps, która pakuje typowe przepływy pracy w ponownie używalne narzędzia."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "index.md" >}}).*

Azure DevOps MCP Server ciągle się poprawia. Kwietniowa aktualizacja Dana Hellema obejmuje zarówno serwer lokalny, jak i zdalny, a pojawiło się tu kilka naprawdę przydatnych rzeczy — zwłaszcza jeśli używasz Copilota do poruszania się po boardach i repozytoriach.

## Obsługa zapytań WIQL

Najważniejsza nowość: nowe narzędzie `wit_query_by_wiql`, które pozwala uruchamiać zapytania Work Item Query Language bezpośrednio z klienta MCP.

Jeśli korzystasz z Azure Boards od dłuższego czasu, znasz WIQL. To składnia zapytań podobna do SQL dla work items: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. Udostępnienie tego jako narzędzia MCP oznacza, że sesje Copilot mogą teraz pobierać precyzyjne zestawy work items bez ręcznego filtrowania i klikania po widokach tablic.

Jedna uwaga: na zdalnym serwerze MCP to narzędzie obecnie wymaga flagi funkcji **Insiders**, dopóki trwa walidacja wydajności zapytań na dużą skalę. Zostanie udostępnione wszystkim, gdy telemetria będzie wyglądać dobrze.

## Osobiste tokeny dostępu na serwerze lokalnym

Lokalny serwer MCP obsługuje teraz uwierzytelnianie PAT. Brzmi to jak drobna poprawka jakości życia, ale ma znaczenie w scenariuszach integracyjnych — zwłaszcza gdy uruchamiasz serwer MCP w kontekście bez interaktywnego uwierzytelniania albo łączysz się z niego z zewnętrznych klientów i automatyzacji.

Kroki konfiguracji są opisane w [przewodniku Getting Started](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat).

## Adnotacje MCP na serwerze zdalnym

Adnotacje to znaczniki metadanych na narzędziach MCP, które mówią modelom językowym, jak używać ich bezpiecznie. Azure DevOps MCP Server wdraża teraz adnotacje dla:

- **Narzędzi tylko do odczytu** — model wie, że można je wywołać bez potwierdzenia użytkownika
- **Narzędzi destrukcyjnych** — model wie, że powinien być ostrożny i potwierdzić przed kontynuowaniem
- **Narzędzi open-world** — model rozumie, że mogą zwracać nieprzewidywalne wyniki

To ma podstawowe znaczenie dla niezawodności agentów. Bez adnotacji model musi zgadywać po nazwie narzędzia, czy jego wywołanie jest bezpieczne. Z adnotacjami zachowanie jest jawne i agent może podejmować lepsze decyzje.

## Konsolidacja narzędzi Wiki

Serwer zdalny zaczyna konsolidować powiązane narzędzia w mniejszą liczbę, ale bardziej możliwościowych narzędzi. Narzędzia wiki są pierwsze, które dostają to traktowanie:

| Nowe narzędzie | Zastępuje |
|----------|----------|
| `wiki` (tylko do odczytu) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

Mniej narzędzi = lepsza wydajność modelu. To stały wzorzec w projektowaniu serwerów MCP — mniejsze, bardziej skupione zestawy narzędzi działają lepiej, bo model nie musi wybierać spośród pięciu niemal identycznych opcji.

## Eksperymentalnie: MCP Apps

To najciekawszy dodatek i wyraźnie jest eksperymentalny. MCP Apps to spakowane przepływy pracy, które działają w środowisku serwera MCP:

```json
{
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "mcp-server-azuredevops",
      "args": ["contoso", "-d", "core", "work", "work-items", "mcp-apps"]
    }
  }
}
```

Pierwszy przykład to `mcp_app_my_work_item` — samodzielne środowisko pracy z work itemami, które pozwala przeglądać, filtrować i edytować przypisane do ciebie work items bez ręcznego łączenia wielu wywołań narzędzi.

Pomysł jest przekonujący: zamiast tego, by agent wywoływał `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` w kilku turach, jedna MCP App dostarcza cały workflow jako jedną ustrukturyzowaną, wielokrotnego użytku jednostkę. Mniej czasu na konfigurację, spójne zachowanie i mniej ruchomych części.

## Podsumowanie

Azure DevOps MCP Server szybko dojrzewa. Obsługa WIQL i uwierzytelnianie PAT to bezpośrednie korzyści dla każdego, kto używa Copilota z Azure Boards. Praca nad adnotacjami sprawia, że serwer zdalny jest bezpieczniejszy dla zastosowań agentowych. A MCP Apps, choć eksperymentalne, pokazują kierunek: od surowych narzędzi do komponowalnych przepływów pracy.

Warto śledzić [dokumentację](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server), gdy serwer zdalny nadal się rozwija.

Oryginalny wpis Dana Hellema: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).