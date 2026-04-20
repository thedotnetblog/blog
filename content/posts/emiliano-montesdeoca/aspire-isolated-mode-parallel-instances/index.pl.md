---
title: "Tryb Izolowany Aspire Rozwiązuje Problem Konfliktów Portów w Równoległym Programowaniu"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 wprowadza tryb --isolated: losowe porty, oddzielne sekrety i zero kolizji przy uruchamianiu wielu instancji tego samego AppHosta. Idealne dla agentów AI, worktrees i równoległych przepływów pracy."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Jeśli próbowałeś uruchomić dwie instancje tego samego projektu jednocześnie, znasz ten ból. Port 8080 jest już zajęty.

Aspire 13.2 naprawia to jedną flagą. James Newton-King [opisał pełne szczegóły](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/).

## Rozwiązanie: `--isolated`

```bash
aspire run --isolated
```

Każde uruchomienie dostaje:
- **Losowe porty** — brak kolizji między instancjami
- **Izolowane sekrety użytkownika** — ciągi połączeń i klucze API zostają oddzielne dla każdej instancji

## Prawdziwe scenariusze gdzie to błyszczy

**Wiele checkoutów:**

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Oba działają bez konfliktów.

**Agenty w tle w VS Code.** Gdy agent w tle Copilot Chat tworzy git worktree, tryb izolowany zapewnia, że obie instancje po prostu działają.

## Jak to działa pod maską

Gdy przekażesz `--isolated`, CLI generuje unikalny identyfikator instancji dla uruchomienia, który napędza randomizację portów i izolację sekretów.

## Podsumowanie

Tryb izolowany to mała funkcja, która rozwiązuje prawdziwy, coraz bardziej powszechny problem. Zdobądź 13.2 z `aspire update --self`.
