---
title: "Gdzie Hostować Agenty AI na Azure? Praktyczny Przewodnik po Decyzjach"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure oferuje sześć sposobów hostowania agentów AI — od surowych kontenerów po w pełni zarządzane Foundry Hosted Agents. Oto jak wybrać odpowiedni dla swojego obciążenia .NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-ai-agent-hosting-options-guide" >}}).*

Jeśli teraz budujesz agenty AI z .NET, pewnie zauważyłeś: jest *wiele* sposobów na hostowanie ich na Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents.

Microsoft opublikował [kompleksowy przewodnik po hostowaniu agentów Azure AI](https://devblogs.microsoft.com/all-things-azure/hostedagent/).

## Sześć opcji na pierwszy rzut oka

| Opcja | Najlepsza dla | Zarządzasz |
|-------|-------------|------------|
| **Container Apps** | Pełna kontrola kontenera bez K8s | Obserwowalność, stan, cykl życia |
| **AKS** | Enterprise compliance, multi-cluster | Wszystkim |
| **Azure Functions** | Sterowane zdarzeniami, krótkotrwałe zadania | Prawie niczym |
| **App Service** | Prosty agent HTTP | Wdrożeniem, skalowaniem |
| **Foundry Agents** | Agenty bez kodu | Prawie niczym |
| **Foundry Hosted Agents** | Agenty z własnym frameworkiem | Tylko kodem agenta |

## Foundry Hosted Agents — słodkie miejsce dla deweloperów agentów .NET

Wdrożenie jest naprawdę proste:

```bash
azd ext install azure.ai.agents
azd ai agent init
azd up
```

To pojedyncze `azd up` buduje kontener, wypycha go do ACR, provisionuje projekt Foundry i uruchamia agenta.

## Mój framework decyzyjny

1. **Potrzebujesz zero infrastruktury?** → Foundry Agents
2. **Masz własny kod agenta ale chcesz zarządzanego hostingu?** → Foundry Hosted Agents
3. **Sterowane zdarzeniami, krótkotrwałe zadania?** → Azure Functions
4. **Maksymalna kontrola kontenera?** → Container Apps
5. **Ścisła zgodność i multi-cluster?** → AKS

## Podsumowanie

Dla większości deweloperów .NET budujących z Semantic Kernel lub Microsoft Agent Framework, Hosted Agents to prawdopodobnie właściwy punkt startowy. Sprawdź [pełny przewodnik Microsoftu](https://devblogs.microsoft.com/all-things-azure/hostedagent/).
