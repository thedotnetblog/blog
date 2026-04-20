---
title: "Tworzenie interfejsów użytkownika dla multi-agentowych systemów w czasie rzeczywistym — bez efektu czarnej skrzynki"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI i Microsoft Agent Framework łączą siły, by zapewnić multi-agentowym przepływom pracy właściwy frontend — ze streamingiem w czasie rzeczywistym, zatwierdzeniami przez człowieka i pełną widocznością działań agentów."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Oto rzecz o systemach wieloagentowych: w demonstracjach wyglądają niesamowicie. Trzy agenty przekazują sobie pracę, rozwiązują problemy, podejmują decyzje. Potem próbujesz pokazać to prawdziwym użytkownikom i... cisza. Kręcący się wskaźnik. Nikt nie wie, który agent co robi ani dlaczego system jest wstrzymany. To nie jest produkt — to problem zaufania.

Zespół Microsoft Agent Framework właśnie opublikował [świetny przewodnik](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) dotyczący łączenia przepływów pracy MAF z [AG-UI](https://github.com/ag-ui-protocol/ag-ui) — otwartym protokołem do strumieniowania zdarzeń wykonania agentów do frontendu przez Server-Sent Events. I szczerze? To jest właśnie ten most, którego nam brakowało.

## Dlaczego to ważne dla programistów .NET

Jeśli budujesz aplikacje oparte na AI, prawdopodobnie trafiłeś już na tę ścianę. Twoja orkiestracja backendowa działa świetnie — agenty przekazują sobie zadania, narzędzia się uruchamiają, decyzje są podejmowane. Ale frontend nie ma pojęcia, co dzieje się za kulisami. AG-UI rozwiązuje to, definiując standardowy protokół do strumieniowania zdarzeń agentów (takich jak `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) bezpośrednio do warstwy interfejsu przez SSE.

Demonstracja, którą zbudowali, to przepływ pracy obsługi klienta z trzema agentami: agent triaży kierujący żądaniami, agent zwrotów obsługujący pieniądze i agent zamówień zarządzający wymianami. Każdy agent ma własne narzędzia, a topologia przekazywania jest jawnie zdefiniowana — żadnego "wyczuj to z kontekstu prompta".

## Topologia przekazywania to prawdziwa gwiazda

Zwróciło moją uwagę to, jak `HandoffBuilder` pozwala zadeklarować skierowany graf routingu między agentami:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Każde `add_handoff` tworzy skierowaną krawędź z opisem w języku naturalnym. Framework generuje narzędzia przekazywania dla każdego agenta na podstawie tej topologii. Decyzje dotyczące routingu są zakorzenione w strukturze orkiestracji, a nie w tym, na co ma ochotę LLM. To ogromna rzecz dla niezawodności produkcji.

## Człowiek w pętli, który naprawdę działa

Demonstracja prezentuje dwa wzorce przerwań, które są potrzebne w każdej prawdziwej aplikacji agentowej:

**Przerwania zatwierdzania narzędzi** — gdy agent wywołuje narzędzie oznaczone jako `approval_mode="always_require"`, przepływ pracy wstrzymuje się i emituje zdarzenie. Frontend renderuje modal zatwierdzenia z nazwą narzędzia i argumentami. Żadnych pętli ponownych prób — tylko czysty przepływ wstrzymaj-zatwierdź-wznów.

**Przerwania żądania informacji** — gdy agent potrzebuje więcej kontekstu od użytkownika (jak numer zamówienia), wstrzymuje się i pyta. Frontend wyświetla pytanie, użytkownik odpowiada, a wykonanie wznawia się dokładnie tam, gdzie się zatrzymało.

Oba wzorce są strumieniowane jako standardowe zdarzenia AG-UI, więc frontend nie potrzebuje niestandardowej logiki dla każdego agenta — po prostu renderuje to, co przychodzi przez połączenie SSE.

## Podłączenie jest zaskakująco proste

Integracja między MAF a AG-UI to jedno wywołanie funkcji:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

`workflow_factory` tworzy nowy przepływ pracy dla każdego wątku, więc każda rozmowa otrzymuje izolowany stan. Endpoint automatycznie obsługuje całe "hydrauliczne" SSE. Jeśli już używasz FastAPI (lub możesz dodać go jako lekką warstwę), to właściwie zerowe tarcie.

## Moje zdanie

Dla nas, programistów .NET, natychmiastowe pytanie brzmi: "Czy mogę to zrobić w C#?" Agent Framework jest dostępny zarówno dla .NET, jak i Python, a protokół AG-UI jest niezależny od języka (to po prostu SSE). Więc choć ta konkretna demonstracja używa Python i FastAPI, wzorzec przekłada się bezpośrednio. Możesz podpiąć minimalne API ASP.NET Core z endpointami SSE zgodnie z tym samym schematem zdarzeń AG-UI.

Ważniejszy wniosek: interfejsy użytkownika dla wielu agentów stają się pierwszoklasowym zagadnieniem, a nie przemyśleniem. Jeśli budujesz cokolwiek, gdzie agenty wchodzą w interakcje z ludźmi — obsługa klienta, przepływy zatwierdzeń, przetwarzanie dokumentów — ta kombinacja orkiestracji MAF i przejrzystości AG-UI to wzorzec do naśladowania.

## Podsumowanie

AG-UI + Microsoft Agent Framework zapewnia to, co najlepsze z obu światów: solidną orkiestrację wieloagentową na backendzie i widoczność w czasie rzeczywistym na frontendzie. Koniec z interakcjami agentów jako czarną skrzynką.

Sprawdź [pełny przewodnik](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) i [repozytorium protokołu AG-UI](https://github.com/ag-ui-protocol/ag-ui), by zagłębić się w temat.
