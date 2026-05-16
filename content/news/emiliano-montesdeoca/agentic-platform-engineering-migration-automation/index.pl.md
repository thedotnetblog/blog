---
title: "Eliminowanie Monotonnej Pracy Migracji z Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape przeprowadza przez migrację prawdziwego wdrożenia AWS Terraform do Azure Bicep — ekstrahując intencję wdrożenia i przemapowując architekturę zamiast wykonywać konwersję składni 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — przewodnik po Git-Ape (narzędzie git do agentycznej inżynierii platform), które migruje prawdziwe repozytorium AWS Terraform do Azure, skupiając się na ekstrakcji intencji zamiast konwersji linia po linii.

## Dane wejściowe: contoso-migration

Źródłem jest prawdziwy projekt Terraform (`contoso-migration`), który wdraża aplikację Next.js na AWS — EC2 do obliczeń, ALB do równoważenia obciążenia, S3 do artefaktów i klucze IAM do tożsamości. Koszt: ~34 $/miesiąc. Celem nie jest odtworzenie tej samej infrastruktury na Azure; chodzi o zrozumienie, co wdrożenie naprawdę próbuje osiągnąć, i odbudowanie tego przy użyciu natywnych usług Azure.

## Krok 1: Walidacja i uwierzytelnienie

Git-Ape rozpoczyna od walidacji wszystkich wymaganych narzędzi CLI — `az`, `aws`, `gh`, `jq`, `git` — i potwierdzenia aktywnych sesji uwierzytelniania przed dotknięciem czegokolwiek. Bez częściowych uruchomień.

## Krok 2: Ekstrakcja intencji

Agent odczytuje całe repozytorium źródłowe przez API GitHub i wyodrębnia intencję wdrożenia: środowisko uruchomieniowe (Node.js), typ obliczeń, wzorzec ingress, obsługę artefaktów, model tożsamości, sieć i monitoring. To jest kluczowy krok — buduje model semantyczny tego, co robi wdrożenie, a nie jakich słów kluczowych Terraform używa.

## Krok 3: Mapowanie usług

Usługi AWS są mapowane na odpowiedniki Azure:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Wbudowane równoważenie obciążenia App Service
- Role/klucze IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Krok 4: Agent krytyczny

Przed wygenerowaniem wyjścia uruchamia się agent krytyczny i wykrywa dwa blokujące problemy:

1. **Anty-wzorzec build-on-startup** — oryginalny Terraform uruchamiał `npm install && npm run build` na EC2 przy starcie. Poprawka: zbuduj w CI, wdróż gotowy artefakt.
2. **Niepotrzebny Blob Storage** — S3 był używany do przygotowywania artefaktów, co można wyeliminować przy odpowiednim CI/CD. Agent krytyczny usunął go całkowicie.

## Krok 5: Wygenerowane wyjście

Wynikiem jest ~80 linii Bicep zamiast oryginalnych ponad 200 linii Terraform. Agent utworzył nowe repozytorium GitHub z `infra/main.bicep` i `.github/workflows/deploy.yml` oraz usunął wszystkie pliki specyficzne dla AWS.

## Porównanie postawy bezpieczeństwa

Migracja przyniosła również znaczącą poprawę bezpieczeństwa:

| AWS oryginał | Wyjście Azure |
|---|---|
| Tylko HTTP | Tylko HTTPS, TLS 1.2 |
| SSH otwarte na 0.0.0.0/0 | Brak ekspozycji SSH |
| Klucze dostępu IAM | OIDC + Managed Identity |
| Brak monitoringu | Application Insights |

Koszt: ~13 $/miesiąc vs oryginalne 34 $/miesiąc.

## Co odróżnia to od konwertera składni

Krok agenta krytycznego jest tym, co odróżnia to od mechanicznego tłumaczenia. Wykrył wzorce, które działałyby na AWS, ale byłyby błędne na Azure — i naprawił je zamiast je replikować. Wyjście to nie "AWS w składni Azure"; to natywne wdrożenie Azure, które osiąga ten sam cel w czystszy sposób.

Zapoznaj się z [pełnym przewodnikiem](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/), aby zobaczyć pełną ścieżkę agenta i wygenerowane pliki.
