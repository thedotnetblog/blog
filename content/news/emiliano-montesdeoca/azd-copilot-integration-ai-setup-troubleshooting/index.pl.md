---
title: "azd + GitHub Copilot: Konfiguracja projektu z AI i inteligentne rozwiązywanie błędów"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI integruje się teraz z GitHub Copilot, żeby wygenerować infrastrukturę projektu i naprawiać błędy wdrożeń — bez wychodzenia z terminala."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Ten artykuł został przetłumaczony automatycznie. Oryginalną wersję angielską znajdziesz [tutaj]({{< ref "index.md" >}}).*

Znasz ten moment, gdy chcesz wdrożyć istniejącą aplikację na Azure i patrzysz na pusty `azure.yaml`, próbując przypomnieć sobie, czy Twoje Express API powinno używać Container Apps czy App Service? Ten moment właśnie stał się znacznie krótszy.

Azure Developer CLI (`azd`) integruje się teraz z GitHub Copilot na dwa konkretne sposoby: scaffolding projektu wspomagany przez AI podczas `azd init` oraz inteligentne rozwiązywanie błędów gdy wdrożenia kończą się niepowodzeniem. Obie funkcje działają całkowicie w terminalu.

## Konfiguracja z Copilotem podczas azd init

Po uruchomieniu `azd init` pojawia się opcja "Set up with GitHub Copilot (Preview)". Wybierz ją, a Copilot przeanalizuje Twój codebase i wygeneruje `azure.yaml`, szablony infrastruktury oraz moduły Bicep — na podstawie Twojego rzeczywistego kodu.

```
azd init
# Wybierz: "Set up with GitHub Copilot (Preview)"
```

Wymagania:

- **azd 1.23.11 lub nowszy** — sprawdź przez `azd version` lub zaktualizuj przez `azd update`
- **Aktywna subskrypcja GitHub Copilot** (Individual, Business lub Enterprise)
- **GitHub CLI (`gh`)** — `azd` poprosi o logowanie jeśli potrzeba

To co uważam za naprawdę użyteczne: działa w obu kierunkach. Budujesz od zera? Copilot pomaga skonfigurować właściwe usługi Azure od początku. Masz istniejącą aplikację do wdrożenia? Wskaż Copilotem na nią — konfiguracja zostanie wygenerowana bez konieczności restrukturyzacji kodu.

### Co faktycznie robi

Powiedzmy, że masz Node.js Express API z zależnością od PostgreSQL. Zamiast ręcznie wybierać między Container Apps a App Service, a potem pisać Bicep od zera, Copilot wykrywa Twój stack i generuje:

- `azure.yaml` z właściwymi ustawieniami `language`, `host` i `build`
- Moduł Bicep dla Azure Container Apps
- Moduł Bicep dla Azure Database for PostgreSQL

Przed jakąkolwiek zmianą przeprowadzane są wstępne sprawdzenia — weryfikuje czystość katalogu roboczego git, pyta z wyprzedzeniem o zgodę na narzędzia serwera MCP. Nic nie dzieje się bez Twojej wiedzy.

## Rozwiązywanie błędów z Copilotem

Błędy wdrożenia są nieuniknione. Brakujące parametry, problemy z uprawnieniami, dostępność SKU — a komunikat o błędzie rzadko mówi to, co naprawdę musisz wiedzieć: *jak to naprawić*.

Bez Copilota pętla wygląda tak: skopiuj błąd → szukaj w dokumentacji → czytaj trzy niepowiązane odpowiedzi na Stack Overflow → uruchom kilka poleceń `az` CLI → spróbuj ponownie. Z Copilotem w `azd` ta pętla znika. Gdy jakiekolwiek polecenie `azd` kończy się błędem, natychmiast oferuje cztery opcje:

- **Explain** — wyjaśnienie w zrozumiałym języku, co poszło nie tak
- **Guidance** — instrukcje krok po kroku jak naprawić problem
- **Diagnose and Guide** — pełna analiza + Copilot stosuje poprawkę (za Twoją zgodą) + opcjonalne ponowienie
- **Skip** — samodzielna obsługa

Kluczowa kwestia: Copilot ma już kontekst Twojego projektu, nieudanego polecenia i szczegółów błędu. Jego sugestie są specyficzne dla *Twojej sytuacji*.

### Ustawianie domyślnego zachowania

Jeśli zawsze wybierasz tę samą opcję, pomiń interaktywny monit:

```
azd config set copilot.errorHandling.category troubleshoot
```

Wartości: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Możesz też włączyć automatyczną naprawę i ponowienie:

```
azd config set copilot.errorHandling.fix allow
```

Powrót do trybu interaktywnego w dowolnym momencie:

```
azd config unset copilot.errorHandling.category
```

## Podsumowanie

Uruchom `azd update` po najnowszą wersję i wypróbuj `azd init` w swoim następnym projekcie.

Przeczytaj [oryginalny komunikat tutaj](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
