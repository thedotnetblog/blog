---
title: "Waar Moet Je je AI-Agents op Azure Hosten? Een Praktische Beslissingswijzer"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure biedt zes manieren om AI-agents te hosten — van ruwe containers tot volledig beheerde Foundry Hosted Agents. Zo kies je de juiste voor je .NET-workload."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-ai-agent-hosting-options-guide" >}}).*

Als je momenteel AI-agents bouwt met .NET, heb je waarschijnlijk iets opgemerkt: er zijn *veel* manieren om ze te hosten op Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents.

Microsoft heeft zojuist een [uitgebreide gids voor Azure AI agent-hosting](https://devblogs.microsoft.com/all-things-azure/hostedagent/) gepubliceerd.

## De zes opties in één oogopslag

| Optie | Beste voor | Je beheert |
|-------|-----------|-----------|
| **Container Apps** | Volledige containercontrole zonder K8s | Observabiliteit, staat, levenscyclus |
| **AKS** | Enterprise-naleving, multi-cluster | Alles |
| **Azure Functions** | Event-gedreven, korte taken | Bijna niets |
| **App Service** | Eenvoudige HTTP-agents | Implementatie, schaling |
| **Foundry Agents** | Optionele code-agents | Bijna niets |
| **Foundry Hosted Agents** | Aangepaste framework-agents | Alleen je agentcode |

## Foundry Hosted Agents — het juiste midden voor .NET agentdevelopers

Implementatie is echt eenvoudig:

```bash
azd ext install azure.ai.agents
azd ai agent init
azd up
```

Die ene `azd up` bouwt je container, stuurt hem naar ACR, richt het Foundry-project in en start je agent.

## Mijn beslissingsraamwerk

1. **Nul infrastructuur nodig?** → Foundry Agents
2. **Eigen agentcode maar beheerde hosting gewenst?** → Foundry Hosted Agents
3. **Event-gedreven, korte taken?** → Azure Functions
4. **Maximale containercontrole?** → Container Apps
5. **Strikte naleving en multi-cluster?** → AKS

## Samenvatting

Voor de meeste .NET-ontwikkelaars die bouwen met Semantic Kernel of Microsoft Agent Framework, is Hosted Agents waarschijnlijk het juiste startpunt. Bekijk de [volledige gids van Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/).
