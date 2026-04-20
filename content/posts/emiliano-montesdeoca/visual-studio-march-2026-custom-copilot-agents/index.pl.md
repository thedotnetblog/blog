---
title: "Aktualizacja Visual Studio z marca pozwala budować własne agenty Copilot — a narzędzie find_symbol to poważna sprawa"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Aktualizacja Visual Studio z marca 2026 dostarcza własne agenty Copilot, wielokrotnego użytku umiejętności agentów, świadome języka narzędzie find_symbol i profilowanie wspomagane przez Copilot z Test Explorer. Oto co ważne."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "visual-studio-march-2026-custom-copilot-agents" >}}).*

Visual Studio właśnie otrzymało swoją najważniejszą aktualizację Copilot do tej pory. Mark Downie [ogłosił wydanie marcowe](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), a nagłówek to własne agenty — ale szczerze, narzędzie `find_symbol` zakopane głębiej może być funkcją, która najbardziej zmieni twój przepływ pracy.

Pozwól, że rozbiję to, co tu faktycznie jest.

## Własne agenty Copilot w twoim repozytorium

Chcesz, by Copilot przestrzegał standardów kodowania twojego zespołu, uruchamiał twój potok kompilacji lub odpytywał wewnętrzną dokumentację? Teraz możesz zbudować dokładnie to.

Własne agenty są definiowane jako pliki `.agent.md`, które wrzucasz do `.github/agents/` w swoim repozytorium. Każdy agent ma pełny dostęp do świadomości przestrzeni roboczej, zrozumienia kodu, narzędzi, preferowanego modelu i połączeń MCP z zewnętrznymi usługami. Pojawiają się w selektorze agentów obok wbudowanych.

To ten sam wzorzec, który VS Code wspierał — i wspaniale zobaczyć, że Visual Studio nadrabia. Dla zespołów, które już zbudowały agenty dla VS Code, twoje pliki `.agent.md` powinny działać w obu IDE (choć nazwy narzędzi mogą się różnić, więc testuj).

Repozytorium [awesome-copilot](https://github.com/github/awesome-copilot) ma konfiguracje agentów dostarczane przez społeczność, których możesz użyć jako punktów startowych.

## Umiejętności agentów: wielokrotnego użytku pakiety instrukcji

Umiejętności są automatycznie wykrywane z `.github/skills/` w twoim repozytorium lub `~/.copilot/skills/` w twoim profilu. Każda umiejętność to plik `SKILL.md` zgodny ze [specyfikacją Agent Skills](https://agentskills.io/specification).

Pomyśl o umiejętnościach jak o modułowej wiedzy specjalistycznej, którą możesz mieszać i dopasowywać. Możesz mieć umiejętność dla konwencji API, inną dla wzorców testowania i jeszcze inną dla przepływu wdrożenia. Gdy umiejętność jest aktywowana, pojawia się w czacie, abyś wiedział, że jest stosowana.

Jeśli używasz umiejętności w VS Code, działają one tak samo w Visual Studio teraz.

## find_symbol: nawigacja z wiedzą o języku dla agentów

Tu robi się naprawdę interesująco. Nowe narzędzie `find_symbol` daje trybowi agenta Copilot faktyczną nawigację po symbolach zasilaną przez usługi językowe. Zamiast przeszukiwać kod jak tekst, agent może:

- Znaleźć wszystkie odwołania do symbolu w twoim projekcie
- Uzyskać informacje o typach, deklaracje i metadane zakresu
- Nawigować po miejscach wywołania z pełną świadomością językową

Co to oznacza w praktyce: gdy pytasz Copilot o refaktoryzację metody lub aktualizację sygnatury parametru w miejscach wywołania, może faktycznie zobaczyć strukturę twojego kodu. Koniec z sytuacjami "agent zmienił metodę, ale pominął trzy miejsca wywołania".

Obsługiwane języki to C#, C++, Razor, TypeScript i wszystko z obsługiwanym rozszerzeniem LSP. Dla programistów .NET to ogromna poprawa — bazy kodu C# z głębokimi hierarchiami typów i interfejsami ogromnie korzystają z nawigacji świadomej symboli.

## Profilowanie testów z Copilot

W menu kontekstowym Test Explorer jest teraz polecenie **Profiluj z Copilot**. Wybierz test, kliknij profiluj, a Agent Profilowania automatycznie go uruchamia i analizuje wydajność — łącząc dane użycia CPU i instrumentacji, by dostarczyć praktycznych spostrzeżeń.

Koniec z ręcznym konfigurowaniem sesji profilera, uruchamianiem testu, eksportowaniem wyników i próbą odczytania wykresu płomieni. Agent robi analizę i mówi ci, co jest wolne i dlaczego. Aktualnie tylko dla .NET, co ma sens, biorąc pod uwagę głęboką integrację diagnostyki .NET w Visual Studio.

## Wskazówki dotyczące wydajności podczas debugowania na żywo

Optymalizacja wydajności dzieje się teraz podczas debugowania, a nie po. Gdy przechodzisz przez kod, Visual Studio wyświetla czas wykonania i sygnały wydajności inline. Widzisz wolną linię? Kliknij Wskazówkę Wydajności i poproś Copilot o sugestie optymalizacji zaraz tam.

Agent Profilowania automatycznie przechwytuje dane czasu działania — czas, użycie CPU, zachowanie pamięci — a Copilot używa ich do wskazania gorących miejsc. Dzięki temu praca z wydajnością jest częścią twojego przepływu debugowania, a nie osobnym zadaniem, które ciągle odkładasz.

## Naprawianie luk bezpieczeństwa NuGet z Eksploratora rozwiązań

Gdy zostanie wykryta luka w pakiecie NuGet, zobaczysz teraz powiadomienie z linkiem **Napraw z GitHub Copilot** bezpośrednio w Eksploratorze rozwiązań. Kliknij i Copilot analizuje lukę, rekomenduje odpowiednie aktualizacje pakietów i je implementuje.

Dla zespołów, które mają problem z utrzymywaniem aktualnych zależności (a to właściwie wszyscy), usuwa to tarcie "wiem, że jest luka, ale wypracowanie właściwej ścieżki aktualizacji to projekt sam w sobie."

## Podsumowanie

Własne agenty i umiejętności to nagłówek, ale `find_symbol` to ukryty hit — fundamentalnie zmienia dokładność Copilot przy refaktoryzacji kodu .NET. W połączeniu z integracją profilowania na żywo i naprawianiem luk bezpieczeństwa, ta aktualizacja sprawia, że funkcje AI Visual Studio wydają się naprawdę praktyczne, a nie tylko gotowe do demonstracji.

Pobierz [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/), by wypróbować wszystko.

