---
title: "Microsoft Foundry kwiecień 2026: Foundry Local GA, GPT-5.5, CodeAct z Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Podsumowanie Foundry za kwiecień jest bogate: Foundry Local osiąga GA, pojawia się GPT-5.5, Agent Framework dostaje śledzenie OpenTelemetry, CodeAct uruchamia Python w mikro-maszynach wirtualnych Hyperlight, a Dashboard Monitorowania Agentów trafia na rynek."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Pracowity miesiąc dla Microsoft Foundry. Oto najważniejsze ogłoszenia.

## Foundry Local ogólnie dostępny

Foundry Local — wieloplatformowe lokalne środowisko uruchomieniowe AI od Microsoft — przeszło z wersji zapoznawczej do GA na Windows, macOS (Apple Silicon) i Linux x64. Gotowe do produkcji lokalne wnioskowanie modeli z przyjaznym dla programistów SDK. Wersja 1.1 dodaje obsługę transkrypcji, embeddings i Responses API.

## GPT-5.5

Najnowszy model w rodzinie GPT-5 jest teraz dostępny w Foundry. Domyślny przydział dla subskrypcji Tier 5 i Tier 6. Jeśli pracowałeś z wcześniejszymi wariantami GPT-5, warto go ocenić pod kątem swojego przypadku użycia.

## Śledzenie Agent Framework w Foundry

W tym miesiącu dwie funkcje śledzenia trafiają do wersji zapoznawczej:

**Śledzenie Microsoft Agent Framework** — Agenci MAF mogą teraz eksportować ślady OpenTelemetry do Foundry. Debuguj zachowanie agentów, śledź wieloetapowe wykonania, ujawniaj opóźnienia i błędy przy wywołaniach narzędzi. To wypełnia prawdziwą lukę: wiedza *co agent faktycznie zrobił w produkcji*, a nie tylko co zwrócił.

**Śledzenie hostowanych agentów** — Sesje, wywołania narzędzi i kroki uruchamiania hostowanych agentów również pojawiają się w śladach Foundry. Ta sama historia obserwowalności rozszerza się na warstwę hostowaną.

## CodeAct z Hyperlight (Alpha)

To jest technicznie najciekawsze uzupełnienie: Agent Framework może teraz wykonywać kod Python wewnątrz mikro-maszyn wirtualnych [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct to wzorzec, w którym agenci generują i wykonują kod Python jako narzędzie. Oczywiste obawy dotyczą bezpieczeństwa — uruchamiasz kod wygenerowany przez model. Mikro-maszyny wirtualne Hyperlight zapewniają izolację na poziomie procesu z czasami uruchomienia zbliżonymi do natywnych, dzięki czemu wykonywanie kodu w piaskownicy jest praktyczne bez narzutu pełnych kontenerów lub maszyn wirtualnych.

Dla przepływów pracy agentów wymagających wykonywania kodu jest to znaczące ulepszenie bezpieczeństwa w porównaniu z uruchamianiem kodu w procesie hosta.

## Dashboard Monitorowania Agentów (Wersja zapoznawcza)

Ujednolicony operacyjny dashboard łączący zużycie tokenów, opóźnienia, wskaźnik powodzenia uruchomień i wyniki ewaluatorów w jednym widoku. Różnica od zwykłych dashboardów obserwowalności: zawiera wyniki ewaluacji obok metryk operacyjnych, dzięki czemu możesz powiązać "agent stał się wolniejszy" z "wyniki ewaluatora spadły" — lub potwierdzić, że są niezwiązane.

## Niestandardowi ewaluatorzy ciągłej ewaluacji (Wersja zapoznawcza)

Możesz teraz wprowadzać własnych ewaluatorów opartych na kodzie lub promptach do potoku ciągłej ewaluacji. Wcześniej ciągła ewaluacja była ograniczona do wbudowanych ewaluatorów. Niestandardowi ewaluatorzy pozwalają stosować specyficzne dla zespołu standardy jakości w pętli monitorowania produkcji.

## Inwentarz agentów w Control Plane

Widok Operate w Foundry Control Plane pokazuje teraz wszystkich obsługiwanych agentów w całej subskrypcji: agentów Foundry, Azure SRE Agent, pętle agentów Logic Apps i zarejestrowanych niestandardowych agentów. Jeden widok, aby zrozumieć, co jest wdrożone i gdzie.

Oryginalny post: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
