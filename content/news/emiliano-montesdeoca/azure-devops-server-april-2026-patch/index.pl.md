---
title: "Aktualizacja Azure DevOps Server Kwiecień 2026 — Poprawka PR i Aktualizacje Bezpieczeństwa"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server otrzymuje Patch 3 z naprawą błędów ukończenia PR, ulepszoną walidacją wylogowania i przywróconymi połączeniami PAT GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-devops-server-april-2026-patch" >}}).*

Szybka informacja dla zespołów uruchamiających samodzielnie hostowany Azure DevOps Server: Microsoft wydał [Patch 3 na kwiecień 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) z trzema celowanymi poprawkami.

## Co zostało naprawione

- **Błędy ukończenia pull requestów** — wyjątek null reference podczas auto-ukończenia elementu roboczego mógł powodować niepowodzenia scalania PR
- **Walidacja przekierowania przy wylogowaniu** — ulepszona walidacja podczas wylogowywania zapobiegająca potencjalnym złośliwym przekierowaniom
- **Połączenia PAT GitHub Enterprise Server** — tworzenie połączeń Personal Access Token zostało przywrócone

## Jak zaktualizować

Pobierz [Patch 3](https://aka.ms/devopsserverpatch3) i uruchom instalator. Aby zweryfikować zastosowanie łatki:

```bash
<patch-installer>.exe CheckInstall
```

Microsoft zdecydowanie zaleca stosowanie najnowszej łatki dla bezpieczeństwa i niezawodności.
