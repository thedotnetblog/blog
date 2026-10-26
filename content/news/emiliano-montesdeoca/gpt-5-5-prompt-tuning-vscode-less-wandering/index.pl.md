---
title: "Strojenie Promptów GPT-5.5 w VS Code Udowadnia Trudną Prawdę: Projekt Harnessa Liczy Się Bardziej Niż Szum"
date: 2026-07-17
author: Emiliano Montesdeoca
description: "Eksperyment VS Code z GPT-5.5 pokazuje, że wymierne zyski pochodzą z zdyscyplinowanego projektowania harnessa i iteracji promptów, a nie tylko z wymiany na nowsze modele fundamentowe."
tags:
  - VS Code
  - GPT-5.5
  - Prompt Engineering
  - AI Agents
  - Developer Tools
  - Benchmarking
---

Najbardziej wartościową częścią wpisu o strojeniu GPT-5.5 w VS Code nie jest zwycięski wariant. To metodologia. Jasna hipoteza, kontrolowane zabiegi, pomiary na żywym ruchu i metryki barier ochronnych – to dokładnie to, jak jakość agentów powinna być ulepszana w środowiskach produkcyjnych.

Oryginalne źródło: https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers

Podstawowa idea była prosta: zmniejszyć dryf eksploracyjny i wcześniej walidować po edycjach. Brzmi oczywiście, ale interesującym odkryciem jest to, że strukturalne wskazówki promptowe na poziomie harnessa przyniosły statystycznie silne ulepszenia w opóźnieniu, zużyciu tokenów ogona i liczbie wywołań narzędzi bez poważnego załamania jakości.

Moje zdanie jest dosadne: **organizacje, które gonią tylko za aktualizacjami modeli, zostawiają na stole łatwe zyski wydajnościowe i kosztowe**. Zachowanie harnessa i projekt promptu systemowego mogą przesuwać metryki biznesowe szybciej niż zmiana modelu, zwłaszcza przy rozliczeniach opartych na użyciu.

**Wariant B wygrał**, ponieważ sformalizował pełną pętlę, a nie tylko ograniczenie wyszukiwania. Zachęcił model do sformułowania lokalnej falsyfikowalnej hipotezy, wykonania ugruntowanej pierwszej edycji i przeprowadzenia natychmiastowej skoncentrowanej walidacji. Ta sekwencja odzwierciedla to, jak dobrzy inżynierowie debugują pod presją czasu.

### Co skopiować z tego podejścia

- **Zdefiniuj bariery ochronne jakości z góry**, a następnie optymalizuj pod kątem opóźnienia i kosztów w ramach tych ograniczeń.
- **Mierz zarówno medianę, jak i zachowanie ogona.** Ulepszenia p95 w czasie do pierwszej edycji i zużyciu tokenów są często cenniejsze niż zwycięstwa p50 dla rzeczywistej satysfakcji użytkownika.
- **Unikaj przetrenowania na samych ewaluacjach offline.** Zespół VS Code użył kontroli offline, a następnie walidował na żywym ruchu przed wdrożeniem. Ta kolejność ma znaczenie, ponieważ prawdziwe przepływy pracy ujawniają zachowania, które syntetyczne benchmarki pomijają.

Jeden kompromis zasługuje na uwagę: niewielki ruch w krótkoterminowych metrykach przetrwania. Zespół poradził sobie z tym prawidłowo, ważąc wielkość efektu i istotność statystyczną przeciwko silniejszym, wysoce istotnym zyskom wydajnościowym. To dojrzałe podejmowanie decyzji, a nie wybiórcze dobieranie metryk.

Szersza lekcja jest **strategiczna**. Inżynieria promptów to nie „magia promptów". To **inżynieria produktu**: hipotezy, eksperymenty, kontrole i bramki wdrożeniowe. Zespoły, które operacjonalizują tę pętlę, będą się stale poprawiać. Zespoły, które debatują o rankingach modeli w mediach społecznościowych, nie.

## Konkluzja

W nadchodzącym roku przewaga konkurencyjna w AI dla programistów będzie pochodzić mniej z dostępu do konkretnej rodziny modeli, a bardziej z **tego, kto potrafi niezawodnie prowadzić tę pętlę optymalizacyjną**. Wyniki VS Code to praktyczny plan: obserwuj, hipotezuj, testuj, wysyłaj, powtarzaj.