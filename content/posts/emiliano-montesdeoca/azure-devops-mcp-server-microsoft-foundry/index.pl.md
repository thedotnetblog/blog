---
title: "Azure DevOps MCP Server Trafia do Microsoft Foundry: Co To Oznacza dla Twoich Agentów AI"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server jest teraz dostępny w Microsoft Foundry. Połącz swoje agenty AI bezpośrednio z przepływami pracy DevOps — elementy robocze, repozytoria, potoki — za pomocą kilku kliknięć."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-devops-mcp-server-microsoft-foundry" >}}).*

MCP (Model Context Protocol) ma swój moment. Jeśli śledzisz ekosystem agentów AI, pewnie zauważyłeś, że serwery MCP pojawiają się wszędzie — dając agentom możliwość interakcji z zewnętrznymi narzędziami i usługami przez standaryzowany protokół.

Teraz [Azure DevOps MCP Server jest dostępny w Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), i jest to jedna z tych integracji, która skłania do myślenia o praktycznych możliwościach.

## Co się faktycznie dzieje

Microsoft już wydał Azure DevOps MCP Server jako [publiczny podgląd](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview). Co nowego, to integracja z Foundry. Możesz teraz dodawać Azure DevOps MCP Server do swoich agentów Foundry bezpośrednio z katalogu narzędzi.

## Konfiguracja

Konfiguracja jest zaskakująco prosta:

1. W swoim agencie Foundry przejdź do **Dodaj narzędzia** > **Katalog**
2. Wyszukaj "Azure DevOps"
3. Wybierz Azure DevOps MCP Server (podgląd) i kliknij **Utwórz**
4. Podaj nazwę swojej organizacji i połącz

## Kontrolowanie dostępu agenta

Możesz określić, które narzędzia są dostępne dla Twojego agenta. Jeśli chcesz, żeby tylko czytał elementy robocze, ale nie dotykał potoków, możesz to skonfigurować. Zasada najmniejszego przywileju, zastosowana do agentów AI.

## Dlaczego to interesujące dla zespołów .NET

- **Asystenci planowania sprintów** — agenty, które mogą pobierać elementy robocze i sugerować pojemność sprintu
- **Boty code review** — agenty rozumiejące kontekst PR
- **Reagowanie na incydenty** — agenty tworzące elementy robocze i korelujące błędy
- **Wdrażanie deweloperów** — "Co powinienem teraz zrobić?" z realną odpowiedzią

## Podsumowanie

Sprawdź [pełne ogłoszenie](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) po szczegóły.
