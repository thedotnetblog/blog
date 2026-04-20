---
title: "Od Laptopa do Produkcji: Wdrażanie Agentów AI do Microsoft Foundry Dwoma Poleceniami"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI ma teraz polecenia 'azd ai agent', które przenoszą Twojego agenta AI z lokalnego dev do żywego endpoint Foundry w minuty."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

Znasz tę lukę między "działa na mojej maszynie" a "jest wdrożone i obsługuje ruch"? Dla agentów AI ta luka była boleśnie szeroka.

Azure Developer CLI właśnie uczyniło to [sprawą dwóch poleceń](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## Nowy workflow `azd ai agent`

```bash
azd ai agent init
azd up
```

To wszystko. `azd ai agent init` tworzy scaffolding infrastruktury-jako-kod w Twoim repozytorium, a `azd up` provisionuje wszystko na Azure i publikuje Twojego agenta.

## Co się dzieje pod maską

Polecenie `init` generuje prawdziwe, inspekowalne szablony Bicep w Twoim repo — Foundry Resource, Foundry Project, konfiguracja wdrożenia modelu, zarządzana tożsamość z RBAC.

## Dev inner loop

```bash
azd ai agent run    # uruchom agenta lokalnie
azd ai agent invoke # wyślij testowe prompty
azd ai agent monitor --follow  # streamuj logi w czasie rzeczywistym
```

## Pełny zestaw poleceń

| Polecenie | Co robi |
|---------|-------------|
| `azd ai agent init` | Scaffold projektu agenta Foundry z IaC |
| `azd up` | Provisionuj zasoby i wdrożyj agenta |
| `azd ai agent invoke` | Wyślij prompty do zdalnego lub lokalnego agenta |
| `azd ai agent run` | Uruchom agenta lokalnie |
| `azd ai agent monitor` | Streamuj logi w czasie rzeczywistym |
| `azd down` | Wyczyść wszystkie zasoby Azure |

Sprawdź [pełny przewodnik](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).
