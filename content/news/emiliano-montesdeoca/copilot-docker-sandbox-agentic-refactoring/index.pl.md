---
title: "Docker Sandbox Pozwala Agentom Copilot Refaktoryzować Kod Bez Ryzyka dla Twojej Maszyny"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox daje agentom GitHub Copilot bezpieczne mikroVM do szalonych refaktoryzacji — bez monitów o uprawnienia, bez ryzyka dla hosta. Oto dlaczego to zmienia wszystko dla dużoskalowej modernizacji .NET."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Jeśli używałeś trybu agenta Copilota do czegoś poza małymi edytami, znasz ten ból. Każdy zapis pliku, każde polecenie terminala — kolejny monit o uprawnienia.

Zespół Azure właśnie opublikował post o [Docker Sandbox dla agentów GitHub Copilot](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/).

## Co Docker Sandbox faktycznie daje

Podstawowy pomysł jest prosty: uruchom lekkie mikroVM z pełnym środowiskiem Linux, zsynchronizuj workspace, i pozwól agentowi Copilota działać swobodnie wewnątrz.

To więcej niż "uruchamiaj rzeczy w kontenerze":
- **Dwukierunkowa synchronizacja workspace** z zachowaniem ścieżek absolutnych
- **Prywatny demon Docker** działający w mikroVM
- **Filtrujące proxy HTTP/HTTPS** kontrolujące dostęp sieciowy
- **Tryb YOLO** — agent działa bez monitów o uprawnienia

## Dlaczego deweloperzy .NET powinni to wziąć pod uwagę

Dzięki Docker Sandbox możesz wskazać agenta Copilota na projekt, pozwolić mu swobodnie refaktoryzować wewnątrz mikroVM, uruchomić `dotnet build` i `dotnet test`, i akceptować tylko zmiany, które faktycznie działają.

Post opisuje uruchamianie **floty równoległych agentów** — każdy we własnym sandboxie — pracujących nad różnymi projektami jednocześnie.

## Wniosek

Docker Sandbox rozwiązuje fundamentalne napięcie w agentic coding: agenty potrzebują wolności, żeby być użyteczne, ale wolność na Twojej maszynie hosta jest niebezpieczna. MicroVM dają ci obie.
