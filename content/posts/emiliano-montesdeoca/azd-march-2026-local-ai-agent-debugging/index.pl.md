---
title: "azd Pozwala Teraz Uruchamiać i Debugować Agenty AI Lokalnie — Co Zmieniło Się w Marcu 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI wypuścił siedem wydań w marcu 2026. Najważniejsze: lokalna pętla uruchamiania i debugowania dla agentów AI, integracja GitHub Copilot w konfiguracji projektu i obsługa Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azd-march-2026-local-ai-agent-debugging" >}}).*

Siedem wydań w jednym miesiącu. To co zespół Azure Developer CLI (`azd`) wypchnął w marcu 2026, a główna funkcja to ta, na którą czekałem: **lokalna pętla uruchamiania i debugowania dla agentów AI**.

## Uruchamiaj i debuguj agenty AI bez wdrażania

To jest ta duża. Nowe rozszerzenie `azure.ai.agents` dodaje zestaw poleceń:

- `azd ai agent run` — uruchamia agenta lokalnie
- `azd ai agent invoke` — wysyła do niego wiadomości (lokalnie lub wdrożone)
- `azd ai agent show` — wyświetla status kontenera i zdrowie
- `azd ai agent monitor` — strumieniuje logi kontenera w czasie rzeczywistym

Wcześniej testowanie agenta AI oznaczało wdrożenie do Microsoft Foundry za każdym razem. Teraz możesz iterować lokalnie.

## GitHub Copilot szkieletuje Twój projekt azd

`azd init` oferuje teraz opcję "Set up with GitHub Copilot (Preview)". Agent Copilot tworzy szkielet konfiguracji dla Twojej struktury projektu.

## Container App Jobs i ulepszenia wdrażania

- **Container App Jobs**: `azd` teraz wdraża `Microsoft.App/jobs` przez istniejącą konfigurację `host: containerapp`
- **Konfigurowalne limity czasu wdrażania**: Nowa flaga `--timeout` na `azd deploy`
- **Automatyczny fallback do lokalnego buildu**: Gdy zdalny build ACR zawiedzie
- **Lokalna walidacja preflightowa**: Parametry Bicep są walidowane lokalnie przed wdrożeniem

## Podsumowanie

Lokalna pętla debugowania agentów AI to gwiazda tego wydania. Sprawdź [pełne notatki wydania](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/).
