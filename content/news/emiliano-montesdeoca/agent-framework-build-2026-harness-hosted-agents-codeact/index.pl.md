---
title: "Agent Harness, Hosted Agents i CodeAct: to właśnie na tę aktualizację Agent Framework zwróciłbym uwagę"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Zapowiedź Agent Framework na Build 2026 jest pełna treści, ale najważniejsze wątki to model harness, hostowane agenty w Foundry i CodeAct, który zmniejsza narzut orkiestracji."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Duże ogłoszenie Agent Framework na Build obejmuje wiele, ale trzy motywy od razu się wyróżniają:

- **harness staje się bardziej pełnoprawnym elementem środowiska uruchomieniowego**
- **hostowane agenty Foundry dają drogę do produkcji**
- **CodeAct zmniejsza narzut orkiestracji wieloetapowej**

Na te trzy rzeczy zwróciłbym uwagę.

## Harness staje się prawdziwym centrum ciężkości

Post źródłowy opisuje harness jako warstwę, w której rozumowanie modelu spotyka się z rzeczywistym wykonaniem.

To trafny opis, ale też powód, dla którego uważam, że ten element ma większe znaczenie niż wiele pojedynczych punktów funkcyjnych.

Gdy agent potrzebuje:

- dostępu do plików
- uruchamiania poleceń w shellu
- trybów planowania
- list zadań
- pamięci sesji
- przepływów akceptacji

nie mówisz już o samym prompcie i modelu.

Mówisz o zachowaniu środowiska uruchomieniowego.

To właśnie tam frameworki stają się naprawdę użyteczne albo zamieniają się w zabawki.

I Microsoft Agent Framework wyraźnie próbuje stać się bardziej użyteczny właśnie na tej warstwie.

## Hostowane agenty są miejscem, w którym historia od lokalnego uruchomienia do produkcji staje się realna

Myślę też, że część z hosted agents jest jednym z najważniejszych strategicznie elementów tej zapowiedzi.

Post źródłowy wprost mówi, że to najłatwiejszy sposób, by dać temu agentowi dom w produkcji.

To sformułowanie ma znaczenie, bo większość frameworków agentowych wciąż jest znacznie silniejsza w lokalnych eksperymentach niż w operacyjnym wdrożeniu.

Jeśli hostowane agenty Foundry sprawią, że przejście z lokalnego developmentu do:

- skalowania
- obserwowalności
- zarządzanej tożsamości
- obsługi sesji
- wersjonowania

będzie wyraźnie łatwiejsze, to zamknie to jedną z największych luk w obecnym ekosystemie agentów.

To znacząca poprawa.

## CodeAct to najbardziej ekscytujący techniczny pomysł w tej aktualizacji

Gdybym miał wybrać najciekawszy koncept techniczny z tego wpisu, prawdopodobnie wybrałbym CodeAct.

Problem, który próbuje rozwiązać, jest bardzo realny: zbyt wiele wieloetapowych workflow agentowych jest kosztownych, bo sama pętla orkiestracji zużywa zbyt wiele kroków modelu.

Więc gdy post źródłowy pokazuje wynik taki jak:

- 52.4% szybciej
- 63.9% mniej tokenów

od razu zwraca to moją uwagę.

Oczywiście są to liczby benchmarkowe powiązane z reprezentatywnym obciążeniem, a nie uniwersalne prawo. Ale szerszy pomysł nadal jest bardzo przekonujący.

Jeśli model potrafi skompresować łańcuch wywołań narzędzi do bardziej wydajnej formy wykonania, ekonomia systemów agentowych może się wyraźnie zmienić.

## To, co moim zdaniem deweloperzy powinni z tej aktualizacji naprawdę wynieść

Najważniejsza lekcja nie brzmi, ile funkcji dostarczono.

Najważniejsze jest to, że framework wzmacnia się tam, gdzie prawdziwe aplikacje potrzebują tego najbardziej:

- runtime shell
- ścieżka wdrożenia
- wydajność wykonania
- wbudowane wzorce operacyjne

Taki sygnał dojrzałości ma dla mnie znacznie większą wartość niż kolejna powierzchowna lista funkcji AI.

## Moja ocena

Ta aktualizacja ma znaczenie, bo nie tylko dodaje więcej powierzchni.

Wzmacnia historię runtime i wdrożenia wokół agentów w sposób, który powinien mieć znaczenie dla prawdziwych aplikacji, zwłaszcza dla zespołów, które chcą przejść od lokalnych eksperymentów do systemów, które naprawdę da się uruchamiać i utrzymywać.

Właśnie tam framework staje się bardziej przekonujący.

A gdybym śledził to wydanie uważnie, harness, hosted agents i CodeAct byłyby bez wątpienia trzema rzeczami, na których skupiłbym najwięcej uwagi.

Oryginalny wpis: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
