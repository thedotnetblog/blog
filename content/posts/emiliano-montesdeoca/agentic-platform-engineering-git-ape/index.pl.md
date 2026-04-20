---
title: "Agentic Platform Engineering Staje Się Rzeczywistością — Git-APE Pokazuje Jak"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Projekt Git-APE Microsoftu wdraża agentic platform engineering w praktyce — używając agentów GitHub Copilot i Azure MCP do zamiany żądań w języku naturalnym na zwalidowaną infrastrukturę chmurową."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform engineering to jeden z tych terminów, które świetnie brzmią na konferencjach, ale zazwyczaj oznaczają "zbudowaliśmy portal wewnętrzny i wrapper Terraform." Prawdziwa obietnica — self-service infrastruktura, która jest bezpieczna, zarządzana i szybka — zawsze była o kilka kroków za daleko.

Zespół Azure właśnie opublikował [Part 2 swojej serii agentic platform engineering](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/). Nazywają to **Git-APE** — projekt open-source, który używa agentów GitHub Copilot i serwerów Azure MCP do zamiany żądań w języku naturalnym na zwalidowaną, wdrożoną infrastrukturę.

## Co faktycznie robi Git-APE

Podstawowy pomysł: zamiast uczyć się modułów Terraform, deweloperzy rozmawiają z agentem Copilot. Agent interpretuje intencje, generuje Infrastructure-as-Code, waliduje wobec zasad i wdraża — wszystko w VS Code.

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Otwórz obszar roboczy w VS Code, a pliki konfiguracji agenta są automatycznie odkrywane przez GitHub Copilot:

```
@git-ape deploy a function app with storage in West Europe
```

Czyszczenie jest równie proste:

```
@git-ape destroy my-resource-group
```

## Dlaczego to ważne

Dla tych z nas budujących na Azure, przesuwa to rozmowę z "jak zbudować portal" na "jak opisać nasze guardrails jako API."

Jako deweloper .NET: Azure MCP Server i agenty GitHub Copilot działają z dowolnym obciążeniem Azure — Twoje ASP.NET Core API, .NET Aspire — wszystko może być celem agentic deployment flow.

## Podsumowanie

Git-APE to wczesne, ale konkretne spojrzenie na agentic platform engineering w praktyce. Sklonuj [repozytorium](https://github.com/Azure/git-ape) i przeczytaj [pełny post](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/).
