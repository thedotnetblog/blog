---
title: "FIDES to dokładnie taki deterministyczny temat bezpieczeństwa agentów, który chcę widywać częściej"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Nowe możliwości FIDES w Agent Framework są ważne, ponieważ przesuwają obronę przed prompt injection z heurystyk w stronę egzekwowalnej polityki opartej na oznaczonych treściach i kontrolach middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Ten wpis został przetłumaczony automatycznie. Aby zobaczyć oryginał, [kliknij tutaj]({{< ref "index.md" >}}).*

Obrona przed prompt injection często sprawia wrażenie, jakby stała na chwiejnej ziemi.

Dodajesz mocniejszy system prompt. Dodajesz filtr. Ustawiasz kilka allowlist. I liczysz, że następne dziwne wejście nie złamie założeń.

Dlatego **FIDES** jest interesujący.

Mocna strona tej historii polega na tym, że przesuwa bezpieczeństwo w stronę czegoś bardziej deterministycznego:

- oznaczenia treści
- propagacja oznaczeń przez workflow
- egzekwowanie przez middleware przed uruchomieniem uprzywilejowanych narzędzi
- jasne granice polityki wokół tego, na co może wpływać nieufny kontekst

## Artykuł źródłowy mówi wprost w dobrym sensie

Otwiera go stwierdzenie, że prompt injection to "**zagrożenie numer 1 w OWASP LLM Top 10**".

Dobrze.

Lubię taką bezpośredniość, bo zbyt wiele zespołów nadal traktuje bezpieczeństwo agentów tak, jakby było problemem przyszłości, a nie aktualnym problemem projektowania runtime.

Artykuł idzie dalej z mocnym praktycznym kontrastem: większość obecnych zabezpieczeń jest heurystyczna, podczas gdy FIDES próbuje przesunąć system w stronę polityki i egzekwowania.

To jest dokładnie właściwa zmiana.

## Co czyni to bardziej przekonującym niż kolejny whitepaper o bezpieczeństwie

Wiele tekstów o bezpieczeństwie AI pozostaje abstrakcyjnych.

Ten artykuł robi coś lepszego. Przechodzi przez bardzo konkretny przykład: agenta do triage issue GitHub, złośliwy body issue, uprzywilejowany odczyt pliku i próbę wycieku publicznego komentarza.

To jest użyteczne, bo osadza całą dyskusję w rzeczywistym workflow.

I kiedy zobaczysz ten scenariusz, wartość deterministycznych kontroli staje się dużo łatwiejsza do zrozumienia.

## Kluczowy pomysł nie brzmi „zrób model mądrzejszym”

Najważniejsze tutaj jest to, że FIDES nie prosi modelu o magicznie lepsze wykrywanie ataków.

Zmienia kontrakt runtime.

To oznacza:

- treści są oznaczane
- oznaczenia propagują się dalej
- narzędzia deklarują, co akceptują
- middleware blokuje niebezpieczne ścieżki przed wykonaniem

To znacznie zdrowsze podejście.

Bo gdy agent może wywoływać narzędzia z realnymi konsekwencjami, bezpieczeństwo nie może zależeć tylko od tego, czy model ma dobry dzień.

## Moja opinia

To dokładnie taki kierunek w bezpieczeństwie agentów, który chcę widywać częściej.

Nie „zaufaj modelowi, że zignoruje złe instrukcje”, tylko „wbuduj policy fence w runtime”.

To znacznie zdrowszy model.

I jeśli frameworki agentów mają być traktowane poważnie w produkcji, będą potrzebowały więcej takich historii.

Oryginalny wpis: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)