---
title: "Aktualizacje Azure Developer CLI (azd) na kwiecień 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd wydał pięć wersji w kwietniu 2026, z główną funkcją wsparcia hooków w wielu językach dla Python, JavaScript, TypeScript i .NET — plus publiczna wersja zapoznawcza azd update, wstępne sprawdzanie limitów przydziałów AI i więcej."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Azure Developer CLI (azd) wydał pięć wersji w kwietniu 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (od 1.23.14 do 1.24.2), z głównym tematem hooków uruchamianych teraz w Pythonie, JavaScript, TypeScript i .NET — nie tylko w Bash i PowerShell.

## Hooki w wielu językach w azure.yaml

Hooki mogą teraz wskazywać pliki `.py`, `.js`, `.ts` lub `.cs` oprócz skryptów powłoki. Każdy język otrzymuje automatyczne rozwiązywanie zależności:

- **Python** — wykrywa `requirements.txt` lub `pyproject.toml`, tworzy virtualenv i instaluje zależności przed uruchomieniem. Nazwę środowiska konfiguruje się za pomocą `virtualEnvName`.
- **JavaScript / TypeScript** — wykrywa `package.json` i automatycznie uruchamia `npm install`. TypeScript jest wykonywany przez `npx tsx` bez kroku kompilacji. Menedżer pakietów wybiera się za pomocą bloku konfiguracji `packageManager`.
- **.NET** — uruchamia pliki `.cs` za pomocą `dotnet run`. Skrypty jednoplikowe są obsługiwane w .NET 10+. Docelowy framework konfiguruje się przez blok `configuration/framework`.

Oznacza to, że zespoły pracujące już w jednym z tych języków nie muszą utrzymywać oddzielnego hooka Bash lub PowerShell tylko po to, by podłączyć zdarzenia cyklu życia aprowizacji.

## azd update w publicznej wersji zapoznawczej

`azd update` jest teraz w publicznej wersji zapoznawczej na wszystkich platformach. Jedno polecenie obsługuje aktualizację niezależnie od tego, jak azd był pierwotnie zainstalowany — nie trzeba już osobno śledzić ścieżek Homebrew, WinGet lub MSI.

## Tryb nieinteraktywny przez AZD_NON_INTERACTIVE

Ustawienie `AZD_NON_INTERACTIVE=true` (lub użycie `--non-interactive` / `--no-prompt`) generuje teraz spójne, deterministyczne błędy w potokach CI/CD, gdy wymagane dane wejściowe nie mogą być rozwiązane automatycznie. Wcześniej zachowanie było niespójne w różnych poleceniach.

## Wstępne sprawdzanie limitu przydziałów modeli AI

`azd provision` weryfikuje limit przydziałów Azure Cognitive Services przed próbą aprowizacji zasobów modeli AI. Wdrożenia, które zakończyłyby się niepowodzeniem z powodu limitów przydziałów, teraz pokazują błąd wcześnie w procesie, zamiast w połowie aprowizacji.

## „Napraw ten błąd" w rozwiązywaniu problemów z Copilot

Integracja rozwiązywania problemów z Copilot w azd zyskuje możliwość bezpośredniego zastosowania sugerowanej poprawki — nie tylko jej opisania. Gdy agent identyfikuje naprawialny problem, może dokonać zmiany na miejscu.

## Niestandardowi dostawcy aprowizacji i resolver sekretów Key Vault

Autorzy rozszerzeń mogą teraz rejestrować alternatywne backendy infrastruktury za pomocą `WithProvisioningProvider()`. Oddzielnie, azd automatycznie rozwiązuje odwołania `@Microsoft.KeyVault(...)` przed przekazaniem konfiguracji do rozszerzeń, eliminując potrzebę ręcznego rozwiązywania sekretów w niestandardowych dostawcach.

## Wykluczenia dla szablonów i trybu obserwacji

Dwa nowe pliki ignore zapewniają dokładniejszą kontrolę nad obsługą plików:
- **`.azdignore`** — wyklucza pliki przeznaczone tylko dla współtwórców (dokumentacja, konfiguracje CI) z kopii szablonów, aby użytkownicy końcowi otrzymali czysty szkielet projektu.
- **`.azdxignore`** — wyklucza katalogi z wyzwalania przebudów podczas `azd x watch`, zmniejszając szum podczas iteracyjnego tworzenia.

## Wstępne sprawdzanie zarezerwowanych nazw i opcja docker.network

azd ostrzega teraz, gdy przewidywane nazwy zasobów zawierałyby zarezerwowane słowa Azure (`MICROSOFT`, `WINDOWS` lub prefiks `LOGIN`) przed rozpoczęciem aprowizacji. Nowa opcja `docker.network` przekazuje `--network` do `docker build`, co jest przydatne w środowiskach proxy korporacyjnych wymagających określonej sieci Docker.

## Poprawki bezpieczeństwa

Pakiet MSI dla Windows zawiera teraz weryfikację podpisu kodu. Oddzielna poprawka zamyka wyciek zmiennych środowiskowych, który mógł ujawnić wartości przez granice poleceń rozszerzeń.

---

Pracowity miesiąc — wsparcie hooków w wielu językach szczególnie usuwa prawdziwy punkt tarcia dla zespołów, które nie pracują głównie w Bash. Pełny dziennik zmian dla wszystkich pięciu wersji znajdziesz w [pełnych notach wydania](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/).
