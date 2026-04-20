---
title: "VS Code 1.112: co programiści .NET powinni naprawdę wiedzieć"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 właśnie wyszedł i jest pełen ulepszeń agentów, zintegrowanego debuggera przeglądarki, piaskownicy MCP i wsparcia dla monorepo. Oto co naprawdę ważne dla programistów .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-112-dotnet-developers" >}}).*

VS Code 1.112 właśnie wylądował i szczerze? Ten uderza inaczej, jeśli spędzasz dni w krainie .NET. Jest wiele w [oficjalnych notatkach wydania](https://code.visualstudio.com/updates/v1_112), ale pozwól, że oszczędzę ci przewijania i skupię się na tym, co naprawdę ważne dla nas.

## Copilot CLI stał się znacznie bardziej użyteczny

Główny temat tego wydania to **autonomia agentów** — danie Copilot więcej przestrzeni do działania bez nadzorowania każdego kroku.

### Kierowanie wiadomościami i kolejkowanie

Znasz ten moment, gdy Copilot CLI jest w połowie zadania i zdajesz sobie sprawę, że zapomniałeś czegoś wspomnieć? Wcześniej musiałeś czekać. Teraz możesz po prostu wysyłać wiadomości, gdy żądanie jest jeszcze w toku — albo by sterować bieżącą odpowiedzią, albo kolejkować kolejne instrukcje.

To ogromne dla dłuższych zadań szkieletowania `dotnet`, gdzie obserwujesz Copilot konfigurujący projekt i myślisz "och, poczekaj, potrzebuję też MassTransit tam".

### Poziomy uprawnień

To jest to, na czym mi najbardziej zależy. Sesje Copilot CLI obsługują teraz trzy poziomy uprawnień:

- **Domyślne uprawnienia** — zwykły przepływ, gdzie narzędzia proszą o potwierdzenie przed uruchomieniem
- **Pomiń zatwierdzenia** — automatycznie zatwierdza wszystko i ponawia przy błędach
- **Autopilot** — pełna autonomia: zatwierdza narzędzia, odpowiada na własne pytania i kontynuuje aż do zakończenia zadania

Jeśli robisz coś jak szkieletowanie nowego API ASP.NET Core z Entity Framework, migracjami i konfiguracją Docker — tryb Autopilot oznacza, że opisujesz co chcesz i idziesz po kawę. Samo to rozgryzie.

Możesz włączyć Autopilot z ustawieniem `chat.autopilot.enabled`.

### Podgląd zmian przed delegowaniem

Gdy delegujesz zadanie do Copilot CLI, tworzy on worktree. Wcześniej, jeśli miałeś niezatwierdzone zmiany, musiałeś sprawdzić Kontrolę źródła, by zobaczyć co zostanie dotknięte. Teraz widok Chat pokazuje oczekujące zmiany tam, zanim zdecydujesz czy je skopiować, przenieść czy zignorować.

Mała rzecz, ale oszczędza ten moment "poczekaj, co miałem w stanie staging?"

## Debuguj aplikacje webowe bez wychodzenia z VS Code

Zintegrowana przeglądarka obsługuje teraz **pełne debugowanie**. Możesz ustawiać punkty przerwania, przechodzić przez kod i inspekcjonować zmienne — wszystko wewnątrz VS Code. Koniec z przełączaniem się do Edge DevTools.

Jest nowy typ debugowania `editor-browser`, a jeśli masz już istniejące konfiguracje uruchamiania `msedge` lub `chrome`, migracja jest tak prosta jak zmiana pola `type` w `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Dla programistów Blazor to zmiana zasad gry. Już uruchamiasz `dotnet watch` w terminalu — teraz debugowanie też pozostaje w tym samym oknie.

Przeglądarka otrzymała też niezależne poziomy powiększenia (wreszcie), właściwe menu kontekstowe prawym przyciskiem i powiększenie jest zapamiętywane dla każdej witryny.

## Piaskownica serwerów MCP

Ta kwestia ma większe znaczenie niż mogłoby się wydawać. Jeśli używasz serwerów MCP — może skonfigurowałeś własny dla zasobów Azure lub zapytań do bazy danych — działały one z tymi samymi uprawnieniami co twój proces VS Code. To oznacza pełny dostęp do systemu plików, sieci, wszystkiego.

Teraz możesz je piaskownicować. W twoim `mcp.json`:

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

Gdy piaskownicowany serwer potrzebuje dostępu do czegoś, czego nie ma, VS Code prosi o przyznanie uprawnień. Znacznie lepsze niż podejście "mam nadzieję, że nikt nic dziwnego nie zrobi".

> **Uwaga:** Piaskownicowanie jest dostępne na macOS i Linux. Wsparcie dla Windows jest w planach — zdalne scenariusze jak WSL jednak działają.

## Odkrywanie dostosowań monorepo

Jeśli pracujesz w monorepo (a szczerze, wiele rozwiązań enterprise .NET kończy się jako jedno), to rozwiązuje realny problem.

Wcześniej, jeśli otwierałeś podfolder repozytorium, VS Code nie znajdował `copilot-instructions.md`, `AGENTS.md` ani własnych umiejętności siedzących w katalogu głównym repozytorium. Teraz z ustawieniem `chat.useCustomizationsInParentRepositories` chodzi w górę do korzenia `.git` i odkrywa wszystko.

To oznacza, że twój zespół może współdzielić instrukcje agenta, pliki promptów i własne narzędzia we wszystkich projektach w monorepo bez konieczności otwierania przez wszystkich folderu głównego.

## /troubleshoot do debugowania agentów

Kiedyś konfigurowałeś własne instrukcje lub umiejętności i zastanawiałeś się, dlaczego nie są wykrywane? Nowa umiejętność `/troubleshoot` czyta logi debugowania agenta i mówi ci co się stało — które narzędzia były użyte lub pominięte, dlaczego instrukcje się nie załadowały i co powoduje wolne odpowiedzi.

Włącz ją z:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Następnie po prostu wpisz `/troubleshoot dlaczego moja własna umiejętność się nie ładuje?` w czacie.

Możesz też teraz eksportować i importować te logi debugowania, co jest świetne do dzielenia się z zespołem, gdy coś nie działa zgodnie z oczekiwaniami.

## Wsparcie dla obrazów i plików binarnych

Agenty mogą teraz czytać pliki obrazów z dysku i pliki binarne natywnie. Pliki binarne są prezentowane w formacie hexdump, a wyjścia obrazów (jak zrzuty ekranu z zintegrowanej przeglądarki) pojawiają się w widoku karuzeli.

Dla programistów .NET, pomyśl: wklej zrzut ekranu błędu interfejsu do czatu i pozwól agentowi zrozumieć, co jest nie tak, lub każ mu przeanalizować wyjście renderowania komponentu Blazor.

## Automatyczne odwołania do symboli

Małe ulepszenie komfortu pracy: gdy kopiujesz nazwę symbolu (klasy, metody itp.) i wklejasz ją do czatu, VS Code teraz automatycznie konwertuje ją na odwołanie `#sym:Nazwa`. Daje to agentowi pełny kontekst dotyczący tego symbolu bez konieczności ręcznego dodawania go.

Jeśli chcesz zwykłego tekstu zamiast, użyj `Ctrl+Shift+V`.

## Wtyczki można teraz włączać/wyłączać

Wcześniej wyłączenie serwera MCP lub wtyczki oznaczało jej odinstalowanie. Teraz możesz je przełączać — globalnie i dla każdego obszaru roboczego. Kliknij prawym przyciskiem w widoku Extensions lub Customizations i gotowe.

Wtyczki z npm i pypi mogą też teraz się automatycznie aktualizować, choć poproszą o zatwierdzenie najpierw, ponieważ aktualizacje oznaczają uruchomienie nowego kodu na twoim komputerze.

## Podsumowanie

VS Code 1.112 wyraźnie mocno napiera na doświadczenie agentów — większa autonomia, lepsze debugowanie, ściślejsze bezpieczeństwo. Dla programistów .NET, zintegrowane debugowanie przeglądarki i ulepszenia Copilot CLI to wyróżniające się funkcje.

Jeśli jeszcze nie próbowałeś pełnej sesji Copilot CLI w trybie Autopilot dla projektu .NET, to wydanie jest dobrym momentem na start. Pamiętaj tylko, by ustawić uprawnienia i pozwolić mu działać.

[Pobierz VS Code 1.112](https://code.visualstudio.com/updates/v1_112) lub zaktualizuj z poziomu VS Code przez **Pomoc > Sprawdź dostępność aktualizacji**.
