---
title: "azd Laat Je Nu AI-Agents Lokaal Uitvoeren en Debuggen — Dit Veranderde in Maart 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI bracht in maart 2026 zeven releases uit. Highlights: een lokale loop voor uitvoeren en debuggen van AI-agents, GitHub Copilot-integratie in projectopstelling en ondersteuning voor Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azd-march-2026-local-ai-agent-debugging" >}}).*

Zeven releases in één maand. Dat is wat het Azure Developer CLI (`azd`)-team in maart 2026 uitbracht, en de hoofdfunctie is waar ik op wachtte: **een lokale loop voor uitvoeren en debuggen van AI-agents**.

## AI-agents uitvoeren en debuggen zonder implementeren

Dit is de grote. De nieuwe extensie `azure.ai.agents` voegt een reeks opdrachten toe:

- `azd ai agent run` — start je agent lokaal
- `azd ai agent invoke` — stuurt berichten naar hem (lokaal of geïmplementeerd)
- `azd ai agent show` — toont containerstatus en gezondheid
- `azd ai agent monitor` — streamt containerlogs in real-time

Voorheen betekende het testen van een AI-agent telkens implementeren naar Microsoft Foundry. Nu kun je lokaal itereren.

## GitHub Copilot maakt je azd-project aan

`azd init` biedt nu een optie "Set up with GitHub Copilot (Preview)". Een Copilot-agent maakt de configuratie voor je projectstructuur.

## Container App Jobs en implementatieverbeteringen

- **Container App Jobs**: `azd` implementeert nu `Microsoft.App/jobs` via de bestaande `host: containerapp`-config
- **Configureerbare implementatie-time-outs**: Nieuwe `--timeout`-vlag op `azd deploy`
- **Lokale build-fallback**: Wanneer remote ACR-build mislukt, schakelt `azd` automatisch terug naar lokale Docker/Podman
- **Lokale preflight-validatie**: Bicep-parameters worden lokaal gevalideerd vóór implementatie

## Samenvatting

De lokale AI-agent debuggingloop is de ster van deze release. Bekijk de [volledige releasenotes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/).
